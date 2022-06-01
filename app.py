from flask import Flask, render_template, request,redirect,flash,url_for, session
import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from sqlalchemy.sql import func
import datetime

app = Flask(__name__,template_folder='template')
# app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///drm1.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://tovclgputfldjg:0bd23a1b03afefb6e11a265e2278ea00e2b8955621e4237d7ddd1b95fc077135@ec2-52-204-195-41.compute-1.amazonaws.com:5432/daqrqthu98nhbv'
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///mark1.sqlite3'
app.permanent_session_lifetime = timedelta(minutes=2)
db = SQLAlchemy(app)
app.secret_key='admin123'
user_cred = {"username":[],"password":[]}
user_cred["username"].append("player1");user_cred["password"].append("player1")

class mark1(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    thought = db.Column(db.String(1000))

    def __init__(self,thought,title):
        self.title = title
        self.thought = thought

@app.route("/")
def index():
    for u in user_cred['username']:
        if('user_cred' in session and session['user_cred'] == u):
            return render_template("home.html",data=f"Succussfully logged in as {u}")

    return render_template("login.html")

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')    
        for u in user_cred['username']:
            for p in user_cred['password']:
                if username == u and password == p:
                    print(f"yes {user_cred['username']}")  
                    session['user_cred'] = username
                    return redirect('/')
    
        msg='wrong password or username'
        return render_template("login.html",msg=msg)    #if the username or password does not matches 
        # if username == user_cred['username'] and password == user_cred['password']:
        #     session['user_cred'] = username
        #     return redirect('/')

    return render_template("login.html")

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        for u in user_cred['username']:
            for p in user_cred['password']:
                if username == u and password == p:    
                    msg='the username with this credentials already exist'
                    return render_template("register.html",msg=msg)
        user_cred["username"].append(username);user_cred["password"].append(password)
        msg=f"Succusffuly, registered as {username}, now you can log in with the entred credentials"
        return render_template("register.html",msg=msg)
    return render_template("register.html")  

@app.route('/logout')
def logout():
    session.pop('user_cred')         #session.pop('user') help to remove the session from the browser
    return redirect('/login')

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/delete/<int:id>",methods=['GET'])
def delete(id):
    user = mark1.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('Goal Deleted','warning')
    return redirect(url_for("view"))

@app.route("/edit/<string:id>",methods=['POST','GET'])
def edit(id):
    uidd = mark1.query.get(id)
    if request.method=='POST':
        db.session.delete(uidd)
        title = request.form["title"]
        thought = request.form["thought"]

        admin = mark1(title=title, thought=thought)
        db.session.add(admin)
        db.session.commit()
        flash('Goal Updated','success')
        return redirect(url_for("view"))

    rows = mark1.query.filter_by(id=id).first()
    return render_template("edit.html",rows=rows)

@app.route("/save_details", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            title = request.form["title"]
            thoughts = request.form["thought"]
            mark = mark1(title, thoughts  )
            db.session.add(mark)
            db.session.commit()
            # with sqlite3.connect("mark1.db") as con:
            #     cur = con.cursor()
            #     cur.execute("INSERT into mark1 (title, thought) values (?,?)", (title,thoughts))
            #     con.commit()
            msg = f" Successfully Added To SDRIA "
        except:
            # con.rollback()
            msg = "We can not add the targets report to the list"
        finally:
            return render_template("suc.html", msg=msg)
            # con.close()

@app.route("/view")
def view():
    # con = sqlite3.connect("mark1.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("select * from mark1")
    # row = cur.fetchall()
    return render_template("view.html",values=mark1.query.all())

# ~!-------- DRM Backend Starts From Here ~!------------ #
class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    Time_of_record = db.Column(db.DateTime(timezone=True), server_default=func.now())
    goal = db.Column(db.String(100))
    goal_desc = db.Column(db.String(1000))
    when_you_offically_started = db.Column(db.String(100))
    learnings = db.Column(db.String(1000))
    improvement = db.Column(db.String(1000))
    category = db.Column(db.String(10))

    def __init__(self,goal,goal_desc,when_you_offically_started,learnings,improvement,category):
        self.goal = goal
        self.goal_desc = goal_desc
        self.when_you_offically_started = when_you_offically_started
        self.learnings = learnings
        self.improvement = improvement
        self.category = category

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/drm")
def drm():
    # con = sqlite3.connect("drm.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("select * from drm1")
    # row = cur.fetchall()
    # return render_template("drm.html",rows=row)
    return render_template("drm.html",values=users.query.all())

@app.route("/create_add", methods=["POST", "GET"])
def create_add():
    msg = "msg"
    if request.method == "POST":
        try:
            goal = request.form["goal"]
            goal_desc = request.form["goal_desc"]
            currentDateTime = datetime.datetime.now()
            currentDateTime = currentDateTime.strftime("%c")
            started = request.form["when_you_offically_started"]
            learnings = "Not Yet"
            improvement = "Not Yet"
            category = request.form["category"]
            usr = users(goal, goal_desc, started, learnings, improvement, category  )
            db.session.add(usr)
            db.session.commit()
            # with sqlite3.connect("drm.db") as con:
            #     cur = con.cursor()
            #     cur.execute("INSERT into drm1 (Time_of_record,goal, goal_desc,when_you_offically_started,category,learnings,improvement) values (?,?,?,?,?,?,?)", (currentDateTime,goal,goal_desc,started,category,"Not Yet","Not Yet"))
            #     con.commit()
            msg = f"Your Goal is Sucussfully created "
        except:
            # con.rollback()
            msg = "We can not add the targets report to the list"
        finally:
            return render_template("suc.html", msg=msg)
            # con.close()

@app.route("/create_view")
def create_view():
    # con = sqlite3.connect("drm.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("select * from drm1")
    # row = cur.fetchall()
    return render_template("create_view.html",values=users.query.all())

@app.route("/create_delete/<int:id>",methods=['GET'])
def create_delete(id):
    # con=sqlite3.connect("drm.db")
    # cur=con.cursor()
    # cur.execute("delete from drm1 where UID=?",(uid,))
    # con.commit()
    user = users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('Goal Deleted','warning')
    return redirect(url_for("create_view"))
     
@app.route("/create_edit/<string:id>",methods=['POST','GET'])
def create_edit(id):
    uidd = users.query.get(id)
    # print(f"uidd is {uidd}")
    if request.method=='POST':
        db.session.delete(uidd)
        goal = request.form["goal"]
        goal_desc = request.form["goal_desc"]
        started = request.form["when_you_offically_started"]
        category = request.form["category"]
        learnings = request.form["learnings"]
        improvement = request.form["improvement"]
        # con=sqlite3.connect("drm.db")
        # cur=con.cursor()
        # cur.execute("update drm1 set goal=?,goal_desc=?,when_you_offically_started=?,category=?,learnings=?,improvement=? where UID=?",(goal,goal_desc,started,category,learnings,improvement,uid))
        # con.commit()

        admin = users(goal=goal, goal_desc=goal_desc, when_you_offically_started=started, category = category,learnings=learnings,
        improvement=improvement)
        db.session.add(admin)
        db.session.commit()
        flash('Goal Updated','success')
        return redirect(url_for("create_view"))
    # con=sqlite3.connect("drm.db")
    # con.row_factory=sqlite3.Row
    # cur=con.cursor()
    # cur.execute("select * from drm1 where UID=?",(uid,))
    # data=cur.fetchone()
    # rows=users.query.all()
    rows = users.query.filter_by(id=id).first()
    print(f"Rows are : {rows}")
    return render_template("create_edit.html",rows=rows)

if __name__ == '__main__':
    app.secret_key='admin123'
    db.create_all()
    app.run(debug=True)
