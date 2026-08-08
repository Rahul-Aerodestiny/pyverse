// Fetch and inject header, then set active nav link
(function(){
  function setActive() {
    var filename = window.location.pathname.split('/').pop();
    if (!filename) filename = 'index.html';
    var links = document.querySelectorAll('#site-header .navbar-nav .nav-link');
    links.forEach(function(a){
      if (a.getAttribute('href') === filename) {
        a.classList.add('active');
      } else {
        a.classList.remove('active');
      }
    });
  }
  fetch('includes/header.html')
    .then(function(res){ if(!res.ok) throw new Error('Header fetch failed'); return res.text(); })
    .then(function(html){
      var container = document.getElementById('site-header');
      if(container){
        container.innerHTML = html;
        setActive();
      }
    })
    .catch(function(err){
      console.error('Could not load header:', err);
    });
})();
