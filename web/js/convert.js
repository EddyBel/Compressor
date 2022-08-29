window.addEventListener('DOMContentLoaded', () => {

    const buttonConvert = document.getElementById('button-convert')
    const input = document.getElementById('input_folder_path')
    const output = document.getElementById('output_folder_path')
    const prefig = document.getElementById('button_extencion_prefig')
    const exten = document.getElementById('button_extencion_select')

    let count;
    let text;

    buttonConvert.addEventListener('click', () => {

        if (exten.innerHTML === 'Extencion' || prefig.innerHTML === 'Prefig') {
            console.log('Rellena los datos')
        } else {
            if (prefig.innerHTML === '[1, 2, 3, ...]') count = 0
            else if (prefig.innerHTML === 'Original') count = ''
            add_spin()
            eel.convert_img_to_folder(input.value, '', '', output.value, exten.innerHTML, count)(response => {
                if (response) add_check()
                else add_erro()
                setTimeout(() => {
                    clean_content()
                }, 2000)
            })
        }
    })

})