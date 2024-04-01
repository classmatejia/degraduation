const app = new Vue({
    el: '#container',
    data: {
        formData: {
            shop_name: '',
            address: '',
            phone: ''
        },
        products: [],
        isModalOpen: false
    },
    methods: {
        setupShop() {
            window.location.href = 'http://127.0.0.1:8000/merchant/setupshop';
        },
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
                        } else {
                            // Show error message
                            this.errorMessage = '开店失败，请重试。'; // Customize error message as needed
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        this.errorMessage = '开店失败，请重试。'; // Show generic error message
                    });
            }
    }
});
