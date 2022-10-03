// declarations

submitjs = document.querySelector('.submitjs')
namejs = document.querySelector('.namejs')
emailjs = document.querySelector('.emailjs')
pass = document.querySelector('.passwordjs')
repass = document.querySelector('.reppasswordjs')


submitjs.onclick = function submit() {
    console.log(namejs.value);
    console.log(emailjs.value);
    passwordChecker(pass, repass)
}

passwordChecker = function (pass, repass) {
    if (pass.value == repass.value) {
        console.log('thanks query received');
        async function sendDataToBackend(namejs, emailjs, pass, repass) {
            fetch('/signup-info', {
                method: 'POST',
                body: JSON.stringify({
                    username: namejs.value,
                    emailId: emailjs.value,
                    password: pass.value,
                    repassword: repass.value
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            })
                .then((resp) => {
                    return resp.json()
                })
                .then((json) => {
                    if (json['message'] == 'signup successful. redirecting to the loign route.') {
                        window.location.href = '/login'
                    }
                    else {
                        window.alert('signup failed')
                    }
                })
        }
        sendDataToBackend(namejs, emailjs, pass, repass)
    } else {
        console.log('reenter password, password does not match');
    }
}