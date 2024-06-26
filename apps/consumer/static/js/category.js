const nav = new Vue({
    el: '#nav',
    delimiters: ['[[', ']]'],
    data: {
        isLoggedIn: false, // 是否已登录
        username: '' // 用户
    },
    mounted() {
        // 检查 cookie 中是否存在用户名vue-init webpack frontend
        const username = this.getCookie('username');
        if (username) {
            this.isLoggedIn = true;
            // 将字符串转换为 Uint8Array
            const byteArray = new Uint8Array(username.match(/[\da-f]{2}/gi).map(function (h) {
                return parseInt(h, 16)
            }));
            // 使用 TextDecoder 解码
            const textDecoder = new TextDecoder('utf-8');
            const decodedString = textDecoder.decode(byteArray);
            console.log(decodedString); // 输出解码后的字符串
            this.username = decodedString;
            console.log(this.username);
        }
    },
    methods: {
        getCookie(name) {
            // 使用JavaScript函数获取cookie
            const cookieName = name + "=";
            const decodedCookie = decodeURIComponent(document.cookie);
            const cookieArray = decodedCookie.split(';');
            for (let i = 0; i < cookieArray.length; i++) {
                let cookie = cookieArray[i];
                while (cookie.charAt(0) === ' ') {
                    cookie = cookie.substring(1);
                }
                if (cookie.indexOf(cookieName) === 0) {
                    return cookie.substring(cookieName.length, cookie.length);
                }
            }
            return '';
        },
        logout() {
            screen.logout();
        }

    }
});

// screen = new Vue({
//     el: "#screen",
//     delimiters: ['[[', ']]'],
//     data: {
//         isLoggedIn: nav.isLoggedIn,
//         username: nav.username // 用户
//     },
//     methods: {
//         logout() {
//             fetch('logout', {
//                 method: 'DELETE',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//             }).then(response => {
//                 if (!response.ok) {
//                     throw new Error('Network response was not ok');
//                 }
//                 return response.json();
//             }).then(data => {
//                     if (data.code === 200) {
//                         // 推出成功，重定向到 index 页面
//                         window.location.href = 'http://127.0.0.1:8000/index';
//                     } else {
//                         // 登录失败，弹窗提示账号或密码错误
//                         alert("错误");
//                     }
//                 }
//             )
//
//         }
//     }
// })

screen = new Vue({
    el: "#screen",
    delimiters: ['[[', ']]'],
    data: {
        isLoggedIn: nav.isLoggedIn,
        username: nav.username // 用户
    },
    methods: {
        logout() {
            fetch('logout', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            }).then(data => {
                    if (data.code === 200) {
                        // 推出成功，重定向到 index 页面
                        window.location.href = 'http://127.0.0.1:8000/index';
                    } else {
                        // 登录失败，弹窗提示账号或密码错误
                        alert("错误");
                    }
                }
            )

        }
    }
})

