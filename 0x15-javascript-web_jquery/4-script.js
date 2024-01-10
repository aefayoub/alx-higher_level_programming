const $ = window.$;
$('DIV#red_header').click(function () {
  if ($('HEADER').hasClass('red') {
    $('HEADER')removeClass('red').addClass('green');
  }
  else if ($('HEADER').hasClass('green') {
    $('HEADER')removeClass('green').addClass('red');
  }
  $('HEADER').addClass('red');
});
