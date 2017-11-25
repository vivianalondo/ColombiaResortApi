from firebase import firebase

firebase = firebase.FirebaseApplication('https://gohotels-5a589.firebaseio.com', None)
result = firebase.get('/users', None)
print result