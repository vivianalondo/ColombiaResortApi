import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase import firebase


#Este es el modulo para probar el token de la app en android
cred = credentials.Certificate('credentialtest.json')
firebase_admin.initialize_app(cred, {
    "apiKey": "AIzaSyAWVcK8FQHJ5mnGZOPj5MBLQXXSr9PndKM",
    "authDomain": "labcompumovilvl.firebaseapp.com",
    "databaseURL": "https://labcompumovilvl.firebaseio.com",
    "storageBucket": "labcompumovilvl.appspot.com"
})


token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ3NjA3YWVhMDdlOTQzNzA1MTdhNjEyNmExODRkMTI3MmE2OTY1OTEifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbGFiY29tcHVtb3ZpbHZsIiwibmFtZSI6IlNhbmRyYSBWaXZpYW5hIExvbmRvw7FvIENvcnTDqXMiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDYuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy10eUlUdFNyYWYwYy9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBQS9BTlEwa2Y1Uy1sblZ5dVJmRmtqTmpvODZGT21XcDg2N0pRL3M5Ni1jL3Bob3RvLmpwZyIsImF1ZCI6ImxhYmNvbXB1bW92aWx2bCIsImF1dGhfdGltZSI6MTUxMTYwMzUyNCwidXNlcl9pZCI6IjNwQWhhZmlaTDhVRTNMem1WT3JqdVoxc3FZbDIiLCJzdWIiOiIzcEFoYWZpWkw4VUUzTHptVk9yanVaMXNxWWwyIiwiaWF0IjoxNTExNjE1NDQ0LCJleHAiOjE1MTE2MTkwNDQsImVtYWlsIjoic3ZpdmlhbmFsb25kb25vQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTAwMTMzNjE0MDcxNTIyOTIxMDk1Il0sImVtYWlsIjpbInN2aXZpYW5hbG9uZG9ub0BnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.oOjs8xAR8Ym7wZ3fnG61ou7i2Btp27WPo_yNIk_0by8gg4VoeVoqDEj0MnltQo6beE0ykDC0LFLTL7ppZO0PSxenf1bAhQlCjwWZAidYbGHnaw0v9tqCPbD1_XccmB7zTAOcXTkDO-CHlCQECJr0WxKURPyOWGRlMdanak5I2ZNQnt34EJiDS7r2eXm9ZQDEEOEfWrWVNSUcxIdLZoikiq3zQ6abJvjdmei9eFcyomyNivUb1SNl1a_vjWBxvGLgbWO9_Gklb-pchzMAa0lQIvipzN9khWxzYqFbGOTeOXi69QzMaLGBIITqsG9jJk0teCryE9wzBAoVx0JIhpouJg"
decoded_token = auth.verify_id_token(token)
email = decoded_token['email']
print(email)