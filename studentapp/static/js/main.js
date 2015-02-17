function initGroupSelector() {
    $('#group-selector select').change(function(event){
        var group = $(this).val();

        if (group) {
            $.cookie('current_group', group, {path: '/', expires: 365});
        } else {
        $.removeCookie('current_group', {path: '/'});
        }

        location.reload(true);

        return true;
    });
}

$(document).ready(function(){
    initGroupSelector();
});