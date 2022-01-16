const open = document.getElementById('open');
const modalContainer = document.getElementById('modal_container_gt');
const close = document.getElementById('no-btn');
const proceed = document.getElementById('yes-btn');

open.addEventListener('click', () => {
    modalContainer.classList.add('show')
});

proceed.addEventListener('click', () => {
    modalContainer.classList.remove('show')
});

close.addEventListener('click', () => {
    modalContainer.classList.remove('show')
});