from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key ='pri'

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="kGISL"
app.config["MYSQL_DB"]="fkiteissue"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
conn=MySQL(app)


@app.route('/',methods = ['GET','POST'])
def index():
   return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
   if request.method =='POST':
      rollno=request.form['rollno']
      password=request.form['password']
      con=conn.connection.cursor()

      sql="insert into login(rollno,password) values(%s,%s)"
      con.execute(sql,(rollno,password))
      con.connection.commit()
      con.close()
      return render_template('complaint.html')
   return render_template('login.html')



# @app.route('/login',methods = ['GET','POST'])
# def login():
#    if request.method =='POST':
#       rollno=request.form['rollno']
#       password=request.form['password']
#       name=request.form['rolno']
#       email=request.form['email']
#       pas=request.form['pass']
#       confirmpassword=request.form['confirmpassword']

#       if (rollno !=None and password !=None):
         
#          con=conn.connection.cursor()

#          sql="insert into login(rollno,password) values(%s,%s)"
#          con.execute(sql,(rollno,password))
#          con.connection.commit()
#          con.close()
#          return render_template('complaint.html')
#       # return render_template('login.html')
   
#       elif (rolno !=None and email != None and pas != None and confirmpassword !=None):
#          con=conn.connection.cursor()
      
#          sql="insert into (name,email,pas,confirmpassword) values(%s,%s,%s,%s)"
#          con.execute(sql,(name,email,pas,confirmpassword))
#          con.connection.commit()
#          con.close()
#          return render_template('login.html')
#       return render_template('complaint.html')
#    return render_template('login.html')
   

@app.route('/about',methods = ['GET','POST'])
def about():
   return render_template('about.html')

@app.route('/contact',methods = ['GET','POST'])
def contact():
   return render_template('contact.html')

@app.route('/complaint',methods = ['GET','POST'])
def complaint():

   return render_template('complaint.html')

@app.route('/admin',methods = ['GET','POST'])
def admin():
   return render_template('admin.html')

@app.route('/cleanliness',methods = ['GET','POST'])
def cleanliness():
    if(request.methods == 'POST'):
        issuename = request.form['issuename']
        date = request.form['date']
        proof = request.files['image']
        proof.save('uploads/'+ proof.filename)
        description = request.form['description']
        cur = conn.connection.cursor()
        with open('uploads/' + proof.filename,'rb') as file:
            binary_proof = file.read()
        cur.execute("insert into Cleanliness(issuename,date,proof,binary_proof,description) values(%s,%s,%s,%s,%s)" ,(issuename,date,proof.filename,binary_proof,description) )
        conn.connection.commit()
        cur.close()
        return redirect(url_for('success.html'))
    return render_template('cleanliness.html')

@app.route('/canteen',methods = ['GET','POST'])
def canteen():
   if(request.methods == 'POST'):
      complaint = request.form["complaint"]
      date = request.form["date"]
      proof = request.files["image"]
      proof.save("uploads/" + proof.filename)
      description = request.form["description"]
      cur = conn.connection.cursor()
      with open("uploads/" + proof.filename,"rb") as file:
         binary_proof = file.read()
      cur.execute("insert into Canteen(complaint,date,proof,binary_proof,description) values(%s,%s,%s,%s,%s)" ,(complaint,date,proof.filename,binary_proof,description))
      cur.commit()
      cur.close()
      return redirect(url_for('success.html'))
   return render_template('canteen.html')
   

@app.route('/Hostelissues',methods = ['GET','POST'])
def Hostelissues():
   if(request.methods == 'POST'):
      firstname = request.form['firstname']
      email = request.form['email']
      phone = request.form['phone']
      room = request.form['room']
      cot = request.form['cot']
      description = request.form['description']
      qualityoffood = request.form["qualityoffood"]
      details = request.form["details"]
      proof = request.files["image"]
      proof.save("uploads/"+ proof.filename)
      cur = conn.connection.cursor()
      with open("uploads/" + proof.filename,"rb")as file:
         binary_proof = file.read()
      cur.execute("insert into Hostel(firstname,email,phone,room,cot,description,qualityoffood,details,proof,binary_proof) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(firstname,email,phone,room,cot,description,qualityoffood,details,proof.filename,binary_proof))
      conn.connection.commit()
      cur.close()
      return redirect(url_for('success.html'))
   return render_template('Hostelissues.html')

@app.route('/restroom',methods = ['GET','POST'])
def restroom():
   if(request.methods == "POST"):
      complaint = request.form["complaint"]
      date = request.form["date"]
      proof = request.files["image"]
      proof.save("uploads/" + proof.filename)
      description = request.form["description"]
      cur = conn.connection.cursor()
      with open("uploads/" + proof.filename,"rb") as file:
         binary_proof = file.read()
      cur.execute("insert into Canteen(complaint,date,proof,binary_proof,description) values(%s,%s,%s,%s,%s)" ,(complaint,date,proof.filename,binary_proof,description))
      cur.commit()
      cur.close()
      return redirect(url_for('success.html'))
   return render_template('restroom.html')

@app.route('/Transportissues',methods = ['GET','POST'])
def Transportissues():
   if(request.methods == "POST"):
        issuename = request.form["issuename"]
        date = request.form["date"]
        proof = request.files["image"]
        proof.save("uploads/" + proof.filename)
        description = request.form["description"]
        cur = conn.connection.cursor()
        with open("uploads/" + proof.filename ,"rb") as file:
            binary_proof = file.read()
        cur.execute("insert into Transport(issuename,date,proof,binary_proof,description) values(%s,%s,%s,%s,%s)" , (issuename,date,proof.filename,binary_proof,description))
        cur.commit()
        cur.close()
        return redirect(url_for('success.html'))
   #  return render_template("transport.html")

   return render_template('Transportissues.html')

@app.route('/wifiissues',methods = ['GET','POST'])
def wifiissues():
   if(request.methods == "POST"):
      name = request.form["name"]
      email = request.form["email"]
      macaddress = request.form["macaddress"]
      otherissue = request.form["otherissue"]
      cur = conn.connection.cursor()
      cur.execute("insert into Wifi(name,email,macaddress,otherwise) values(%s,%s,%s,%s)" , (name,email,macaddress,otherissue))
      cur.commit()
      cur.close()
      return redirect(url_for('success.html'))
   return render_template('wifiissues.html')

@app.route('/infra',methods = ['GET','POST'])
def infra():
   if(request.methods=="POST"):
      complaint = request.form["complaint"]
      date = request.form["date"]
      proof = request.files["image"]
      proof.save("uploads/" + proof.filename)
      description = request.form["description"]
      cur = conn.connection.cursor()
      with open("uploads/" + proof.filename,"rb") as file:
         binary_proof = file.read()
      cur.execute("insert into Infra(complaint,date,proof,binary_proof,description) values(%s,%s,%s,%s,%s)" , (complaint,date,proof.file,binary_proof,description))
      cur.commit()
      cur.close()
      return redirect(url_for('success.html'))
    
   return render_template('infra.html')

@app.route('/success',methods = ['GET','POST'])
def success_msg_hostel():
    return render_template('success.html')
   





# @app.route('/',methods = ['GET','POST'])
# def login():
#    if request.method =='POST':
#       username=request.form['username']
#       password=request.form['password']
      
#       con=conn.connection.cursor()
#       sql="insert into login(username,password) values(%s,%s)"
#       con.execute(sql,(username,password))
#       con.connection.commit()
#       con.close()
#       return render_template('home.html')
#    return render_template('login.html')

# # @app.route('/homepage')
# # def homepage():
# #    if request.method =='POST':

# #       return render_template('home.html')
# #    return render_template('login.html')


# @app.route('/home')
# def home():
#    return render_template('home.html')
# @app.route('/hostel_issue_form')
# def hostel_issue_form():
#    return render_template('hostel_issue_form.html')

# # @app.route('/hostel_issue')
# # def hostel_issuee():
# #    if request.method =='POST':

# #       return render_template(redirect (url_for('hostel_issue_form.html')))
# #    return render_template('home.html')

# @app.route('/hostel_issue_form',methods = ['GET','POST'])
# def hostelissue():
#    if request.method =='POST':
#       name=request.form['firstName']
#       email=request.form['email']
#       room=request.form['room']
#       cot=request.form['cot']
#       natureOfComplaint=request.form['complaintNature']
#       quality=request.form['qualityOfFood']
#       description=request.form['detailsOfComplaint']
      
#       con=conn.connection.cursor()
#       sql="insert into hostelissue(name,email,room,cot,natureOfComplaint,quality,description) values(%s,%s,%s,%s,%s,%d,%s)"
#       con.execute(sql, (name,email,room,cot,natureOfComplaint,quality,description) )
#       con.connection.commit()
#       con.close()
#       return render_template('success_msg_hostel.html')
#    return render_template('hostel_issue_form.html')

# @app.route('/success_msg_hostel')
# def success_msg_hostel():
#    return render_template('success_msg_hostel.html')
   






if __name__=='__main__':
    app.run(debug=True)