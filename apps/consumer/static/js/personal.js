const app = new Vue({
    el: '#comments',
    delimiters: ['[[', ']]'],
    data: {

    },
    methods: {
        deleteComment(e) {
            fetch(`http://127.0.0.1:8000/personal`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'id': e.currentTarget.dataset.id})
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            }).then(data => {
                if (data.code === 200) {
                    // 删除成功，刷新页面
                    window.location.reload();
                } else {
                    // 删除失败，弹出错误消息
                    alert("删除失败，请重试");
                }
            }).catch(error => {
                console.error('Error deleting comment:', error);
            });
        }
    }
})