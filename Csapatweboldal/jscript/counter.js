const counters = document.querySelectorAll(".counter");
let hasAnimated = false;

function animateCounter(counter) {
  const target = +counter.dataset.target;
  const duration = 1500;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    counter.textContent = Math.floor(progress * target);

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      counter.textContent = target;
    }
  }

  requestAnimationFrame(update);
}

const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !hasAnimated) {
        hasAnimated = true;

        counters.forEach(counter => {
          animateCounter(counter);
        });

        observer.disconnect();
      }
    });
  },
  {
    threshold: 0.5
  }
);

counters.forEach(counter => observer.observe(counter));