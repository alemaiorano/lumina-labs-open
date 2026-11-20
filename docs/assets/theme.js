const theme = document.querySelector('#theme');
const root = document.documentElement;
const systemDark = matchMedia('(prefers-color-scheme: dark)');
const themeKey = 'lumina-labs-theme';

function currentTheme() {
  return root.dataset.theme || (systemDark.matches ? 'dark' : 'light');
}

function syncThemeControl() {
  theme.setAttribute('aria-pressed', String(currentTheme() === 'dark'));
}

try {
  const saved = localStorage.getItem(themeKey);
  if (saved === 'dark' || saved === 'light') root.dataset.theme = saved;
} catch {
  // Browser storage can be unavailable when opening the demo from disk.
}
theme.hidden = false;
syncThemeControl();
systemDark.addEventListener('change', syncThemeControl);
theme.addEventListener('click', () => {
  root.dataset.theme = currentTheme() === 'dark' ? 'light' : 'dark';
  try {
    localStorage.setItem(themeKey, root.dataset.theme);
  } catch {
    // The current document still uses the selected theme.
  }
  syncThemeControl();
});
