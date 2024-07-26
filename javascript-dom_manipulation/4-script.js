const list = document.querySelector("ul.my_list")
const addItem = document.getElementById("add_item")

function itemAdder() {
    const newItem = document.createElement("li")

    newItem.textContent("item")
    list.appendChild(newItem)
}


addItem.addEventListener("click", itemAdder)