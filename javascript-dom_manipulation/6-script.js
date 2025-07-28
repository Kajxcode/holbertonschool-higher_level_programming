fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    console.log(data.name);


    const characterDisplay = document.createElement('p');
    characterDisplay.textContent = `Character: ${data.name}`;
    document.body.appendChild(characterDisplay);
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
