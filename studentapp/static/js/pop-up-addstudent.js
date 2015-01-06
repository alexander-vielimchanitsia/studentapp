// POP-UP MENU ADD GROUP
(function($) {

    // Open pop-up
    $("#button-add-student").click(function() {

        // Download form in pop-up
        $("#modal-body").load("/students/add/ #id-student-form",function(){

            // Pop-up submit button
            $("#submit-id-save_button_add").click(function(e) {
                e.preventDefault();
                var inputs = $('input,select'),
                    mForm = $("#id-student-form").serialize(),
                    valid = true;
                $.ajax({
                    url: '/students/add/',
                    type: 'POST',
                    data: mForm,
                    success: function(data){

                        inputs.onfocus = function() {
                            inputs.tooltip({
                                trigger: 'manual',
                                placement: 'right',
                                title: textError
                            }).tooltip('show');
                        };
                        inputs.onblur = function() {
                            if (inputs.val() !== "") {
                                inputs.tooltip('destroy');
                            };
                        };

                        $.each(inputs, function(index, val) {
                            var input = $(val),
                                val = input.val(),
                                formGroup = input.parents('.form-group'),
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
                            };

                        });
                        if ( valid == true) {
                            $("#myModal").modal('hide'); // Ховаємо попап меню.
                            $("#status-message-text").text("Студент успішно доданий!"); // Додаємо текст в статус месседж.
                            $("#content-columns").load("/ #content-students_list"); // Оновлюємо список груп.
                        };
                    },
                    error: function(data){
                        console.log('error')
                    },
                });

            });

            // Pop-up close
            $("#submit-id-cancel_button_add").click(function(e) {
                e.preventDefault();
                $("#myModal").modal('hide');
            });

        });

    });

})(jQuery);
