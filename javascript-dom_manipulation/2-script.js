const clickable = document.querySelector('#red_header');
const header = document.querySelector('header');

if (clickable && header) {
  clickable.addEventListener('click', () => {
    header.classList.add('red');
  });
}
