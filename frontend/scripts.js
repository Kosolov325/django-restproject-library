async function fetchUsers() {
    const response = await fetch('https://library-project-backend.herokuapp.com/users/');
    const data = await response.json()
    console.log(data)
  }

  fetchUsers()