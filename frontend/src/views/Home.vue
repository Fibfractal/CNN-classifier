<template>

    <div class = "container">
        <h1>Import images of numbers for classification</h1>
        <form enctype="multipart/form-data" novalidate>

            <div class="dropbox">
                <input type="file" multiple :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length" accept="image/*" class="input-file" >
                <p v-if="isInitial"> 
                    Drag your images(s) here or<br> or click to import
                </p>
                <p v-if="isSaving">
                    Uploading {{ fileCount }} files...
                </p>
                <p v-if="isServerFailed">
                    Server error, click or drag to try again!
                </p>
                <p v-if="isWrongFile">
                    Wrong file type click or drag <br> to try again!
                </p>
            </div>
        </form>

        <select class="drop-down" v-model="selectedModel" >
            <option value="" disabled>- Select model -</option>
            <option value="standard">Standard classifier</option>
            <option value="transferlearning">Optional classifier</option>
        </select>

        <div class="spinnerContainer">
          <div v-if="isSaving" class="loader"></div>
        </div>

    </div>

</template>

<script>

  const STATUS_INITIAL = 1, STATUS_SAVING = 2, STATUS_SERVER_FAILED = 3, STATUS_WRONG_FILE = 4;


  export default {
    
    data() {
      return {
        currentStatus: STATUS_INITIAL,
        uploadFieldName: 'photos',
        selectedModel: "standard"
      }
    },
    computed: {
      isInitial() {
        return this.currentStatus === STATUS_INITIAL;
      },
      isSaving() {
        return this.currentStatus === STATUS_SAVING;
      },
      isServerFailed() {
        return this.currentStatus === STATUS_SERVER_FAILED;
      },
      isWrongFile(){
        return this.currentStatus === STATUS_WRONG_FILE;
      }

    },
    methods: {

      async sendPost(formData) {

        this.currentStatus = STATUS_SAVING;

        var res = await fetch('/api/predict/' + this.selectedModel, {
          method: 'POST',
          body: formData
        })

        if (res.ok){

            let predictions = await res.json()
            console.log(predictions)

            this.$store.commit('setPredictions', predictions)
            this.$store.commit('mergePredictImage')
            this.$store.commit('setCountedLabels', this.countLabels())

            this.$router.push('/predictions')
        }
        else {
            console.log("Error")
            this.currentStatus = STATUS_SERVER_FAILED
        }
      },
      filesChange(fieldName, fileList) {

        

        this.$store.commit('setImages', fileList)

        const formData = new FormData();
        if (!fileList.length) return;

        for( var i = 0; i < fileList.length; i++){
            var a = i + 1
            formData.append("image" + a , fileList[i]);
        }

        let flag = true
        let imageAcceptList = ["image/png", "image/jpg", "image/jpeg", "image/bmp", "image/tif", "image/tiff" ]

        // Display the key/value pairs
        for (var file of formData.entries()) {

            console.log(file)

            if(!imageAcceptList.includes(file[1]["type"])){
                flag = false
            }
        }

        flag ? this.sendPost(formData) : this.currentStatus = STATUS_WRONG_FILE

      },
      countLabels(){
        let predictions = this.$store.state.predictions
        console.log("Predictions length: ", predictions.length)
        let counter = [0,0,0,0,0,0,0,0,0,0]
        let dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}


        for(let i = 0; i < predictions.length; i++) {
            dict[predictions[i].prediction] += 1
            console.log("Dictionary: " + dict[predictions[i].prediction])
        }

        for (var key in dict){

            counter[parseInt(key)] = dict[key]
        }
        console.log("List: ", counter) 

        return counter
      }
    },
    updated(){
      // Clears eventual previous error requests
      // so new uploads work
    }


  }

</script>

<style scoped>

  .container {
    display:inline-block;
    width: 80%;
  }

  .container h1 {
    margin-top: 20px;
    margin-bottom: 50px;
  }

  
  /* -- dropbox area -- */

  .dropbox {
    display: flex;
    justify-content: center;
    outline: 2px dashed grey; 
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
    padding: 10px 10px;
    min-height: 200px; 
    position: relative;
    cursor: pointer;
    margin: 30px;
  }

  .input-file {
    opacity: 0; 
    width: 100%;
    height: 200px;
    position: absolute;
    cursor: pointer;
  }

  .dropbox:hover {
    background: lightblue; 
  }

  .dropbox p {
    text-align: center;
    padding: 50px 0;
  }

  /* -- spinner -- */

  .spinnerContainer {
    margin-top: 50px;
    display:flex;
    justify-content: center;
  }

  .loader {

    border: 10px solid #f3f3f3; 
    border-top: 10px solid rgb(206, 90, 90,0.8); 
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

    /* If the screen size is 601px wide or more*/
    @media screen and (min-width: 601px) {
      .dropbox p {
        font-size: 1.2em;
      }

      .drop-down {
        padding: 8px;
        font-size: 16px;
        margin-top: 5px;
      }      
    }

    /* If the screen size is 600px wide or less*/
    @media screen and (max-width: 600px) {
      h1 {
          font-size: 20px;
      }

      .dropbox p {
        font-size: 0.8em;
      }

      .drop-down {
        padding: 3px;
        font-size: 12px;
      }      
    }

</style>