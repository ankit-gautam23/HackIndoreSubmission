#! C:/Users/Ankit/AppData/Local/Programs/Python/Python36-32/python.exe

print("Content-type: text/html")
print("")


import cgi
import cgitb
import MySQLdb
cgitb.enable()
db = MySQLdb.connect(host="localhost", user='root',password='kuber', database='messman')
curs = db.cursor()
form = cgi.FieldStorage()



print("""


<!DOCTYPE html>
<html >
<head>
 <link href="assets/css/signup.css" rel="stylesheet">
    <title>Products-BestSeller.COM</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="css/ie/html5shiv.js"></script><![endif]-->
		<script src="js/jquery.min.js"></script>
		<script src="js/jquery.poptrox.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-xlarge.css" />
		</noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
 <style>
 body{
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
<div>
        
<br><br>
<center><form>
        <h3>Enter Date : <input class="6u 12u$(small)" type="date" name="datess" />
        <input type="submit" value="Find" name="Find" />
        <a href="report.py" class="button special">Report<a/></form></center>
<ul class="actions">
<center><li><form><input type="submit" class="button special" value="BreakFast " name="breakfast"/></form></li>
<li><form><input type="submit" class="button special" value="Lunch" name="lunch"/></form></li>
<li><form><input type="submit" class="button special" value="Dinner" name="dinner"/></form></li>
</center></div>
<hr>

   
							<div class="table-wrapper">
								<table class="alt">
									<thead>
										<tr>
											<th>Item Name</th>
                                            <th>Description</th>
											<th>Item Price</th>
											<th>Image</th>
                                            <th>Delete</th>
										</tr>
									</thead>
									<tbody>
                                    
                                    
""")
import datetime

date = str(datetime.date.today())
btna = form.getvalue('breakfast')
btnb = form.getvalue('lunch')
btnc = form.getvalue('dinner')
btnd = form.getvalue('Find')

if btna!= None:
    query="select * from admain where date = '"+date+"' AND Type = '"+btna+"'"
    res = curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("<tr>")
        print("<td>'"+str(n[1])+"'</td>")
        print("<td>'"+str(n[4])+"'</td>")
        print("<td>'"+str(n[5])+"'</td>")
        print("<td><img src='images/"+str(n[2])+"' width='150px' height='150px'/></td>")
        print("<td><form><input type='submit' value='"+ str(n[3])+"' name='abtn'/></form></td>")
        print("</tr>")
        
if btnb!= None:
    query="select * from admain where date = '"+date+"' AND Type = '"+btnb+"'"
    res = curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("<tr>")
        print("<td>'"+str(n[1])+"'</td>")
        print("<td>'"+str(n[4])+"'</td>")
        print("<td>'"+str(n[5])+"'</td>")
        print("<td><img src='images/"+str(n[2])+"' width='150px' height='150px'/></td>")
        print("<td><form><input type='submit' value='"+ str(n[3])+"' name='abtn'/></form></td>")
        print("</tr>")

if btnc!= None:
    query="select * from admain where date = '"+date+"' AND Type = '"+btnc+"'"
    res = curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("<tr>")
        print("<td>'"+str(n[1])+"'</td>")
        print("<td>'"+str(n[4])+"'</td>")
        print("<td>'"+str(n[5])+"'</td>")
        print("<td><img src='images/"+str(n[2])+"' width='150px' height='150px'/></td>")
        print("<td><form><input type='submit' value='"+ str(n[3])+"' name='abtn'/></form></td>")
        print("</tr>")
if btnd!= None:
    dates = str(form.getvalue('datess'))
    query="select * from admain where date = '"+dates+"'"
    res = curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("<tr>")
        print("<td>'"+str(n[1])+"'</td>")
        print("<td>'"+str(n[4])+"'</td>")
        print("<td>'"+str(n[5])+"'</td>")
        print("<td><img src='images/"+str(n[2])+"' width='150px' height='150px'/></td>")
        print("<td><form><input type='submit' value='"+ str(n[3])+"' name='abtn'/></form></td>")
        print("</tr>")

        
print("""								    

                                     </tbody>		
								</table>
							</div>
                            <center><a href="apanel.py" class="button">Add Products</a></center>
						
   
</body>
</html>

""")


