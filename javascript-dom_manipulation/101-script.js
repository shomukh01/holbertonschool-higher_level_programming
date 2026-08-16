document.addEventListener('DOMContentLoaded', () => {
  const language = document.querySelector('#language_code');
  const button = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  button.addEventListener('click', () => {
    const lang = language.value;

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
      .then((response) => response.json())
      .then((data) => {
        hello.textContent = data.hello;
      });
  });
});
