(function ($) {

    "use strict";

        function initParallax() {
          $('#home').parallax("100%", 0.3);
          $('#about').parallax("20%", 0.3);
          $('#footer').parallax("80%", 0.3);
          }
        initParallax(); 


        new WOW({ mobile: false }).init();

})(jQuery);
