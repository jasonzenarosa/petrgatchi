function checkIfUserExists1() {
    http = new XMLHttpRequest;
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

checkIfUserExists1()
checkIfUserExists2()