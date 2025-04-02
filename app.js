const { createApp, ref } = Vue;

const API_BASE = "https://amvekere.pythonanywhere.com/api";

createApp({
  setup() {
    const user = ref(null);
    const chats = ref([]);

    // Check if logged in on load
    if (localStorage.getItem('token')) {
      fetch(`${API_BASE}/me`, {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
      })
        .then(res => res.json())
        .then(data => user.value = data);
    }

    const login = (username, password) => {
      fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      })
        .then(res => res.json())
        .then(data => {
          if (data.access_token) {
            localStorage.setItem('token', data.access_token);
            user.value = { username }; // Update UI
          }
        });
    };

    return { user, chats, login };
  }
}).mount('#app');