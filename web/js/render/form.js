/**
 * Function that updates the dom to show the current value of input quality.
 * @param {number} quality Selected quality of the form
 */
function qualityUpdate(quality) {
  ELEMENTS.ViewPercentage.innerHTML = `${quality}%`;
}

function initialOutputPath() {
  eel.get_output_path()(function (response) {
    if (response) {
      ELEMENTS.InputOutput.value = response;
      store.dispatch({ type: TYPES.UPDATE_OUTPUT_PATH, payload: response });
    }
  });
}

initialOutputPath();
