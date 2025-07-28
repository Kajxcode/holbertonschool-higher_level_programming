document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloElement = document.getElementById('hello');
      if (helloElement) {
        helloElement.textContent = data.hello;
      }
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
    });
});
