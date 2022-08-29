window.addEventListener('DOMContentLoaded', () => {

    // const inputFile = document.getElementById('filepicker')
    const buttonFile = document.getElementById('button-file-or-folder')
    const input_path = document.getElementById('input_folder_path')

    const output_path = document.getElementById('output_folder_path')
    const buttonOutput = document.getElementById('button-file-or-folder_output')
    // const number_files = document.querySelector('.number-files')

    buttonFile.addEventListener('click', () => {
        eel.open_select_folder()(path => {
            input_path.value = path
            output_path.value = path + '/output_media'
        })
    })

    buttonOutput.addEventListener('click', () => {
        eel.open_select_folder()(path => {
            output_path.value = path
        })
    })

})