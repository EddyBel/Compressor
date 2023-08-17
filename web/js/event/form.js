/**
 * This function is executed every time a change occurs in the photo upload input.
 */
ELEMENTS.InputFiles.addEventListener("change", (event) => {
  const target = event.target;

  if (target) {
    const files = target.files;
    store.dispatch({ type: TYPES.UPDATE_SELECTED_IMAGES, payload: files });
  }
});

ELEMENTS.InputPrefix.addEventListener("change", (event) => {
  const target = event.target;

  if (target) {
    const value = target.value;
    store.dispatch({ type: TYPES.UPDATE_PREFIX, payload: value });
  }
});

ELEMENTS.InputQuality.addEventListener("input", (event) => {
  const target = event.target;

  if (target) {
    const value = target.value;
    store.dispatch({ type: TYPES.UPDATE_QUALITY, payload: value });
  }
});

ELEMENTS.InputOutput.addEventListener("change", (event) => {
  const target = event.target;

  if (target) {
    const value = target.value;
    store.dispatch({ type: TYPES.UPDATE_OUTPUT_PATH, payload: value });
  }
});

ELEMENTS.ButtonCompress.addEventListener("click", () => {
  const files = ELEMENTS.InputFiles.files;
  compressIMGS(files);
});
