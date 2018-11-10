/* Project specific Javascript goes here. */
(function() {
    $('.delete-button').click(function(e) {
        var href = e.target.dataset.href;
        $('#modal_action_form').attr('action', href);
        $('#delete_modal').modal();
    });
    $('.btnChangePass').click(function(e) {
        var href = e.target.dataset.href,
            csrf = e.target.dataset.csrf;
        $.post({
            url: href,
            data: { csrfmiddlewaretoken: csrf }
        }).done(function(response) {
            $('#password_modal .modal-title')
                .text('Contraseña cambiada con exito');
            $('#password_modal .modal-body p')
                .html('La contraseña del responsable es: <b>' + response + '</b>');
        }).fail(function(response){
            $('#password_modal .modal-title')
                .text('Ocurrió un error');
            $('#password_modal .modal-body p')
                .text('No fue posible cambiar la contraseña debido a un error interno.');
        }).always(function() {
            $('#password_modal').modal();
        });
    });
})();