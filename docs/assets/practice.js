const form = document.querySelector('#practice-form');
const prompt = document.querySelector('#result-prompt');
const outcomes = document.querySelectorAll('[data-answer]');
const evidence = document.querySelector('#evidence');

form.hidden = false;
prompt.hidden = false;

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const selected = new FormData(form).get('answer');
  for (const outcome of outcomes) {
    outcome.hidden = outcome.dataset.answer !== selected;
  }
  prompt.hidden = true;
  evidence.hidden = false;
});

form.addEventListener('change', () => {
  for (const outcome of outcomes) outcome.hidden = true;
  evidence.hidden = true;
  prompt.hidden = false;
});
