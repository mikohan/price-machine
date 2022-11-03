const { createApp } = Vue;

createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      message: 'Hello Vue!',
    };
  },
}).mount('#app');
