function validarContacto(id, errorId, minLen, msg) {
  const val = document.getElementById(id).value.trim();
  const campo = document.getElementById(id);
  const error = document.getElementById(errorId);
  if (!val || val.length < minLen) {
    campo.classList.add('is-invalid');
    campo.classList.remove('is-valid');
    error.textContent = msg;
    return false;
  }
  campo.classList.add('is-valid');
  campo.classList.remove('is-invalid');
  error.textContent = '';
  return true;
}

function validarCorreo(id, errorId) {
  const val = document.getElementById(id).value.trim();
  const campo = document.getElementById(id);
  const error = document.getElementById(errorId);
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(val)) {
    campo.classList.add('is-invalid');
    campo.classList.remove('is-valid');
    error.textContent = 'Correo inválido.';
    return false;
  }
  campo.classList.add('is-valid');
  campo.classList.remove('is-invalid');
  error.textContent = '';
  return true;
}

document.getElementById('cNombre').addEventListener('blur', () =>
  validarContacto('cNombre', 'eCNombre', 3, 'Mínimo 3 caracteres.'));
document.getElementById('cCorreo').addEventListener('blur', () =>
  validarCorreo('cCorreo', 'eCCorreo'));
document.getElementById('cAsunto').addEventListener('blur', () =>
  validarContacto('cAsunto', 'eCAsunto', 3, 'Mínimo 3 caracteres.'));
document.getElementById('cMensaje').addEventListener('blur', () =>
  validarContacto('cMensaje', 'eCMensaje', 10, 'Mínimo 10 caracteres.'));

document.getElementById('formContacto').addEventListener('submit', function(e) {
  e.preventDefault();
  const v1 = validarContacto('cNombre', 'eCNombre', 3, 'Mínimo 3 caracteres.');
  const v2 = validarCorreo('cCorreo', 'eCCorreo');
  const v3 = validarContacto('cAsunto', 'eCAsunto', 3, 'Mínimo 3 caracteres.');
  const v4 = validarContacto('cMensaje', 'eCMensaje', 10, 'Mínimo 10 caracteres.');
  if (!v1 || !v2 || !v3 || !v4) return;
  document.getElementById('msgContacto').innerHTML =
    '<div class="alert alert-success">✅ Formulario enviado correctamente.</div>';
  this.reset();
  ['cNombre','cCorreo','cAsunto','cMensaje'].forEach(id =>
    document.getElementById(id).classList.remove('is-valid'));
});