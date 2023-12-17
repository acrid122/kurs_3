$(document).ready(function() {
    $('#registrationForm').submit(function(e) {
        e.preventDefault();

        var formData = {
            login: $('#id_login').val(),
            email: $('#id_email').val(),
            password: $('#id_password').val(),
            password2: $('#id_password2').val(),
            // Добавьте другие поля формы, если они есть
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/autth/reg/',  // Используйте конечную точку вашего API
            data: formData,
            success: function(response) {
                console.log(response);
                if (response.status === 201) {
                    // Редирект на страницу 'verify-email' после успешной регистрации
                    window.location.href = '/api/v1/autth/verify-email/';
                } else {
                    console.error('Произошла ошибка при регистрации');
                }
            },
            error: function(error) {
                console.error('Произошла ошибка:', error);
            }
        });
    });
});