<!-- REGISTRO DINÁMICO -->
      <section id="registro" class="p-3 mb-4 bg-white rounded">
        <h2>Registrar Herramienta de IA</h2>
        <div id="mensaje" class="mb-2"></div>
        <p>Total de registros: <strong id="total">0</strong></p>
        <form id="formRegistro">
          <input type="text" id="nombre" class="form-control mb-2" placeholder="Nombre de la herramienta">
          <input type="text" id="descripcion" class="form-control mb-2" placeholder="Descripción">
          <input type="text" id="categoria" class="form-control mb-2" placeholder="Categoría">
          <button type="submit" class="btn btn-primary">Registrar</button>
        </form>
        <div id="listaRegistros" class="mt-3"></div>
      </section>