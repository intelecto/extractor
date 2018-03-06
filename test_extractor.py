import unittest
import extractor
import os.path

class TestCase(unittest.TestCase):

    def setUp(self):
        self.extract = extractor.Extractor()
        self.extract.ROOT_DIR = '.\\SIS'
        self.extract.EXCLUDE_DIRS = [r'.\SIS\ACBr', 
                                r'.\SIS\SISMobile', 
                                r'.\SIS\SISDLL'] 

        self.extract.EXCLUDE_FILES_WITH = ['900A.dfm',
                                      'BARVERTICAL',
                                      'Frame',
                                      'PAI']

        self.extract.VALID_EXTENSION = '.dfm'
        self.extract.CSV_FILE = 'result.csv'
        self.extract.formList = {}
        if os.path.isfile('result.csv'):
            os.remove('result.csv')

    # isolated
    def test_isolated_onlyFormname(self):
        result = self.extract.onlyFormname('VEN601E.dfm')
        self.assertTrue(result == 'FVEN601E')

    def test_isolated_lineCaption(self):
        result = self.extract.lineCaption('Caption = Nome do Form')
        self.assertTrue(result == 'Nome do Form')

    def test_isolated_lineBreak(self):
        result = self.extract.lineCaption('Nome do Form\n')
        self.assertTrue(result == 'Nome do Form')

    def test_isolated_fixFormCaption(self):
        result = self.extract.fixFormCaption('Aten#231#227o')
        self.assertTrue(result == 'Atenção')

    # integrated 
    #def test_findFiles(self):
    #    self.extract.findFiles()
    #    self.assertTrue(len(self.extract.formList.items()) > 0)
    
    #def test_saveCSV(self):
    #    self.extract.saveCSV()
    #    self.assertTrue(os.path.isfile('result.csv'))

if __name__ == '__main__':
    unittest.main()
