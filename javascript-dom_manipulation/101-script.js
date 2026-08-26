document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.querySelector('#btn_translate');
  const langCode = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  btnTranslate.addEventListener('click', function () {
    const lang = langCode.value;
    if (lang) {
      fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
        .then((response) => response.json())
        .then((data) => {
          helloDiv.textContent = data.hello;
        });
    }
  });
});
