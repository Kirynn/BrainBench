const defaultOptions = {
    viewMode: 'days',
    collapse: true
}

function SubmitForm(formid, location) {
    

    let el = $(`form#${formid}`);
    let data = el.serialize();

    if (el.attr('method') == 'POST')
        $.post(location, data);
}

$(function () {

    $.fn.datetimepicker.Constructor.Default = $.extend({}, $.fn.datetimepicker.Constructor.Default, {
        icons: {
            time: 'far fa-clock',
            date: 'far fa-calendar',
            up: 'fa fa-arrow-up',
            down: 'fa fa-arrow-down',
            previous: 'fa fa-chevron-left',
            next: 'fa fa-chevron-right',
            today: 'fa fa-calendar-check-o',
            clear: 'fa fa-trash',
            close: 'fa fa-times'
        }
    });

    $('#add-datetime').datetimepicker(defaultOptions);
    $('#update-datetime').datetimepicker(defaultOptions);

    // USING /login as api endpoint for testing, make sure to change this!!!
    $('#submit_new_ticket').click(function () {SubmitForm('submit_new_tickets', '/login')});
    $("#submit_update").click(function() {SubmitForm('update_ticket', '/login')});
});