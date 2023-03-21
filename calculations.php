<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="stylesheet.css" />
</head>
<body>
<h1 class="text">Here are your results!</h1>
<br>
<br>
<?php
if ( isset( $_POST['diameter'] ) ){
    $diameter = $_POST['diameter'];
    $pi = 3.14159;
    $radius = $diameter / 2;
    $circumference = 2 * $pi * $radius;
    $area = $pi * $radius * $radius;
    echo "The circumference is: " . $circumference . "<br>";
    echo "The area is: " . $area;
    
}
?>
<br>
<br>
<p>Click on the link below to go back to the main page.</p>
<a href="./index.html">Click here</a>
</body>
</html>
