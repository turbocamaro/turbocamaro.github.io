---
layout: page
permalink: /
hide_title: true
---

<style>
  #topbar-title { display: none !important; }
  .tc-container { position: relative; width: 320px; height: 320px; margin: 0 auto; cursor: pointer !important; z-index: 1000; }
  .tc-base-logo-bg { position: absolute; top: 50%; left: 50%; width: 205px; height: 205px; transform: translate(-50%, -50%); background: url("{{ '/assets/img/tc_logo_tp.png' | relative_url }}") no-repeat center; background-size: contain; z-index: 1; pointer-events: none; }
  .tc-racetrack-bg { position: absolute; top: 0; left: 0; width: 320px; height: 320px; background: url("{{ '/assets/img/Racetrack2.png' | relative_url }}") no-repeat center; background-size: contain; z-index: 2; pointer-events: none; will-change: transform, filter; }
</style>

<audio id="turbo-audio" src="{{ '/assets/wav/logospool.wav' | relative_url }}" preload="auto"></audio>

<div id="launch-wrapper" class="d-flex justify-content-center w-100" style="margin-top: -30px;" markdown="0">
  <div class="tc-container" id="launch-container">
    <div class="tc-base-logo-bg"></div>
    <div id="racetrack" class="tc-racetrack-bg"></div>
  </div>
</div>

<br>

Follow along and witness a transformation as this base model 1967 Chevrolet Camaro receives custom fabrication and modern styling...



<script type="text/javascript">
(function() {
  // CONFIG
  var IDLE = 0.75;    
  var PEAK = 20.0;    
  var DURATION = 5300; 
  var ACCEL_S = 0.0035; 
  var BRAKE_S = 0.05;  
  var BLUR_M = 0.15; 

  // STATE
  var rot = 0;
  var speed = IDLE; 
  var target = IDLE;
  var launching = false;

  function animate() {
    var track = document.getElementById('racetrack');
    var lerp = launching ? ACCEL_S : BRAKE_S; 
    
    speed += (target - speed) * lerp;
    rot -= speed;

    if (track) { 
      track.style.transform = "rotate(" + rot + "deg)"; 
      var b = Math.max(0, (speed - IDLE) * BLUR_M);
      track.style.filter = "blur(" + b + "px)";
    }
    requestAnimationFrame(animate);
  }

  function run() {
    var audio = document.getElementById('turbo-audio');
    if (!launching) {
      launching = true;
      target = PEAK;
      if (audio) {
        audio.currentTime = 0;
        audio.volume = 1.0;
        audio.play().catch(function(e){ console.log("Audio play blocked"); });
        setTimeout(function() {
          launching = false;
          target = IDLE; 
          var f = setInterval(function() {
            if (audio.volume > 0.1) audio.volume -= 0.1;
            else { audio.pause(); clearInterval(f); }
          }, 100);
        }, DURATION); 
      }
    }
  }

  // Persistent Linker
  setInterval(function() {
    var c = document.getElementById('launch-container');
    if (c && !c.dataset.hooked) {
      c.dataset.hooked = "true";
      c.onclick = run;
      c.ontouchstart = run;
    }
  }, 500);

  requestAnimationFrame(animate);
})();
</script>