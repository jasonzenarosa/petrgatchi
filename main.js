import { particle } from "./petr.js"

function checkIfUserExists() {
    let http = new XMLHttpRequest;
    const url = "http://127.0.0.1:8000/check"
    http.open("GET", url, false)
    http.send( null )
    return http.responseText
}

function newUser (username) {
    let userdata = {"username": username}
    let xhr = new XMLHttpRequest;
    const url = "http://127.0.0.1:8000/register"
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(userdata))
    return xhr.responseText
}

let r = checkIfUserExists()
if (r === '0') {
    let username = prompt('Enter a username')
    console.log(newUser(username))
    // fetch('http://127.0.0.1:8000/register', {
    //     method: 'POST',
    //     headers: {
    //         'Accept': 'application/json',
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(userdata)
    // })
    // .then(response => response.json())
    // .then(response => console.log(JSON.stringify(response)))
}



const SCREEN_HEIGHT = window.innerHeight;
const SCREEN_WIDTH = window.innerWidth;
let petrParticle = new particle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0);
petrParticle.randomize_angle();
petrParticle.set_speed(0.125);

function positionElement(el, x, y) {
    el.style.position = 'absolute';
    el.style.left = x + 'px';
    el.style.top = y + 'px';
}

const petr = document.querySelector('.petr');

function updatePetrPosition() {
    // console.log(petrParticle.get_angle(), petrParticle.get_speed())
    petrParticle.move();
    let chance = Math.floor(Math.random() * 100)
    if (chance === 5) {petrParticle.set_angle(petrParticle.get_angle()+0.2)}
    if (chance === 10) {petrParticle.set_angle(petrParticle.get_angle()-0.2)}
    let [x, y] = petrParticle.get_position();
    positionElement(petr, x, y);
}

setInterval(updatePetrPosition, 5)

const imagePaths = {
    "normal_petr": "./images/petr.png"
}

let example = {
    "ip": "0.0.0.0",
    "username": "peteranteater",
    "mood": "happy",
    "petr_sprite": "normal_petr",
    "hunger_value": 100,
    "clean_level": 100,
    "boredom_level": 100
}

function loadPetr(petr) {
    // document.querySelector('.username').textContent = `username: ${petr.username}`
    // document.querySelector('.hunger').textContent = `hunger: ${petr.hunger_value}`
    // document.querySelector('.clean').textContent = `clean: ${petr.clean_level}`
    // document.querySelector('.boredom').textContent = `boredom: ${petr.boredom_level}`

    const img = document.createElement("img")
    img.src = imagePaths[petr.petr_sprite]
    const insert = document.querySelector('.petr');
    insert.appendChild(img)
    // load sprite
    // load mood
}

let food = document.querySelector('.feed')
let _play = document.querySelector('.play')
let _shower = document.querySelector('.shower')

function feed() {
    let btn = document.createElement("button");
    btn.innerHTML = food;
    document.body.appendChild(btn);
}

function play() {
    let btn = document.createElement("button");
    btn.innerHTML = _play;
    document.body.appendChild(btn);
}

function shower() {
    let btn = document.createElement("button");
    btn.innerHTML = _shower;
    document.body.appendChild(btn);
}

loadPetr(example)


