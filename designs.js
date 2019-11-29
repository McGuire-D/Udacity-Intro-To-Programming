var height, width, color;

//table input using makeGrid function
$("#sizePicker").submit(function (event) {
    event.preventDefault();
    height = $('#inputHeight').val();
    width = $('#inputWidth').val();
    makeGrid(height, width);
})

// make grid function that adjusts size with user input
function makeGrid(x, y) {
    $('tr').remove();

    for (var i = 1; i <= x; i++) {
        $('#pixelCanvas').append('<tr id=table' + i + '></tr>')
        for (var j = 1; j <=y; j++) {
            $('#table' + i).append('<td></td>');
        }
    }

    // color code with click color function
    $('td').click(function addColor() {
       color = $('#colorPicker').val();

       if ($(this).attr('style')) {
           $(this).removeAttr('style')
       } else {
           $(this).attr('style' , 'background-color:' + color);
       }
    })
}
