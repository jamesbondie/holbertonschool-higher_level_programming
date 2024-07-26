const url = "https://swapi-api.hbtn.io/api/people/6/?format=json"
const characterId = document.getElementById("character")

function fetcher() {
    fetch(url)
    .then(response => {
        return response.json()
    })
    .then(response => {
        characterId.textContent = response.name
    })
}
fetcher()