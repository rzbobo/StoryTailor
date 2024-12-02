<template>
    <div class="home">
      <!-- 배너 섹션 -->
      <section class="banner">
        <img src="@/assets/banner.jpg" alt="StoryTailor Banner" />
        <h1>맞춤형 스토리를 생성하세요</h1>
        <p>간단한 키워드로 나만의 이야기를 만들어보세요.</p>
      </section>
  
      <!-- 주요 기능 버튼 -->
      <section class="features">
        <button @click="goToStoryEditor">스토리 생성</button>
        <button @click="goToStoryList">저장된 스토리 보기</button>
        <button @click="goToStoryUpdate">스토리 수정하기</button>
        <button @click="goToAudioView">오디오북 듣기</button>
      </section>
  

    </div>
  </template>
  
  <script>
    import axios from 'axios';

  export default {
    
    data() {
      return {
        keyword: '',
        stories: [],
      };
    },
    methods: {
      goToStoryEditor() {
        this.$router.push('/story-editor');
      },
      goToStoryList() {
        this.$router.push('/story-list');
      },
      goToAudioView() {
        this.$router.push('/audio-view');
      },
      goToStoryUpdate() {
        this.$router.push('/story-update');
      },
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
    },
    async mounted() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/get-stories');
        this.stories = response.data.stories;
      } catch (error) {
        console.error(error);
      }
    }
  };
  </script>
  
  <style scoped>
  .banner {
  text-align: center;
  padding: 40px 20px;
  color: rgb(18, 9, 9);
}

.banner img {
  max-width: 100%;
  height: auto;
  margin-bottom: 20px;
}

.banner h1 {
  font-size: 2.5rem;
  margin-bottom: 5px;
  text-shadow: 2px 2px 4px rgba(19, 14, 14, 0.399);
}

.banner p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

.features {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 30px 0;
}

.features button {
  padding: 10px 20px;
  font-size:  1rem;
  font-weight: bold;
  background-color: #7eb7c5;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, background-color 0.2s;
}

.features button:hover {
  background-color: #1e63d9;
  transform: translateY(-2px);
}

.features button:active {
  transform: translateY(1px);
}

.story-generator {
  text-align: center;
  margin: 40px 0;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.story-generator h2 {
  font-size: 1.5rem;
  margin-bottom: 15px;
}

.story-generator input[type="text"] {
  width: 60%;
  padding: 10px;
  font-size: 1rem;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}

.story-generator button {
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: bold;
  background-color: #6a11cb;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: transform 0.2s, background-color 0.2s;
}

.story-generator button:hover {
  background-color: #541cae;
  transform: translateY(-2px);
}

.story-generator button:active {
  transform: translateY(1px);
}

.recent-stories {
  padding: 30px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.recent-stories h2 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  text-align: center;
}

.recent-stories ul {
  list-style-type: none;
  padding: 0;
}

.recent-stories li {
  padding: 10px;
  margin-bottom: 10px;
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
}

.recent-stories li strong {
  color: #2575fc;
}

.recent-stories li:hover {
  background: #eef3fc;
}

  </style>
  