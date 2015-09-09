#!/usr/bin/python3
import zipfile
import csv
import os
import sys
from io import TextIOWrapper
import DataMap
import urllib.request as urllib2
import urllib.parse as urlparse

'''
This script will parse data from
http://www.fec.gov/finance/disclosure/ftpdet.shtml
'''

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BASEURL = 'ftp://ftp.fec.gov/FEC/{}/{}'
HEADER_BASEURL = 'http://www.fec.gov/finance/disclosure/metadata/{}'
ELASTIC = 'http://localhost:9200'
index = True
TYPES = {'ccl': {'args': {},
                 'unique': 'LINKAGE_ID'},
         'cm': {'args': {},
                'unique': 'CMTE_ID'},
         'cn': {'args': {},
                'unique': 'CAND_ID'},
         'indiv': {'args':
                       { 'in_zip_filename': 'itcont.txt'},
                   'unique': 'SUB_ID'},
         'pas2': {'args': {'in_zip_filename': 'itpas2.txt'},
                  'unique': 'SUB_ID'},
         'oppexp': {'args': {'in_zip_filename': 'oppexp.txt'},
                    'unique': 'SUB_ID'},
}
DMAP = {
    'CMTE_ID': {'d': 'cm'},
    'CAND_ID': {'d': 'cn'}
}

DATA_DIR = SCRIPT_DIR + os.sep + 'data'
YEAR = sys.argv[1] if len(sys.argv) > 1 else '2016'
YR = YEAR[-2:]
data = {}
emap = DataMap.FIELDEXPANSION


def main():

    if not os.path.isdir(DATA_DIR):
        print("Creating Data Directory: " + DATA_DIR)
        os.mkdir(DATA_DIR)
    os.chdir(DATA_DIR)

    for tp in ['ccl', 'cm', 'cn']:
        temp = read_file(tp, YR, gen=True, **TYPES[tp]['args'])
        ntemp = []
        for item in temp:
            for k in (k for k in item if item[k]):
                item[k] = translate_codes(tp, k, item[k]) if k in emap['cm'] else item[k]
            ntemp.append(item)
        data[tp] = {i[TYPES[tp]['unique']]: i for i in ntemp}
        assert len(data[tp]) > 1000
        sys.stdout.flush()

    indiv = read_file('indiv', YR, gen=True, **TYPES['indiv']['args'])
    write_csv(indiv, '_indiv{}.csv'.format(YR), func=proc_contrib)

    pas = read_file('pas2', YR, gen=True, **TYPES['pas2']['args'])
    write_csv(pas, '_pas2{}.csv'.format(YR), func=proc_contrib)

    exp = read_file('oppexp', YR, gen=True, **TYPES['oppexp']['args'])
    write_csv(exp, '_exp{}.csv'.format(YR), func=proc_contrib)


def write_csv(out_gen, filename, func=None, data_dir=DATA_DIR):
    print("Writing CSV To: {}".format(filename))
    out_gen = func(out_gen) if func else out_gen
    with open(filename, 'w') as csvfile:
        try:
            cols, temp_items = get_cols(out_gen, count=800)
            writer = csv.DictWriter(csvfile, fieldnames=cols)
            writer.writeheader()
            for item in temp_items:
                writer.writerow(item)
            for item in out_gen:
                writer.writerow(item)
        except StopIteration:
            print("Done Writing")
            return True
    return True


def proc_contrib(gen, data=data, dmap=DMAP):
    for item in gen:
        if 'CMTE_ID' in item and item['CMTE_ID']:
            nd = get_other_data('CMTE_ID', item['CMTE_ID'], data=data, dmap=dmap)
            item.update(nd)
        if 'CAND_ID' in item and item['CAND_ID']:
            nd = get_other_data('CAND_ID', item['CAND_ID'], dmap=dmap, data=data)
            item.update(nd)
        if 'TRANSACTION_DT' in item and item['TRANSACTION_DT']:
            item['TRANSACTION_DT'] = format_date(item['TRANSACTION_DT'])
        yield item


def get_other_data(field_n, field_v, dmap=DMAP, data=data):
    try:
        where_in_data = dmap[field_n]['d']
        return data[where_in_data][field_v]
    except KeyError as e:
        print("WARN: Failed to perform a look up on: [{}] by [{}]".format(field_v, field_n))
        raise e


def get_cols(iter, count=1000):
    cols = []
    temp_items = []
    for i, item in enumerate(iter):
        cols.append(list(item.keys()))
        temp_items.append(item)
        if i >= count:
            break
    cols = set(i for b in cols for i in b)
    return cols, temp_items


def translate_codes(dtype, field_n, field_v, emap=DataMap.FIELDEXPANSION):
    if field_v and dtype in emap and field_n in emap[dtype]:
        lookup_dict = emap[dtype][field_n]
        try:
            return lookup_dict[field_v]
        except KeyError as e:
            print("ERROR: Key Error in Enriching: Couldn't find [{}] in [{}], leaving as is".format(field_v, field_n))
            return field_v
    else:
        if not field_v:
            print("WARN: Empty Field Value for [{}] in type [{}], value [{}]".format(field_n, dtype, field_v))
        else:
            print("WARN: Couldn't find a lookup map for [{}] in type [{}], value [{}]".format(field_n, dtype, field_v))
        return field_v


def format_date(date_s):
    try:
        if '/' in date_s:
            m = date_s[0:2]
            d = date_s[3:5]
            y = date_s[6:]
        else:
            m = date_s[0:2]
            d = date_s[2:4]
            y = date_s[4:]
        if int(y) > 2020 or int(y) < 2000 or int(d) > 32 or int(m) > 12:
            print("Bad Data in Date: {}".format(date_s))
            # raise(ValueError)
        return "{}-{}-{}".format(y, m, d)
    except TypeError as e:
        print("Convering bad date to string:")
        return format_date(str(date_s))
    except Exception as e:
        print("ERROR: Parsing Date [{}]".format(date_s))
        raise (e)


def get_file(type, YR):
    url = BASEURL.format(YEAR, "{}{}.zip".format(type, YR))
    print(url)
    download_file(url)


def download_file(url, desc=None):
    print("Downloading " + url)
    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    head = {
        'User-Agent': "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
        'Accept': '*'
    }
    r = urllib2.Request(url, headers= head)
    filename = os.path.basename(path)
    fl = urllib2.urlopen(r)
    if not filename:
        filename = 'downloaded.file'
    if desc:
        filename = os.path.join(desc, filename)
    with open(DATA_DIR + '/' + filename, 'wb') as f:
        f.write(fl.read())
        print()
    return filename


def read_file(type, YR, data_dir=DATA_DIR, in_zip_filename=None, gen=False):
    filename = "{}{}{}".format(data_dir + os.sep, type + YR, '.zip')
    header_filename = "{}{}{}".format(data_dir + os.sep, type, '_header_file.csv')
    if not os.path.isfile(filename) or not os.path.isfile(header_filename):
        download_file(BASEURL.format(YEAR, "{}{}.zip".format(type, YR)))
        download_file(HEADER_BASEURL.format('{}_header_file.csv'.format(type)))

    print("Processing {} and {}".format(filename, header_filename))
    with zipfile.ZipFile(filename) as d:
        with open(header_filename, 'r') as hd:
            header = csv.reader(hd).__next__()
        inzipfile = in_zip_filename or type + '.txt'
        if inzipfile in d.namelist():
            t = d.open(inzipfile, 'r')
            reader = csv.DictReader(TextIOWrapper(t), fieldnames=header, delimiter='|')
            if gen:
                return gen_content(reader)
            else:
                return read_content(reader)
        else:
            print("Couldn't find {} in the zip file".format(inzipfile))
            raise IOError()
            sys.exit(1)
    return out


def read_content(reader):
    c = 0
    out = []
    while True:
        try:
            line = reader.__next__()
            out.append(line)
            c += 1
        except UnicodeDecodeError:
            print("Error reading in a line: UnicodeDecodeError")
        except StopIteration:
            break
    print("Read {} Lines from File. Counted {} in Data".format(c, len(out)))
    assert c == len(out)
    return out


def gen_content(reader):
    while True:
        try:
            yield reader.__next__()
        except UnicodeDecodeError:
            print("Error reading in a line: UnicodeDecodeError")
        except StopIteration:
            break


if __name__ == '__main__':
    sys.exit(main())