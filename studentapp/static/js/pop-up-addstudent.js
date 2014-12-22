// POP-UP MENU ADD GROUP
(function($) {
    // Open pop-up
    $("#button-add-student").click(function() {
        $("#div_id_first_name_popup").load("/students/add/ #div_id_first_name");
        $("#div_id_last_name_popup").load("/students/add/ #div_id_last_name");
        $("#div_id_middle_name_popup").load("/students/add/ #div_id_middle_name");
        $("#div_id_date_popup").load("/students/add/ #div_id_date");
        $("#div_id_foto_popup").load("/students/add/ #div_id_foto");
        $("#div_id_stud_bilet_popup").load("/students/add/ #div_id_stud_bilet");
        $("#div_id_stud_group_popup").load("/students/add/ #div_id_stud_group");
    });

    $("#send-popup-form").click(function(e) {
        e.preventDefault()
        var mForm = $("#id-student-form-popup").serialize(),
            inputs = $('input,select'),
            valid = true;
        $.ajax({
            url: '/students/add/',
            type: 'POST',
            data: mForm,
            success: function(data){
                inputs.tooltip('destroy');

                $.each(inputs, function(index, val) {
                    var input = $(val),
                        val = input.val(),
                        formGroup = input.parents('.form-group');
                        label = formGroup.find('label').text().toLowerCase(),
                        textError = 'Заповніть поле ' + label;

                    if (val.length === 0){
                        formGroup.addClass('has-error').removeClass('has-success');
                        input.tooltip({
                            trigger: 'manual',
                            placement: 'right',
                            title: textError
                        }).tooltip('show');
                        valid = false
                    }else {
                        formGroup.addClass('has-success').removeClass('has-error');
                    }

                });
                if ( valid == true) {
                    $("#myModal").modal('hide'); // Ховаємо попап меню.
                    $("#status-message-text").text("Студент успішно доданий!"); // Додаємо текст в статус месседж.
                    $("#content-columns").load("/ #content-students_list"); // Оновлюємо список груп.
                }
            },
            error: function(data){
                console.log('error')
            }
        })
    });
})(jQuery);
