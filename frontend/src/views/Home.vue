<template>

    <div>
        <form enctype="multipart/form-data" novalidate v-if="isInitial || isSaving">
            <h1>Import images to classify</h1>
            <div class="dropbox">
                <input type="file" multiple :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length" accept="image/*" class="input-file" >
                <p v-if="isInitial"> 
                    Drag your images(s) here or<br> or click to import
                </p>
                <p v-if="isSaving">
                    Uploading {{ fileCount }} files...
                </p>
                <p v-if="isFailed">
                    Uploading failed, click or drag to try again!
                </p>
            </div>
        </form>

    </div>

</template>

<script>

  const STATUS_INITIAL = 1, STATUS_SAVING = 2, STATUS_SUCCESS = 3, STATUS_FAILED = 4;


  export default {
    
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: 1,
        uploadFieldName: 'photos',
      }
    },
    computed: {
      isInitial() {
        return this.currentStatus === STATUS_INITIAL;
      },
      isSaving() {
        return this.currentStatus === STATUS_SAVING;
      },
      isSuccess() {
        return this.currentStatus === STATUS_SUCCESS;
      },
      isFailed() {
        return this.currentStatus === STATUS_FAILED;
      }
    },
    methods: {
      reset() {
        // reset form to initial state
        this.currentStatus = STATUS_INITIAL;
        this.uploadedFiles = [];
        this.uploadError = null;
      },
      async sendPost(formData, testFile) {

        this.currentStatus = STATUS_SAVING;

        var res = await fetch('/api/predict', {
          method: 'POST',
          body: formData
        })

        if (res.ok){

            let predictions = await res.json()
            console.log(predictions)

            this.$store.commit('setPredictions', predictions)
            this.$store.commit('mergePredictImage')

            this.$router.push('Predictions')
        }
        else {
            console.log("Error")
            this.currentStatus = STATUS_FAILED
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

        flag ? this.sendPost(formData, fileList) : console.log("Wrong file type!")
      }
    },


  }

</script>

<style scoped>
    
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
    
    font-size: 1.2em;
    text-align: center;
    padding: 50px 0;
  }

</style>