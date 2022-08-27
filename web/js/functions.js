window.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('button-compress')
    const input_path = document.getElementById('text-input-path')
    const input_quality = document.getElementById('quality-compress')
    const input_prefig = document.getElementById('prefig_text')

    button.addEventListener('click', () => {
        if (input_quality === null || input_quality === '') {
            console.log('Error en input calidad')
        } else {
            const interval = progress_bar()
            eel.compress_img(input_path.value, input_prefig.value, parseInt(input_quality.value))((response) => {
                clearInterval(interval)
                if (response) {
                    complete_progress_bar()
                } else {
                    error_progress_bar()
                }
                setTimeout(() => {
                    clean_progress_bar()
                }, 2000)
            })
        }
    })

})