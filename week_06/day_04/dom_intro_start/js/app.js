console.log('app loaded', window);

document.addEventListener('DOMContentLoaded', () => { // NEW
    const title = document.querySelector('h1');
    title.textContent = 'JavaScript says, Hello World!';
});