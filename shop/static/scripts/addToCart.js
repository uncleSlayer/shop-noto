cartAddBtn = document.querySelectorAll('.cart-adder')
cartValue = document.querySelectorAll('cart-value')


cartAddBtn.forEach(element => {
    element.onclick = () => {
        cartAdderClick()
        async function cartAdderClick() {
            cartName = element.getAttribute('data-name')
            fetch('/cart-add', {
                method: 'post',
                body: JSON.stringify({
                    message: 'success',
                    cart_name: element.getAttribute('data-name'),
                    cart_value: document.querySelector(`.${cartName}`).value
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            })
                .then((res) => {
                    return res.json()
                })
                .then((res) => {
                    console.log(res);
                })
        }
    }
});