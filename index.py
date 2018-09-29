#! C:/Users/Ankit/AppData/Local/Programs/Python/Python36-32/python.exe

print("Content-type: text/html")
print("")


import cgi
import cgitb
import MySQLdb
import datetime
cgitb.enable()
db = MySQLdb.connect(host="localhost", user='root',password='kuber', database='messman')
curs = db.cursor()
form = cgi.FieldStorage()
date = str(datetime.date.today())

print("""

<!DOCTYPE HTML>
<html>
	<head>
		<title>Home-OnlineMess</title>
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
        marquee{
            margin-bottom:0 %;
            color:red;
        }
        </style>
	</head>
    
	<body id="top">

		<!-- Header -->
			<header id="header">
				<a href="alogin.py" class="image avatar"><img src="images/code%20seeker.jpg" alt="" /></a>
				<h1><strong>Online Mess</strong>, a super simple<br />
				Website for viewing and rating the items in the Mess<br/>
				made by <a href="#">Me and My Team</a>.</h1>
			</header>

		<!-- Main -->
			<div id="main">

				<!-- One -->
                               
					<section id="one">
						<header class="major">
							<center><h2>Today's item for Students Mess</h2></center>
						</header>
                        
					</section><hr>

""")
query = "select Notice from notice where date = '"+date+"'"
res =curs.execute(query)
data = curs.fetchall()
for n in data:
    print("<marquee onmouseover='this.stop();' onmouseout='this.start();'>")
    print("<ul>")
    print("<li><b>'"+str(n[0])+"'<b></li>")
    print("</ul>")
    print("</marquee>")
print("""


				<!-- Two -->
					<section id="two">
                        
                        <center><h2>BreakFast</h2></center>
						<div class="row">
                        
""")

query="select * from admain where date = '"+date+"' AND Type = 'BreakFast'"
res = curs.execute(query)
data = curs.fetchall()
for n in data:
    print("<article class='6u 12u$(xsmall)'>")
    print("<a href='images/"+str(n[2])+"' class='image fit thumb'><img width='200px' height='200px' src='images/"+str(n[2])+"'/></a>")
    print("<ul style='list-style:none;'><li><h3>"+str(n[1])+"</h3></li>")
    print("<li>"+str(n[4])+"</li>")
    print("<li>Rs "+str(n[5])+"</li></ul>")
    print("</article>")

print("""
                        </div>
                        <hr>
                        <form></form>
                        <center><h2>Lunch</h2></center>
						<div class="row">
                        
""")

query="select * from admain where date = '"+date+"' AND Type = 'Lunch'"
res = curs.execute(query)
data = curs.fetchall()
for n in data:
    print("<article class='6u 12u$(xsmall)'>")
    print("<a href='images/"+str(n[2])+"' class='image fit thumb'><img width='200px' height='200px' src='images/"+str(n[2])+"'/></a>")
    print("<ul style='list-style:none;'><li><h3>"+str(n[1])+"</h3></li>")
    print("<li>"+str(n[4])+"</li>")
    print("<li>Rs "+str(n[5])+"</li></ul>")
    print("</article>")


print("""
                        </div>
                        <hr>
                        <center><h2>Dinner</h2></center>
						<div class="row">
                        
""")

query="select * from admain where date = '"+date+"' AND Type = 'Dinner'"
res = curs.execute(query)
data = curs.fetchall()
for n in data:
    print("<article class='6u 12u$(xsmall)'>")
    print("<a href='images/"+str(n[2])+"' class='image fit thumb'><img width='200px' height='200px' src='images/"+str(n[2])+"'/></a>")
    print("<ul style='list-style:none;'><li><h3>"+str(n[1])+"</h3></li>")
    print("<li>"+str(n[4])+"</li>")
    print("<li>Rs "+str(n[5])+"</li></ul>")
    print("</article>")

print("""
						</div>
                        <hr>
                        
				<!-- Three -->
					<section id="three">
						<h2>Place Your Order</h2>
						<p></p>
						<div class="row">
							<div class="8u 12u$(small)">
								<form method="post" action="">
									<div class="row uniform 50%">
										<div class="12u$"><input type="text" name="roll" id="roll" placeholder="Roll Number" required/></div>
										<h4>BreakFast</h4>
										  <div class="6u 12u$">
										      <div class="select-wrapper">
											     <select name="breakfast" id="demo-category">
												    <option value="">- Choose -</option>
												    <option value="Yes">Yes</option>
                                                    <option value="No">No</option>
												</select>
										      </div>
									       </div>
										  
									   
                                       <h4>Lunch</h4>
                                       	  <div class="6u 12u$">
										      <div class="select-wrapper">
											     <select name="lunch" id="demo-category">
												    <option value="">- Choose -</option>
												    <option value="Yes">Yes</option>
                                                    <option value="No">No</option>
												</select>
										      </div>
									       </div>
										  
                                       <h4>Dinner</h4>
                                       	  <div class="6u 12u$">
										      <div class="select-wrapper">
											     <select name="dinner" id="demo-category">
												    <option value="">- Choose -</option>
												    <option value="Yes">Yes</option>
                                                    <option value="No">No</option>
												</select>
										      </div>
									       </div>
										  
									</div>
								<br>
								<ul class="actions">
									<li><input type="submit" name="messi" value="Submit" /></li>
								</ul>
                                                                </form>
							</div>
							<div class="4u$ 12u$(small)">
								<ul class="labeled-icons">
									<li>
										<h3 class="icon fa-home"><span class="label">Address</span></h3>
										Indore indori<br />
										Aurobindo, TN 00000<br />
										Madhya Pradesh
									</li>
									<li>
										<h3 class="icon fa-mobile"><span class="label">Phone</span></h3>
										000-000-0000
									</li>
									<li>
										<h3 class="icon fa-envelope-o"><span class="label">Email</span></h3>
										<a href="#">Ankicode4u@gmail.com</a>
									</li>
								</ul>
							</div>
						</div>
					</section>

                
				

		<!-- Footer -->
			<footer id="footer">
				<ul class="icons">
					<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
					<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
					<li><a href="#" class="icon fa-facebook"><span class="label">FaceBook</span></a></li>
					<li><a href="#" class="icon fa-envelope-o"><span class="label">Email</span></a></li>
				</ul>
				<ul class="copyright">
					<li>&copy; Ankicode</li><li>Design: <a href="">Ankit Gautam</a></li>
				</ul>
			</footer>
	</body>
</html> 


""")


messi = form.getvalue('messi')
if messi != None:
    roll=form.get('roll')
    a= form.getvalue('breakfast')
    b= form.getvalue('lunch')
    c= form.getvalue('dinner')
    query = "insert into mess values('"+roll+"','"+date+"','"+a+"','"+b+"','"+c+"')"
    res = curs.execute(query)
db.commit()
curs.close()
db.close()