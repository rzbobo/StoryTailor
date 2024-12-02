<template>
    <div>
      <input v-model="keyword" placeholder="Enter a keyword" />
      <button @click="generateStory">Generate Story</button>
      <div v-if="story">
        <textarea v-model="editedStory" rows="10" cols="50"></textarea>
        <button @click="saveStory">Save Story</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        keyword: '',
        story: '',
        editedStory: ''
      };
    },
    methods: {
      async generateStory() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/generate-story', {
            keyword: this.keyword
          });
          this.story = response.data.story;
          this.editedStory = this.story;
        } catch (error) {
          console.error(error);
        }
      },
      async saveStory() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/save-story', {
            story: this.editedStory,
            keyword: this.keyword
          });
          console.log(response.data.message);
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
/* 전체 컨테이너 스타일 */
div {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Noto Sans", sans-serif;
  color: #333;
  text-align: center;
}

/* 제목 및 입력 필드 스타일 */
input {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  margin: 10px 0;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  outline: none;
}

input:focus {
  border-color: #007bff;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

/* 버튼 스타일 */
button {
  padding: 10px 20px;
  margin-top: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

/* 텍스트 에어리어 스타일 */
textarea {
  width: 100%;
  max-width: 100%;
  padding: 10px;
  margin-top: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  resize: vertical;
}

textarea:focus {
  border-color: #007bff;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

/* 반응형 디자인 */
@media screen and (max-width: 600px) {
  input, textarea {
    font-size: 0.9rem;
    padding: 8px;
  }

  button {
    font-size: 0.9rem;
    padding: 8px 15px;
  }
}
</style>
