const header = document.querySelector("header")
const redHeader = document.getElementById("red_header")

function changer() {
    header.style.color = "#FF0000"
}

redHeader.addEventListener("click", changer)
