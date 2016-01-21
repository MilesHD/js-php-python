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
                   <div id="IndicatorError">Please enter a valid indicator Id.</div> 
                   <div id="DaysBackError">Please enter a number of days back.</div> 
                   <div id="SourcesError">Please select at least one source.</div> 
                   <div id="UnknownError">Something went wrong. Please check your inputs and
                   contact the application admin if problem persists.</div> 
                </div>
                <div class="medusaMenuControls">
                   <form id="MedusaQuery">
                        <label for="indicator"></label>
                        <input type="text" name="indicator" id="Indicator" 
                        class="medusaMenuControlsInput" placeholder="Indicator">

                        <label for="daysBack"></label>
                        <input type="number" name="daysBack" id="DaysBack" 
                        class="medusaMenuControlsInput" placeholder="DaysBack">

                        <div class="medusaMenuControlsSources">
                            Sources
                            <input type="checkbox" name="sources" value="ETJF"> ETFJ 
                            <input type="checkbox" name="sources" value="HF"> HF 
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
