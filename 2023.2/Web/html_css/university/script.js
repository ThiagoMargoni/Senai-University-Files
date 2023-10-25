function login_submit(event) {
    event.preventDefault();
    
    const email = document.querySelector('#e').value;
    const password = document.querySelector('#p').value;

    console.log("email: ", email);
    console.log("password: ", password);
}