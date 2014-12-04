// POP-UP MENU ADD GROUP
$.ajax({
   type: "GET",
   url: "/groups/addgroup/ #tab-content-addgroup",
   dataType: "html",
   success: function(addgroup){
    // Open pop-up
    $("#button-add-group").click(function() {
        $("#tab-content-addgroup", addgroup).fadeIn(300).appendTo("#popup-box-addgroup").html();
        $("#ajax-fone-addgroup").fadeIn(300);
        });
    // Close pop-up
    $("#button-id-cancel, #ajax-fone-addgroup").click(function() {
        $("#ajax-fone-addgroup, #popup-box-addgroup").fadeOut(300);
    });
    }
});