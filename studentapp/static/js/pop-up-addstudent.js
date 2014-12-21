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
        var input = document.getElementsByName('input, select'),
            inputs = $(this).input,
            mForm = $("#id-student-form-popup").serialize(),
            textError = 'Поле обов’язкове';
        console.log(input);
        $.ajax({
            url: '/students/add/',
            type: 'POST',
            data: mForm,
            success: function(data){
                inputs.onfocus = function() {
                        $("inputs").tooltip({
                            trigger: 'manual',
                            placement: 'right',
                            title: textError
                        }).tooltip('show');
                };
                inputs.onblur = function() {
                    if ($('inputs').val()!=="") {
                        $("inputs").tooltip('destroy');
                    }
                };
                if ($('inputs').val()!=="") {
                    $("#myModal").modal('hide'); // Ховаємо попап меню.
                    $("#status-message-popup").show(); // Показуємо статус месседж.
                    $("#status-message-text").text("Студент успішно доданий!"); // Додаємо текст в статус месседж.
                    $("#content-columns").load("127.0.0.1:8000/ #content-students_list"); // Оновлюємо список груп.
                }
                else {
                    $("inputs").tooltip({
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
