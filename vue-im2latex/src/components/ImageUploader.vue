<template>
    <div class="image-uploader">
        <input type="file" @change="onFileChange" />
        <div v-if="imageUrl">
            <img :src="imageUrl" alt="Preview" />
        </div>
        <button @click="uploadImage" :disabled="!selectedFile">Upload</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            imageUrl: null,
            selectedFile: null,
        };
    },
    methods: {
        onFileChange(event) {
            const file = event.target.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.imageUrl = e.target.result;
                    this.selectedFile = file;
                };
                reader.readAsDataURL(file);
            } else {
                alert('Please select an image file.');
            }
        },
        async uploadImage() {
            if (!this.selectedFile) {
                alert("Please select a file first!");
                return;
            }

            const formData = new FormData();
            formData.append("image", this.selectedFile);

            try {
                const response = await fetch('http://localhost:80/upload', {
                    method: 'POST',
                    body: formData,
                });
                const result = await response.json();
                this.$emit('upload-success', result.latexStr); // 이벤트 발생
            } catch (error) {
                console.error("Error uploading file:", error);
            }
        }
    }
};
</script>

<style scoped>
.image-uploader {
    text-align: center;
    margin-top: 20px;
}

.image-uploader img {
    max-width: 100%;
    height: auto;
    margin-top: 10px;
}
</style>
