function visualiza_login() {
  document.getElementById('login').style.visibility = 'visible';
  document.getElementById('login').style.display = 'block';
  document.getElementById('registro').style.visibility = 'hidden';
  document.getElementById('registro').style.display = 'none';
};
function visualiza_registro() {
  document.getElementById('registro').style.visibility = 'visible';
  document.getElementById('registro').style.display = 'block';
  document.getElementById('login').style.visibility = 'hidden';
  document.getElementById('login').style.display = 'none';
};
var check = function() {
  if (document.getElementById('password').value == document
      .getElementById('confirm_password').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
  }
}
function __(id) {
  return document.getElementById(id);
}
//Validar contraseña
function validarContrasena() {
  var pass = __('contrasena').value, pass2 = __('contrasena2').value;
  if (pass != '' && pass2 != '') {
    if (pass != pass2) {
      //si las contraseÃ±as no coinciden
      __('resultado').innerHTML = '<p class="error"><strong>Error: </strong>¡Las contraseñas no coinciden!</p>';
    } else {
      //Si todo esta correcto 
      document.getElementById("registro").submit();
    }
  } else {
    //si los campos o uno, este vacio
    __('resultado').innerHTML = '<p class="error"><strong>Error: </strong>¡Los campos no deben estar vacios!</p>';
  }
}
//enviar formulario con la tecla ENTER
function enterEnviar(event) {
  if (event.keyCode == 13) {
    validarContrasena()
  }
}