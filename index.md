---
layout: page
permalink: /
hide_title: true
---

<div id="launch-container" class="d-flex justify-content-center w-100" style="position: relative; height: 320px; cursor: pointer; z-index: 100;" markdown="0">
  <div style="position: relative; width: 320px; height: 320px; pointer-events: none;">
    <img src="{{ '/assets/img/tc_logo_tp.png' | relative_url }}" 
         class="no-zoom tc-base-logo" 
         style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1;" 
         alt="Logo">
    
    <img src="{{ '/assets/img/Racetrack2.png' | relative_url }}" 
         id="racetrack"
         class="no-zoom tc-rotating-overlay" 
         style="position: absolute; top: 0; left: 0; z-index: 2; object-fit: contain;" 
         alt="Racetrack">
  </div>
</div>

<br>Follow along and witness a transformation as this base model 1967 Chevrolet Camaro receives custom fabrication and modern styling all backed by a turbocharged alcohol injected highly modified 250 cubic inch inline 6 engine. No big sponsors or corporate bill folds, every upgrade is completed by a regular guy on a family conscious budget. Since 2007, this has been a work in progress, but 20+ years later, things are just getting interesting.

<div id="video-wrapper" style="max-width: 540px; margin: 2rem auto;" markdown="0">
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" src="https://www.youtube.com/embed/b_vNRvV7slQ" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

Want to know the history of Turbo Camaro? Read [About the Build]({{ '/about/' | relative_url }}).

<script>
  (function() {
    const track = document.getElementById('racetrack');
    let currentRotation = 0;

    // Function to keep the "Idle" rotation going
    function idleSpin() {
      if (!track.classList.contains('is-launching')) {
        currentRotation -= 360; // Keep spinning counter-clockwise
        track.style.transform = `rotate(${currentRotation}deg)`;
      }
    }

    // Start the idle spin immediately
    let idleInterval = setInterval(idleSpin, 8000);
    idleSpin(); // Run once at start

    window.addEventListener('click', function(event) {
      const container = event.target.closest('#launch-container');
      
      if (container && !track.classList.contains('is-launching')) {
        // 1. Stop the idle timer
        clearInterval(idleInterval);
        
        // 2. Add the fast transition class
        track.classList.add('is-launching');
        
        // 3. Add 3 full rotations (1080 degrees) to current position
        currentRotation -= 1080; 
        track.style.transform = `rotate(${currentRotation}deg)`;

        // 4. After the "Launch" (0.6s), go back to idle
        setTimeout(() => {
          track.classList.remove('is-launching');
          // Restart the idle loop from the new position
          idleInterval = setInterval(idleSpin, 8000);
        }, 600); // Matches the 0.6s CSS transition
      }
    });
  })();
</script>