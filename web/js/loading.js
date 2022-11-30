/** Add a spin. */
function add_spin() {
  const content = document.querySelector(".content_loading");
  content.innerHTML = '<div class="Loading"></div>';
}

/** Add the correct identifier. */
function add_check() {
  const content = document.querySelector(".content_loading");
  content.innerHTML = '<h3 class="text_status_loading" >Correcto</h3>';
}

/** Add the error message. */
function add_erro() {
  const content = document.querySelector(".content_loading");
  content.innerHTML = '<h3 class="text_status_loading" >Error</h3>';
}

/** Clean item. */
function clean_content() {
  const content = document.querySelector(".content_loading");
  content.innerHTML = "";
}
