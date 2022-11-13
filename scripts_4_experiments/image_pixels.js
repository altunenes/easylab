document.addEventListener("DOMContentLoaded", function() {
    var importImageButton = document.createElement('button');
    importImageButton.innerHTML = 'Import Image';
    importImageButton.onclick = function() {
      var fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.onchange = function() {
        var file = fileInput.files[0];
        var reader = new FileReader();
        reader.onload = function(e) {
          var image = document.createElement('img');
          image.src = e.target.result;
          document.body.appendChild(image);
        };
        reader.readAsDataURL(file);
      };
      fileInput.click();
    };
    document.body.appendChild(importImageButton);
    
    var getRGBButton = document.createElement('button');
    getRGBButton.innerHTML = 'Get RGB';
    getRGBButton.onclick = function() {
      var image = document.querySelector('img');
      var canvas = document.createElement('canvas');
      canvas.width = image.width;
      canvas.height = image.height;
      var context = canvas.getContext('2d');
      context.drawImage(image, 0, 0);
      var imageData = context.getImageData(0, 0, image.width, image.height);
      var data = imageData.data;
      var zoom = 20;
      var canvas2 = document.createElement('canvas');
      canvas2.width = image.width * zoom;
      canvas2.height = image.height * zoom;
      var context2 = canvas2.getContext('2d');
      context2.fillStyle = 'white';
      context2.fillRect(0, 0, canvas2.width, canvas2.height);
      for (var i = 0; i < data.length; i += 4) {
        var x = (i / 4) % image.width;
        var y = Math.floor((i / 4) / image.width);
        var r = data[i];
        var g = data[i + 1];
        var b = data[i + 2];
        var a = data[i + 3];
        context2.fillStyle = 'rgb(' + r + ',' + g + ',' + b + ')';
        context2.fillRect(x * zoom, y * zoom, zoom, zoom);
        context2.fillStyle = 'black';
        context2.font = '10px sans-serif';
        context2.fillText(r + ',' + g + ',' + b, x * zoom, y * zoom + zoom);
      }
      document.body.appendChild(canvas2);
    };
    document.body.appendChild(getRGBButton);
    });
    
