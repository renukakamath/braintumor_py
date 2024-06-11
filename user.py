from flask import *
from database import*
import uuid
from newcnn import *

user=Blueprint('user',__name__)

@user.route('/user_home')
def user_home():
	return render_template("user_home.html")


@user.route('/user_send_complaints',methods=['get','post'])
def user_send_complaints():
	data={}
	uid=session['uid']

	if 'submit' in request.form:
		
		complaint=request.form['Complaint']
		q="INSERT INTO `enquiry`VALUES(null,'%s','%s','pending',NOW())"%(uid,complaint)
		insert(q)

		flash("success...")

		return redirect(url_for('user.user_send_complaints'))

	q="SELECT * FROM `enquiry` WHERE `user_id`='%s'"%(uid)
	res=select(q)
	data['complaints']=res
	return render_template("user_send_complaints.html",data=data)


@user.route('/user_upload_file',methods=['get','post'])
def user_upload_file():
	data={}
	uid=session['uid']
	if 'upload' in request.form:
		file=request.files['file']

		path='static/uploads'+str(uuid.uuid4())+file.filename
		file.save(path)
		n='Normal'
		s=predictcnn(path)

		if s==0:
			print("Normal")
			n="Normal"
		elif s==1:
			print("glioma")
			n="glioma"
		elif s==2:
			print("meningioma")
			n="meningioma"
		elif s==3:
			print("notumor")
			n="notumor"
		elif s==4:
			print("pituitary")
			n="pituitary"
			

		print(s)
		q="insert into upload_file values(null,'%s','%s','%s')"%(uid,path,n)
		insert(q)
		flash("Added Successfully.......!")
		return redirect(url_for('user.user_upload_file'))

	q="select * from upload_file WHERE user_id='%s'"%(uid)
	res=select(q)
	data['upload']=res
	return render_template("user_upload_file.html",data=data)

@user.route('/user_view_disease',methods=['get','post'])
def user_view_disease():
	data={}
	q="SELECT * FROM `disease` INNER JOIN `medicine` USING(`disease_id`) INNER JOIN `symptoms` USING(`disease_id`)"
	data['view']=select(q)
	return render_template('user_view_disease.html',data=data)

@user.route('/user_basic_details',methods=['get','post'])
def user_basic_details():
	data={}
	name=request.args['name']
	q="SELECT * FROM `disease` where disease='%s'"%(name)
	data['diseaseview']=select(q)
	
	q="select * from medicine"
	data['ageview']=select(q)

	med="no specific medicine for this age"
	

	if 'submit' in request.form:
		disease=request.form['disease']
		age=request.form['age']
		q="select * from medicine where age='%s'"%(age)
		val=select(q)
		if val:
			med=val[0]['medicine']
		else:
			flash("no specific medicine for this age")
		q="INSERT INTO `predict_medicine` VALUES(NULL,'%s','%s','%s','%s')"%(session['uid'],disease,age,med)
		insert(q)

	q="SELECT * FROM `disease` INNER JOIN `predict_medicine` USING(`disease_id`)"
	data['view']=select(q)
	return render_template('user_basic_details.html',data=data,name=name)