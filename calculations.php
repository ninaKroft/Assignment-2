<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="stylesheet.css" />
</head>
<body>
<h1 class ="title">Here are your results!</h1>
<br>
<br>
<br>
<p class ="text">Click on the link below to go back to the main page.</p>
<a href="./index.html">Click here</a>
<br>
<br>
<br>
<?php
if ( isset( $_POST['diameter'] ) ){
    $diameter = $_POST['diameter'];
    $radius = $diameter / 2;

        function checkNegative($diameter) {
            if ($diameter<0) {
                throw new Exception("You entered a negative number. Please return to the calculator page and enter a valid number.");
            }
            return true;
        }

        function checkNumber($diameter) {
            return is_numeric($diameter);
        }

        function circumference($radius) {
            $pi = 3.14159;
            $circumference = 2 * $pi * $radius;
            return $circumference;
        }
    
        function area($radius){
            $pi = 3.14159;
            $area = $pi * $radius * $radius;
            return $area;
        }

    if (checkNumber($diameter) == False) {
        echo "You entered text. Please return to the calculator page and enter a valid number.";
        exit();
    }

    try {
        checkNegative($diameter);  #runs the checkNegative() function. If the number is negative, it will "throw" an exception.
    }
    catch(Exception $e) {
        echo "Error: " .$e->getMessage();   #If an exception is thrown by the checkNegative() function, this will "catch" it then print the error message I defined above then stop the code.
        exit();
    }
    echo "The circumference is: " . circumference($radius) . "<br>";
    echo "The area is: " . area($radius);
        
    }
        
?>

</body>
</html>
