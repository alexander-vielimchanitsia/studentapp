// POP-UP MENU ADD GROUP
(function($) {

    // open pop-up
    $("#button-add-student").click(function() {

        // download form in pop-up
        $("#modal-body").load("/students/add/ #id-student-form",function(){

            // pop-up submit button
            $("#submit-id-save_button_add").click(function(e) {
                e.preventDefault();

                // SERIALIZE FILES AND DATE FORM
                $.fn.serializefiles = function() {
                    var obj = $(this);
                    /* ADD FILE TO PARAM AJAX */
                    var formData = new FormData();
                    $.each($(obj).find("input[type='file']"), function(i, tag) {
                        $.each($(tag)[0].files, function(i, file) {
                            formData.append(tag.name, file);
                        });
                    });
                    var params = $(obj).serializeArray();
                    $.each(params, function (i, val) {
                        formData.append(val.name, val.value);
                    });
                    return formData;
                };

                var inputs = $('#id-student-form select, input'), // all input fields in the form
                    mForm = $("#id-student-form").serializefiles(),
                    valid = true;

                $.ajax({
                    url: '/students/add/',
                    type: 'POST',
                    data: mForm,
                    contentType: false,
                    processData: false,
                    success: function(data){

                        $.each(inputs, function(index, val) {
                            var input = $(val),
                                val = input.val(),
                                formGroup = input.parents('.form-group'),
                                label = formGroup.find('label').text().toLowerCase(),
                                textError = 'Заповніть поле ' + label;

                            if (val.length == 0){
                                input.tooltip({
                                    trigger: 'manual',
                                    placement: 'right',
                                    title: textError
                                }).tooltip('show');
                                valid = false
                            }else {
                                input.tooltip('destroy');
                            };

                        });
                        if (valid == true) {
                            $("#myModal").modal('hide'); // hiding popup menu
                            document.getElementById("id-student-form").reset(); // cleaning fields after successfully saved data
                            $("#content-columns").load("/ #content-students_list"); // updating the list of students

                            // add the status messages
                            document.getElementById("status-message-popup").innerHTML=
                                '<div class="row" id="status-message">'+
                                    '<div class="col-xs-12">'+
                                        '<div class="alert alert-success">'+
                                            '<button type="button" class="close" data-dismiss="alert">'+
                                                '&times;'+
                                            '</button>'+
                                            '<p id="status-message-text" name="status_message_text">'+
                                                'Студент успішно доданий!'+
                                            '</p>'+
                                        '</div>'+
                                    '</div>'+
                                '</div>';
                        };
                    },

                    error: function(data){
                        alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
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
