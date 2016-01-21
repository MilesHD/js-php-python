<?php
    // This script is only an integration point between the client and the python script

    // Get indicator, daysBack, and sources submitted from client
    $indicator = $_POST["indicator"];
    $daysBack = $_POST["daysBack"];
    $sources = $_POST["sources"];

    // run script.py, passing in arguments
    $response = exec("python script.py " . $indicator . " " . $daysBack . " " . $sources);

    // pass the values written to stdout from script.py
    echo $response;
?>
