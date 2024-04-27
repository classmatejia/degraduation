<<<<<<< HEAD
const demo =new Vue({
    el: '#demo',
    delimiters: ['[[', ']]'],
    data: {
        cartItems: [], //
=======
const a = new Vue({
    el: '#shopmsg',
    delimiters: ['[[', ']]'],
    data: {
        isLoggedIn: false, // 是否已登录
        username: '', // 用户
        cartItems: [], //
        mark:'',
>>>>>>> origin/main
    },
    methods: {
        addCart(e) {
            var id = e.currentTarget.dataset.id
            fetch("http://127.0.0.1:8000/cart", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({"id": e.currentTarget.dataset.id})
            }).then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Form submission failed');
                }
            }).then(data => {
                // 使用 Array.prototype.some() 来检查是否已经存在相同的商品
                const existingItemIndex = this.cartItems.findIndex(item => item.name === data.name);
                if (existingItemIndex !== -1) {
                    // 如果存在相同的商品，则增加该商品的数量
                    this.cartItems[existingItemIndex].count += 1;
                } else {
                    // 否则，将该商品添加到购物车中
                    this.cartItems.push({"id": id, "name": data.name, "count": 1});
                }
            })
        },
<<<<<<< HEAD
    }


})

const a = new Vue({
    el: '#cart',
    delimiters: ['[[', ']]'],
    data: {
        isLoggedIn: false, // 是否已登录
        username: '', // 用户
        cartItems: demo.cartItems, //
        mark: '',
    },
    methods: {

=======
>>>>>>> origin/main
        removeFromCart(index) {
            if (this.cartItems[index].count > 1) {
                this.cartItems[index].count--;
            } else {
                this.cartItems.splice(index, 1);
            }
        },
        placeAnOrder() {
            const currentUrl = window.location.href;
            if (this.cartItems.length !== 0) {
                fetch(currentUrl, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(this.cartItems)
                }).then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Form submission failed');
                    }
                }).then(data => {
                    if (data.code === 200) {
                        alert('Success')
                    } else {
                        alert('Error')
                    }
                })
<<<<<<< HEAD
            } else {
=======
            }else {
>>>>>>> origin/main
                alert('哒没！')
            }

        },
<<<<<<< HEAD
=======
        getComment() {
            const currentUrl = window.location.href;
            const textarea = document.getElementById('comment');
            const comment = textarea.value;
            fetch('http://127.0.0.1:8000/comment', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({'comment':comment,'path':currentUrl,'mark':this.mark})
            }).then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Form submission failed');
                }
            }).then(data => {
                if (data.code === 200) {
                    window.location.reload();
                } else {
                    alert('评论失败')
                }
            })
            console.log(comment);
            textarea.value = '';
        }
>>>>>>> origin/main


    }

})


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
<<<<<<< HEAD
new Vue({
    el: '#comments',
    delimiters: ['[[', ']]'],
    data: {
        mark: '',
    },
    methods: {
        getComment() {
            const currentUrl = window.location.href;
            const textarea = document.getElementById('comment');
            const comment = textarea.value;
            fetch('http://127.0.0.1:8000/comment', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({'comment': comment, 'path': currentUrl, 'mark': this.mark})
            }).then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Form submission failed');
                }
            }).then(data => {
                if (data.code === 200) {
                    window.location.reload();
                } else {
                    alert('评论失败')
                }
            })
            console.log(comment);
            textarea.value = '';
        }
    }

})
=======
>>>>>>> origin/main

