 // Select the loader element
  const loader = document.querySelector('#loader');

  // Show the loader when the form is submitted
  const form = document.querySelector('form');
  form.addEventListener('submit', () => {
    loader.style.display = 'block';
  });

  // Hide the loader after 10 seconds
  setTimeout(() => {
    loader.style.display = 'none';
  }, 5000);
