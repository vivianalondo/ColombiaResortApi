import model
import unittest
#import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
#sys.path.append('.app')


class ColombiaResortTestCase(unittest.TestCase):

  def setUp(self):
    # creates a test client
    self.cliente = app.app.test_client()
    # propagate the exceptions to the test client
    app.app.config['TESTING'] = True

  def tearDown(self):
    pass

  #Testing status code in home
  def test_home_status_code(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = self.cliente.get('/')

    # assert the status code of the response
    self.assertEqual(result.status_code, 404)
    print ("Ruta no encontrada"

if __name__ == '__main__':
    unittest.main()