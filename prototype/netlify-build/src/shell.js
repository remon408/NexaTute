/* Shell for phone and fixed-size boards: the board runs in an iframe of its canvas size.
   Phones narrower than the board are scaled down to fit the screen width. */
(function () {
  'use strict';
  var frame = document.querySelector('.dcx-frame');
  if (!frame) return;
  var phone = document.documentElement.classList.contains('dcx-phone');
  var w = parseFloat(frame.getAttribute('data-w')), h = parseFloat(frame.getAttribute('data-h'));
  var holder = frame.parentNode;
  function fit() {
    var vw = document.documentElement.clientWidth || window.innerWidth;
    if (phone && vw < w) {
      var s = vw / w;
      frame.style.transform = 'scale(' + s + ')';
      frame.style.transformOrigin = '0 0';
      frame.style.margin = '0';
      holder.style.height = Math.ceil(h * s) + 'px';
      holder.style.width = vw + 'px';
    } else {
      frame.style.transform = ''; frame.style.transformOrigin = ''; frame.style.margin = '';
      holder.style.height = ''; holder.style.width = '';
    }
  }
  fit();
  window.addEventListener('resize', fit);
})();
