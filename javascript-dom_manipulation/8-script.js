document.addEventListener('DOMContentLoaded', function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
    const hello = document.getElementById("hello")

    fetch(url)
    .then(response => {
        return response.json()
    })
    .then(response => {
        hello.textContent = response.hello
    })
})
