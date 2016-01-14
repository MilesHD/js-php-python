<!DOCTYPE html>
<html>
    <head>
        <title>
            JS-PHP-PYTHON AJAX Call
        </title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.12.0/vis.min.css">
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
       <div class="medusa">
            <div class="medusaMenu">
                <div class="medusaMenuHeader">
                   <img src="http://placehold.it/200x100"> 
                </div>
                <div class="medusaMenuValidationError">
                   <div id="ReferenceError">Please enter a valid reference</div> 
                   <div id="DaysBackError">Please enter a number of days back</div> 
                   <div id="SourcesError">Please select at least one source</div> 
                </div>
                <div class="medusaMenuControls">
                   <form id="MedusaQuery">
                        <label for="reference"></label>
                        <input type="text" name="reference" id="Reference" 
                        class="medusaMenuControlsInput" placeholder="Reference">

                        <label for="daysBack"></label>
                        <input type="number" name="daysBack" id="DaysBack" 
                        class="medusaMenuControlsInput" placeholder="DaysBack">

                        <div class="medusaMenuControlsSources">
                            Sources
                            <input type="checkbox" name="sources" value="DISE"> DSIE
                            <input type="checkbox" name="sources" value="GE"> GE 
                        </div>

                        <div>
                            <button id="SubmitQuery" class="medusaMenuButton medusaMenuButtonSubmit">Submit</button>
                            <button id="CleaerForm" class="medusaMenuButton medusaMenuButtonClear">Clear</button>
                        </div>
                    </form>
                </div>
            </div>
            <div id="MedusaVis" class="medusaVis">
            </div>
            <!-- DEVELOPMENT ONLY -->
            <div id="ServerOutput">
            </div>
       </div>
        <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.12.0/vis.min.js"></script>
        <script src="./main.js"></script>
    </body>
</html>
