<template>
    <div class="edit-view">
      <h1>스토리 편집</h1>
      <p>생성된 스토리를 선택하고 추가 키워드를 입력하여 수정하세요!</p>
  
      <!-- 스토리 선택 -->
      <section class="story-selector">
        <h2>스토리 선택</h2>
        <select v-model="selectedStory">
          <option v-for="(story, index) in stories" :key="index" :value="story">
            {{ story.keyword }}
          </option>
        </select>
      </section>
  
      <!-- 선택된 스토리 내용 -->
      <section v-if="selectedStory" class="story-content">
      <h2>선택된 스토리</h2>
      <p>{{ selectedStory.story }}</p>
    </section>
      
      <!-- 키워드 추가 -->
      <section class="keyword-editor" v-if="selectedStory">
        <h2>추가 키워드 입력</h2>
        <input
          type="text"
          v-model="newKeyword"
          placeholder="추가할 키워드를 입력하세요"
        />
        <button @click="addKeyword" :disabled="!newKeyword">키워드 추가</button>
      </section>
  
      <!-- 결과 출력 -->
      <section v-if="updatedStory">
        <h2>수정된 스토리</h2>
        <p>{{ updatedStory.story }}</p>
      </section>
  
      <p v-else-if="loading">스토리를 불러오는 중입니다...</p>
    </div>
  </template>
  
  <script>
  import axios from "axios"; // 컴포넌트별로 axios를 직접 임포트
  
  export default {
    data() {
      return {
        stories: [], // 저장된 스토리 목록
        selectedStory: null, // 선택된 스토리
        newKeyword: "", // 새 키워드
        updatedStory: null, // 수정된 스토리
        loading: false, // 로딩 상태
      };
    },
    methods: {
      async fetchStories() {
        try {
          this.loading = true;
          const response = await axios.get("http://127.0.0.1:5000/get-stories");
          this.stories = response.data.stories;
        } catch (error) {
          console.error("스토리를 불러오지 못했습니다:", error);
        } finally {
          this.loading = false;
        }
      },
      async addKeyword() {
  if (!this.selectedStory || !this.newKeyword) return;

  try {
    this.loading = true;

    // API 호출로 키워드 추가 요청
    const response = await axios.post(
      "http://127.0.0.1:5000/update-story",
      {
        keyword: this.selectedStory.keyword, // 기존 키워드
        newKeyword: this.newKeyword, // 추가 키워드
      }
    );

    // 업데이트된 스토리 데이터를 저장
    this.updatedStory = response.data.updatedStory;
    this.newKeyword = ""; // 입력 필드 초기화
  } catch (error) {
    console.error("스토리를 수정하지 못했습니다:", error);
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
  /* 공통 스타일 */
  .edit-view {
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    font-family: "Noto Sans", sans-serif;
    color: #333;
  }

  h1 {
    font-size: 2.5rem;
    color: #0056b3;
    margin-bottom: 10px;
  }

  h2 {
    font-size: 1.5rem;
    color: #0056b3;
    margin-bottom: 15px;
  }

  p {
    font-size: 1rem;
    line-height: 1.6;
    color: #555;
  }

  /* 섹션 스타일 */
  section {
    background-color: #f9f9f9;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }

  .story-selector select,
  .keyword-editor input {
    width: 100%;
    max-width: 400px;
    padding: 10px;
    margin-top: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    color: #333;
    outline: none;
  }

  .story-selector select:focus,
  .keyword-editor input:focus {
    border-color: #007bff;
    box-shadow: 0 0 4px rgba(0, 123, 255, 0.5);
  }

  .story-content p {
    background-color: #e9ecef;
    padding: 15px;
    border-radius: 5px;
    text-align: left;
    color: #444;
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

  /* 반응형 디자인 */
  @media screen and (max-width: 600px) {
    h1 {
      font-size: 2rem;
    }

    h2 {
      font-size: 1.2rem;
    }

    .edit-view {
      padding: 15px;
    }

    section {
      padding: 15px;
    }

    button {
      font-size: 0.9rem;
      padding: 8px 15px;
    }
  }
</style>