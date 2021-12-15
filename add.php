<?php  
	$sid = $_POST['student_id'];
	$fname = $_POST['first_name'];
	$lname = $_POST['last_name'];
	$cjob = $_POST['current_job'];
	$location = $_POST['location'];
	$servername = "192.168.236.173";
	$username = "root";
	$password = "G0d!sgreat";
	$database = "php_project";
	$conn = new mysqli($servername, $username, $password, $database);
	$q = "insert into student_info values ('$sid','$fname','$lname','$cjob','$location')";
	mysqli_query($conn,$q);
	mysqli_close($conn);
	include("./add.html");
?>
