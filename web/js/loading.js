function add_spin() {
    const content = document.querySelector('.content_loading')
    content.innerHTML = '<div class="Loading"></div>'
}

function add_check() {
    const content = document.querySelector('.content_loading')
    content.innerHTML = '<h3 class="text_status_loading" >Correcto</h3>'
}

function add_erro() {
    const content = document.querySelector('.content_loading')
    content.innerHTML = '<h3 class="text_status_loading" >Error</h3>'
}

function clean_content() {
    const content = document.querySelector('.content_loading')
    content.innerHTML = ''
}