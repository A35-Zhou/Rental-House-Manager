$('#pay').click(function () {
    $.ajax({
        url: '',
        type: 'post',
        headers: { 'X-CSRFtoken': csrftoken },
        success: function (resultData) {
            if (resultData.ret == 1) {
                alert('支付成功');
                window.location.reload();
            } else if (resultData.ret == -1) {
                alert(resultData.msg);
            } else {
                console.log('ret:', resultData.ret, '\n', '错误：未知ret码,请联系管理员');
            }
        }
    })
})