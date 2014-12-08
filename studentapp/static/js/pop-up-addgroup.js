// POP-UP MENU ADD GROUP
$.ajax({
   type: "GET",
   url: "/groups/add/ #div_id_name_group",
   dataType: "html",
   success: function(){
        // Open pop-up
        $("#button-add-group").click(function() {
            $("#div_id_name_group_popup").load("/groups/add/ #div_id_name_group");
            $("#div_id_king_group_popup").load("/groups/add/ #div_id_king_group");
            });

        $("#send-popup-form").click(function(e) {
            e.preventDefault()
            var mForm = $("#id-group-form-popup").serialize();
            $.ajax({
                type: 'POST',
                data: mForm,
                success: function(data){
                    console.log(data)
                },
                error: function(data){
                    console.log(data)
                }
            })
        });
    }
});
// $(document).ready(function(){
//   $('#myModal').modal()
// });
