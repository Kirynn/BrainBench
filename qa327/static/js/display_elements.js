const buyModal = "#buy-modal"
const submitModal = "#submit-modal"

const defaultDateTimePickerOptions = {
    viewMode: 'days',
    collapse: true,
    format: 'L'
}

function SubmitForm(formid, location) {
    

    let el = $(`form#${formid}-ticket-form`);
    let data = el.serialize();

    if (el.attr('method') == 'POST') $.post(location, data);
    else if(el.attr('method') == 'PUT') $.put(location, data);

    $(`#${formid}-modal`).modal('hide');
}

function LoadBuyModal(name, quantity, price, date) {

    $(buyModal).modal('show');
    $(buyModal).find("#cost-output").html(`Cost: \$${$(buyModal).find("input[name='Price']").val() * $(buyModal).find("input[name='Quantity']").val()}`)

    $(buyModal).find("input[name='Quantity']").attr("max", quantity);
    $(buyModal).find("#buy-max").html("Max available " + quantity + ".");

    $(buyModal).find("input[name='Name']").val(name);
    $(buyModal).find("input[name='Price']").val(price);
    $(buyModal).find("input[name='Date']").val(date);

    $(buyModal).find("input[name='Quantity']").change(function() {
        $(buyModal).find("#cost-output").html(`Cost: \$${$(buyModal).find("input[name='Price']").val() * $(buyModal).find("input[name='Quantity']").val()}`)        
    });
}

function LoadUpdateModal(name, quantity, price, date) {

    $(submitModal).modal('show');
    $(submitModal + " input[name='Name']").val(name);
    $(submitModal + " input[name='Quantity']").val(quantity);
    $(submitModal + " input[name='Price']").val(price);
    $(submitModal + " input[name='Date']").val(date);
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

    $('#add-datetime').datetimepicker(defaultDateTimePickerOptions);
    $('#update-datetime').datetimepicker(defaultDateTimePickerOptions);

    // User /login as api endpoint for testing, make sure to change this!!! (you can see it in the console)

    $('#submit-ticket-button').click(function () {SubmitForm('submit', '/viewPOST')});
    $("#update-ticket-button").click(function() {SubmitForm('update', '/viewPOST')});
    $("#buy-ticket-button").click(function() {SubmitForm('buy', '/viewPOST')});
});

