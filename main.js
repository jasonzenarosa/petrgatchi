import { particle } from "./petr.js"

const SCREEN_HEIGHT = window.innerHeight;
const SCREEN_WIDTH = window.innerWidth;
let petrParticle = new particle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0);
petrParticle.randomize_angle();
petrParticle.set_speed(0.25);

function positionElement(el, x, y) {
    el.style.position = 'absolute';
    el.style.left = x + 'px';
    el.style.top = y + 'px';
}

const petr = document.querySelector('.petr');

function updatePetr() {
    // console.log(petrParticle.get_angle(), petrParticle.get_speed())
    petrParticle.move();
    let chance = Math.floor(Math.random() * 100)
    if (chance === 5) {petrParticle.randomize_angle()}
    let [x, y] = petrParticle.get_position();
    positionElement(petr, x, y);
}

setInterval(updatePetr, 5)

const imagePaths = {
    "normal_petr": "./images/petr.png"
}

const example = {
    "ip": "0.0.0.0",
    "username": "peteranteater",
    "mood": "happy",
    "petr_sprite": "normal_petr",
    "hunger_value": 100,
    "clean_level": 100,
    "boredom_level": 100
}

function loadPetr(petr) {
    document.querySelector('.username').textContent = `username: ${petr.username}`
    document.querySelector('.hunger').textContent = `hunger: ${petr.hunger_value}`
    document.querySelector('.clean').textContent = `clean: ${petr.clean_level}`
    document.querySelector('.boredom').textContent = `boredom: ${petr.boredom_level}`

    const img = document.createElement("img")
    img.src = imagePaths[petr.petr_sprite]
    const insert = document.querySelector('.petr');
    insert.appendChild(img)
    // load sprite
    // load mood
}

loadPetr(example)
