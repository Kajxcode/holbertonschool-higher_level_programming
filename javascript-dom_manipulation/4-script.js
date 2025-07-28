const addButton = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

if (addButton && list) {
  addButton.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });
}
