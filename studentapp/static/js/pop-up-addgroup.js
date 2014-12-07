// POP-UP MENU ADD GROUP
$.ajax({
   type: "GET",
   url: "/groups/add/ #div_id_name_group",
   dataType: "html",
   success: function(data){
        // Open pop-up
        $("#button-add-group").click(function() {
            $("#div_id_name_group_popup").load("/groups/add/ #div_id_name_group");
            $("#div_id_king_group_popup").load("/groups/add/ #div_id_king_group");
            });

        var str = find('input, select');

        $("#button-add-group").click(function() {
            $.ajax({
                url: '/groups/add/',
                type: 'POST',
                data: str
            })
        });
    }
});
// $(document).ready(function(){
//   $('#myModal').modal()
// });
