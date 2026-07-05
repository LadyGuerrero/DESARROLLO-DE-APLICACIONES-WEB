function validar(id, errorId, minLen, msg) {
  const campo = document.getElementById(id);
  const val = campo.value.trim();
  const ok = val.length >= minLen;
  campo.classList.toggle('is-valid', ok);
  campo.classList.toggle('is-invalid', !ok);
  document.getElementById(errorId).textContent = ok ? '' : msg;
  return ok;
}

function validarEmail(id, errorId) {
  const campo = document.getElementById(id);
  const ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(campo.value.trim());
  campo.classList.toggle('is-valid', ok);
  campo.classList.toggle('is-invalid', !ok);
  document.getElementById(errorId).textContent = ok ? '' : 'Correo inválido.';
  return ok;
}

// REGISTRO
document.getElementById('nombre').addEventListener('blur', () => validar('nombre','errorNombre',3,'Mínimo 3 caracteres.'));
document.getElementById('descripcion').addEventListener('blur', () => validar('descripcion','errorDescripcion',10,'Mínimo 10 caracteres.'));
document.getElementById('categoria').addEventListener('change', () => validar('categoria','errorCategoria',1,'Selecciona una categoría.'));

document.getElementById('formRegistro').addEventListener('submit', function(e) {
  e.preventDefault();
  if (!validar('nombre','errorNombre',3,'Mínimo 3 caracteres.') |
      !validar('descripcion','errorDescripcion',4,'Mínimo 4 caracteres.') |
      !validar('categoria','errorCategoria',1,'Selecciona una categoría.')) return;

  const nombre = document.getElementById('nombre').value.trim();
  const descripcion = document.getElementById('descripcion').value.trim();
  const categoria = document.getElementById('categoria').value;
  const card = document.createElement('div');
  card.className = 'card mb-2';
  card.innerHTML = `<div class="card-body">
    <strong>${nombre}</strong> — ${descripcion}
    <span class="badge bg-primary ms-1">${categoria}</span>
    <button class="btn btn-danger btn-sm float-end">Eliminar</button>
  </div>`;
  card.querySelector('button').addEventListener('click', () => {
    card.remove();
    document.getElementById('total').textContent--;
  });
  document.getElementById('listaRegistros').appendChild(card);
  document.getElementById('total').textContent++;
  document.getElementById('mensaje').innerHTML = '<div class="alert alert-success">✅ Herramienta registrada.</div>';
  this.reset();
});

// CONTACTO
document.getElementById('cNombre').addEventListener('blur', () => validar('cNombre','eCNombre',3,'Mínimo 3 caracteres.'));
document.getElementById('cCorreo').addEventListener('blur', () => validarEmail('cCorreo','eCCorreo'));
document.getElementById('cAsunto').addEventListener('blur', () => validar('cAsunto','eCAsunto',3,'Mínimo 3 caracteres.'));
document.getElementById('cMensaje').addEventListener('blur', () => validar('cMensaje','eCMensaje',10,'Mínimo 10 caracteres.'));

document.getElementById('formContacto').addEventListener('submit', function(e) {
  e.preventDefault();
  if (!validar('cNombre','eCNombre',3,'Mínimo 3 caracteres.') |
      !validarEmail('cCorreo','eCCorreo') |
      !validar('cAsunto','eCAsunto',3,'Mínimo 3 caracteres.') |
      !validar('cMensaje','eCMensaje',10,'Mínimo 10 caracteres.')) return;
  document.getElementById('msgContacto').innerHTML = '<div class="alert alert-success">✅ Mensaje enviado correctamente.</div>';
  this.reset();
});