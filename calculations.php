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
