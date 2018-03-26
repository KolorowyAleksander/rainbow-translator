var socket = io.connect('http://' + document.domain + ':' + location.port, {
    reconnection: true,
    reconnectionDelay: 1000,
    reconnectionDelayMax : 5000,
    reconnectionAttempts: Infinity
});

var color = ''; // global state Kappa 

socket.on('colors', function(message) {
  var template = $('#template').html();  // mustache template
  Mustache.parse(template);
  $('#c2').html(Mustache.render(template, {colors: message}));  
});

socket.on('color', function(message) {
  $('#color').css('background-color', message.rgb);
  $('#message').text(message.color);
  color = message.rgb;
  socket.emit('request', {});
});

function deleteItem(item) {
  let e = $(item.parentElement);

  socket.emit('delete', {
      rgb: e.children('.leftspan').text(),
  });
}

function deleteAll() {
  socket.emit('deleteAll', {});
}

$(document).ready(function() {
  $('#switch').click(function() {
    socket.emit('click', {});
  });

  $('#bookmark').click(function() {
    socket.emit('insert', {
      rgb: color,
      color: $('#message').text()
    });
  });

  socket.emit('select', {});  // get initial list
});
