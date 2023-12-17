$(document).ready(function() {
    $('#verificationForm').submit(function(e) {
        e.preventDefault();

        var formData = {
            otp: $('#otp').val(),
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/autth/verify-email/',  // Используйте конечную точку вашего API
            data: formData,
            success: function(response) {
                console.log(response);
                if (response.status === 200) {
                    alert('Верификация успешна!');
                    // Дополнительные действия при успешной верификации
                    window.location.href = '/api/v1/autth/login/'
                } else if (response.status === 204) {
                    alert('Код неверный или пользователь уже верифицирован!');
                } else {
                    alert('Произошла ошибка при верификации!');
                }
            },
            error: function(error) {
                console.error('Произошла ошибка:', error);
            }
        });
    });
});
