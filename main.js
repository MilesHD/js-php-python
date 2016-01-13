$(document).ready(function () {

    function render(nodes, edges) {
        var container, data, options, network;
        container = document.getElementById("visualization");
        data = {
            nodes: new vis.DataSet(nodes),
            edges: new vis.DataSet(edges)    
        };
        options = {};
        network = new vis.Network(container, data, options);
    }

    $("#submit-ajax-form").click(function handleAjaxForm(evt) {
        evt.preventDefault();
        
        // Get Name
        var name = $("#name").val().trim();

        // Validation
        if (name === undefined || name === "") {
           alert("Please enter a name"); 
           return false;
        }

        // Make Ajax Call
        var jqxhr = $.ajax({
            type: "POST",
            url: "./controller.php",
            data: {name: name}
        })
        .done(function handleJQXHR(data) {
            var splitData, nodes, edges;
            console.log("Data Arrived ", data);
            splitData = data.split("split");
            nodes = JSON.parse(splitData[0]);
            edges = JSON.parse(splitData[1]);

            $("#response").html(data);
            render(nodes, edges);

        });
    });

});
