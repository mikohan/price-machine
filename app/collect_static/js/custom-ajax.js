/* globals Chart:false, feather:false */

(() => {
  //   'use strict';

  //   feather.replace({ 'aria-hidden': 'true' });
  console.log(MAIN_HOST_URL);

  $('.get-price-ajax').on('click', function (e) {
    var id = e.target.id;
    $.ajax({
      url: `${MAIN_HOST_URL}/supplier/${id}/`,
      // url: `${MAIN_HOST_URL}/ajax-update-supplier/`,
      datatype: 'json',
      type: 'GET',
      beforeSend: function () {
        $('#spinner-' + id).show();
        $('#' + id).hide();
        // $('#' + id).show();
      },
      success: function (data) {
        $('#spinner-' + id).hide();
        $('#' + id).show();
        console.log(data);

        // location.reload();
      },
    });
  });

  $('#load-all').on('click', function (e) {
    $.ajax({
      // url: `${MAIN_HOST_URL}/supplier/${id}/`,
      url: `${MAIN_HOST_URL}/ajax-update-suppliers/`,
      datatype: 'json',
      type: 'GET',
      beforeSend: function () {
        $('#spinner-all').show();
        $('#button-text').hide();
      },
      success: function (data) {
        $('#spinner-all').hide();
        $('#button-text').show();
        var str = '';
        data.foo.forEach((item) => {
          var entry = Object.entries(item);
          if (entry[0][1]) {
            str += `<li><span class="text-success">${entry[0][0]}</span> : <span class="text-success">${entry[0][1]}</span></li>`;
          } else {
            str += `<li><span class="text-danger">${entry[0][0]}</span> : <span class="text-danger">${entry[0][1]}</span></li>`;
          }
        });
        console.log(data);
        $('#update-time').html(
          `<span class="text-success">Время обновления: ${data.time} секунд.</span>`
        );
        $('#left-ul').html(str);
        // location.reload();
      },
    });
  });
})();
