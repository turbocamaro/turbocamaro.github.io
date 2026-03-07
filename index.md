---
layout: page
permalink: /
hide_title: true
---
<STYLE>
/* --- Landing Page Logo Kill --- */
/* This hides the topbar logo ONLY on the home page */
#topbar-title {
    display: none !important;
    opacity: 0 !important;
}
</STYLE>

<div id="launch-container" class="d-flex justify-content-center w-100" style="position: relative; height: 320px; cursor: pointer; z-index: 999;" markdown="0">
  <div style="position: relative; width: 320px; height: 320px;">
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
    const handler = function(e) {
      const container = document.getElementById('launch-container');
      const track = document.getElementById('racetrack');
      
      if (container && (e.target === container || container.contains(e.target))) {
        if (track && !track.classList.contains('is-launching')) {
          // 1. Hammer the gas (Accelerates over 0.3s due to SCSS transition)
          track.classList.add('is-launching');
          
          // 2. Keep the pedal down for 1.2 seconds
          setTimeout(() => {
            // 3. Let off the gas (Decelerates smoothly back to 8s over 0.8s)
            track.classList.remove('is-launching');
          }, 1200);
        }
      }
    };

    window.addEventListener('mousedown', handler);
    window.addEventListener('touchstart', handler);
  })();
</script>