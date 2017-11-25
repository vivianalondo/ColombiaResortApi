import model
import app
import unittest
import conexion
from flask_pymongo import PyMongo
from flask import Flask, current_app

#import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
#sys.path.append('.app')

class ColombiaResortUnitTestCaseUni(unittest.TestCase):

  conn =conexion.connection()
  app2 = conn.create_connection('colombiaresort','mongodb://localhost:27017/colombiaresort','DB_URI')
  mongo = PyMongo(app2)
  cliente = model.model()
  
  app = Flask(__name__)

  with app.app_context():
    # within this block, current_app points to app.
    print current_app.name

  def test_json(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = {
    "Id_Reserva" : "CR170010",
    "State" : "InActive",
    "Id_Hotel" : "01",
    "Number_Room" : "301",
    "Arrive_Date" : "2017-04-16",
    "Leave_Date" : "2017-04-19",
    "Document_Type" : "01",
    "Identification" : "1152439890",
    "Email" : "usuario5@correo.com",
    "Cell_Phone" : "3007654532"
}
    # assert the status code of the response
    self.assertEqual(result,{
      "Id_Reserva" : "CR170010",
      "State" : "InActive",
      "Id_Hotel" : "01",
      "Number_Room" : "301",
      "Arrive_Date" : "2017-04-16",
      "Leave_Date" : "2017-04-19",
      "Document_Type" : "01",
      "Identification" : "1152439890",
      "Email" : "usuario5@correo.com",
      "Cell_Phone" : "3007654532"
      })
    print (result)

  def test_get_all_hotels_info(self):
    # with model.model_context():
    # sends HTTP GET request to the application
    # on the specified path
    
    result = self.cliente.get_all_hotels_info(self.mongo)

      # assert the status code of the response
    self.assertEqual(result, {
      "hotel": [
        {
          "check_in": "15:00", 
          "check_out": "13:00", 
          "hotel_id": "01", 
          "hotel_location": {
            "address": "Calle 105 #83 - 04", 
            "lat": "6.26695330174546", 
            "long": "-75.56911130000003"
          }, 
          "hotel_name": "Colombia Resort Spring", 
          "hotel_thumbnail": "https://seedubaitours.com/wp-content/uploads/2014/08/Image-11.jpg", 
          "hotel_website": "www.colombiaresort.com/170/med/01", 
          "rooms": [
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 80000, 
              "room_thumbnail": "http://1.bp.blogspot.com/-VeD-AethQ3U/U6SHrMrD9YI/AAAAAAAABaE/_2EgtygHfKI/s1600/Foto+15-04-14+4+46+33+p.m..jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 100000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/16/16307H/16307_4.jpeg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 180000, 
              "room_thumbnail": "https://media-cdn.tripadvisor.com/media/photo-s/08/01/d3/b9/hotel-casa-de-yaro.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 200000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/18/18748H/18748_7.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 50000, 
              "room_thumbnail": "http://www.turismoenelejecafetero.com/userfiles/images/habit.JPG", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 150000, 
              "room_thumbnail": "http://www.villetaresort.com/images/fotos/Estandar/estan2.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 50000, 
              "room_thumbnail": "http://hostalpenalty.com/sites/default/files/habitacion-doble-1-cama-exterior.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 150000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/53/53991H/53991_12.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 50000, 
              "room_thumbnail": "http://hostalpenalty.com/sites/default/files/habitacion-doble-1-cama-exterior.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 250000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/53/53991H/53991_12.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 3
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 150000, 
              "room_thumbnail": "http://dibullatropical.com/wp-content/uploads/2015/02/Habitacion-triple.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 350000, 
              "room_thumbnail": "https://media-cdn.tripadvisor.com/media/photo-s/08/01/d3/b9/hotel-casa-de-yaro.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 190000, 
              "room_thumbnail": "http://1.bp.blogspot.com/-VeD-AethQ3U/U6SHrMrD9YI/AAAAAAAABaE/_2EgtygHfKI/s1600/Foto+15-04-14+4+46+33+p.m..jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 120000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/16/16307H/16307_4.jpeg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 220000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/18/18748H/18748_7.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 370000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/53/53991H/53991_12.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 70000, 
              "room_thumbnail": "http://hostalpenalty.com/sites/default/files/habitacion-doble-1-cama-exterior.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 70000, 
              "room_thumbnail": "http://www.turismoenelejecafetero.com/userfiles/images/habit.JPG", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 170000, 
              "room_thumbnail": "http://www.villetaresort.com/images/fotos/Estandar/estan2.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 3
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 90000, 
              "room_thumbnail": "http://dibullatropical.com/wp-content/uploads/2015/02/Habitacion-triple.jpg", 
              "room_type": "S"
            }
          ]
        }, 
        {
          "check_in": "15:00", 
          "check_out": "13:00", 
          "hotel_id": "02", 
          "hotel_location": {
            "address": "Calle 501 #43 - 23", 
            "lat": "908.26695330174546", 
            "long": "-2375.56911130000003"
          }, 
          "hotel_name": "Colombia Resort Winter", 
          "hotel_thumbnail": "http://www.carlosbriquethoteles.com/wp-content/uploads/2015/08/Dubai-1.jpg", 
          "hotel_website": "www.colombiaresort.com/170/bog/02", 
          "rooms": [
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 80000, 
              "room_thumbnail": "http://1.bp.blogspot.com/-VeD-AethQ3U/U6SHrMrD9YI/AAAAAAAABaE/_2EgtygHfKI/s1600/Foto+15-04-14+4+46+33+p.m..jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 100000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/16/16307H/16307_4.jpeg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 180000, 
              "room_thumbnail": "https://media-cdn.tripadvisor.com/media/photo-s/08/01/d3/b9/hotel-casa-de-yaro.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 200000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/18/18748H/18748_7.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 50000, 
              "room_thumbnail": "http://www.turismoenelejecafetero.com/userfiles/images/habit.JPG", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 150000, 
              "room_thumbnail": "http://www.villetaresort.com/images/fotos/Estandar/estan2.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 50000, 
              "room_thumbnail": "http://hostalpenalty.com/sites/default/files/habitacion-doble-1-cama-exterior.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 150000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/53/53991H/53991_12.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 50000, 
              "room_thumbnail": "http://hostalpenalty.com/sites/default/files/habitacion-doble-1-cama-exterior.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 250000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/53/53991H/53991_12.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 3
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 150000, 
              "room_thumbnail": "http://dibullatropical.com/wp-content/uploads/2015/02/Habitacion-triple.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 350000, 
              "room_thumbnail": "https://media-cdn.tripadvisor.com/media/photo-s/08/01/d3/b9/hotel-casa-de-yaro.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 2
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 190000, 
              "room_thumbnail": "http://1.bp.blogspot.com/-VeD-AethQ3U/U6SHrMrD9YI/AAAAAAAABaE/_2EgtygHfKI/s1600/Foto+15-04-14+4+46+33+p.m..jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 120000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/16/16307H/16307_4.jpeg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 2, 
                "simple": 0
              }, 
              "capacity": 4, 
              "currency": "COP", 
              "price": 220000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/18/18748H/18748_7.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 370000, 
              "room_thumbnail": "https://cdnh.octanio.com/photos/53/53991H/53991_12.jpeg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 1, 
                "simple": 0
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 70000, 
              "room_thumbnail": "http://hostalpenalty.com/sites/default/files/habitacion-doble-1-cama-exterior.jpg", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 70000, 
              "room_thumbnail": "http://www.turismoenelejecafetero.com/userfiles/images/habit.JPG", 
              "room_type": "S"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 2
              }, 
              "capacity": 2, 
              "currency": "COP", 
              "price": 170000, 
              "room_thumbnail": "http://www.villetaresort.com/images/fotos/Estandar/estan2.jpg", 
              "room_type": "L"
            }, 
            {
              "beds": {
                "double": 0, 
                "simple": 3
              }, 
              "capacity": 3, 
              "currency": "COP", 
              "price": 90000, 
              "room_thumbnail": "http://dibullatropical.com/wp-content/uploads/2015/02/Habitacion-triple.jpg", 
              "room_type": "S"
            }
          ]
        }
      ]
        })
    print (result)

  def test_get_disponible_rooms(self):
    # sends HTTP GET request to the application
    # on the specified path
    result = self.cliente.get_disponible_rooms(self.mongo, "20171224", "20171225", 050010)

    # assert the status code of the response
    self.assertEqual(result, [])
    print (result)

if __name__ == '__main__':
    unittest.main()