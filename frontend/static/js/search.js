const searchForm = document.querySelector('#search-form');
searchForm.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent the form from submitting normally

  // Get the search query from the input field
  const searchInput = document.querySelector('input[name="search"]');
  const decks = searchInput.value;

  // Send an AJAX request to the server
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `/api/search?decks=${decks}`);
  xhr.onload = function() {
    // handle the response from the server
    console.log(decks);
  };
  xhr.send();
});

