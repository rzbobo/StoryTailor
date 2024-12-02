import { createRouter, createWebHistory } from 'vue-router';

// 컴포넌트 가져오기
import HomeView from '@/views/HomeView.vue';
import StoryEditor from '@/views/StoryEditor.vue';
import StoryList from '@/views/StoryList.vue';
import AudioView from '@/views/AudioView.vue';
import StoryUpdateView from '@/views/StoryUpdateView.vue';

// 라우터 설정
const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView, // 홈 화면
  },
  {
    path: '/story-editor',
    name: 'StoryEditor',
    component: StoryEditor, // 스토리 생성 및 편집 화면
  },
  {
    path: '/story-list',
    name: 'StoryList',
    component: StoryList, // 저장된 스토리 보기 화면
  },
  {
    path: '/audio-view',
    name: 'AudioView',
    component: AudioView, // 오디오북 페이지
  },
  {
    path: '/story-update',
    name: 'StoryUpdateView',
    component: StoryUpdateView, // 스토리 생성 및 편집 화면
  }
  , 
  {
    path: '/:pathMatch(.*)*', // 정의되지 않은 경로에 대한 처리
    redirect: '/',
  },
];

const router = createRouter({
  history: createWebHistory(), // 히스토리 모드 사용
  routes,
});

export default router;
