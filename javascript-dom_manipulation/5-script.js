const header = document.querySelector("header")
const headerId = document.getElementById("update_header")

function newHeader() {
    header.textContent("New Header!!!")
}

headerId.addEventListener("click", newHeader)