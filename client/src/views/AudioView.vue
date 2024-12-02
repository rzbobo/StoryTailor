<template>
  <div class="audio-view">
    <h1>오디오북</h1>
    <p>생성된 스토리를 오디오로 들어보세요!</p>

    <!-- 스토리 선택 및 오디오 변환 버튼 -->
    <section class="story-selector">
      <h2>스토리 선택</h2>
      <select v-model="selectedStory">
        <option v-for="(story, index) in stories" :key="index" :value="story">
          {{ story.keyword }}
        </option>
      </select>
      <button @click="convertToAudio" :disabled="!selectedStory">오디오 변환</button>
    </section>

    <!-- 오디오 플레이어 -->
    <section class="audio-player" v-if="audioUrl">
      <h2>오디오 플레이어</h2>
      <audio :src="audioUrl" controls></audio>
    </section>

    <p v-else-if="loading">오디오를 생성 중입니다. 잠시만 기다려주세요...</p>
  </div>
</template>

<script>
import axios from 'axios'; // axios를 개별적으로 임포트

export default {
  data() {
    return {
      stories: [], // 저장된 스토리 목록
      selectedStory: null, // 선택된 스토리
      audioUrl: '', // 생성된 오디오 파일 URL
      loading: false, // 로딩 상태
    };
  },
  methods: {
    async fetchStories() {
      try {
        // API 호출로 저장된 스토리 가져오기
        const response = await axios.get('http://127.0.0.1:5000/get-stories');
        this.stories = response.data.stories;
      } catch (error) {
        console.error('스토리를 불러오지 못했습니다:', error);
      }
    },
    async convertToAudio() {
      if (!this.selectedStory) return;

      try {
        this.loading = true;

        // API 호출로 선택된 스토리를 오디오로 변환
        const response = await axios.post('http://127.0.0.1:5000/convert-to-audio', {
          story: this.selectedStory.story,
        });

        this.audioUrl = response.data.audio_url; // 반환된 오디오 URL 저장
      } catch (error) {
        console.error('오디오 변환 실패:', error);
      } finally {
        this.loading = false;
      }
    },
  },
  mounted() {
    this.fetchStories(); // 컴포넌트가 로드되면 저장된 스토리를 불러옴
  },
};
</script>

<style scoped>
/* 전체 컨테이너 스타일 */
.audio-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  font-family: "Noto Sans", sans-serif;
  color: #333;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

/* 제목 스타일 */
h1 {
  font-size: 2.5rem;
  color: #0056b3;
  margin-bottom: 10px;
}

h2 {
  font-size: 1.8rem;
  color: #007bff;
  margin-bottom: 15px;
}

p {
  font-size: 1rem;
  line-height: 1.6;
  color: #555;
}

/* 스토리 선택 섹션 */
.story-selector {
  margin: 20px 0;
  text-align: center;
}

.story-selector select {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  color: #333;
  outline: none;
  transition: border-color 0.3s ease;
}

.story-selector select:focus {
  border-color: #007bff;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
}

/* 버튼 스타일 */
button {
  margin-top: 15px;
  padding: 10px 20px;
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

/* 오디오 플레이어 */
.audio-player {
  margin-top: 20px;
}

.audio-player audio {
  width: 100%;
  max-width: 600px;
  outline: none;
  border-radius: 5px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

/* 로딩 상태 스타일 */
p[loading] {
  font-size: 1rem;
  color: #888;
  font-style: italic;
}

/* 반응형 디자인 */
@media screen and (max-width: 600px) {
  .audio-view {
    padding: 15px;
  }

  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  button {
    font-size: 0.9rem;
    padding: 8px 15px;
  }

  .story-selector select {
    font-size: 0.9rem;
    padding: 8px;
  }

  .audio-player audio {
    max-width: 100%;
  }
}
</style>