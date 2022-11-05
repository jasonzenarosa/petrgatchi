function checkIfUserExists1() {
    const http = new XMLHttpRequest;
    const url = "FILL THIS IN WITH THE REAL URL"
    http.open("GET", url)
    http.responseType = 'json'
    http.send()
    http.onload = _ =>{
        console.log(http.response)
    }
}

function checkIfUserExists2() {
    http = new XMLHttpRequest;
    const url = "FILL THIS IN WITH THE REAL URL"
    http.open("GET", url)
    http.send()
    http.onreadystatechange = _ =>{
        console.log(http.responseText)
    }
}

function getUserState(username) {
    const http = new XMLHttpRequest;
    const url = "FILL THIS IN WITH THE REAL URL"

    let json = JSON.stringify({
        "username": username
    })

    http.open("POST", url)
    http.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    http.send(json);
    http.onload = () => alert(http.response);
}