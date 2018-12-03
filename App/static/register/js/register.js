

$(function () {
    // 验证 用户名是否为空 是否重复
    $('#inputusername').blur(function () {

        var name = $(this).val()
        if (name == '') {
            $('#name_err').show()
            $('#name_no').hide()
            // 添加按钮不能点击
            $('#bt').attr('disabled', 'disabled')
        } else {
            $('#name_err').hide()

            // 判断是不是重复
            $.getJSON('/checkuser/', {"username": $("#inputusername").val()}, function (response) {
                // console.log(response['status'])
                if (response['status'] == 200) {  // 用户名可用
                    // console.log('可用')
                    $('#name_no').hide()
                    //删除不可点击
                    $('#bt').removeAttr('disabled')


                } else if (response['status'] == 401) { //用户名不可用
                    // console.log('不可用')
                    $('#name_ok').hide()
                    $('#name_no').show()
                    // 添加按钮不能点击
                    $('#bt').attr('disabled', 'disabled')

                }
            })
        }
    })
    // 密码不能为纯数字且不能小于6位
    $('#pwd1').blur(function () {

        var pwd = $(this).val()
        console.log(pwd)
        if (pwd.length >= 6) {
            $('#pwd1_err').hide()
            //删除不可点击
            $('#bt').removeAttr('disabled')

        } else {
            $('#pwd1_err').show()
            // 添加按钮不能点击
            $('#bt').attr('disabled', 'disabled')

        }
    })
    //两次密码不一致
    $('#pwd2').blur(function () {
        var pwd1 = $(this).val()
        var pwd2 = $('#pwd1').val()
        if (pwd1 == pwd2) {
            $('#pwd2_err').hide()
            //删除不可点击
            $('#bt').removeAttr('disabled')
        } else {

            $('#pwd2_err').show()
            // 添加按钮不能点击
            $('#bt').attr('disabled', 'disabled')
        }
    })
})



