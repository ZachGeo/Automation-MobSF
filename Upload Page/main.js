$(document).ready(function(){
    $('#file-upload').change(function (){
        var selectedfile = $('#file-upload')[0].files[0].name;
        $('form p').text(selectedfile + " file has been selected!");
    });
});