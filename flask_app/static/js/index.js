$(document).ready(function(){

$('.button-submit').on('click', function(e) {
    e.preventDefault();
    var itemData = new FormData();
    itemData.set('name', $('#name').val());
    itemData.set('price', $('#price').val());
    itemData.set('description', $('#description').val());
    if ($('#file')[0].files.length) {
      itemData.set('thumbnail', $('#file')[0].files[0]);
    }
    
    $.ajax({
        type: 'POST',
        url: '/api/items/',
        processData: false,
        cache: false,
        contentType: false,
        data: itemData,
        success: function(response_msg, status, jqXHR){
            console.log(response_msg)
            $('input').val('');
            $('textarea').val('');
        },
        error: function(error) {
            console.log(error)
        }
    });
  
    
  }
)



})