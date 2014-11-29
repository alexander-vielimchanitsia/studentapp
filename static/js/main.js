$.ajax({
   type: "GET",
   url: "/addstudent/ #tab-content",
   dataType: "html",
   success: function(addstudent){
    $("#button-add-student").click(function() {
        // $("#popup-box").html(addstudent);
        $("#tab-content", addstudent).appendTo("#popup-box").html();
        $("#ajax-fone").show();
        alert($("#tab-content", addstudent).html());
        });
    }
});