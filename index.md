---
layout: page
permalink: /
hide_title: true
---

<style>
  /* 1. Hide the topbar logo */
  #topbar-title { display: none !important; }

  /* 2. Setup the Racetrack and Logo as CSS Backgrounds to avoid theme auto-linking */
  .tc-container {
    position: relative;
    width: 320px;
    height: 320px;
    margin: 0 auto;
    cursor: pointer;
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
    /* Use the class from your SCSS for the idle spin */
    animation: tc-spin-ccw 8s infinite linear;
    transition: animation-duration 1.2s ease-in-out;
  }

  /* Faster spin when class is added */
  .is-launching {
    animation-duration: 0.6s !important;
    transition: animation-duration 0.3s ease-in !important;
  }
</style>

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
    const init = () => {
      const container = document.getElementById('launch-container');
      const track = document.getElementById('racetrack');
      if (container && track && !container.dataset.hooked) {
        container.dataset.hooked = "true";
        
        const launch = (e) => {
          e.preventDefault();
          if (!track.classList.contains('is-launching')) {
            track.classList.add('is-launching');
            setTimeout(() => { track.classList.remove('is-launching'); }, 1500);
          }
        };

        container.addEventListener('click', launch);
        container.addEventListener('touchstart', launch, {passive: true});
      }
    };
    setInterval(init, 500);
  })();
</script>