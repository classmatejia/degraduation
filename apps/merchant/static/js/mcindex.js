const app = new Vue({
    el: '#container',
    delimiters: ['[[', ']]'],
    data: {
        alterData: {
            alterName: '',
            alterAddress: '',
            alterNumber: '',
        },
        formData: {
            shop_name: '',
            address: '',
            phone: '',
            shop_type: ''
        },
        addGoodsData: {
            goods_name: '',
            goods_desc: '',
            goods_price: '',
        },
        products: [],
        isModalOpen: false
    },
    mounted() {
        fetch('http://127.0.0.1:8000/merchant/isopen', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        }).then(data => {
                this.isModalOpen = data.code === 200;
            }
        )
    },
    methods: {
        submitForm() {
            fetch('http://127.0.0.1:8000/merchant/setupshop', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.formData)
            })
                .then(response => {
                    if (response.ok) {
                        return response.json(); // Parse response JSON
                    } else {
                        throw new Error('Form submission failed');
                    }
                })
                .then(data => {
                    // Check response code
                    if (data.code === 200) {
                        // Redirect to index page
                        window.location.href = 'index'; // Change to your index page URL
                    } else if (data.code === 202) {
                        alert('已有店铺')
                    } else {
                        // Show error message
                        alert('开店失败，请重试。'); // Customize error message as needed
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        logout() {
            fetch('http://127.0.0.1:8000/merchant/logout', {
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
                        window.location.href = 'index';
                    } else {
                        // 登录失败，弹窗提示账号或密码错误
                        alert("错误");
                    }
                }
            )

        },
        alterInfo() {
            fetch('http://127.0.0.1:8000/merchant/alterinfo', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.alterData)
            })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Form submission failed');
                    }
                }).then(data => {
                if (data.code === 200) {
                    window.location.href = 'index';
                    alert('修改成功')
                } else if (data.code === 202) {
                    alert('修改失败,你还没有店铺')
                } else {
                    alert('修改失败😢')
                }
            })
                .catch(error => {
                    console.error('Error:', error);
                });
        },
        addGoods() {
            fetch('http://127.0.0.1:8000/merchant/index', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.addGoodsData)
            }).then(r => {
                if (r.ok) {
                    return r.json();
                } else {
                    throw new Error('Form submission failed');
                }
            }).then(data => {
                if (data.code === 200) {
                    window.location.href = 'index';
                } else {
                    alert('添加失败')
                }
            }).catch(error => {
                console.error('Error:', error);
            });
        },
        deleteGoods(e) {
            fetch("http://127.0.0.1:8000/merchant/index", {
                method: 'DELETE',
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
                if (data.code === 200) {
                    window.location.href = 'index';
                } else {
                    alert('删除失败')
                }
            }).catch(error => {
                console.error('Error:', error);
            });
        },
    }
});
