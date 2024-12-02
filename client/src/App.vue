<template>
  <div id="app">
    <nav>
      <router-link to="/"><img src="@/assets/home.jpg"></router-link>
      <router-link to="/story-editor"><img src="@/assets/create.jpg"></router-link>
      <router-link to="/story-list"><img src="@/assets/list.jpg"></router-link>
      <router-link to="/story-update"><img src="@/assets/edit.jpg"></router-link>
      <router-link to="/audio-view"><img src="@/assets/audio.jpg"></router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
nav {
  display: flex;  
  background: #f5f5f5;
}
</style>
