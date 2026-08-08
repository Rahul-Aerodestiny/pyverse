(function(){
  function insertFooter(html) {
    var container = document.getElementById('site-footer');
    if (container) {
      container.innerHTML = html;
    }
  }

  fetch('includes/footer.html')
    .then(function(res) {
      if (!res.ok) throw new Error('Footer fetch failed');
      return res.text();
    })
    .then(insertFooter)
    .catch(function(err) {
      console.error('Could not load footer:', err);
    });
})();
