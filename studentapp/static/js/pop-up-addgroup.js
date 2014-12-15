// POP-UP MENU ADD GROUP
// Open pop-up
$("#button-add-group").click(function() {
    $("#div_id_name_group_popup").load("/groups/add/ #div_id_name_group");
    $("#div_id_king_group_popup").load("/groups/add/ #div_id_king_group");
});

$("#send-popup-form").click(function(e) {
    e.preventDefault()
    var input = document.getElementsByName('name_group')[0],
        mForm = $("#id-group-form-popup").serialize(),
        textError = 'Поле обов’язкове';
    $.ajax({
        url: '/groups/add/',
        type: 'POST',
        data: mForm,
        success: function(data){
            input.onfocus = function() {
                    $("#id_name_group").tooltip({
                        trigger: 'manual',
                        placement: 'right',
                        title: textError
                    }).tooltip('show');
            };
            input.onblur = function() {
                if ($('#id_name_group').val()!=="") {
                    $("#id_name_group").tooltip('destroy');
                }
            };
            if ($('#id_name_group').val()!=="") {
                $("#myModal").modal('hide'); // Ховаємо попап меню.
                $("#status-message-popup").show(); // Показуємо статус месседж.
                $("#status-message-text").text("Група успішно додана!"); // Додаємо текст в статус месседж.
                $("#content-columns").load("/groups/ #content-groups-list"); // Оновлюємо список груп.
            }
            else {
                $("#id_name_group").tooltip({
                    trigger: 'manual',
                    placement: 'right',
                    title: textError
                }).tooltip('show');
            }
        },
        error: function(data){
            console.log('error')
        }
    })
});
