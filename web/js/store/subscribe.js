const prevState = { ...initialState };

store.subscribe(() => {
  const state = store.getState();

  if (prevState != state) {
    console.log("State: ", state);
  }

  if (prevState.form.quality != state.form.quality) {
    qualityUpdate(state.form.quality);
    prevState.form.quality = state.form.quality;
  }

  if (prevState.form.images != state.form.images) {
    RenderIMGS(state.form.images);
    prevState.form.images = state.form.images;
  }
});
