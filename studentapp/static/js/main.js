function initGroupSelector() {
    // look up select element with groups and attach our even handler
    // on field "change" event
    $('#group-selector select').change(function(event){
        // get value of currently selected group option
        var group = $(this).val();

        if (group) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            $.cookie('current_group', group, {path: '/', expires: 365});
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_group', {path: '/'});
        }

        // and reload a page
        location.reload(true);

        return true;
    });
}

$(document).ready(function(){
    initGroupSelector();
});