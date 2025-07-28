const header = document.querySelector('header');

const clickable = document.querySelector('#red_header');

if (clickable && header) {
  clickable.addEventListener('click', () => {
    header.style.color = '#FF0000';
  });
}