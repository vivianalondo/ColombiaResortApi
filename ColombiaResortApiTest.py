import app
import unittest
import json

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
    print ("Ruta no encontrada")

  #Testing status code in path get all rooms
  def test_get_all_rooms_status_code(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = self.cliente.get('/V1/AllRooms')

    # assert the status code of the response
    self.assertEqual(result.status_code, 200)
    #print(result.data)


  #Testing status code in path get rooms acording to parameters
  def test_get_rooms_with_parameters_status_code(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = self.cliente.get('/V1/rooms/?room_type=S&hosts=4&city=05001&arrive_date=2017-12-12&leave_date=2017-12-12')
    # assert the status code of the response
    self.assertEqual(result.status_code, 200)

  #Testing not rooms available
  def test_get_rooms_is_null(self):
    result = self.cliente.get('/V1/rooms/?room_type=S&hosts=4&city=05001&arrive_date=2017-12-12&leave_date=2017-12-12')
    # assert the status code of the response
    data = json.loads(result.get_data(as_text=True))
    self.assertEqual(data['rooms'], [])
    print(data['rooms'])


if __name__ == '__main__':
    unittest.main()