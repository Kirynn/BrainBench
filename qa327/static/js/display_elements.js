const dtp = "#sumbit-ticket-modal > div > div > div.modal-body > form > div:nth-child(4) > div"

$(function() {

    $('#add-datetime').datetimepicker({
        viewMode: 'years',
    });

    $('#submit_new_ticket').click(function() {


        var data = $("form#submit_new_tickets").serialize();
        console.log(data);
        $.post('/login', data)

        /*
    console.log('getting all inputs....');

    stuff = {
        name
    }
    let outputs = [];
    $("form#submit_new_tickets :input").each(function(){
        outputs.push($(this).val());
       });
       */
    });
});