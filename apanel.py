#! C:/Users/Ankit/AppData/Local/Programs/Python/Python36-32/python.exe

print("Content-type: text/html")
print("")

print("""

<!DOCTYPE HTML>

	<head>
		<title>Admin Panel-OnlineMess</title>
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
            h1{
                margin-top: 0px;
            }
            h3{
                margin-bottom: 0px;
            }
        </style>
	</head>
	<body id="top">

		<!-- Header -->
			<header id="header">
				<a href="index.py" class="image avatar"><img src="images/code%20seeker.jpg" alt="" /></a>
				<h1><strong>Online Mess</strong>, a super simple<br />
				Website for viewing and rating the items in the Mess<br/>
				made by <a href="#">Me and My Team</a>.</h1>
			</header>
		<!-- Main -->
		 	<div id="main">

                            
                            
                <div class="action small">
                         
                        
							<div class="box alt">
								<div class="row 50% uniform">
                                        <h1>Add Food details</h1>
                                        <form method="post" enctype="multipart/form-data">
                                        <input type="text" name="pname"  placeholder="Enter Product Name"/><br>
                                        <input type="text" name="pdesc"  placeholder="Enter Product Description"/><br>
										<input type="text" name="price" placeholder="Enter price"/><br>
										<div class="12u$">
                                            <div class="select-wrapper">
                                                <select name="pcate" id="pcate">
                                                    <option value="">- Item Category -</option>
                                                    <option value="BreakFast">BreakFast</option>
                                                    <option value="Lunch">Lunch</option>
                                                    <option value="Dinner">Dinner</option>
                                                    
                                                </select>
                                            </div>
                                        </div><br>
                                        <div class="actions">
                                            <label class="button"><span class="icon fa-upload"/> Product Image
											<input type="file" name="img" class="inputfile" required/>
                                            </label>
										</div>
									   <br>
                                        <ul class="actions fit small">
                                            <li><input type="submit" class="button special" name="btn" value="Submit"></li>
                                            <li><a href="aprod.py" class="button">View Products</a></li>
                                        </ul>
                                        </form>
                                        
                                </div><hr>
                                <center><h3>Create Notice</h3></center>
                                        <form>
                                            <input type="text" name="notice" placeholder="Notice"/><br>
                                            <input type="submit" class="button special" name="noti" value="Submit"/>
                                        </form>
                           		</div>
							</div>

                
		
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

import cgi
import cgitb
import MySQLdb
import datetime
cgitb.enable()
db = MySQLdb.connect(host="localhost", user='root',password='kuber', database='messman')
curs = db.cursor()
form = cgi.FieldStorage()
btn = form.getvalue('btn')
noti = form.getvalue('noti')
ndate = str(datetime.date.today())
if btn!=None:
    pname = form.getvalue('pname')
    pdesc = form.getvalue('pdesc')
    price = form.getvalue('price') 
    pcate = form.getvalue('pcate')
    pic=form['img']
    picpath=pic.filename
    picd=pic.file.read()
    pica= open("images/"+picpath,"wb")
    pica.write(picd)
    pica.close()
    sqlquery="insert into admain values('"+ ndate +"','"+ pname +"','"+ picpath +"','"+ pcate +"','"+ pdesc +"',"+ price +")"
    res = curs.execute(sqlquery)
if noti!=None:
    notices = form.getvalue("notice")
    query = "insert into notice values('"+ndate+"','"+notices+"')"
    res = curs.execute(query)
db.commit()
curs.close()
db.close()  