(function() {

    var app = {

        initialize : function () {
            this.setUpListeners();
        },

        setUpListeners: function () {
            $('form').on('submit', app.submitForm);
            $('form').on('keydown', 'input', app.removeError);
        },

        submitForm: function  (e) {
            e.preventDefault();
            var form = $(this);

            if( app.validateForm(form) === false) return false;

            var str = form.serialize();

            $.ajax({
                url: '/students/add/',
                type: 'POST',
                data: str
            })
            .done(function(msg) {
                if(msg === "OK"){
                    var result = "<div class='bg-succcess'>Дякую за заявку</div>"
                    form.html(result);
                }else{
                    form.html(msg);
                }
            });
        },

        validateForm: function (form){
            var inputs = form.find('input, select'),
                valid = true;

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

            return valid;

        },

        removeError: function() {
            $(this).tooltip('destroy').parents('.form-group').removeClass('has-error');
        }

    }

    app.initialize();

}());