document.addEventListener('DOMContentLoaded', () => {
  const list = document.querySelector('.my_list');
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');

  addItem.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });

  removeItem.addEventListener('click', () => {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  clearList.addEventListener('click', () => {
    list.innerHTML = '';
  });
});
