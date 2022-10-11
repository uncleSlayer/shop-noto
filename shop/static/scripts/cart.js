buyBtn = document.querySelector('.order-btn')
console.log(buyBtn);
buyBtn.onlcick = function buy() {
    buyReq()
    async function buyReq() {
        console.log('btn is pressed');
    //     fetch('/make-order',{
    //         method: 'POST',
    //         body: JSON.stringify({'message': 'create order'}),
    //         headers: {'Content-type': 'application/json; charset=UTF-8'}
    //     })
    //     .then((response)=>{
    //         console.log(response);
    //     })
    }
}