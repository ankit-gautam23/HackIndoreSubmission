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
    <title>Reports-OnlineMess</title>
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
        <input type="submit" value="Report" name="Report" />
        </form></center>
<hr>
							<div class="table-wrapper">
								<table class="alt">
									<thead>
										<tr>
											<th>Roll Number</th>
                                            <th>Date</th>
											<th>Breakfast</th>
											<th>Lunch</th>
                                            <th>Dinner</th>
										</tr>
									</thead>
									<tbody>
                                    
                                    
""")
import datetime

date = str(datetime.date.today())
btnd = form.getvalue('Report')

if btnd!= None:
    dates = str(form.getvalue('datess'))
    query="select * from mess where date = '"+dates+"'"
    res = curs.execute(query)
    data = curs.fetchall()
    for n in data:
        print("<tr>")
        print("<td>'"+str(n[0])+"'</td>")
        print("<td>'"+str(n[1])+"'</td>")
        print("<td>'"+str(n[2])+"'</td>")
        print("<td>'"+str(n[3])+"'</td>")
        print("<td>'"+ str(n[4])+"'</td>")
        print("</tr>")

        
print("""								    

                                    </tbody>		
								</table>
							</div>
                            <center><a href="apanel.py" class="button">Add Products</a></center>
						
   
</body>
</html>

""")


