

#ספריות
import socket
import pyrebase
import os
import pickle


# הגדרות של פיירבייס
firebase_config = {
  "apiKey": "AIzaSyDNzmz-XuofVXxBkg_8YJ7RA-T3Tut86I8",
  "authDomain": "leaf-detector-robot.firebaseapp.com",
  "projectId": "leaf-detector-robot",
  "storageBucket": "leaf-detector-robot.firebasestorage.app",
  "messagingSenderId": "826780316854",
  "appId": "1:826780316854:web:eb492c616ce57d69406217",
  "databaseURL":"https://leaf-detector-robot-default-rtdb.europe-west1.firebasedatabase.app/"
}
    


firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()
storage = firebase.storage()
##############################



# בדיקת חיבור לאינטרנט
def is_connected():
    try: 
        socket.create_connection(("8.8.8.8", 53))
        print("Connected To The Internet!")
        return True
    except:
        print("Not Connected To The Internet :(")
        return False
###################################


#בדיקה והעלאה של קבצים מקומיים
def are_local_files():
    is_dir = False
    try:
        os.mkdir("data")
        is_dir =True
        print("created")
    except FileExistsError:
        is_dir = True

    if is_dir:
        if len(os.listdir("data"))  == 0:
            print("No Local Files Detected, Moving On") 
        else:    
            for file in os.listdir("data"):
                print(file)#TODO debugging
                if file.endswith(".json"):
                    dict = pickle.load(open("data/" + file, "rb"))
                    Location = dict["Location"]
                    Gas = dict["Gas"]
                    Date = dict["Date"]
                    database.child("Uploads").child(Date).child("Long").set(Location[0])
                    database.child("Uploads").child(Date).child("Lat").set(Location[1])
                    database.child("Uploads").child(Date).child("Gas").set(Gas)
                 
                elif file.endswith(".png"):
                    storage.child(Date + ".png").put(file)
                    database.child("Uploads").child(Date).child("Img").push(storage.child(Date + ".png").get_url())
                    
                os.remove("data/" + file)
                
######################################





# התעוררת
if(is_connected()):
    are_local_files()

    
    
    
    
    
    
    