const url = "https://swapi-api.hbtn.io/api/films/?format=json"
const total = document.getElementById("list_movies")

function lister() {
    fetch(url)
    .then(response => {
        return response.json()
    })
    .then(response => {
        const movies = response.results
        movies.forEach(movie => {

            const li = document.createElement("li")
            li.textContent = movie.title
            total.appendChild(li)
        })
    })
}
lister()