<template>
    <div>
      <h2>Saved Stories</h2>
      <ul>
        <li v-for="(s, index) in stories" :key="index">
          <strong>{{ s.keyword }}:</strong> {{ s.story}}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        stories: []
      };
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
  /* 전체 컨테이너 스타일 */
  div {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Noto Sans", sans-serif;
    color: #333;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }

  /* 제목 스타일 */
  h2 {
    font-size: 1.8rem;
    color: #0056b3;
    margin-bottom: 20px;
    text-align: center;
  }

  /* 목록 스타일 */
  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    background-color: #ffffff;
    padding: 15px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    transition: box-shadow 0.3s ease, transform 0.3s ease;
  }

  li:hover {
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
  }

  strong {
    color: #007bff;
  }

  /* 반응형 디자인 */
  @media screen and (max-width: 600px) {
    div {
      padding: 15px;
    }

    h2 {
      font-size: 1.5rem;
    }

    li {
      padding: 10px;
    }
  }
</style>