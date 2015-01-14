(function($) {
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
                    document.getElementById("id-group-form-popup").reset(); // Чистка полів після успішного збереження данных.
                    $("#content-columns").load("/groups/ #content-groups-list"); // Оновлюємо список груп.
                    // Додаємо статус месседж.
                    document.getElementById("status-message-popup").innerHTML=
                        '<div class="row" id="status-message">'+
                            '<div class="col-xs-12">'+
                                '<div class="alert alert-success">'+
                                    '<button type="button" class="close" data-dismiss="alert">'+
                                        '&times;'+
                                    '</button>'+
                                    '<p id="status-message-text" name="status_message_text">'+
                                        'Група успішно додана!'+
                                    '</p>'+
                                '</div>'+
                            '</div>'+
                        '</div>';
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

})(jQuery);