new Vue({
    el: '#nav',
    delimiters: ['[[', ']]'],
    data: {
        isLoggedIn: false, // 是否已登录
        username: '' // 用户名
    },
    mounted() {
        // 检查 cookie 中是否存在用户名
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
        }
    }
});
