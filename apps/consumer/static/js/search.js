<<<<<<< HEAD
const search = new Vue({
    el: '#search-container',
    delimiters: ['[[', ']]'],
    data: {
        search_string: '',
    },
    methods: {
        search() {
            // 发送搜索请求
            fetch('http://127.0.0.1:8000/search?query=' + encodeURIComponent(this.search_string))
                .then(response => {
                    if (!response.ok) {
                        throw new Error('搜索请求失败');
                    }
                    return response.json();
                })
                .then(data => {
                    // 处理搜索结果
                    console.log(data);
                })
                .catch(error => {
                    console.error('搜索失败：', error);
                });
=======
new Vue({
    el: '#search-container',
    delimiters: ['[[', ']]'],
    data:{
        search_string: ''
    },
    methods: {
        search(){

>>>>>>> origin/main


        }
    }

})