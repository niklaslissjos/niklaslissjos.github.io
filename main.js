document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('a[href^="#equation-"]');
  
  links.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').slice(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    });
  });
});

// Theme switch code
const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');
const themeIcon = document.querySelector('.theme-icon');

if (currentTheme) {
  document.documentElement.classList.add(currentTheme);
  document.body.classList.add(currentTheme);
  if (currentTheme === 'dark-theme') {
    toggleSwitch.checked = true;
    themeIcon.textContent = '🌙';
  }
}

function switchTheme(e) {
  if (e.target.checked) {
    document.documentElement.classList.add('dark-theme');
    document.body.classList.add('dark-theme');
    localStorage.setItem('theme', 'dark-theme');
    themeIcon.textContent = '🌙';
  } else {
    document.documentElement.classList.remove('dark-theme');
    document.body.classList.remove('dark-theme');
    localStorage.setItem('theme', 'light-theme');
    themeIcon.textContent = '☀️';
  }    
}

toggleSwitch.addEventListener('change', switchTheme, false);

// Copyright year update
document.getElementById('year').textContent = new Date().getFullYear();
