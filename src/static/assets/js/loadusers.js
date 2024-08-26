async function loadUser() {
  try {
    const response = await fetch('/auth/get-all-users');
    const users = await response.json();
    const dropdown = document.getElementById('taskAssignedTo');
    dropdown.innerHTML = '';
    users.forEach((user) => {
      const option = document.createElement('option');
      option.value = user.id;
      option.textContent = user.username;
      dropdown.appendChild(option);
    });
  } catch (error) {
    console.error('Error loading users', error);
  }
}

// document.addEventListener('DOMContentLoaded', loadUser);
