$('#btn_commit').click(function () {
    $.ajax({
        url: '',
        type: 'post',
        data: {
            'room': $('#room').val(),
            'inTime': $('#inTime').val(),
            'outTime': $('#outTime').val(),
            'orderDesc': $('#orderDesc').val(),
            'method': $('#method').val()
        },
        headers: { 'X-CSRFtoken': csrftoken },
        success: function (resultData) {
            if (resultData.ret == 1) {
                alert('预约成功')
                window.location.href = resultData.url
            } else if (resultData.ret == 0) {
                $.each(resultData.msg, function (index, item) {
                    let eleId = '#' + index;
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