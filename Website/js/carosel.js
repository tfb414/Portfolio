(function($){
    'use strict';
    $('.carousel .touch-control').each(function(){
      var $this = $(this);
      var $item = $this.closest('.item');
      var $carousel = $this.closest('.carousel');
      var $link = $item.find('a');
      var mc = new Hammer(this);
      mc.on("panleft panright tap", function(ev) {
          switch( ev.type ){
            case 'panleft':
              $carousel.carousel('next');
              break;
            case 'panright':
              $carousel.carousel('prev');
              break;
            case 'tap':
              alert( $link.attr('href') );
              break;
          }
      });
    });
  })(jQuery);