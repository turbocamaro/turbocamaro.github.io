---
layout: page
permalink: /
hide_title: true
---

<style>
  /* 1. Hide the topbar logo on this page */
  #topbar-title { display: none !important; }

  /* 2. Interactive Logo Styling */
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
    pointer-events: none; 
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
    pointer-events: none; 
    /* will-change ensures the browser optimizes for both rotation and blur filters */
    will-change: transform, filter; 
  }
</style>

<audio id="turbo-audio" src="{{ '/assets/wav/logospool.wav' | relative_url }}" preload="auto"></audio>

<div id="launch-wrapper" class="d-flex justify-content-center w-100" style="margin-top: -30px;" markdown="0">
  <div class="tc-container" id="launch-container">
    <div class="tc-base-logo-bg"></div>
    <div id="racetrack" class="tc-racetrack-bg"></div>
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
    /* --- TUNER SETTINGS --- */
    const IDLE_SPEED = 0.75;    // Degrees per frame (Cruise)
    const PEAK_SPEED = 20.0;    // Degrees per frame (Top End)
    const ACCEL_DURATION = 5300; // Your exact 5.3s timing
    
    // Physics Tuning: Lower = heavier feel
    const ACCEL_SMOOTHNESS = 0.0035; 
    const BRAKE_SMOOTHNESS = 0.05;  

    // Blur Intensity: Controls the "streakiness" at top speed
    const BLUR_MULTIPLIER = 0.15; 
    /* ---------------------- */

    let rotation = 0;
    let currentSpeed = IDLE_SPEED; 
    let targetSpeed = IDLE_SPEED;
    let isLaunching = false;

    // The Animation Loop
    const animate = () => {
      const track = document.getElementById('racetrack');
      const lerpFactor = isLaunching ? ACCEL_SMOOTHNESS : BRAKE_SMOOTHNESS; 
      
      currentSpeed += (targetSpeed - currentSpeed) * lerpFactor;
      rotation -= currentSpeed;

      if (track) { 
        // 1. Update Rotation
        track.style.transform = `rotate(${rotation}deg)`; 
        
        // 2. Update Blur (Calculates how much blur to add based on speed above idle)
        const blurAmount = Math.max(0, (currentSpeed - IDLE_SPEED) * BLUR_MULTIPLIER);
        track.style.filter = `blur(${blurAmount}px)`;
      }
      requestAnimationFrame(animate);
    };

    const runTurbo = (e) => {
      if (e) e.preventDefault();
      const audio = document.getElementById('turbo-audio');
      
      if (!isLaunching) {
        isLaunching = true;
        targetSpeed = PEAK_SPEED;

        if (audio) {
          audio.currentTime = 0;
          audio.volume = 1.0;
          audio.play().catch(err => console.log("Audio waiting for user click."));
          
          setTimeout(() => {
            isLaunching = false;
            targetSpeed = IDLE_SPEED; 

            // Smooth audio fade out over 1 second
            let fadeOut = setInterval(() => {
              if (audio.volume > 0.1) {
                audio.volume -= 0.1;
              } else {
                audio.pause();
                clearInterval(fadeOut);
              }
            }, 100);
          }, ACCEL_DURATION); 
        }
      }
    };

    // Re-hook listener to handle Chirpy's page transitions
    setInterval(() => {
      const container = document.getElementById('launch-container');
      if (container && !container.dataset.hooked) {
        container.dataset.hooked = "true";
        container.onclick = runTurbo;
        container.ontouchstart = runTurbo;
      }
    }, 500);

    // Initial Kick-off
    requestAnimationFrame(animate);
  })();
</script>