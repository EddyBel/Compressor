window.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('button-compress')
    const input_path = document.getElementById('input_folder_path')
    const input_quality = document.getElementById('quality-compress')
    const input_prefig = document.getElementById('prefig_text')
    const input_output = document.getElementById('output_folder_path')

    button.addEventListener('click', () => {
        if (input_quality.value === null || input_quality.value === '') {
            console.log('Error en input calidad')
        } else {
            add_spin()
            eel.compress_img_to_folder(input_path.value, input_prefig.value, parseInt(input_quality.value), input_output.value)(response => {
                if (response) add_check()
                else add_erro()
                setTimeout(() => {
                    clean_content()
                }, 2000)
            })
        }
    })

})