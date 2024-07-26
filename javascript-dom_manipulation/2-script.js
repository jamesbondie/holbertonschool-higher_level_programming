const header = document.querySelector('header')
const red_header = document.getElementById("red_header")

function classadder() {
    header.classList.add("red")
}

red_header.addEventListener("click", classadder)