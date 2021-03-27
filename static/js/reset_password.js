$('#btn_commit').click(function () {
    $.ajax({
        url: 'user/reset_password/',
        type: 'post',
        data: {
            'oldpassword': $('#id_oldpassword').val(),
            'newpassword': $('#id_newpassword').val(),
            'repassword': $('#id_repassword').val(),
        },
        headers: { 'X-CSRFtoken': csrftoken },
        success: function (resultData) {
            if (resultData.ret == 1) {
                alert('修改成功,请重新登录')
                window.location.href = resultData.url
            } else if (resultData.ret == 0) {
                $.each(resultData.msg, function (index, item) {
                    let eleId = '#id_' + index;
                    $(eleId).next().text(item[0]).parent().addClass('has-error')
                })
            } else if (resultData.ret == -1) {
                alert(resultData.msg)
            } else {
                console.log('ret:', resultData.ret, '\n', '错误：未知ret码,请联系管理员')
            }
        }
    })
});
$('input').focus(function () {
    $(this).next().text('').parent().removeClass('has-error')
});
$('#btn_cancel').click(function () {
    $('#id_oldpassword').val('');
    $('#id_newpassword').val('');
    $('#id_repassword').val('');
});
