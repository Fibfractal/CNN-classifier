import { createStore } from 'vuex'

const state = {
  predictions: [],
  images: [],
  countedLabels: []
}

const mutations = {
  setPredictions(state, predictions) {
    state.predictions = predictions
  },
  setImages(state, images) {
    state.images = images
  },
  setCountedLabels(state, countedLabels){
    state.countedLabels = countedLabels
  },
  mergePredictImage(state){
    for(let i = 0; i < state.predictions.length; i++){
      state.predictions[i].img = state.images[i]
      state.predictions[i].img_url = URL.createObjectURL(state.images[i])
    }
    state.predictions = state.predictions.sort((a,b) => (a.prediction > b.prediction) ? 1 : 
    (a.prediction === b.prediction) ? ((a.probability > b.probability) ? 1 : -1) : -1);

  },
}

export default createStore({ state, mutations })