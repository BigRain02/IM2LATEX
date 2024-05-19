<template>
    <div class="image-uploader">
        <input type="file" @change="onFileChange" />
        <div v-if="imageUrl">
            <img :src="imageUrl" alt="Preview" />
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            imageUrl: null
        };
    },
    methods: {
        onFileChange(event) {
            const file = event.target.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.imageUrl = e.target.result;
                };
                reader.readAsDataURL(file);
            } else {
                alert('Please select an image file.');
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
