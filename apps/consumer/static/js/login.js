// login.js

new Vue({
    el: '#app',
    data: {
        formData: {
            username: '',
            password: ''
        }
    },
    methods: {
        submitForm() {
            // 发送 POST 请求
            fetch('http://127.0.0.1:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.formData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.code === 200) {
                    // 登录成功，重定向到 index 页面
                    window.location.href = 'http://127.0.0.1:8000/index';
                } else {
                    // 登录失败，弹窗提示账号或密码错误
                    alert("密码账号错误");
                }
            })
            .catch(error => {
                console.error('Error during login:', error);
                // 在这里处理登录失败的逻辑
            });
        }
    }
});
