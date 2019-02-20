import unittest
import extractor
import os.path

class TestCase(unittest.TestCase):

    def setUp(self):
        self.extract = extractor.Extractor()
        self.extract.ROOT_DIR = 'C:\\SIS'
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

    # isolated tests
    def test_isolated_onlyFormname(self):
        result = self.extract.onlyFormname('VEN601E.dfm')
        self.assertTrue(result == 'FVEN601E')

    def test_isolated_lineCaption(self):
        result = self.extract.lineCaption('Caption = Nome do Form')
        self.assertTrue(result == 'Nome do Form')

    def test_isolated_lineBreak(self):
        result = self.extract.lineCaption('Nome do Form\n')
        self.assertTrue(result == 'Nome do Form')

    def test_isolated_fixFormCaption_174(self):
        result = self.extract.fixFormCaption('Empresa#174')
        self.assertTrue(result == 'EmpresaC')

    def test_isolated_fixFormCaption_186(self):
        result = self.extract.fixFormCaption('1#186')
        self.assertTrue(result == '1º')

    def test_isolated_fixFormCaption_192(self):
        result = self.extract.fixFormCaption('#192')
        self.assertTrue(result == 'A')

    def test_isolated_fixFormCaption_193(self):
        result = self.extract.fixFormCaption('#193')
        self.assertTrue(result == 'Á')

    def test_isolated_fixFormCaption_194(self):
        result = self.extract.fixFormCaption('#194')
        self.assertTrue(result == 'Â')

    def test_isolated_fixFormCaption_195_199(self):
        result = self.extract.fixFormCaption('ATEN#195#199O')
        self.assertTrue(result == 'ATENÇÃO')

    def test_isolated_fixFormCaption_205(self):
        result = self.extract.fixFormCaption('#205ndice')
        self.assertTrue(result == 'Índice')

    def test_isolated_fixFormCaption_224(self):
        result = self.extract.fixFormCaption('#224 Vista')
        self.assertTrue(result == 'à Vista')

    def test_isolated_fixFormCaption_231_227(self):
        result = self.extract.fixFormCaption('Aten#231#227o')
        self.assertTrue(result == 'Atenção')

    def test_isolated_fixFormCaption_237(self):
        result = self.extract.fixFormCaption('#237ndice')
        self.assertTrue(result == 'índice')

    def test_isolated_fixFormCaption_233(self):
        result = self.extract.fixFormCaption('#233')
        self.assertTrue(result == 'é')

    def test_isolated_fixFormCaption_224_2(self):
        result = self.extract.fixFormCaption('#224')
        self.assertTrue(result == 'à')

    def test_isolated_fixFormCaption_225(self):
        result = self.extract.fixFormCaption('#225')
        self.assertTrue(result == 'á')

    def test_isolated_fixFormCaption_226(self):
        result = self.extract.fixFormCaption('#226')
        self.assertTrue(result == 'â')
               
    def test_isolated_fixFormCaption_201(self):
        result = self.extract.fixFormCaption('#201')
        self.assertTrue(result == 'É')

    def test_isolated_fixFormCaption_202(self):
        result = self.extract.fixFormCaption('#202')
        self.assertTrue(result == 'Ê')
               
    def test_isolated_fixFormCaption_234(self):
        result = self.extract.fixFormCaption('#234')
        self.assertTrue(result == 'ê')
               
    def test_isolated_fixFormCaption_211(self):
        result = self.extract.fixFormCaption('#211')
        self.assertTrue(result == 'Ó')

    def test_isolated_fixFormCaption_212(self):
        result = self.extract.fixFormCaption('#212')
        self.assertTrue(result == 'Ô')

    def test_isolated_fixFormCaption_243(self):
        result = self.extract.fixFormCaption('#243')
        self.assertTrue(result == 'ó')

    def test_isolated_fixFormCaption_244(self):
        result = self.extract.fixFormCaption('#244')
        self.assertTrue(result == 'ô')

    def test_isolated_fixFormCaption_245(self):
        result = self.extract.fixFormCaption('#245')
        self.assertTrue(result == 'õ')

    def test_isolated_fixFormCaption_218(self):
        result = self.extract.fixFormCaption('#218')
        self.assertTrue(result == 'Ú')

    def test_isolated_fixFormCaption_220(self):
        result = self.extract.fixFormCaption('#220')
        self.assertTrue(result == 'Ü')

    def test_isolated_fixFormCaption_250(self):
        result = self.extract.fixFormCaption('#250')
        self.assertTrue(result == 'ú')

    def test_isolated_fixFormCaption_252(self):
        result = self.extract.fixFormCaption('#252')
        self.assertTrue(result == 'ü')

    # integrated tests
    """
	def test_findFiles(self):
        self.extract.findFiles()
        self.assertTrue(len(self.extract.formList.items()) > 0)
    
    def test_oneFiles_VEN200P(self):
        self.extract.findFiles()
        self.assertTrue('FVEN200P' in self.extract.formList)

    def test_oneFiles_REC601E(self):
        self.extract.findFiles()
        self.assertTrue('FREC601E' in self.extract.formList)

    def test_oneFiles_IFP001C(self):
        self.extract.findFiles()
        self.assertTrue('FIFP001C' in self.extract.formList)

    def test_oneFiles_notExist(self):
        self.extract.findFiles()
        self.assertFalse('FICP000F' in self.extract.formList)

    def test_saveCSV(self):
        self.extract.saveCSV()
        self.assertTrue(os.path.isfile('result.csv'))
	"""

if __name__ == '__main__':
    unittest.main()
