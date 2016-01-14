$(document).ready(function () {

    'use strict';

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
        var reference, daysBack, sources, serializedSources;
        evt.preventDefault();
        
        // Get Name
        reference = $("#Reference").val().trim();
        daysBack = $("#DaysBack").val().trim();
        sources = $('input[name="sources"]:checked').map(function() {
            return $(this).val();
        });
        sources = sources.toArray().slice(0, 2);

        // Validation
        $(".medusaMenuValidationError div").hide();
        if (reference === undefined || reference === "") {
            $("#ReferenceError").show();
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

        // serialize for sending
        serializedSources = sources.toString();
        console.log(serializedSources);

        // Make Ajax Call to perform CRITS query
        var jqxhr = $.ajax({
            type: "POST",
            url: "./controller.php",
            data: {
                reference: reference,
                daysBack: daysBack,
                sources: serializedSources 
            }
        })
        // Handle server response, render visualization
        // with JSON nodes and edges
        .done(function handleJQXHR(data) {
            var splitData, nodes, edges;
            console.log("Data Arrived ", data);
            splitData = data.split("split");
            nodes = JSON.parse(splitData[0]);
            edges = JSON.parse(splitData[1]);

            //$("#response").html(data);
            render(nodes, edges);

        });
    });

});
