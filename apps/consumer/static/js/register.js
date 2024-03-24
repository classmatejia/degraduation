new Vue({
    el: '#app',
    data: {
        consumerName: '', // 存储用户名输入框的值
        email: '', // 存储邮箱输入框的值
        captchaUUID: '', // 存储生成的 UUID
        captchaTimestamp: 0, // 存储验证码生成的时间戳
        emailExists: false // 存储邮箱是否已被注册的状态
    },
    methods: {
        // 发送邮箱到后端的方法
        sendEmail() {
            // 发送 AJAX 请求
            fetch('http://127.0.0.1:8000/registercountemail', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: this.email
                })
            })
                .then(response => response.json())
                .then(data => {
                    this.emailExists = data.count !== 0;
                })
                .catch(error => {
                    console.error('Error:', error); // 如果请求失败，在控制台输出错误信息
                });
        },
        fetchCaptcha() {
            // 生成9位数字的UUID
            let uuid = Math.floor(Math.random() * 1000000000).toString().padStart(9, '0');

            // 构建验证码图片的 URL
            let captchaUrl = `http://127.0.0.1:8000/captcha/${uuid}`;

            // 发送 AJAX 请求获取图片验证码
            fetch(captchaUrl)
                .then(response => response.blob()) // 将响应转换为 Blob 对象
                .then(blob => {
                    // 使用 Blob 对象创建 URL
                    // 将图片 URL 设置为 img 元素的 src
                    document.getElementById('captcha-image').src = URL.createObjectURL(blob);
                })
                .catch(error => {
                    console.error('Error:', error); // 如果请求失败，在控制台输出错误信息
                });
        },


    },
    submitForm() {

    },
    mounted() {
        // 页面加载时获取验证码
        this.fetchCaptcha();
    }
});

