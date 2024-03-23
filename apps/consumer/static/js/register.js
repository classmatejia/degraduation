new Vue({
    el: '#app',
    data: {
        consumerName: '', // 存储姓名输入框的值
        captchaUUID: '', // 存储生成的 UUID
        captchaTimestamp: 0 // 存储验证码生成的时间戳
    },
    methods: {
        // 生成 UUID 并请求验证码图片
        fetchCaptcha() {
            const currentTime = Math.floor(Date.now() / 1000); // 获取当前时间戳（以秒为单位）
            // 如果验证码的时间戳不存在或者已经超过300秒，则生成新的验证码
            if (!this.captchaTimestamp || currentTime - this.captchaTimestamp > 300) {
                // 生成 9 位数字的 UUID
                this.captchaUUID = this.generateUUID();
                // 更新验证码的时间戳
                this.captchaTimestamp = currentTime;
            }
            // 请求验证码图片
            fetch(`http://127.0.0.1:8000/captcha/${this.captchaUUID}`)
                .then(response => {
                    // 将返回的验证码图片设置到页面上
                    document.getElementById('captcha-image').src = response.url;
                })
                .catch(error => {
                    console.error('Error fetching captcha:', error);
                });
        },
        // 发送姓名到后端的方法
        sendName() {
            // 发送 AJAX 请求
            fetch('http://127.0.0.1:8080/registercountname', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    consumer_name: this.consumerName,
                    captcha_uuid: this.captchaUUID // 将 UUID 作为参数发送到后端
                })
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data); // 在控制台输出返回的数据
                })
                .catch(error => {
                    console.error('Error:', error); // 如果请求失败，在控制台输出错误信息
                });
        },
        // 生成 9 位数字的 UUID 的方法
        generateUUID() {
            return Math.floor(100000000 + Math.random() * 900000000);
        }
    },
    mounted() {
        // 页面加载时获取验证码
        this.fetchCaptcha();
    }
});

