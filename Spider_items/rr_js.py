'''
formSubmit: function() {
        var e, t = {};
        $(".login").addEventListener("click", function() {
            t.phoneNum = $(".phonenum").value,
            t.password = $(".password").value,
            e = loginValidate(t),
            t.c1 = c1 || 0,
            e.flag ? ajaxFunc("get", "http://activity.renren.com/livecell/rKey", "", function(e) {
                var n = JSON.parse(e).data;
                if (0 == n.code) {
                    t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
                } else
                    toast("公钥获取失败"),
                    t.rKey = "";
                ajaxFunc("post", "http://activity.renren.com/livecell/ajax/clog", t, function(e) {
                    var e = JSON.parse(e).logInfo;
                    0 == e.code ? location.href = localStorage.getItem("url") || "" : toast(e.msg || "登录出错")
                })
            }) : toast(e.msg)
        })
    }
'''