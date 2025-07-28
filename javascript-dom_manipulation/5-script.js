const updateButton = document.querySelector('#update_header');
const header = document.querySelector('header');

if (updateButton && header) {
  updateButton.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
  });
}
