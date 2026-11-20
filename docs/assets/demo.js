const locale = document.documentElement.lang === 'pt-BR' ? 'pt' : 'en';
const results = window.luminaScenarios;
const form = document.querySelector('#gate-form');
const prompt = document.querySelector('#prompt');
const verdict = document.querySelector('#verdict');
const decision = document.querySelector('#decision');
const score = document.querySelector('#score');
const evidence = document.querySelector('#evidence');
const number = new Intl.NumberFormat(locale === 'pt' ? 'pt-BR' : 'en', {
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

function showResult(days) {
  const scenario = results[days];
  decision.textContent = scenario.decision;
  decision.dataset.decision = scenario.decision;
  score.textContent = locale === 'pt'
    ? `Nota ${number.format(scenario.score)} · limite ${number.format(scenario.threshold)}`
    : `Score ${number.format(scenario.score)} · threshold ${number.format(scenario.threshold)}`;
  evidence.textContent = scenario.explanation[locale];
}

if (results) {
  form.hidden = false;
  prompt.hidden = false;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    showResult(new FormData(form).get('days'));
    prompt.hidden = true;
    verdict.hidden = false;
  });
  form.addEventListener('change', () => {
    verdict.hidden = true;
    prompt.hidden = false;
  });
}
