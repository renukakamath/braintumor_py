from flask import * 
from database import * 

public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template("index.html")




@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=='admin':
				flash("login successfully....!")
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=='user':
				q="select * from user where login_id='%s'"%(session['lid'])
				res=select(q)
				print(res)
				if res:
					session['uid']=res[0]['user_id']
					flash("login successfully....!")
					return redirect(url_for('user.user_home'))
		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template("login.html")


@public.route('/user_registration',methods=['get','post'])
def user_registration():
	if 'manage' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		ph=request.form['ph']
		em=request.form['em']

		uname=request.form['uname']
		psw=request.form['psw']

		q="select * from login where username='%s' and password='%s'"%(uname,psw)
		res=select(q)
		if res:
			flash('THIS USER IS ALREADY EXIST')
		else:
			q="insert into login values(NULL,'%s','%s','user')"%(uname,psw)
			lid=insert(q)
			q="insert into user values(NULL,'%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,ph,em)
			insert(q)
			flash("Registration Completed.....!")
			return redirect(url_for('public.user_registration'))
	return render_template("user_registration.html")


