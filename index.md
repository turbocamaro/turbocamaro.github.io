---
layout: page
permalink: /
hide_title: true
---

<style>
  #topbar-title { display: none !important; }

  /* The Container is the ONLY thing that should be clickable */
  .tc-container {
    position: relative;
    width: 320px;
    height: 320px;
    margin: 0 auto;
    cursor: pointer !important;
    z-index: 1000;
  }

  .tc-base-logo-bg {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 205px;
    height: 205px;
    transform: translate(-50%, -50%);
    background: url("{{ '/assets/img/tc_logo_tp.png' | relative_url }}") no-repeat center;
    background-size: contain;
    z-index: 1;
    pointer-events: none; /* Let the click pass through to the container */
  }

  .tc-racetrack-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 320px;
    height: 320px;
    background: url("{{ '/assets/img/Racetrack2.png' | relative_url }}") no-repeat center;
    background-size: contain;
    z-index: 2;
    pointer-events: none; /* Let the click pass through to the container */
    
    /* NEW ANIMATION NAME to bypass any cached SCSS */
    animation: tc-turbo-spin 8s infinite linear;
    transition: animation-duration 1.5s ease-out;
  }

  .is-launching {
    animation-duration: 4s !important;
    transition: animation-duration 5.0s ease-in !important;
  }

  @keyframes tc-turbo-spin {
    from { transform: rotate(360deg); }
    to { transform: rotate(0deg); }
  }
</style>

<audio id="turbo-audio" src="{{ '/assets/wav/logospool.wav' | relative_url }}" preload="auto"></audio>

<div id="launch-wrapper" class="d-flex justify-content-center w-100" style="margin-top: -30px;" markdown="0">
  <div class="tc-container" id="launch-container">
    <div class="tc-base-logo-bg"></div>
    <div class="tc-racetrack-bg" id="racetrack"></div>
  </div>
</div>

<br>

Follow along and witness a transformation as this base model 1967 Chevrolet Camaro receives custom fabrication and modern styling all backed by a turbocharged alcohol injected highly modified 250 cubic inch inline 6 engine. No big sponsors or corporate bill folds, every upgrade is completed by a regular guy on a family conscious budget. Since 2007, this has been a work in progress, but 20+ years later, things are just getting interesting.

<div id="video-wrapper" style="max-width: 540px; margin: 2rem auto;" markdown="0">
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" src="https://www.youtube.com/embed/b_vNRvV7slQ" title="YouTube video player" allowfullscreen></iframe>
  </div>
</div>

Want to know the history of Turbo Camaro? Read [About the Build]({{ '/about/' | relative_url }}).

<script type="text/javascript">
  (function() {
    // The "Engine" for the click event
    const runTurbo = () => {
      const track = document.getElementById('racetrack');
      const audio = document.getElementById('turbo-audio');
      
      if (track && !track.classList.contains('is-launching')) {
        track.classList.add('is-launching');
        
        if (audio) {
          audio.currentTime = 0;
          audio.volume = 1.0;
          audio.play().catch(e => console.warn("Audio blocked. Interact with page first."));
        }

        // 6.5s Duration (5s spool + 1.5s hold)
        setTimeout(() => {
          track.classList.remove('is-launching');
          if (audio) {
            let fadeOut = setInterval(() => {
              if (audio.volume > 0.1) {
                audio.volume -= 0.1;
              } else {
                audio.pause();
                clearInterval(fadeOut);
              }
            }, 150);
          }
        }, 6500);
      }
    };

    // Attachment Logic
    const init = () => {
      const container = document.getElementById('launch-container');
      if (container && !container.dataset.hooked) {
        container.dataset.hooked = "true";
        // Directly assigning the function to ensure it's not blocked by other listeners
        container.onclick = runTurbo;
      }
    };

    setInterval(init, 500);
  })();
</script>