import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 위에서 만든 라우터 가져오기

createApp(App)
  .use(router) // 라우터 연결
  .mount('#app');
