/* Project specific Javascript goes here. */
(function() {
    $('.delete-button').click(function(e) {
        var href = e.target.dataset.href;
        $('#modal_action_button').attr('href', href);
        $('#delete_modal').modal();
    });
})();