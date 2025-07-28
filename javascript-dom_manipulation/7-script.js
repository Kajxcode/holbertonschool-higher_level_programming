fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById('list_movies');
    if (!list) return;

    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      list.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
