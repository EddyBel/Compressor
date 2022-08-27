function progress_bar() {
    const content_bar = document.querySelector('.content_bar')
    const bar = document.querySelector('.compress_bar_loading')

    const long = bar.clientWidth

    let porst = 0

    return setInterval(() => {
        if (long > content_bar.clientWidth) {
            porst = porst + 0.5
            content_bar.style.width = `${porst}%`
        }
    }, 1000)
}

function complete_progress_bar() {
    const content_bar = document.querySelector('.content_bar')
    content_bar.style.width = '100%'
}

function clean_progress_bar() {
    const content_bar = document.querySelector('.content_bar')
    content_bar.style.width = '0%'
}

function error_progress_bar() {
    const content_bar = document.querySelector('.content_bar')
    content_bar.style.background = 'red'
}