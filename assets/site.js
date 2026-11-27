/* O relatório do hero "roda" a análise: a varredura passa pelo cabeçalho, cada falha acende na sua vez
   e o score sobe de 0 a 95 (1,1 s). Uma vez quando a página abre e de novo quando o mouse entra no palco.
   É uma animação de carga, não um loop: o Glass Fold atrás já é o efeito do hero (motion.md, Tech budget).
   Movimento reduzido e sem script: o relatório já está pronto no HTML, com o 95 no lugar. */
const rep = document.querySelector('[data-rep]');
const num = rep && rep.querySelector('[data-rep-num]');
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;

if (rep && num && !still) {
  const final = Number(num.textContent) || 0;
  let last = 0;
  const run = () => {
    const now = performance.now();
    if (now - last < 1800) return;
    last = now;
    rep.classList.remove('is-run');
    void rep.offsetWidth; // reinicia as animações CSS
    rep.classList.add('is-run');
    const t0 = now + 250, dur = 1100;
    const tick = (t) => {
      const k = Math.min(1, Math.max(0, (t - t0) / dur));
      num.textContent = String(Math.round(final * (1 - Math.pow(1 - k, 3))));
      if (k < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  // depois da entrada do hero (motion.md: cerca de 1,1 s)
  setTimeout(run, 650);
  const stage = rep.closest('.hero__stage');
  if (stage && matchMedia('(hover: hover) and (pointer: fine)').matches) stage.addEventListener('pointerenter', run);
}
