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

// Ranking view
setInterval(() => {
  FadeOut();
  listMove();
  FadeIn();
}, 8000);

const rankingList = document.querySelector('.rank-list');

function listMove() {
  setTimeout(() => {
    if (rankingList.classList.contains('list-move')) {
      rankingList.classList.remove('list-move');
    } else {
      rankingList.classList.add('list-move');
    }
  }, 800);
}

function FadeOut() {
  setTimeout(() => {
    rankingList.style.opacity = '0';
  }, 100);
}

function FadeIn() {
  setTimeout(() => {
    rankingList.style.opacity = '1';
  }, 1200);
}
