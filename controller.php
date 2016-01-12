<?php
    $name = $_POST["name"];
    $greeting = exec("python script.py");
    echo $greeting . " " . $name;
?>
