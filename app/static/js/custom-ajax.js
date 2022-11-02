/* globals Chart:false, feather:false */

(() => {
  //   'use strict';

  //   feather.replace({ 'aria-hidden': 'true' });
  console.log('Working');

  $('.get-price-ajax').on('click', function (e) {
    var id = e.target.id;
    $.ajax({
      url: `http://localhost:8000/supplier/${id}/`,
      // url: `http://0.0.0.0:8000/ajax-update-supplier/`,
      datatype: 'json',
      type: 'GET',
      beforeSend: function () {
        console.log('Beforesend', id);
        $('#spinner-' + id).show();
        $('#' + id).hide();
        // $('#' + id).show();
      },
      success: function (data) {
        $('#spinner-' + id).hide();
        $('#' + id).show();
        console.log(data);
      },
    });
  });
})();
