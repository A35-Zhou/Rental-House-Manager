$('#btn_commit').click(function () {
    let formData = new FormData();
    $.each($('#accountForm').serializeArray(), function (index, item) {
        formData.append(item.name, item.value)
    });
    $.ajax({
        url: '',
        type: 'post',
        data: formData,
        contentType: false,
        processData: false,
        success: function (resultData) {
            if (resultData.ret == 1) {
                alert('修改成功')
                window.location.reload()
            } else if (resultData.ret == 0) {
                $.each(resultData.msg, function (index, item) {
                    let eleId = '#id_' + index;
                    $(eleId).next().text(item[0]).parent().addClass('has-error')
                })
            } else if (resultData.ret == -1) {
                alert(resultData.msg)
            } else {
                console.log('ret:', resultData.ret, '/n', '错误：未知ret码,请联系管理员')
            }
        }
    })
});
$('input').focus(function () {
    $(this).next().text('').parent().removeClass('has-error')
})