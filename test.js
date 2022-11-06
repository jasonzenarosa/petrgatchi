function checkIfUserExists1() {
    const http = new XMLHttpRequest();
    const url = "http://127.0.0.1:8000/check"
    http.open("GET", url)
    http.responseType = 'json'
    http.send()
    http.onload = _ => {
        return http.response
    }
}

function getUserState(username) {
    const http = new XMLHttpRequest();
    const url = `http://127.0.0.1:8000/user/${username}`

    let json = JSON.stringify({
        "username": username
    })

    http.open("POST", url)
    http.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    http.send(json);
    http.onload = () => console.log(http.response);
}

checkIfUserExists1()
checkIfUserExists2()