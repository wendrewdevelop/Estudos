import unittest


class TestFile(unittest.TestCase):
    """
        Validando o arquivo
    """
    
    def test_validando_path_arquivo(path_file):
        '''
            Verificando se o nosso arquivo
            esta no path correto
        '''
        path_file='batch.csv'

        assert path_file


if __name__ == '__main__':
    unittest.main()