import unittest
import os
import sys
from pprint import pprint
import build
from DataMap import *

class builder_UnitTests(unittest.TestCase):

    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    #TYPES = ['ccl','cm','cn','indiv','openexp','oth','pas2']
    DATA_DIR=SCRIPT_DIR+os.sep+'data'
    YR = '16'

    def tearDown(self):
        sys.stdout.flush()

    #@unittest.skip("a")
    def test_FileChecker(self):
        from build import read_file
        #Regular Sample File
        res = read_file('cm', '16', data_dir=self.DATA_DIR)
        self.assertTrue(len(res) == 22)

    #@unittest.skip("a")
    def test_cm(self):
        from build import read_file
        print('a')
        cm = read_file('cm', '16', data_dir=self.DATA_DIR)
        comm = {i['CMTE_ID']:i for i in cm}
        self.assertEqual(comm['C00001461']['CMTE_NM'],'ALASKA STATE MEDICAL ASSOCIATION POLITICAL ACTION COMMITTEE (ALPAC)')
        self.assertEqual(comm['C00001461'],{'CAND_ID': '',
         'CMTE_CITY': 'ANCHORAGE',
         'CMTE_DSGN': 'U',
         'CMTE_FILING_FREQ': 'Q',
         'CMTE_ID': 'C00001461',
         'CMTE_NM': 'ALASKA STATE MEDICAL ASSOCIATION POLITICAL ACTION COMMITTEE '
                    '(ALPAC)',
         'CMTE_PTY_AFFILIATION': '',
         'CMTE_ST': 'AK',
         'CMTE_ST1': '4107 LAUREL STREET',
         'CMTE_ST2': '',
         'CMTE_TP': 'Q',
         'CMTE_ZIP': '99508',
         'CONNECTED_ORG_NM': 'ALASKA STATE MEDICAL ASSOCIATION',
         'ORG_TP': 'M',
         'TRES_NM': 'ELLERBE, DWIGHT DR. '})

    #@unittest.skip("a")
    def test_cn(self):
        from build import read_file
        cn = read_file('cn', '16', data_dir=self.DATA_DIR)
        cand = {i['CAND_ID']:i for i in cn}
        assert len(cand) > 3

        self.assertEqual(cand['H0NH02017'],{'CAND_CITY': 'PETERBOROUGH',
               'CAND_ELECTION_YR': '2012',
               'CAND_ICI': 'C',
               'CAND_ID': 'H0NH02017',
               'CAND_NAME': 'BASS, CHARLES F.',
               'CAND_OFFICE': 'H',
               'CAND_OFFICE_DISTRICT': '02',
               'CAND_OFFICE_ST': 'NH',
               'CAND_PCC': 'C00302570',
               'CAND_PTY_AFFILIATION': 'REP',
               'CAND_ST': 'NH',
               'CAND_ST1': 'PO BOX 210',
               'CAND_ST2': '',
               'CAND_STATUS': 'P',
               'CAND_ZIP': '03458'})

        self.assertEqual(cand['H0MN08115'],{'CAND_CITY': 'ST PAUL',
               'CAND_ELECTION_YR': '2012',
               'CAND_ICI': 'C',
               'CAND_ID': 'H0MN08115',
               'CAND_NAME': 'CRAVAACK, RAYMOND J MR.',
               'CAND_OFFICE': 'H',
               'CAND_OFFICE_DISTRICT': '08',
               'CAND_OFFICE_ST': 'MN',
               'CAND_PCC': 'C00475632',
               'CAND_PTY_AFFILIATION': 'REP',
               'CAND_ST': 'MN',
               'CAND_ST1': 'PO BOX 40040',
               'CAND_ST2': '',
               'CAND_STATUS': 'P',
               'CAND_ZIP': '55101'})

        self.assertEqual(cand['H0MI01088'],{'CAND_CITY': 'CRYSTAL FALLS',
               'CAND_ELECTION_YR': '2016',
               'CAND_ICI': 'I',
               'CAND_ID': 'H0MI01088',
               'CAND_NAME': 'BENISHEK, DANIEL J. M.D.',
               'CAND_OFFICE': 'H',
               'CAND_OFFICE_DISTRICT': '01',
               'CAND_OFFICE_ST': 'MI',
               'CAND_PCC': 'C00476325',
               'CAND_PTY_AFFILIATION': 'REP',
               'CAND_ST': 'MI',
               'CAND_ST1': '802 PENTOGA TRAIL',
               'CAND_ST2': '',
               'CAND_STATUS': 'C',
               'CAND_ZIP': '499208518'})

    #@unittest.skip("a")
    def test_pas(self):
        from build import read_file
        pas = read_file('pas2', '16', in_zip_filename= 'itpas2.txt', data_dir=self.DATA_DIR)
        ipas = {i['TRAN_ID']:i for i in pas}
        self.assertEqual(ipas['SB23.I21988'],{'AMNDT_IND': 'N',
                 'CAND_ID': 'H0IL10302',
                 'CITY': 'LIBERTYVILLE',
                 'CMTE_ID': 'C00305805',
                 'EMPLOYER': '',
                 'ENTITY_TP': 'CCM',
                 'FILE_NUM': '999281',
                 'IMAGE_NUM': '15951092984',
                 'MEMO_CD': '',
                 'MEMO_TEXT': '',
                 'NAME': 'DOLD FOR CONGRESS',
                 'OCCUPATION': '',
                 'OTHER_ID': 'C00465971',
                 'RPT_TP': 'M3',
                 'STATE': 'IL',
                 'SUB_ID': '4032320151240925784',
                 'TRANSACTION_AMT': '5000',
                 'TRANSACTION_DT': '02232015',
                 'TRANSACTION_PGI': 'P',
                 'TRANSACTION_TP': '24K',
                 'TRAN_ID': 'SB23.I21988',
                 'ZIP_CODE': '600488145'})

        self.assertEqual(ipas['SB23.9146'],{'AMNDT_IND': 'N',
               'CAND_ID': 'H0MI01088',
               'CITY': 'CRYSTAL FALLS',
               'CMTE_ID': 'C00330720',
               'EMPLOYER': '',
               'ENTITY_TP': 'CCM',
               'FILE_NUM': '1009653',
               'IMAGE_NUM': '15971199757',
               'MEMO_CD': '',
               'MEMO_TEXT': '',
               'NAME': 'BENISHEK FOR CONGRESS',
               'OCCUPATION': '',
               'OTHER_ID': 'C00476325',
               'RPT_TP': '30S',
               'STATE': 'MI',
               'SUB_ID': '4060520151244032747',
               'TRANSACTION_AMT': '2000',
               'TRANSACTION_DT': '05182015',
               'TRANSACTION_PGI': 'P',
               'TRANSACTION_TP': '24K',
               'TRAN_ID': 'SB23.9146',
               'ZIP_CODE': '49920'})

    #@unittest.skip("a")
    def test_individual(self):
        from build import read_file
        ind_t = read_file('indiv', self.YR, in_zip_filename='itcont.txt', data_dir=self.DATA_DIR)
        ind = {i['SUB_ID']:i for i in ind_t}
        assert len(ind) > 3
        self.assertEqual(ind['4071720151247463287'], {'AMNDT_IND': 'N',
                         'CITY': 'MARQUETTE',
                         'CMTE_ID': 'C00476325',
                         'EMPLOYER': '',
                         'ENTITY_TP': 'IND',
                         'FILE_NUM': '1015681',
                         'IMAGE_NUM': '201507159000226039',
                         'MEMO_CD': '',
                         'MEMO_TEXT': '',
                         'NAME': 'FARBOD, JEAN L. DR.',
                         'OCCUPATION': '',
                         'OTHER_ID': '',
                         'RPT_TP': 'Q2',
                         'STATE': 'MI',
                         'SUB_ID': '4071720151247463287',
                         'TRANSACTION_AMT': '250',
                         'TRANSACTION_DT': '04072015',
                         'TRANSACTION_PGI': 'P',
                         'TRANSACTION_TP': '22Y',
                         'TRAN_ID': 'B7763216465004035A6B',
                         'ZIP_CODE': '49855'})
        self.assertEqual(ind['4071720151247404714'],{'AMNDT_IND': 'N',
                         'CITY': 'BANNING',
                         'CMTE_ID': 'C00476325',
                         'EMPLOYER': '',
                         'ENTITY_TP': 'ORG',
                         'FILE_NUM': '1015681',
                         'IMAGE_NUM': '201507159000225949',
                         'MEMO_CD': '',
                         'MEMO_TEXT': '',
                         'NAME': 'MORONGO BAND OF MISSION INDIANS',
                         'OCCUPATION': '',
                         'OTHER_ID': '',
                         'RPT_TP': 'Q2',
                         'STATE': 'CA',
                         'SUB_ID': '4071720151247404714',
                         'TRANSACTION_AMT': '1000',
                         'TRANSACTION_DT': '06012015',
                         'TRANSACTION_PGI': 'P',
                         'TRANSACTION_TP': '11',
                         'TRAN_ID': 'AC93EF91A931D4EA6981',
                         'ZIP_CODE': '922206977'})

    #@unittest.skip("a")
    def test_like_build(self):
        from build import TYPES as TYPES, read_file
        data = {}
        for tp in TYPES.keys():
            temp = read_file(tp, self.YR, data_dir=self.DATA_DIR, **TYPES[tp]['args'])
            data[tp] = {i[TYPES[tp]['unique']]:i for i in temp}
            self.assertGreaterEqual(len(data[tp]),1)
            sys.stdout.flush()

    #@unittest.skip("a")
    def test_data_replace(self):
        '''
        Tests updating codes with the current config
        '''
        from build import TYPES as TYPES, read_file, enrich_data
        DATA = {
            'cm':{
                'fakeid1':{
                    'CMTE_TP':'H',
                    'CMTE_DSGN':'A',
                    'CMTE_PTY_AFFILIATION':'IGR',
                    'CMTE_FILING_FREQ':'M',
                    'ORG_TP':'C'
                    }
                }
            }
        enrich_data('cm', data=DATA)
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_TP'], 'House')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_DSGN'], 'Authorized by a candidate')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_PTY_AFFILIATION'], 'Independent Green')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_FILING_FREQ'], 'Monthly filer')
        self.assertEqual(DATA['cm']['fakeid1']['ORG_TP'], 'Corporation')

    ####@unittest.skip("a")
    def test_data_replace2(self):
        '''
        Tests updating codes with the current config
        '''
        from build import TYPES as TYPES, read_file, enrich_data
        DATA = {
            'cm':{
                'fakeid1':{
                    'CMTE_TP':'S',
                    'CMTE_DSGN':'P',
                    'CMTE_PTY_AFFILIATION':'IGR',
                    'CMTE_FILING_FREQ':'W',
                    'ORG_TP':''
                    }
                }
            }
        enrich_data('cm', data=DATA)
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_TP'], 'Senate')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_DSGN'], 'Principal campaign committee of a candidate')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_PTY_AFFILIATION'], 'Independent Green')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_FILING_FREQ'], 'Waived')
        self.assertEqual(DATA['cm']['fakeid1']['ORG_TP'], '')

    #@unittest.skip("a")
    def test_data_replace3(self):
        '''
        Tests updating codes with the current config
        '''
        from build import TYPES as TYPES, read_file, enrich_data
        DATA = {
            'cn':{
                'fakeid1':{
                    'CAND_PTY_AFFILIATION':'IGR',
                    'CAND_OFFICE': 'H',
                    'CAND_ICI' : 'I',
                    'CAND_STATUS': 'P'
                    }
                }
            }
        enrich_data('cn', data=DATA)
        self.assertEqual(DATA['cn']['fakeid1']['CAND_PTY_AFFILIATION'], 'Independent Green')
        self.assertEqual(DATA['cn']['fakeid1']['CAND_OFFICE'], 'House')
        self.assertEqual(DATA['cn']['fakeid1']['CAND_ICI'], 'Incumbent')
        self.assertEqual(DATA['cn']['fakeid1']['CAND_STATUS'], 'Statutory candidate in prior cycle')

    #@unittest.skip("a")
    def test_data_expansion1(self):
        from build import get_other_data
        data = {
            'cn': {
                'cn1':{
                    'cn_1':1,
                    'cn_2':'cn-two',
                },
                'cn2':{
                    'cn_1':2,
                    'cn_2':'cn-three'}
                },
            'cm': {
                'cm1':{
                    'cn_1':3,
                    'cn_2':'cm-two',
                    'cn_lookup': 'cn1'
                },
                'cm2':{
                    'cn_1':4,
                    'cn_2':'cm-three',
                    'cn_lookup': 'cn5' #Missing
                }
            }}

        DMAP = {
            'CMTE_ID': {'d': 'cm'},
            'CAND_ID': {'d': 'cn'},
            'cn_lookup':{'d':'cn'},
            'cm_lookup': {'d':'cm'}
            }

        self.assertEqual(get_other_data('cn_lookup', 'cn1', dmap=DMAP, data=data),
                        data['cn']['cn1'])
        self.assertEqual(get_other_data('cm_lookup', 'cm1', dmap=DMAP, data=data),
                        data['cm']['cm1'])
        with self.assertRaises(KeyError):
            self.assertEqual(get_other_data('cn_lookup', 'cn5', dmap=DMAP, data=data),
                        data['cn']['cn1'])

    #@unittest.skip("a")
    def test_date_translation(self):
        from build import format_date
        self.assertEqual(format_date('12122014'),
                        '12-12-2014')

        self.assertEqual(format_date('01012013'),
                        '01-01-2013')

        self.assertEqual(format_date(11012013),
                        '11-01-2013')

        with self.assertRaises(ValueError):
            format_date('13012013')

        with self.assertRaises(ValueError):
            format_date('130120')
        with self.assertRaises(ValueError):
            format_date(1)

    @unittest.skip("WIP")
    def test_enrich_with_lookup(self):
        '''
        Tests updating codes with the current config
        '''
        from build import TYPES as TYPES, read_file, enrich_data
        DATA = {
            'cm':{
                'fakeid1':{
                    'CMTE_TP':'S',
                    'CMTE_DSGN':'P',
                    'CMTE_PTY_AFFILIATION':'IGR',
                    'CMTE_FILING_FREQ':'W',
                    'ORG_TP':'',
                    'CAND_ID':'cn2'
                    },
                'cm1':{
                    'cn_1':3,
                    'cn_2':'cm-two',
                    'CAND_ID': 'cn1'
                },
                'cm2':{
                    'cn_1':4,
                    'cn_2':'cm-three',
                    'CAND_ID': 'cn5' #Missing
                }},
            'cn': {
                'cn1':{
                    'cn_1':1,
                    'cn_2':'cn-two',
                },
                'cn2':{
                    'cn_1':2,
                    'cn_2':'cn-three'}
                }
            }

        DMAP = {
            'CMTE_ID': {'d': 'cm'},
            'CAND_ID': {'d': 'cn'},
            'cn_lookup':{'d':'cn'},
            'cm_lookup': {'d':'cm'}
            }


        enrich_data('cm', data=DATA,dmap=DMAP)
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_TP'], 'Senate')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_DSGN'], 'Principal campaign committee of a candidate')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_PTY_AFFILIATION'], 'Independent Green')
        self.assertEqual(DATA['cm']['fakeid1']['CMTE_FILING_FREQ'], 'Waived')
        self.assertEqual(DATA['cm']['fakeid1']['ORG_TP'], '')


    #@unittest.skip("a")
    def test_translate_codes(self):
        from build import translate_codes

        EMAP = {
            'cm':{'CMTE_TP':CMTE_TP,
                  'CMTE_DSGN':CMTE_DSGN,
                  'CMTE_PTY_AFFILIATION':CMTE_PTY_AFFILIATION,
                  'CMTE_FILING_FREQ':CMTE_FILING_FREQ,
                  'ORG_TP':ORG_TP
                  },
            'cn' : {
                'CAND_PTY_AFFILIATION':CMTE_PTY_AFFILIATION,
                'CAND_OFFICE':CAND_OFFICE,
                'CAND_ICI' : CAND_ICI,
                'CAND_STATUS': CAND_STATUS
                },
            'indiv' : {
                'ENTITY_TP': ENTITY_TP,
                'TRANSACTION_TP': TRANSACTION_TP
            }}


        self.assertEqual(
            translate_codes('cm', 'CMTE_DSGN','A', emap=EMAP), CMTE_DSGN['A'])

        self.assertEqual(
            translate_codes('cm', 'CMTE_DSGN','NOTFOUND', emap=EMAP), 'NOTFOUND')

    #@unittest.skip("a")
    def test_enrich_item_1(self):
        from build import enrich_item

        EMAP = {
            'cm':{'CMTE_TP':CMTE_TP,
                  'CMTE_DSGN':CMTE_DSGN,
                  'CMTE_PTY_AFFILIATION':CMTE_PTY_AFFILIATION,
                  'CMTE_FILING_FREQ':CMTE_FILING_FREQ,
                  'ORG_TP':ORG_TP
                  },
            'cn' : {
                'CAND_PTY_AFFILIATION':CMTE_PTY_AFFILIATION,
                'CAND_OFFICE':CAND_OFFICE,
                'CAND_ICI' : CAND_ICI,
                'CAND_STATUS': CAND_STATUS
                },
            'indiv' : {
                'ENTITY_TP': ENTITY_TP,
                'TRANSACTION_TP': TRANSACTION_TP
            }}

        data = {
            'cn': {
                'cn1':{
                    'cn_1':1,
                    'cn_2':'cn-two',
                },
                'cn2':{
                    'cn_1':2,
                    'cn_2':'cn-three'}
                },
            'cm': {
                'cm1':{
                    'cm_1':3,
                    'CMTE_DSGN':'A',
                    'cm_lookup': 'cn1'
                },
                'cm2':{
                    'cm_1':4,
                    'cm_2':'cm-three',
                    'cm_lookup': 'cn5' #Missing
                }
            }}

        a = {'cm_1':3, 'CMTE_DSGN':'A','cn_lookup': 'cn1'}
        enrich_item('cm',a,emap=EMAP,data=data)
        self.assertEqual(a['CMTE_DSGN'],'Authorized by a candidate')

        b = {'cn':3, 'CAND_PTY_AFFILIATION':'NOTFOUND','cn_lookup': 'cn1'}
        enrich_item('cn',b,emap=EMAP,data=data)
        self.assertEqual(b['CAND_PTY_AFFILIATION'],'NOTFOUND')

        c = {'cn':3, 'CAND_PTY_AFFILIATION':'FRE','cn_lookup': 'cn1'}
        enrich_item('cn',c,emap=EMAP,data=data)
        self.assertEqual(c['CAND_PTY_AFFILIATION'],'Freedom Party')


    def test_individual_contrib(self):
        from build import proc_indiv_contrib
        DMAP = {
            'CMTE_ID': {'d': 'cm'},
            'CAND_ID': {'d': 'cn'}
            }
        data = {
            'cn': {
                'cn1':{
                    'cn_1':1,
                    'CAND_PTY_AFFILIATION':'LBR',
                },
                'cn2':{
                    'cn_1':2,
                    'CAND_OFFICE':'P'}
                },
            'cm': {
                'cm1':{
                    'cm_1':3,
                    'CMTE_DSGN':'A',
                    'CMTE_PTY_AFFILIATION': 'FRE',
                    'CAND_ID' :'cn2'
                },
                'cm2':{
                    'cm_1':4,
                    'ORG_TP':'C',
                    'CMTE_DSGN': 'NOT_FOUND'
                }
            }}


        d = {'CMTE_ID': 'cm1'}
        pprint(d)
        proc_indiv_contrib(d,data=data,dmap=DMAP)
        pprint(d)

        self.assertEqual(d,
                         {'CAND_ID': 'cn2',
                         'CAND_OFFICE': 'P',
                         'CMTE_DSGN': 'A',
                         'CMTE_ID': 'cm1',
                         'CMTE_PTY_AFFILIATION': 'FRE',
                         'cm_1': 3,
                         'cn_1': 2})



if __name__ == '__main__':
    a = builder_UnitTests()
    unittest.main()

