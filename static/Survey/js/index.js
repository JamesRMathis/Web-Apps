const form = document.getElementById("form")
form.addEventListener("submit", (e) => {
    e.preventDefault()

    if (document.cookie.includes("survey=true")) {
        alert("You have already taken the survey!")
        return
    }

    const formData = new FormData(form)
    const data = Object.fromEntries(formData)
    document.cookie = 'survey=true;'
    form.submit()
})

function takenSurvey() {
    if(document.cookie.includes("survey=true")) {
        document.getElementById("goToResults").submit()
    }
}