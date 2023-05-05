function checkOnlyOne(el) {
  const checkboxes = document.getElementsByName('exchange');

  checkboxes.forEach((box) => {
    box.checked = false;
  });

  el.checked = true;
}

function is_checked() {
  const is_checked = document.querySelector('#id_all_check').checked;

  document.querySelector('#id_use_check').checked = is_checked;
  document.querySelector('#id_pi_check').checked = is_checked;
}
