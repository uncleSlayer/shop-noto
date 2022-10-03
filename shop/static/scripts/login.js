email = document.querySelector('.emailjs')
password = document.querySelector('.passjs')
submit = document.querySelector('.submitjs')


submit.onclick = function submit() {
    loginSender(email, password)
}

function loginSender(email, password){
    fetch('/login-info', {
        method: 'POST',
        body: JSON.stringify({
            email: email.value,
            password: password.value
        }),
        headers: {
            'Content-type': "application/json; charset=UTF-8"
        }
    })
    .then((resp)=>{
        return resp.json()
        console.log(resp);
    })
    .then((resp)=>{
        window.location.href = '/shop'
    })
}