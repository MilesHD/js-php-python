$(document).ready(function () {

    'use strict';

    // Draw network visualization from nodes and edges JSON
    // objects returned from server
    function render(nodes, edges, indicator) {
        var container, data, options, network;
        var colors = {
            yellow: '#FFFF00',
            green: '#4AA02C',
            blue: '#3BB9FF'
        };
        container = document.getElementById("MedusaVis");

        // Color nodes based on their type 
        nodes = nodes.map(function (node) {
           node.color = {};
           // User input indicator id
           if (node.id === indicator) {
                node.color.background = colors.yellow;
           // Reference node     
           } else if (node.type === "reference") {
                node.color.background = colors.green;
           // Indicator node
           } else {
                node.color.background = colors.blue;
           }
           return node;
        });
        data = {
            nodes: new vis.DataSet(nodes),
            edges: new vis.DataSet(edges)    
        };
        options = {
            nodes: {
                color: {
                    background: 'green'
                }
            }
        };
        network = new vis.Network(container, data, options);
    }

    $("#SubmitQuery").click(function handleAjaxForm(evt) {
        var indicator, daysBack, sources, serializedSources, linksOnly;
        evt.preventDefault();
        
        // Get Indicator, DaysBack, and Sources Inputs 
        indicator = $("#Indicator").val().trim();
        daysBack = $("#DaysBack").val().trim();
        sources = $('input[name="sources"]:checked').map(function() {
            return $(this).val();
        });
        sources = sources.toArray().slice(0, 2);
        linksOnly = $('input[name="links-only"]:checked').map(function() {
            return $(this).val();
        })[0];
        if (linksOnly !== 'yes') {
            linksOnly = 'no';
        }

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
                sources: serializedSources,
                linksOnly: linksOnly
            }
        })
        // Handle server response, render visualization
        // with JSON nodes and edges
        .done(function handleJQXHR(data) {
            var splitData, nodes, edges;
            console.log("AJAX Call Complete");

            // Error Handling
            $(".medusaMenuValidationError div").hide();
            if (data.substr(0, 5) === "ERROR") {
                if (data.substr(7) === "Invalid Indicator Id") {
                    $("#IndicatorError").show();
                } else {
                    $("#UnknownError").show();
                }
                return;    
            }

            // Python script can output one string, so nodes and edges JSON
            // were concatentated with 'SPLIT' string separating them
            splitData = data.split("SPLIT");
            nodes = JSON.parse(splitData[0]);
            edges = JSON.parse(splitData[1]);

            /********** DEVELOPMENT ONLY **********/
            $("#ServerOutput").html(data);
            /********** DEVELOPMENT ONLY **********/

            render(nodes, edges, indicator);

        });
    });

});
