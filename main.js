$(document).ready(function () {

    'use strict';

    // Draw network visualization from nodes and edges JSON
    // objects returned from server
    function render(nodes, edges) {
        var container, data, options, network;
        container = document.getElementById("MedusaVis");
        data = {
            nodes: new vis.DataSet(nodes),
            edges: new vis.DataSet(edges)    
        };
        options = {};
        network = new vis.Network(container, data, options);
    }

    $("#SubmitQuery").click(function handleAjaxForm(evt) {
        var indicator, daysBack, sources, serializedSources;
        evt.preventDefault();
        
        // Get Indicator, DaysBack, and Sources Inputs 
        indicator = $("#Indicator").val().trim();
        daysBack = $("#DaysBack").val().trim();
        sources = $('input[name="sources"]:checked').map(function() {
            return $(this).val();
        });
        sources = sources.toArray().slice(0, 2);

        // Validation
        $(".medusaMenuValidationError div").hide();
        if (indicator === undefined || indicator === "") {
            $("#IndicatorError").show();
            return false;
        }
        if (daysBack === undefined || daysBack === "") {
            $("#DaysBackError").show();
            return false;
        }
        if (sources.length === 0) {
            $("#SourcesError").show();
            return false;
        }

        // Serialize sources for Ajax Call 
        serializedSources = sources.toString();

        // Make Ajax Call to perform CRITS query
        var jqxhr = $.ajax({
            type: "POST",
            url: "./controller.php",
            data: {
                indicator: indicator,
                daysBack: daysBack,
                sources: serializedSources 
            }
        })
        // Handle server response, render visualization
        // with JSON nodes and edges
        .done(function handleJQXHR(data) {
            var splitData, nodes, edges;
            console.log("Query Completed Successfully!");
            splitData = data.split("SPLIT");
            nodes = JSON.parse(splitData[0]);
            edges = JSON.parse(splitData[1]);

            $("#ServerOutput").html(data);
            //render(nodes, edges);

        });
    });

});
