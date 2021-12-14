<?php  
	$sid = $_POST['student_id'];
	$fname = $_POST['first_name'];
	$lname = $_POST['last_name'];
	$cjob = $_POST['current_job'];
	$location = $_POST['location'];
	$servername = "db-project.cjkzu1bulk3s.ap-south-1.rds.amazonaws.com";
	$username = "admin";
	$password = "G0d!sgreat";
	$database = "student";
	$conn = new mysqli($servername, $username, $password, $database);
	$q = "insert into student_info values ('$sid','$fname','$lname','$cjob','$location')";
	mysqli_query($conn,$q);
	mysqli_close($conn);
	include("./add.html");
?>
