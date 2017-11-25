import model
import app
import unittest
import conexion
from datetime import datetime
from flask_pymongo import PyMongo
from flask import Flask, current_app

#import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
#sys.path.append('.app')
app = Flask(__name__)
conn =conexion.connection()
app = conn.create_connection('colombiaresort','mongodb://localhost:27017/colombiaresort','DB_URI')
mongo = PyMongo(app)
cliente = model.model()


class ColombiaResortUnitTestCaseUni(unittest.TestCase):


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
    with app.app_context():

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
      print ("Test 1 Ready")

  def test_get_all_hotels_info(self):
    # with model.model_context():
    # sends HTTP GET request to the application
    # on the specified path
    with app.app_context():
    # within this block, current_app points to app.

      result = cliente.get_all_hotels_info(mongo)

        # assert the status code of the response
      self.assertEqual.__self__.maxDiff = None
      self.assertEqual(result, {
  "result": {
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
  }
})
      print ("Test 2 Ready")

  def test_get_disponible_rooms(self):

    with app.app_context():

      self.Arrive_Date = datetime.strptime("2017-12-12", '%Y-%m-%d')
      self.Leave_Date = datetime.strptime("2017-12-12", '%Y-%m-%d')

      result = cliente.get_disponible_rooms(mongo,self.Arrive_Date,self.Leave_Date,"05001","4","S")
      self.assertEqual(result, {
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
  "rooms": []
})
      print("Test 3 Ready")

  def test_create_reserve(self):

    with app.app_context():

      result = cliente.create_reserve(mongo,"2017-12-12","2017-12-12","S","4","0","2","01","CC","12345","lopera@lope","311123")
      self.assertEqual(result,{"message": "Su reserva no fue realizada"})
    print("Test 4 Ready")


  def test_list_reservations(self):

      with app.app_context():

        result = cliente.list_reservations(mongo)
        self.assertEqual(result,{
  "Reservas": [
    {
      "Arrive_Date": "2017-11-01", 
      "Cell_Phone": "3001234567", 
      "Document_Type": "CC", 
      "Email": "usuario@correo.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170001", 
      "Identification": "1234567890", 
      "Leave_Date": "2017-11-03", 
      "Number_Room": "203", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-12-01", 
      "Cell_Phone": "3001234567", 
      "Document_Type": "01", 
      "Email": "usuario@correo.com", 
      "Id_Hotel": "02", 
      "Id_Reserva": "CR170002", 
      "Identification": "1234567890", 
      "Leave_Date": "2017-12-03", 
      "Number_Room": "101", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-12-01", 
      "Cell_Phone": "3056525421", 
      "Document_Type": "01", 
      "Email": "cliente@correo.com", 
      "Id_Hotel": "02", 
      "Id_Reserva": "CR170003", 
      "Identification": "0987654321", 
      "Leave_Date": "2017-12-03", 
      "Number_Room": "401", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-11-01", 
      "Cell_Phone": "3001234523", 
      "Document_Type": "01", 
      "Email": "usuario2@correo.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170004", 
      "Identification": "1234567888", 
      "Leave_Date": "2017-11-03", 
      "Number_Room": "201", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-11-01", 
      "Cell_Phone": "3001567343", 
      "Document_Type": "01", 
      "Email": "usuario3@correo.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170005", 
      "Identification": "12345677777", 
      "Leave_Date": "2017-11-03", 
      "Number_Room": "301", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-12-01", 
      "Cell_Phone": "30034565456", 
      "Document_Type": "01", 
      "Email": "usuario4@correo.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170006", 
      "Identification": "98756712341", 
      "Leave_Date": "2017-12-03", 
      "Number_Room": "101", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-10-01", 
      "Cell_Phone": "3007654532", 
      "Document_Type": "01", 
      "Email": "usuario5@correo.com", 
      "Id_Hotel": "02", 
      "Id_Reserva": "CR170007", 
      "Identification": "1152439890", 
      "Leave_Date": "2017-10-03", 
      "Number_Room": "401", 
      "State": "InActive"
    }, 
    {
      "Arrive_Date": "2017-10-21", 
      "Cell_Phone": "3056525421", 
      "Document_Type": "01", 
      "Email": "cliente@correo.com", 
      "Id_Hotel": "02", 
      "Id_Reserva": "CR170008", 
      "Identification": "0987654321", 
      "Leave_Date": "2017-10-25", 
      "Number_Room": "402", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-10-21", 
      "Cell_Phone": "3007654532", 
      "Document_Type": "01", 
      "Email": "usuario5@correo.com", 
      "Id_Hotel": "02", 
      "Id_Reserva": "CR170009", 
      "Identification": "1152439890", 
      "Leave_Date": "2017-10-25", 
      "Number_Room": "401", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-04-16", 
      "Cell_Phone": "3007654532", 
      "Document_Type": "01", 
      "Email": "usuario5@correo.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170010", 
      "Identification": "1152439890", 
      "Leave_Date": "2017-04-19", 
      "Number_Room": "301", 
      "State": "InActive"
    }, 
    {
      "Arrive_Date": "2017-04-21", 
      "Cell_Phone": "3056525421", 
      "Document_Type": "01", 
      "Email": "cliente@correo.com", 
      "Id_Hotel": "02", 
      "Id_Reserva": "CR170011", 
      "Identification": "0987654321", 
      "Leave_Date": "2017-04-25", 
      "Number_Room": "402", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-12-12", 
      "Cell_Phone": "321", 
      "Document_Type": "CC", 
      "Email": "yeifer@yh", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170002", 
      "Identification": "123", 
      "Leave_Date": "2017-12-12", 
      "Number_Room": "102", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-12-12", 
      "Cell_Phone": "3456787687", 
      "Document_Type": "cc", 
      "Email": "jhonatorozco@gmail.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170002", 
      "Identification": "1040046999", 
      "Leave_Date": "2017-12-12", 
      "Number_Room": "103", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-10-28", 
      "Cell_Phone": "2424241", 
      "Document_Type": "cc", 
      "Email": "yoinergomez@gmail.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170002", 
      "Identification": "108989786", 
      "Leave_Date": "2017-10-31", 
      "Number_Room": "101", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-10-27", 
      "Cell_Phone": "1511512", 
      "Document_Type": "cc", 
      "Email": "yoinergomez@gmail.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170002", 
      "Identification": "18978333333", 
      "Leave_Date": "2017-10-30", 
      "Number_Room": "202", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2018-12-12", 
      "Cell_Phone": "321", 
      "Document_Type": "CC", 
      "Email": "yeifer@yh", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170002", 
      "Identification": "123", 
      "Leave_Date": "2018-12-12", 
      "Number_Room": "102", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2017-11-28", 
      "Cell_Phone": "3214567890", 
      "Document_Type": "cc", 
      "Email": "leidybd@gmail.com", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR170002", 
      "Identification": "719632147", 
      "Leave_Date": "2017-11-30", 
      "Number_Room": "201", 
      "State": "Active"
    }, 
    {
      "Arrive_Date": "2018-10-31", 
      "Cell_Phone": "321", 
      "Document_Type": "CC", 
      "Email": "yeiferhh@yh", 
      "Id_Hotel": "01", 
      "Id_Reserva": "CR1230110220181031", 
      "Identification": "123", 
      "Leave_Date": "2018-10-31", 
      "Number_Room": "102", 
      "State": "Active"
    }
  ]
})
      print("Test 5 Ready")


if __name__ == '__main__':
    unittest.main()