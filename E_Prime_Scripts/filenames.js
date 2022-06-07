var browseFolder = document.createElement('input');
browseFolder.type = 'file';
browseFolder.webkitdirectory = true;
browseFolder.multiple = true;
browseFolder.id = 'browseFolder';
browseFolder.addEventListener('change', function(e) {
  var files = e.target.files;
  for (var i = 0, f; f = files[i]; i++) {
    console.log(f.webkitRelativePath);
  }
});
document.body.appendChild(browseFolder);


var fileNames = document.createElement('button');
fileNames.innerHTML = 'Export File Names';
fileNames.addEventListener('click', function(e) {
  var files = document.getElementById('browseFolder').files;
  var csv = '';
  for (var i = 0, f; f = files[i]; i++) {
    csv += f.name + '\n';
  }
  var blob = new Blob([csv], {type: 'text/csv'});
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  a.download = 'export.csv';
  a.click();
});
document.body.appendChild(fileNames);

var rect = document.createElement('div');
rect.style.backgroundColor = '#00f';
rect.style.width = '130px';
rect.style.height = '130px';
rect.style.position = 'absolute';
rect.style.left = '57%';
rect.style.top = '50%';
document.body.appendChild(rect);
var spin = document.createElement('div');
spin.style.position = 'absolute';
spin.style.left = '57%';
spin.style.top = '50%';
spin.style.width = '120px';
spin.style.height = '120px';
spin.style.backgroundColor = '#00f';
spin.style.backgroundImage = 'linear-gradient(yellow 50%,blue 50%)';
spin.style.transform = 'rotate(0deg)';
spin.style.transition = 'transform 1s linear';
document.body.appendChild(spin);
function spinAround() {
  spin.style.transform = 'rotate(' + (parseInt(spin.style.transform.match(/\d+/)) + 10) + 'deg)';
}
setInterval(spinAround, 15);
var spinningAround = document.createElement('div');
spinningAround.innerHTML = 'spinning around';
spinningAround.style.position = 'absolute';
spinningAround.style.left = '52%';
spinningAround.style.top = '50%';
spinningAround.style.color = '#f00';
document.body.appendChild(spinningAround);
spinningAround.style.fontSize = '30px';
spinningAround.style.fontFamily = 'Arial';
spinningAround.style.fontWeight = 'bold';
spinningAround.style.textAlign = 'center';
spinningAround.style.lineHeight = '120px';


var jitter = document.createElement('div');
jitter.innerHTML = '<input type="number" id="jitterMin" value="0" min="0" max="100" step="1">' +
  '<input type="number" id="jitterMax" value="100" min="0" max="100" step="1">' +
  '<input type="number" id="jitterN" value="10" min="0" max="100" step="1">' +
  '<button id="jitterButton">Jitter</button>';
jitter.querySelector('#jitterButton').addEventListener('click', function(e) {
  var min = parseInt(jitter.querySelector('#jitterMin').value);
  var max = parseInt(jitter.querySelector('#jitterMax').value);
  var n = parseInt(jitter.querySelector('#jitterN').value);
  var csv = '';
  for (var i = 0; i < n; i++) {
    csv += Math.floor(Math.random() * (max - min + 1)) + min + '\n';
  }
  var blob = new Blob([csv], {type: 'text/csv'});
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  a.download = 'export.csv';
  a.click();
});
document.body.appendChild(jitter);
