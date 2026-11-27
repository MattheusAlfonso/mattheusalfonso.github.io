/* Antes da primeira pintura (fora do HTML por causa da CSP, que não aceita script inline):
   a entrada do hero (motion.md) e a guarda dos momentos (moments.md). */
(function () {
  var r = document.documentElement;
  r.classList.add('m-enter', 'mo-js');
  setTimeout(function () { r.classList.add('m-enter-done'); }, 700);
  setTimeout(function () { r.classList.add('mo-safe'); }, 2500);
})();
