window.addEventListener('DOMContentLoaded', () => {

    const inputFile = document.getElementById('filepicker')
    const buttonFile = document.getElementById('button-file-or-folder')

    buttonFile.addEventListener('click', () => {
        inputFile.click()
    })

})