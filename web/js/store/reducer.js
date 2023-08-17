function reducer(state, action) {
  const type = action.type;
  const payload = action.payload;

  switch (type) {
    case TYPES.UPDATE_SELECTED_IMAGES:
      return {
        ...state,
        form: {
          ...state.form,
          images: payload,
        },
      };

    case TYPES.UPDATE_PREFIX:
      return {
        ...state,
        form: {
          ...state.form,
          prefix: payload,
        },
      };

    case TYPES.UPDATE_QUALITY:
      return {
        ...state,
        form: {
          ...state.form,
          quality: payload,
        },
      };

    case TYPES.UPDATE_OUTPUT_PATH:
      return {
        ...state,
        form: {
          ...state.form,
          outputPath: payload,
        },
      };

    case TYPES.ADD_IMAGES_COMPRESSED:
      return {
        ...state,
        status: {
          ...state.status,
          imagesCompressed: [...state.status.imagesCompressed, payload],
        },
      };

    case TYPES.CLEAN_IMAGES_COMPRESSED:
      return {
        ...state,
        status: {
          ...state.status,
          imagesCompressed: [],
        },
      };

    default:
      return state;
  }
}
