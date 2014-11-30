// POP-UP MENU ADD STUDENT
$.ajax({
   type: "GET",
   url: "/addstudent/ #tab-content-addstudent",
   dataType: "html",
   success: function(addstudent){
    // Open pop-up
    $("#button-add-student").click(function() {
        $("#tab-content-addstudent", addstudent).fadeIn(300).appendTo("#popup-box-addstudent").html();
        $("#ajax-fone-addstudent").fadeIn(300);
        });
    // Close pop-up
    $('#button-id-cancel, #ajax-fone-addstudent').click(function() {
        $('#ajax-fone-addstudent, #popup-box-addstudent').fadeOut(300);
    });
    }
});
