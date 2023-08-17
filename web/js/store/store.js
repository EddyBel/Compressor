const initialState = {
  form: {
    images: [],
    quality: 50,
    prefix: "",
    outputPath: "",
  },
  status: {
    imagesCompressed: [],
  },
};

const store = Redux.createStore(reducer, initialState);
