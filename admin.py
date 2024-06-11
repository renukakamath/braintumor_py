from flask import *
from database import*
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template("admin_home.html")


@admin.route('/admin_view_user')
def admin_view_user():
	data={}
	q="select * from user"
	res=select(q)
	data['user']=res
	return render_template("admin_view_user.html",data=data)



@admin.route('/admin_view_complaints',methods=['get','post'])
def admin_view_complaints():
	data={}
	q="SELECT *,CONCAT(`fname`,' ',`lname`) AS `name` FROM `enquiry` INNER JOIN `user` USING(`user_id`)"
	res=select(q)
	print(res)
	print(q)
	data['complaints']=res

	j=0
	for i in range(1,len(res)+1):
		print(len(res))
		print('submit'+str(i))
		if 'submit'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(reply)
			print(j)
			print(res[j]['complaints_id'])
			q="update enquiry set reply='%s' where complaints_id='%s'" %(reply,res[j]['complaints_id'])
			print(q)
			update(q)
			flash("success")
			return redirect(url_for('admin.admin_view_complaints')) 	
		j=j+1
	return render_template("admin_view_complaints.html",data=data)



@admin.route('/admin_view_upload_files')
def admin_view_upload_files():
	data={}
	q="select * from user inner join upload_file using(user_id)"
	res=select(q)
	data['user']=res
	return render_template("admin_view_upload_files.html",data=data)

@admin.route('/admin_manage_disease',methods=['get','post'])
def admin_manage_disease():
	data={}
	if 'submit' in request.form:
		disease=request.form['disease']
		q="INSERT INTO `disease` VALUES(NULL,'%s')"%(disease)
		insert(q)

	if 'action' in request.args:
		action=request.args['action']
		dis_id=request.args['dis_id']
	else:
		action=None

	if action=='remove':
		q="DELETE FROM `disease` WHERE `disease_id`='%s'"%(dis_id)
		delete(q)

	if action=='update':
		q="SELECT * FROM `disease` WHERE `disease_id`='%s'"%(dis_id)
		data['up']=select(q)

	if 'update' in request.form:
		disease=request.form['disease']
		q="UPDATE `disease` SET `disease`='%s' WHERE `disease_id`='%s'"%(disease,dis_id)
		update(q)
		return redirect(url_for('admin.admin_manage_disease'))

	q="SELECT * FROM `disease`"
	data['view']=select(q)
	return render_template('admin_manage_disease.html',data=data)

@admin.route('/adimin_manage_symptoms',methods=['get','post'])
def adimin_manage_symptoms():
	data={}
	dis_id=request.args['dis_id']
	if 'submit' in request.form:
		symptoms=request.form['symptoms']
		q="INSERT INTO `symptoms` VALUES(NULL,'%s','%s')"%(dis_id,symptoms)
		insert(q)

	if 'action' in request.args:
		action=request.args['action']
		sym_id=request.args['sym_id']
	else:
		action=None

	if action=='remove':
		q="DELETE FROM `symptoms` WHERE `symptom_id`='%s'"%(sym_id)
		delete(q)

	if action=='update':
		q="SELECT * FROM `symptoms` WHERE `symptom_id`='%s'"%(sym_id)
		data['up']=select(q)

	if 'update' in request.form:
		symptoms=request.form['symptoms']
		q="UPDATE `symptoms` SET `symptoms`='%s' WHERE `symptom_id`='%s'"%(symptoms,sym_id)
		update(q)
		return redirect(url_for('admin.adimin_manage_symptoms',dis_id=dis_id))

	q="SELECT * FROM `symptoms` INNER JOIN disease USING(disease_id) WHERE `disease_id`=(SELECT `disease_id` FROM `disease` WHERE `disease_id`='%s' )"%(dis_id)
	print(q)
	data['view']=select(q)
	
	return render_template('adimin_manage_symptoms.html',data=data)

@admin.route('/admin_manage_medicines',methods=['get','post'])
def admin_manage_medicines():
	data={}
	dis_id=request.args['dis_id']
	if 'submit' in request.form:
		med=request.form['med']
		age=request.form['age']
		q="INSERT INTO `medicine` VALUES(NULL,'%s','%s','%s')"%(dis_id,age,med)
		insert(q)

	if 'action' in request.args:
		action=request.args['action']
		med_id=request.args['med_id']
	else:
		action=None

	if action=='remove':
		q="DELETE FROM `medicine` WHERE `medicine_id`='%s'"%(med_id)
		delete(q)

	if action=='update':
		q="SELECT * FROM `medicine` WHERE `medicine_id`='%s'"%(med_id)
		data['up']=select(q)

	if 'update' in request.form:
		med=request.form['med']
		age=request.form['age']
		q="UPDATE `medicine` SET `medicine`='%s', age='%s' WHERE `medicine_id`='%s'"%(med,age,med_id)
		update(q)
		return redirect(url_for('admin.admin_manage_medicines',dis_id=dis_id))

	q="SELECT * FROM `medicine` INNER JOIN disease USING(disease_id) WHERE `disease_id`=(SELECT `disease_id` FROM `disease` WHERE `disease_id`='%s' )"%(dis_id)
	print(q)
	data['view']=select(q)
	
	return render_template('admin_manage_medicines.html',data=data)