// POP-UP MENU ADD STUDENT
$.ajax({
   type: "GET",
   url: "/students/add/ #tab-content-addstudent",
   dataType: "html",
   success: function(addstudent){
    // Open pop-up
    $("#button-add-student").click(function() {
        $("#tab-content-addstudent", addstudent).fadeIn(300).appendTo("#popup-box-addstudent").html();
        $("#ajax-fone-addstudent").fadeIn(300);
        $("#popup-menu").fadeIn(300);
        });
    // Close pop-up
    $("#popup-box-close-addstudent, #ajax-fone-addstudent").click(function() {
        $("#ajax-fone-addstudent, #popup-menu").fadeOut(300);
    });
    }
});
