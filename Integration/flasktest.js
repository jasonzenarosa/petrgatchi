document.getElementById("btn").addEventListener('click', add);
function add()
{
    const url = "localhost:8000/test";
    const http = new XMLHttpRequest();
    http.open("GET", url);
    http.send();
    http.onreadystatechange=(e)=> {
        console.log(http.responseText)
    }
}