new Vue({
    el: '#app',
    data: {
        consumerName: '', // 用户名存储用户名输入框的值
        email: '', // 存储邮箱输入框的值
        captchaUUID: '', // 存储生成的 UUID
        captchaTimestamp: 0, // 存储验证码生成的时间戳
        emailExists: false, // 存储邮箱是否已被注册的状态
        password: '', //密码
        confirmPassword: '', //'
        // Verification_code: '', //
        captcha: '', //
        passwordsMatch: true, //
        captchaMatch: true, //
        captchaUrl: '',
        loginDirectly:false,//
        phoneNumber: '', //
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
        // sendVerificationCode() {
        //     fetch('http://127.0.0.1:8000/captcha/sendemail', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json'
        //         },
        //         body: JSON.stringify({
        //             email: this.email
        //         })
        //     })
        //         .then(response => {
        //             if (response.ok) {
        //                 console.log('Verification code sent successfully.');
        //             } else {
        //                 throw new Error('Failed to send verification code.');
        //             }
        //         })
        //         .catch(error => {
        //             console.error('Error:', error); // 如果请求失败，在控制台输出错误信息
        //         });
        // },

        comparePasswords() {
            // 检查密码是否匹配
            this.passwordsMatch = this.password === this.confirmPassword;
        },

        fetchCaptcha() {
            // 检查验证码是否过期
            const currentTime = new Date().getTime();
            if (currentTime - this.captchaTimestamp > 300000) { // 300000 毫秒 = 5 分钟
                // 生成9位数字的UUID
                this.captchaUUID = Math.floor(Math.random() * 1000000000).toString().padStart(9, '0');

                // 更新验证码生成的时间戳
                this.captchaTimestamp = currentTime;

                // 构建验证码图片的 URL
                this.captchaUrl = `http://127.0.0.1:8000/captcha/${this.captchaUUID}`;

                // 发送 AJAX 请求获取图片验证码
            }
            fetch(this.captchaUrl)
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
        submitForm() {
            fetch('http://127.0.0.1:8000/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    consumerName: this.consumerName,
                    email: this.email,
                    password: this.password, //密码
                    captcha: this.captcha,
                    captchaUUID: this.captchaUUID,
                    loginDirectly:this.loginDirectly,
                    phone: this.phoneNumber
                })
            })
                .then(response => response.json())
                .then(data => {
                    // 处理返回的数据
                    console.log(data);
                    this.captchaMatch = !(data.register === "error" && data.captcha === 0);
                })
                .catch(error => {
                    console.error('Error:', error); // 如果请求失败，在控制台输出错误信息
                });
        }


    },

    mounted() {
        // 页面加载时获取验证码
        this.fetchCaptcha();
    }
})
;

