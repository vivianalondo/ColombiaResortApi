
from datetime import datetime

class model:
			
	def get_all_hotels_info(self,conexion):
		hotels = conexion.db.hotels
  		rooms = conexion.db.rooms
  
  		responseHotels = []
  		responseRooms = []
  
	  	for hotel in hotels.find():
		    #hotel = hotels.find({Id_hotel: room['Id_Hotel']})
		    for room in rooms.find({"Id_Hotel":hotel['Id_Hotel']}):
		      responseRooms.append({"room_type" : room['Room_Type'],
		                        "capacity" :room['Hosts'],
		                        "price" :room['Price'],
		                        "currency" :hotel['Currency'],
		                        "room_thumbnail" :room['Room_Thumbnail'],
		                        "beds" :{"simple": room['Single_Bed'],
		                                  "double": room['Double_Bed']}}
		                        )

		    responseHotels.append({"hotel_id" : hotel['Id_Hotel'],
		                        "hotel_name" :hotel['Name'],
		                        "hotel_location":{"address":hotel['Address'],
		                                          "lat":hotel['Latitude'],
		                                          "long":hotel['Longitude']},
		                        "hotel_thumbnail" :hotel['Hotel_Thumbnail'],
		                        "check_in" :hotel['Check_In'],
		                        "check_out" :hotel['Check_Out'],
		                        "hotel_website" :hotel['Hotel_Website'],
		                        "rooms":responseRooms}

		      )
	  	response = {'result' : {
	                      "hotel" :responseHotels}}
	  	return response


	def get_disponible_rooms(self, conexion, arrive_date_param, leave_date_param, city_param , hosts_param, room_type_param):
	 	collection_hotels = conexion.db.hotels
		collection_rooms = conexion.db.rooms
		collection_reservations = conexion.db.reservations

		responseRooms = []
		response = []
		responseHotels = collection_hotels.find_one({'Area_Code' : city_param})
		for room in collection_rooms.find({"Id_Hotel":responseHotels['Id_Hotel'], "Hosts": int(hosts_param) , "Room_Type" : room_type_param}):

		    add = True
		    for reserve in collection_reservations.find({"Number_Room": room['Number_Room'], "State": "Active"}):
		       
		        Arrive_Date = datetime.strptime(reserve['Arrive_Date'], '%Y-%m-%d')
		        Leave_Date = datetime.strptime(reserve['Leave_Date'], '%Y-%m-%d')

		        if ((Arrive_Date <= arrive_date_param <= Leave_Date) or (Arrive_Date <= leave_date_param <= Leave_Date)) :
		            add = False


		    if add:
		      beds = {"simple": room['Single_Bed'],"double": room['Double_Bed']}
		      validator = True
		      for dato in responseRooms:
		        if dato['beds'] == beds :
		          validator = False
		          break
		      if validator:
		        responseRooms.append({"room_type" : room['Room_Type'],"capacity" :room['Hosts'],"price" :room['Price'],"currency" :responseHotels['Currency'],"description":room["Description"],"room_thumbnail" :room['Room_Thumbnail'],"beds" :{"simple": room['Single_Bed'],"double": room['Double_Bed']}})
		        
		        
		response = {"hotel_id" : responseHotels['Id_Hotel'],
		                      "hotel_name" :responseHotels['Name'],
		                      "hotel_location":{"address":responseHotels['Address'],
		                                        "lat":responseHotels['Latitude'],
		                                        "long":responseHotels['Longitude']},
		                      "hotel_thumbnail" :responseHotels['Hotel_Thumbnail'],
		                      "check_in" :responseHotels['Check_In'],
		                      "check_out" :responseHotels['Check_Out'],
		                      "hotel_website" :responseHotels['Hotel_Website'],
		                      "rooms":responseRooms}
		return response


	def create_reserve(self,conexion, arrive_date,leave_date,room_type,capacity,simple,double,hotel_id,doc_type,doc_id,email,phone_number):

	  collection_rooms = conexion.db.rooms
  	  collection_reservations = conexion.db.reservations

	  date_arrive_date = datetime.strptime(arrive_date, '%Y-%m-%d')
	  date_leave_date = datetime.strptime(leave_date, '%Y-%m-%d')
	  response = []
	  for room in collection_rooms.find({"Id_Hotel":hotel_id , "Hosts": capacity , "Room_Type" : room_type, "Single_Bed" : simple,"Double_Bed" : double}):
	      
	      add = True
	      for reserve in collection_reservations.find({"Number_Room": room['Number_Room'], "State": "Active"}):
	         
	          Arrive_Date = datetime.strptime(reserve['Arrive_Date'], '%Y-%m-%d')
	          Leave_Date = datetime.strptime(reserve['Leave_Date'], '%Y-%m-%d')
	          response.append({ "room" : room['Number_Room'],"Arrive_DateRes" : Arrive_Date,"date_arrive_date" : date_arrive_date,"Leave_DateRes" : Leave_Date})
	          if ((Arrive_Date <= date_arrive_date <= Leave_Date) or (Arrive_Date <= date_leave_date <= Leave_Date)) :
	              add = False


	      arrive = arrive_date.replace('-', '')
	      if add:
	        collection_reservations.insert(
	        {"Id_Reserva":"CR"+doc_id+hotel_id+room['Number_Room']+arrive,
	        "State":"Active",
	        "Id_Hotel":hotel_id,
	        "Number_Room":room['Number_Room'],
	        "Arrive_Date":arrive_date,
	        "Leave_Date":leave_date,
	        "Document_Type":doc_type,
	        "Identification":doc_id,
	        "Email":email,
	        "Cell_Phone":phone_number})
	        return ({"reservation_id":"CR"+doc_id+hotel_id+room['Number_Room']+arrive})
	  
	  return ({"message": arrive})


	def list_reservations(self,conexion):

  	  	collection_reservations = conexion.db.reservations

	  	response = []
	 	for reserve in collection_reservations.find():

		       	response.append({"Id_Reserva":reserve["Id_Reserva"],
		        "State":reserve["State"],
		        "Id_Hotel":reserve["Id_Hotel"],
		        "Number_Room":reserve["Number_Room"],
		        "Arrive_Date":reserve["Arrive_Date"],
		        "Leave_Date":reserve["Leave_Date"],
		        "Document_Type":reserve["Document_Type"],
		        "Identification":reserve["Identification"],
		        "Email":reserve["Email"],
		        "Cell_Phone":reserve["Cell_Phone"]})
		  	
	  	return ({"Reservas": response})