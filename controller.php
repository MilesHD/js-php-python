<?php
    // Get name input submitted from client
    $name = $_POST["name"];
    // run script.py, passing in name
    $response = exec("python script.py " . $name);
    // pass the values written to stdout from script.py
    echo $response;
?>
