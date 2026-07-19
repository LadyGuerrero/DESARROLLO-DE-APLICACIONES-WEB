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

// DATOS INICIALES - preparado para Flask
const herramientas = [
  { nombre: 'ChatGPT', descripcion: 'Asistente de escritura e investigación', categoria: 'Asistente Virtual' },
  { nombre: 'Consensus', descripcion: 'Búsqueda de papers científicos', categoria: 'Investigación' },
  { nombre: 'Canva IA', descripcion: 'Diseño con inteligencia artificial', categoria: 'Diseño' }
];

function renderizarHerramientas() {
  const lista = document.getElementById('listaRegistros');
  const total = document.getElementById('total');
  lista.innerHTML = '';
  if (herramientas.length === 0) {
    lista.innerHTML = '<div class="alert alert-warning">No hay herramientas registradas.</div>';
    total.textContent = 0;
    return;
  }
  herramientas.forEach((h, i) => {
    const card = document.createElement('div');
    card.className = 'card mb-2';
    card.innerHTML = `<div class="card-body">
      <strong>${h.nombre}</strong> — ${h.descripcion}
      <span class="badge bg-primary ms-1">${h.categoria}</span>
      <button class="btn btn-danger btn-sm float-end" data-index="${i}">Eliminar</button>
    </div>`;
    card.querySelector('button').addEventListener('click', () => {
      herramientas.splice(i, 1);
      renderizarHerramientas();
    });
    lista.appendChild(card);
  });
  total.textContent = herramientas.length;
}

// REGISTRO
document.getElementById('nombre').addEventListener('blur', () => validar('nombre','errorNombre',3,'Mínimo 3 caracteres.'));
document.getElementById('categoria').addEventListener('change', () => validar('categoria','errorCategoria',1,'Selecciona una categoría.'));

document.getElementById('formRegistro').addEventListener('submit', function(e) {
  e.preventDefault();
  if (!validar('nombre','errorNombre',3,'Mínimo 3 caracteres.') |
      !validar('descripcion','errorDescripcion',4,'Mínimo 4 caracteres.') |
      !validar('categoria','errorCategoria',1,'Selecciona una categoría.')) return;
  herramientas.push({
    nombre: document.getElementById('nombre').value.trim(),
    descripcion: document.getElementById('descripcion').value.trim(),
    categoria: document.getElementById('categoria').value
  });
  const spinner = document.getElementById('spinner');
  spinner.classList.remove('d-none');
  setTimeout(() => {
    spinner.classList.add('d-none');
    renderizarHerramientas();
    document.getElementById('mensaje').innerHTML = '<div class="alert alert-success">✅ Herramienta registrada.</div>';
  }, 1000);
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

renderizarHerramientas();