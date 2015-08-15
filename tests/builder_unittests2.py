import unittest
import os
import sys
from pprint import pprint
from DataMap import *
from time import time

class builder_UnitTests(unittest.TestCase):
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    DATA_DIR=SCRIPT_DIR+os.sep+'data'
    YR = '16'

    def tearDown(self):
        sys.stdout.flush()

    #@unittest.skip('dev')
    def test_read_file1(self):
        from build2 import read_file
        #Regular Sample File
        res = read_file('cm', '16', data_dir=self.DATA_DIR)
        self.assertTrue(len(res) == 22)
        self.assertTrue(res,[{'CMTE_DSGN': 'U', 'CMTE_CITY': 'KANSAS CITY', 'CMTE_ST': 'MO', 'CMTE_ZIP': '64108', 'TRES_NM': 'DEAN RODENBOUGH', 'ORG_TP': 'C', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'HALLMARK CARDS PAC', 'CAND_ID': '', 'CMTE_ST1': '2501 MCGEE', 'CMTE_TP': 'Q', 'CMTE_ST2': 'MD#288', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000059', 'CONNECTED_ORG_NM': ''}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20001', 'TRES_NM': 'WALKER, KEVIN', 'ORG_TP': 'M', 'CMTE_PTY_AFFILIATION': '', 'CMTE_NM': 'AMERICAN MEDICAL ASSOCIATION POLITICAL ACTION COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '25 MASSACHUSETTS AVE, NW', 'CMTE_TP': 'Q', 'CMTE_ST2': 'SUITE 600', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000422', 'CONNECTED_ORG_NM': 'AMERICAN MEDICAL ASSOCIATION'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'OKLAHOMA CITY', 'CMTE_ST': 'OK', 'CMTE_ZIP': '73107', 'TRES_NM': 'TOM RITTER', 'ORG_TP': 'L', 'CMTE_PTY_AFFILIATION': '', 'CMTE_NM': 'D R I V E POLITICAL FUND CHAPTER 886', 'CAND_ID': '', 'CMTE_ST1': '3528 W RENO', 'CMTE_TP': 'N', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00000489', 'CONNECTED_ORG_NM': 'TEAMSTERS LOCAL UNION 886'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'TOPEKA', 'CMTE_ST': 'KS', 'CMTE_ZIP': '66612', 'TRES_NM': 'C. RICHARD BONEBRAKE, M.D.', 'ORG_TP': 'T', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'KANSAS MEDICAL SOCIETY POLITICAL ACTION COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '623 SW 10TH AVE', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00000547', 'CONNECTED_ORG_NM': ''}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'INDIANAPOLIS', 'CMTE_ST': 'IN', 'CMTE_ZIP': '46202', 'TRES_NM': 'VIDYA KORA, M.D.', 'ORG_TP': 'M', 'CMTE_PTY_AFFILIATION': '', 'CMTE_NM': 'INDIANA STATE MEDICAL ASSOCIATION POLITICAL ACTION COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '322 CANAL WALK, CANAL LEVEL', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00000638', 'CONNECTED_ORG_NM': ''}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20005', 'TRES_NM': 'HARRISON, THOMAS C. DR', 'ORG_TP': 'M', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'AMERICAN DENTAL ASSOCIATION POLITICAL ACTION COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '1111 14TH STREET, NW', 'CMTE_TP': 'Q', 'CMTE_ST2': 'SUITE 1100', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000729', 'CONNECTED_ORG_NM': 'AMERICAN DENTAL ASSOCIATION'}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'HANOVER', 'CMTE_ST': 'MD', 'CMTE_ZIP': '21076', 'TRES_NM': 'GALIS, GEORGE', 'ORG_TP': 'L', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'INTERNATIONAL UNION OF PAINTERS AND ALLIED TRADES POLITICAL ACTION TOGETHER POLITICAL COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '7234 PARKWAY DRIVE', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000885', 'CONNECTED_ORG_NM': 'INTERNATIONAL UNION OF PAINTERS AND ALLIED TRADES'}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20005', 'TRES_NM': 'RAMAGE, EILEEN', 'ORG_TP': 'T', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'BUILD POLITICAL ACTION COMMITTEE OF THE NATIONAL ASSOCIATION OF HOME BUILDERS (BUILDPAC)', 'CAND_ID': '', 'CMTE_ST1': '1201 15TH STREET, NW', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000901', 'CONNECTED_ORG_NM': 'NATIONAL ASSOCIATION OF HOME BUILDERS'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20003', 'TRES_NM': 'WARD, KELLY C.', 'ORG_TP': '', 'CMTE_PTY_AFFILIATION': 'DEM', 'CMTE_NM': 'DEMOCRATIC CONGRESSIONAL CAMPAIGN COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '430 SOUTH CAPITOL STREET, SE', 'CMTE_TP': 'Y', 'CMTE_ST2': '2ND FLOOR', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000935', 'CONNECTED_ORG_NM': ''}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20005', 'TRES_NM': 'ROTH, ALAN J.', 'ORG_TP': 'T', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'UNITED STATES TELECOM ASSOCIATION POLITICAL ACTION COMMITTEE (TELECOMPAC)', 'CAND_ID': '', 'CMTE_ST1': '607 14TH STREET NORTHWEST', 'CMTE_TP': 'Q', 'CMTE_ST2': 'SUITE 400', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00000984', 'CONNECTED_ORG_NM': 'UNITED STATES TELECOM ASSOCIATION'}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20001', 'TRES_NM': 'SILINS, ANDRIS', 'ORG_TP': 'L', 'CMTE_PTY_AFFILIATION': 'NNE', 'CMTE_NM': 'CARPENTERS LEGISLATIVE IMPROVEMENT COMMITTEE UNITED BROTHERHOOD OF CARPENTERS AND JOINERS', 'CAND_ID': '', 'CMTE_ST1': '101 CONSTIUTION AVENUE, NW', 'CMTE_TP': 'Q', 'CMTE_ST2': '10TH FLOOR WEST', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00001016', 'CONNECTED_ORG_NM': 'UNITED BROTHERHOOD OF CARPENTERS AND JOINERS OF AMERICA'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'EAST LANSING', 'CMTE_ST': 'MI', 'CMTE_ZIP': '48826', 'TRES_NM': 'SCOT F. GOLDBERG, MD', 'ORG_TP': 'T', 'CMTE_PTY_AFFILIATION': 'NNE', 'CMTE_NM': 'MICHIGAN DOCTORS POLITICAL ACTION COMMITTEE - MICHIGAN STATE MEDICAL SOCIETY', 'CAND_ID': '', 'CMTE_ST1': 'P.O. BOX 769', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00001180', 'CONNECTED_ORG_NM': 'MICHIGAN STATE MEDICAL SOCIETY'}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'WASHINGTON', 'CMTE_ST': 'DC', 'CMTE_ZIP': '20005', 'TRES_NM': 'JEON, JOORI MS.', 'ORG_TP': 'T', 'CMTE_PTY_AFFILIATION': '', 'CMTE_NM': "AMERICAN HOTEL AND LODGING ASSOCIATION POLITICAL ACTION COMMITTEE ('HOTELPAC')", 'CAND_ID': '', 'CMTE_ST1': '1201 NEW YORK AVENUE, NW', 'CMTE_TP': 'Q', 'CMTE_ST2': 'SIXTH FLOOR', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00001198', 'CONNECTED_ORG_NM': ''}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'AUSTIN', 'CMTE_ST': 'TX', 'CMTE_ZIP': '78701', 'TRES_NM': 'STEWART, CLAYTON MR.', 'ORG_TP': 'T', 'CMTE_PTY_AFFILIATION': 'NNE', 'CMTE_NM': 'TEXAS MEDICAL ASSOCIATION POLITICAL ACTION COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '401 WEST 15TH STREET', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00001214', 'CONNECTED_ORG_NM': 'AMPAC'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'RICHMOND', 'CMTE_ST': 'VA', 'CMTE_ZIP': '232191741', 'TRES_NM': 'NILSEN, RICHARD A MR.', 'ORG_TP': '', 'CMTE_PTY_AFFILIATION': 'REP', 'CMTE_NM': 'REPUBLICAN PARTY OF VIRGINIA INC', 'CAND_ID': '', 'CMTE_ST1': '115 EAST GRACE STREET', 'CMTE_TP': 'Y', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00001305', 'CONNECTED_ORG_NM': 'GILLESPIE VICTORY FUND'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'MINNEAPOLIS', 'CMTE_ST': 'MN', 'CMTE_ZIP': '554042395', 'TRES_NM': 'SCHERER, BRON', 'ORG_TP': '', 'CMTE_PTY_AFFILIATION': 'REP', 'CMTE_NM': 'REPUBLICAN PARTY OF MINNESOTA - FEDERAL', 'CAND_ID': '', 'CMTE_ST1': '2200 E  FRANKLIN AVENUE', 'CMTE_TP': 'Y', 'CMTE_ST2': 'SUITE 201', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00001313', 'CONNECTED_ORG_NM': 'TARGETED STATE VICTORY'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'HONOLULU', 'CMTE_ST': 'HI', 'CMTE_ZIP': '96814', 'TRES_NM': 'SPANGLER, JOHN DR.', 'ORG_TP': 'M', 'CMTE_PTY_AFFILIATION': 'UNK', 'CMTE_NM': 'HAWAII MEDICAL POLITICAL ACTION COMMITTEE', 'CAND_ID': '', 'CMTE_ST1': '1360 S. BERETANIA ST.', 'CMTE_TP': 'Q', 'CMTE_ST2': '#200', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00001347', 'CONNECTED_ORG_NM': 'HAWAII MEDICAL ASSOCIATION'}, {'CMTE_DSGN': 'B', 'CMTE_CITY': 'KANSAS CITY', 'CMTE_ST': 'MO', 'CMTE_ZIP': '641909700', 'TRES_NM': 'STONE, J.S.', 'ORG_TP': 'V', 'CMTE_PTY_AFFILIATION': '', 'CMTE_NM': 'DAIRY FARMERS OF AMERICA, INC. - DEPAC (DAIRY EDUCATIONAL POLITICAL ACTION COMMITTEE)', 'CAND_ID': '', 'CMTE_ST1': 'P.O. BOX 909700', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00001388', 'CONNECTED_ORG_NM': 'DAIRY FARMERS OF AMERICA, INC.'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'ANCHORAGE', 'CMTE_ST': 'AK', 'CMTE_ZIP': '99508', 'TRES_NM': 'ELLERBE, DWIGHT DR. ', 'ORG_TP': 'M', 'CMTE_PTY_AFFILIATION': '', 'CMTE_NM': 'ALASKA STATE MEDICAL ASSOCIATION POLITICAL ACTION COMMITTEE (ALPAC)', 'CAND_ID': '', 'CMTE_ST1': '4107 LAUREL STREET', 'CMTE_TP': 'Q', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00001461', 'CONNECTED_ORG_NM': 'ALASKA STATE MEDICAL ASSOCIATION'}, {'CMTE_DSGN': 'P', 'CMTE_CITY': 'GLADSTONE', 'CMTE_ST': 'MI', 'CMTE_ZIP': '498370108', 'TRES_NM': 'BENISHEK, TRENT J.', 'ORG_TP': '', 'CMTE_PTY_AFFILIATION': 'REP', 'CMTE_NM': 'BENISHEK FOR CONGRESS, INC.', 'CAND_ID': 'H0MI01088', 'CMTE_ST1': 'PO BOX 108', 'CMTE_TP': 'H', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00476325', 'CONNECTED_ORG_NM': 'PATRIOT DAY II 2015'}, {'CMTE_DSGN': 'P', 'CMTE_CITY': 'LIBERTYVILLE', 'CMTE_ST': 'IL', 'CMTE_ZIP': '60048', 'TRES_NM': 'KILGORE, PAUL', 'ORG_TP': '', 'CMTE_PTY_AFFILIATION': 'REP', 'CMTE_NM': 'DOLD FOR CONGRESS', 'CAND_ID': 'H0IL10302', 'CMTE_ST1': 'PO BOX 6312', 'CMTE_TP': 'H', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'Q', 'CMTE_ID': 'C00465971', 'CONNECTED_ORG_NM': 'SCHILLING DOLD NEXT GENERATION COMMITTEE'}, {'CMTE_DSGN': 'U', 'CMTE_CITY': 'TOPEKA', 'CMTE_ST': 'KS', 'CMTE_ZIP': '66604', 'TRES_NM': 'ANDERSON, T.C.', 'ORG_TP': '', 'CMTE_PTY_AFFILIATION': 'REP', 'CMTE_NM': 'KANSAS REPUBLICAN PARTY', 'CAND_ID': '', 'CMTE_ST1': 'P.O. BOX 4157', 'CMTE_TP': 'Y', 'CMTE_ST2': '', 'CMTE_FILING_FREQ': 'M', 'CMTE_ID': 'C00004606', 'CONNECTED_ORG_NM': 'NONE'}])

    #@unittest.skip('dev')
    def test_read_file2(self):
        from build2 import read_file
        #Test with non-existent file
        with self.assertRaises(OSError):
            res = read_file('cm1', '16', data_dir=self.DATA_DIR)

    #@unittest.skip('dev')
    def test_read_file3(self):
        from build2 import read_file
        #Test with gen file
        test1 = read_file('cm', '16', data_dir=self.DATA_DIR)
        res = read_file('cm', '16', data_dir=self.DATA_DIR,gen=True)
        for i,x in enumerate(res):
            self.assertEqual(test1[i],x)

    #@unittest.skip('dev')
    def test_date_translation(self):
        from build2 import format_date
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

    #@unittest.skip('dev')
    def test_translate_codes(self):
        from build2 import translate_codes
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
            translate_codes('cm', 'CMTE_DSGN','A'), CMTE_DSGN['A'])
        self.assertEqual(
            translate_codes('cm', 'CMTE_DSGN','NOTFOUND'), 'NOTFOUND')


    #@unittest.skip('dev')
    def test_translate_codes_2(self):
        from build2 import read_file, translate_codes
        from DataMap import FIELDEXPANSION as emap
        #Test with gen file
        reps = 1000
        stime = time()
        for _ in range(0,reps):
            temp = read_file('cm', '16', data_dir=self.DATA_DIR,gen=True)
            otemp = []
            ntemp = []
            for item in temp:
                otemp.append(dict(item))
                #Translate Codes
                for k in (k for k in item if item[k]):
                    item[k]=translate_codes('cm',k,item[k]) if k in emap['cm'] else item[k]
                ntemp.append(item)
        print("Completed {} reps  in {} seconds".format(reps,time()-stime))
        for i in range(len(otemp)):
            for k,v in otemp[i].items():
                if k in emap['cm'] and v:
                    self.assertEqual(
                        emap['cm'][k][v],
                        ntemp[i][k]
                    )
                    #print("FIELD: {} OLD: {} NEW: {}".format(k,v,ntemp[i][k]))

    #@unittest.skip('dev')
    def test_get_cols(self):
        from build2 import get_cols
        gen = (x for x in [
            {'CMTE_TP':'test',
                  'CMTE_DSGN':'test',
                  'CMTE_PTY_AFFILIATION':'test',
                  'CMTE_FILING_FREQ':'test',
                  'ORG_TP':'test'
                  },
            {
                'CAND_PTY_AFFILIATION':'test',
                'CAND_OFFICE':'test',
                'CAND_ICI' : 'test',
                'CAND_STATUS': 'test'
                },
            {
                'ENTITY_TP': 'test',
                'TRANSACTION_TP': 'test'
            }])
        cols,d = get_cols(gen)
        self.assertEqual(cols,{'CMTE_FILING_FREQ', 'CMTE_TP', 'CMTE_PTY_AFFILIATION', 'CAND_ICI', 'ORG_TP', 'CAND_PTY_AFFILIATION', 'ENTITY_TP', 'CAND_STATUS', 'TRANSACTION_TP', 'CMTE_DSGN', 'CAND_OFFICE'})
        self.assertEqual(d,[{'CMTE_FILING_FREQ': 'test', 'ORG_TP': 'test', 'CMTE_TP': 'test', 'CMTE_DSGN': 'test', 'CMTE_PTY_AFFILIATION': 'test'}, {'CAND_OFFICE': 'test', 'CAND_STATUS': 'test', 'CAND_PTY_AFFILIATION': 'test', 'CAND_ICI': 'test'}, {'ENTITY_TP': 'test', 'TRANSACTION_TP': 'test'}])

    ##@unittest.skip('dev')
    def test_write_csv(self):
        from build2 import write_csv,read_file
        data = [{'data':k} for k in range(100)]
        res = write_csv((k for k in data),'test',data_dir=self.DATA_DIR)
        self.assertEqual(res,True)

if __name__ == '__main__':
    a = builder_UnitTests()
    unittest.main()

