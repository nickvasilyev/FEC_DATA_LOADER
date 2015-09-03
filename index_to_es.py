__author__ = 'vasilyen'
#!/usr/bin/python3
import sys
from elasticsearch import Elasticsearch
import elasticsearch
import csv
import os
ES_HOST = 'http://192.168.1.11:9200'
INDEX = 'fec'
YEAR = sys.argv[1] if len(sys.argv)>1 else '2016'
YR = YEAR[-2:]
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR=SCRIPT_DIR+os.sep+'data'

es = Elasticsearch(ES_HOST)
es.indices.create(index='fec', ignore=[404,400])


NUMBER_FIELDS  = ['CAND_ELECTION_YR', 'TRANSACTION_AMT']
DATE_FIELDS = ['TRANSACTION_DT']
STRING_FIELDS = ['CMTE_TP',
    'CAND_NAME',
    'CAND_ST2',
    'CMTE_ID',
    'CAND_OFFICE_DISTRICT',
    'CAND_PCC',
    'CMTE_PTY_AFFILIATION',
    'CAND_ZIP',
    'ENTITY_TP',
    'CONNECTED_ORG_NM',
    'CAND_ICI',
    'IMAGE_NUM',
    'ORG_TP',
    'CMTE_DSGN',
    'NAME',
    'CMTE_ST1',
    'CMTE_FILING_FREQ',
    'RPT_TP',
    'SUB_ID',
    'TRAN_ID',
    'CMTE_ST2',
    'CAND_CITY',
    'CAND_ST',
    'RPT_YR',
    'AMNDT_IND',
    'CATEGORY_DESC',
    'CAND_STATUS',
    'CMTE_ZIP',
    'TRANSACTION_PGI',
    'CAND_ID',
    'BACK_REF_TRAN_ID',
    'MEMO_CD',
    'CAND_ST1',
    'CMTE_CITY',
    'CMTE_ST',
    'MEMO_TEXT',
    'CMTE_NM',
    'FILE_NUM',
    'CITY',
    'PURPOSE',
    'TRES_NM',
    'CATEGORY',
    'FORM_TP_CD',
    'STATE',
    'CAND_PTY_AFFILIATION',
    'CAND_OFFICE',
    'ZIP_CODE',
    'LINE_NUM',
    'CAND_OFFICE_ST',
    'SCHED_TP_CD',
    'EMPLOYER',
    'OTHER_ID',
    'TRANSACTION_TP',
    'OCCUPATION',
    ]

def process_file(doc_type, fname):
    print("Opening: " + fname)
    with open(DATA_DIR + os.sep + fname, 'r') as f:
        reader = csv.DictReader(f)
        first = True
        for row in reader:
            if first:
                make_mapping(doc_type, row.keys())
                first = False
            d = {k:v for k,v in row.items() if len(v)>0}
            try:
                es.index(index='fec',doc_type=doc_type,body=d)
            except:
                print("Couldn't index")
                print(d)



def make_mapping(doc_type, fields):

    for field in fields:
        print("Creating field " + field)
        if field in STRING_FIELDS:
            create_string_field(doc_type, field)
        elif field in DATE_FIELDS:
            create_date_field(doc_type, field)
        elif field in NUMBER_FIELDS:
            create_num_field(doc_type, field)

def create_string_field(doc_type,field):
    es.indices.put_mapping(index=INDEX,doc_type=doc_type,body = '''
    {%(doc_type)s:{
        "properties": {
            %(field)s: {
				"type": "string",
				"fields": {
				"raw": {
					"type": "string",
					"index": "not_analyzed"
					}
				}
			}
		}
    }}
    ''' % {'doc_type': doc_type,'field':field}
    )

def create_date_field(doc_type,field):
    es.indices.put_mapping(index=INDEX,doc_type=doc_type,body = '''
    {%(doc_type)s:{
        "properties": {
            %(field)s: {
				"type": "date"
			}
		}
    }}
    ''' % {'doc_type': doc_type,'field':field}
    )

def create_num_field(doc_type,field):
    es.indices.put_mapping(index=INDEX,doc_type=doc_type,body = '''
    {%(doc_type)s:{
        "properties": {
            %(field)s: {
				"type": "double"
			}
		}
    }}
    ''' % {'doc_type': doc_type,'field':field}
    )

if __name__ == '__main__':
    FILES = {
        'indiv':'_indiv{}.csv'.format(YR),
        'pas':'_pas2{}.csv'.format(YR),
        'exp':'_exp{}.csv'.format(YR)
    }
    for file in FILES.keys():
        process_file(file, FILES[file])

