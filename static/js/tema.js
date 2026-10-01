// Tema claro/oscuro. Guarda la preferencia en el navegador (localStorage).
(function () {
  var raiz = document.documentElement;

  function leer() {
    try { return localStorage.getItem("tema"); } catch (e) { return null; }
  }
  function guardar(valor) {
    try { localStorage.setItem("tema", valor); } catch (e) { /* sin almacenamiento: no pasa nada */ }
  }
  function esOscuro() {
    var t = raiz.getAttribute("data-theme");
    if (t) return t === "dark";
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  function pintarBoton(boton) {
    var oscuro = esOscuro();
    boton.textContent = oscuro ? "Tema claro" : "Tema oscuro";
    boton.setAttribute("aria-pressed", oscuro ? "true" : "false");
  }

  // Se aplica de inmediato (antes de pintar) para evitar un parpadeo.
  var guardado = leer();
  if (guardado === "dark" || guardado === "light") raiz.setAttribute("data-theme", guardado);

  document.addEventListener("DOMContentLoaded", function () {
    var boton = document.getElementById("boton-tema");
    if (!boton) return;
    pintarBoton(boton);
    boton.addEventListener("click", function () {
      var nuevo = esOscuro() ? "light" : "dark";
      raiz.setAttribute("data-theme", nuevo);
      guardar(nuevo);
      pintarBoton(boton);
    });
  });
})();