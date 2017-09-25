$('#myModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var title = button.data('title') // Extract info from data-* attributes
    var image_url = button.data('image_url') // Extract info from data-* attributes
    var description = button.data('description') // Extract info from data-* attributes
    var price = button.data('price') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    modal.find('#myModal-title').text(title)
    modal.find('#myModal-image_url').attr('src','/media/' + image_url)
    modal.find('#myModal-description').text(description)
    modal.find('#myModal-price').text('₹' + price)
})
