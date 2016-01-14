<?php
    // Get name input submitted from client
    $reference = $_POST["reference"];
    $daysBack = $_POST["daysBack"];
    $sources = $_POST["sources"];

    // run script.py, passing in name
    $response = exec("python script.py " . $reference . " " . $daysBack . " " . $sources);
    // pass the values written to stdout from script.py
    echo $response;
?>
