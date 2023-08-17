function compressIMGS(files) {
  const output = ELEMENTS.InputOutput.value;
  const prefix = ELEMENTS.InputPrefix.value;
  const quality = ELEMENTS.InputQuality.value;

  store.dispatch({ type: TYPES.CLEAN_IMAGES_COMPRESSED });

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const name = file.name + prefix;

    let reader = new FileReader();
    reader.onload = function (e) {
      const img = e.target.result;

      if (img) {
        eel.compress_img(
          img,
          name,
          output,
          parseInt(quality)
        )(function (response) {
          store.dispatch({
            type: TYPES.ADD_IMAGES_COMPRESSED,
            payload: response.name,
          });
        });
      }
    };

    reader.readAsDataURL(file);
  }
}
