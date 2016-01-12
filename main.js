$(document).ready(function () {

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
            console.log("Data Arrived ", data);
        });
    });
});
