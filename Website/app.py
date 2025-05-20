from flask import Flask, render_template, redirect , request, url_for, session
import pyrebase
from datetime import datetime
import random
import googlemaps
config = {
  "apiKey": "AIzaSyDNzmz-XuofVXxBkg_8YJ7RA-T3Tut86I8",
  "authDomain": "leaf-detector-robot.firebaseapp.com",
  "projectId": "leaf-detector-robot",
  "storageBucket": "leaf-detector-robot.firebasestorage.app",
  "messagingSenderId": "826780316854",
  "appId": "1:826780316854:web:eb492c616ce57d69406217",
  "databaseURL":"https://leaf-detector-robot-default-rtdb.europe-west1.firebasedatabase.app/"
}# משתנה שמכיל את כל ההגדרות של פיירבייס

firebase = pyrebase.initialize_app(config) # משתנה של הפיירבייס
db = firebase.database()#משתנה של המסד נתונים
storage = firebase.storage() # משתנה של המאגר קבצים
auth = firebase.auth() # משתנה של מנהל ההזדהות

gmaps = googlemaps.Client(key="AIzaSyBBu7A9tY6X5AEm5MHcsN8ktghH4ZWuppQ")


app = Flask(__name__,template_folder='template',static_folder='static') # משתנה שמריץ את האתר 

@app.route("/")# מסמן את הכתובת שאליה הפונקציה שולחת
def home():
    now = datetime.now()# לא יהיה קיים
    strnow = now.strftime("%Y-%m-%d %H:%M:%S")#לא יהיה קיים 
    # db.child("Uploads").child(strnow).set(random.randint(3,9))#לא יהיה קיים
    uploads = db.child("Uploads").get().val()#משיג מילון של כל ההעלאות
    return render_template("home.html", db=uploads,css=url_for('static', filename='des.css')) #מציג את הקובץ הנתון ומעביר לג'ינג'ה את המילון



@app.route("/stats/<key>")
def stats(key):#פונקציה לדף נתונים שמקבלת את התאריך כמשתנה
    stat=db.child("Uploads").child(key)#משיג מילון של כל הערכים תחת התאריך הנתון
    lat=stat.child("Lat").get().val()
    long=db.child("Uploads").child(key).child("Long").get().val()

    try:
      return render_template("stats.html",
                             img1=storage.child(key+"1.jpg").get_url("AdFvNtPX7JfgfX6pD037Hhq5OfC2"),
                             img2=storage.child(key+"2.jpg").get_url("AdFvNtPX7JfgfX6pD037Hhq5OfC2"),
                             img3=storage.child(key+"3.jpg").get_url("AdFvNtPX7JfgfX6pD037Hhq5OfC2"),
                             gas=stat.child("Gas_PPM").get().val(),
                             is_gas=stat.child("Is_Gas").get().val(),                         
                             lat=lat,
                             long=long,                            
                             css=url_for('static', filename='des.css'))# מציג את הקובץ הנתון ומעביר לג'ינג'ה משתנים
    except:
      return render_template("stats.html",
                             img1=0,
                             img2=0,
                             img3=0,
                             gas=0,
                             is_gas=0,
                             lat=0,
                             long=0,                            
                             css=url_for('static', filename='des.css'))
  
if __name__ == "__main__":
    app.run(debug=True)