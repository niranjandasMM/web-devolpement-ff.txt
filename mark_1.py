# # import sqlite3
# # conn = sqlite3.connect("mark1.db")
# # conn.execute("create table mark1 ( UID	INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL, thought TEXT UNIQUE NOT NULL)")

# # import datetime
# # import sqlite3
 
# # # get the current datetime and store it in a variable
# # currentDateTime = datetime.datetime.now()

# # # make the database connection with detect_types
# # conn = sqlite3.connect('drm.db',
# #                              detect_types=sqlite3.PARSE_DECLTYPES |
# #                              sqlite3.PARSE_COLNAMES)
# # cur = conn.cursor()
 
# # conn.execute("create table drm1 ( UID	INTEGER PRIMARY KEY AUTOINCREMENT,Time_of_record TIMESTAMP,goal TEXT NOT NULL, goal_desc TEXT  NOT NULL, when_you_offically_started TEXT  NOT NULL,learnings TEXT NOT NULL,improvement TEXT  NOT NULL,category TEXT  NOT NULL)")
# # # create query to insert the data
# # insertQuery = """INSERT INTO drm1 (Time_of_record, goal,goal_desc,when_you_offically_started,learnings,improvement,category)
# #     VALUES (?, ?, ?, ?, ?, ?, ?);"""

# # # insert the data into table
# # conn.execute(insertQuery, (currentDateTime,"Being Positive","im practising being positive ",
# # "well i started to plan of attack from januray 2022 , the beggining . started as one of my new year resoultiosn and to make my life more planned and discliplned and better , but inbetween i somehow failed a lot ofd times , but actaul implentation started from april and march , but no real consistency was found , iam trying daily to think positve and rameanin consistency so that it can became a habit for my mind in subconsious . i think now i have started more to foucs on being postive , i think its goona work graduulay step by step . i am never goona give up "
# # ,"as usual when iam doing nothing and thoughts came up , however i mostly dwell on negative thoughts which happend to me in the past i mean i know what and wehre i went wronf , but it is life , no matter what you goota move on like others animals and nature , and you dont have to worry about those stupid people's making you less worthy , you know who you you are and what you are capable of , you have faced and struggled a lot and went thorugha lot and learned a lot , still you are learning and going on and have a positive aspect towards your life and trying to achoeve your great dreams , its life you have to go through it , dont take anything too personally , cuz its people who creates probelms , you cant dwell in thoer world  , even they are struggling with thier own life , so forget what they think and start doing what you love , and thus i clear my negatives thoughs and move on . when ever i start having nergatives thoughts about me and having self doubt , i think about the positive aspect of me , positives scnes of me , thaths how you defeats your negatives , your gang is bigger than your negatives . And one thing which worries me is that people around me and friends always take me lighlty , cuz i dont have that badass actions and all , and my personality is differant but indeed i know im atleast better than them who are not being themselevs , and hell yeah one thing is for sure when times comes i dont hesistae and will beat the shit out of somebody without even thinking , thats it i will go for it no matter , i got beat up or got pucnhes i will fight with all i got , chathal virilla , i wont rep[aet my mistakes from past and feel regreted , thats all and iam trying to accomlosh my works and protise as much as i can , for me now not studying and reveisong is giving me a lot of  insatisfactriona and negatives thoughts , but i will cover it up and solev like as i always do . ",
# # " i ahve been follwing to try being positive and ingonre all negatives thoughts an past events but somehow i end up but yeah imporvemnt is there indeeed , i came up positive past thougths to tackle my negative shtoughts and i always win , i dont overthink over anything which make easy for me live happily and focus on work . "
# # ,"Mindest"))

# # print("Data Inserted Successfully !")
 
# # # commit the changes,
# # # close the cursor and database connection
# # conn.commit()
# # cur.close()
# # conn.close()

# from flask import Flask, render_template, request,redirect,flash,url_for, session
# from flask_sqlalchemy import SQLAlchemy
# from datetime import timedelta
# from sqlalchemy.sql import func
# import datetime

# app = Flask(__name__,template_folder='template')
# app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///users.sqlite3'
# app.permanent_session_lifetime = timedelta(minutes=2)
# db = SQLAlchemy(app)

# class users(db.Model):
#     id = db.Column("id", db.Integer, primary_key=True)
#     user = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     email = db.Column(db.String(100))

#     def __init__(self,user,email):
#         self.user = user
#         self.email = email

# @app.route("/")
# def index():
#     return render_template("home2.html")

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method== "POST":
#         session.permanent = True
#         user = request.form["user"]
#         passw = request.form["passw"]
#         session["user"] = user

#         found_user = users.query.filter_by(user=user).first()
#         if found_user:
#             session["passw"]= found_user.email
#         else:
#             usr = users(user, passw)
#             db.session.add(usr)
#             db.session.commit()
#         flash("Login Succeussfully")
#         return redirect(url_for("user"))
#     else:
#         if "user" in session:
#             flash("Already loged in")
#             return redirect(url_for("user"))
        
#         return render_template("login.html")

# @app.route("/user",methods=["POST","GET"])
# def user():
#     passw = None
#     if "user" in session:
#         user = session["user"]

#         if request.method == "POST":
#             passw = request.form["passw"]
#             session["passw"] = passw
#             found_user = users.query.filter_by(user=user).first()
#             found_user.passw= passw
#             db.session.commit()
#             flash("passw was saved ")
#         else:
#             if "passw" in session:
#                 passw = session["passw"]
        
#         return render_template("user.html",passw=passw)
#     else:
#         flash("You are not logged in !")
#         return redirect(url_for("login"))

# @app.route("/login_view")
# def login_view():
#     return render_template("login_view.html",values=users.query.all())


# if __name__ == "__main__":
#     db.create_all()
#     app.secret_key='admin123'
#     app.run(debug=True)

from flask import Flask, render_template, request,redirect,flash,url_for, session
import sqlite3
import datetime

from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from sqlalchemy.sql import func
import datetime

app = Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///drm1.sqlite3'
app.permanent_session_lifetime = timedelta(minutes=2)
db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column("UID", db.Integer, primary_key=True)
    Time_of_record = db.Column(db.DateTime(timezone=True), server_default=func.now())
    goal = db.Column(db.String(100))
    goal_desc = db.Column(db.String(1000))
    when_you_offically_started = db.Column(db.String(100))
    learnings = db.Column(db.String(1000))
    improvement = db.Column(db.String(1000))
    category = db.Column(db.String(10))

    def __init__(self,goal,goal_desc,when_you_offically_started,learnings,improvement,category):
        # self.Time_of_record = Time_of_record
        self.goal = goal
        self.goal_desc = goal_desc
        self.when_you_offically_started = when_you_offically_started
        self.learnings = learnings
        self.improvement = improvement
        self.category = category

usr = users("dfdf", "gfg", "gthjy", "pqwdsa", "ptor", "skills"  )
db.session.add(usr)
db.session.commit()