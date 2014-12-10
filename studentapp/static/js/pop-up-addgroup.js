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
            $("#myModal").modal('hide'); // Ховаємо попап меню.
            $("#status-message-popup").show(); // Показуємо статус месседж.
            $("#status-message-text").text("Група успішно додана!"); // Додаємо текст в статус месседж.
            $("#content-columns").load("/groups/ #content-groups-list"); // Оновлюємо список груп.
        },
        error: function(data){
            console.log('error')
        }
    })
});
