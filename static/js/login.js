$('#btn_commit').click(function () {
    $.ajax({
        url: '',
        type: 'post',
        data: {
            'username': $('#username').val(),
            'password': $('#password').val(),
        },
        headers: { 'X-CSRFtoken': csrftoken },
        success: function (resultData) {
            if (resultData.ret == 1) {
                alert('登录成功')
                window.location.href = resultData.url
            } else if (resultData.ret == 0) {
                alert(resultData.msg)
            } else {
                console.log('ret:', resultData.ret, '\n', '错误：未知ret码,请联系管理员')
            }
        }
    })
})