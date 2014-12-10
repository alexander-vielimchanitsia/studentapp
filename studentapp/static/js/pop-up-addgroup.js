// POP-UP MENU ADD GROUP
// Open pop-up
$("#button-add-group").click(function() {
    $("#div_id_name_group_popup").load("/groups/add/ #div_id_name_group");
    $("#div_id_king_group_popup").load("/groups/add/ #div_id_king_group");
    });

$("#send-popup-form").click(function(e) {
    e.preventDefault()
    var mForm = $("#id-group-form-popup").serialize();
    $.ajax({
        url: '/groups/add/',
        type: 'POST',
        data: mForm,
        success: function(data){
            console.log(data)
            $("#myModal").modal('hide');
            $("#status-message-popup").show();
            $("#status-message-text").text("Група успішно додана!");
            $("#content-columns").load("/groups/ #content-groups-list");
        },
        error: function(data){
            console.log('error')
        }
    })
});
