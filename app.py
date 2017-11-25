# mongo.py

from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from datetime import datetime
import model
import conexion

conn =conexion.connection()
app = conn.create_connection('colombiaresort','mongodb://localhost:27017/colombiaresort','DB_URI')
mongo = PyMongo(app)
m = model.model()

@app.route('/V1/AllRooms', methods=['GET'])
def get_all_hotels():
  return jsonify(m.get_all_hotels_info(mongo))

@app.route('/V1/rooms/', methods=['GET'])
def get_rooms():

  arrive_date_param = datetime.strptime(request.args.get('arrive_date'), '%Y-%m-%d')
  leave_date_param = datetime.strptime(request.args.get('leave_date'), '%Y-%m-%d')
  city_param = request.args.get('city')
  hosts_param = request.args.get('hosts')
  room_type_param = request.args.get('room_type')

  return jsonify(m.get_disponible_rooms(mongo,arrive_date_param, leave_date_param, city_param ,hosts_param, room_type_param))

@app.route('/V1/rooms/reserve', methods=['POST'])
def add_reserva():

  arrive_date = request.json['arrive_date']
  leave_date = request.json['leave_date']
  room_type = request.json['room_type']
  capacity = request.json['capacity']
  simple = request.json['beds']['simple']
  double = request.json['beds']['double']
  hotel_id = request.json['hotel_id']
  doc_type = request.json['user']['doc_type']
  doc_id = request.json['user']['doc_id']
  email = request.json['user']['email']
  phone_number = request.json['user']['phone_number']

  return jsonify(m.create_reserve(mongo, arrive_date,leave_date,room_type,capacity,simple,double,hotel_id,doc_type,doc_id,email,phone_number))

@app.route('/V1/AllReservations', methods=['GET'])
def get_all_reservations():
  return jsonify(m.list_reservations(mongo))


@app.route('/V1/reservations', methods=['GET'])
def get_my_reservations():
  token = request.headers['Authorization']
  email = m.validate_user(token)
  return jsonify(m.list_reservations_by_user(mongo,email))


if __name__ == '__main__':
    app.run()