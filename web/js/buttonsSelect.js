window.addEventListener('DOMContentLoaded', () => {

    const button_exten = document.getElementById('button_extencion_select')
    const button_prefig = document.getElementById('button_extencion_prefig')
    const list_prefig = document.getElementById('list_prefig')
    const list_exten = document.getElementById('list_extencion')

    let open_prefig = false
    let open_exten = false

    button_exten.addEventListener('click', () => {
        if (!open_exten) {
            list_exten.style.display = 'block'
            open_exten = true
        } else {
            list_exten.style.display = 'none'
            open_exten = false
        }
    })

    button_prefig.addEventListener('click', () => {
        if (!open_prefig) {
            list_prefig.style.display = 'block'
            open_prefig = true
        } else {
            list_prefig.style.display = 'none'
            open_prefig = false
        }
    })

    list_prefig.addEventListener('click', (event) => {
        if (event.target.tagName === 'H4') {
            const element = event.target
            button_prefig.innerHTML = element.innerHTML
        }
    })

    list_exten.addEventListener('click', (event) => {
        if (event.target.tagName === 'H4') {
            const element = event.target
            button_exten.innerHTML = element.innerHTML
        }
    })

})