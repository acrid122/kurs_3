// login_script.js

$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault();

        var formData = {
            email: $('#email').val(),
            password: $('#password').val(),
        };

        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/api/v1/autth/login/',
            data: formData,
            success: function(response) {
                console.log(response);
                if (response.status === 200) {
                    var accessToken = response.data.access;

                    // Добавляем токен в заголовок Authorization
                    $.ajax({
                        type: 'POST',
                        url: '/sic/stat/',
                        headers: {
                            'Authorization': 'Bearer ' + accessToken,
                        },
                        success: function(statResponse) {
                            console.log(statResponse);
                            // Обработка успешного запроса к странице /sic/stat/
                            // Можете добавить дополнительные действия при успешном входе
                            window.location.href = '/sic/stat/';
                        },
                        error: function(statError) {
                            console.error('Ошибка запроса к странице /sic/stat/:', statError);
                        }
                    });
                } else {
                    console.error('Ошибка входа');
                }
            },
            error: function(error) {
                console.error('Произошла ошибка:', error);
            }
        });
    });
});
