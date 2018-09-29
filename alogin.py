#! C:/Users/Ankit/AppData/Local/Programs/Python/Python36-32/python.exe

print("Content-type: text/html")
print("")


print("""


<!DOCTYPE html>
<html >
<head>
 <link href="assets/css/signup.css" rel="stylesheet">
    <title>Admin Login-OnlineMess</title>
 <style>
 body{
	background-image: url(images/fulls/bg.jpg);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
	}
   .register-switch{
      background-color:#5b3256;
   }
     a{
         text-decoration: none;
         color: green;
     }
		</style>
 
 </head>

<body>
   <h1 class="register-title">Admin Login!!</h1>
   <form class="register" method="post">
    <input type="text" class="register-input" name="username" placeholder="ID">
    <input type="password" class="register-input" name="pswrd" placeholder="Password">
    <input type="submit" name="btn" value="Login" class="register-button">
    </form>
</body>
</html>



""")

import cgi
import cgitb
import MySQLdb

db = MySQLdb.connect(host="localhost", user='root',password='kuber', database='messman')
curs = db.cursor()
form = cgi.FieldStorage()
btn = form.getvalue('btn')


if btn!=None:
    uname= form.getvalue('username')
    psw = form.getvalue('pswrd')
    query = "select id, password from admin where id = '"+uname+"' and password = '"+psw+"'"
    res = curs.execute(query)
    if res == 1:
        print("Connection granted")
        print("<html><script>window.location='apanel.py'</script></html>")
    else:
        print("Access Denied, Wrong Credentials")
        
db.commit()
db.close()
curs.close()