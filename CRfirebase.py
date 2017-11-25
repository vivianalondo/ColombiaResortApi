import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase import firebase


cred = credentials.Certificate('credential.json')
firebase_admin.initialize_app(cred, {
    "apiKey": "AIzaSyBPu2i5JN2L-THImOfA98EHnoj1M8j5mhw",
    "authDomain": "gohotels-5a589.firebaseapp.com",
    "databaseURL": "https://gohotels-5a589.firebaseio.com",
    "storageBucket": "gohotels-5a589.appspot.com"
})


user2 = auth.get_user_by_email('sandrislc@gmail.com')
print(user2.uid)
