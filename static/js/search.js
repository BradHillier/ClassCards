document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.querySelector('#search-form');
  searchForm.addEventListener('submit', function(event) {
    event.preventDefault(); // prevent the form from submitting normally

    // Get the search query from the input field
    const searchInput = document.querySelector('input[name="search"]');
    const decks = searchInput.value;

    const deckContainer = document.querySelector("#deck-container")

    fetch(`/api/decks?search=${decks}`)
      .then(response => response.json())
      .then(data => {
         const deckCards = data.map((deck) => {
            return `
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">${deck.name}</h5>
                </div>
              </div>
            `;
         })
         deckContainer.innerHTML = deckCards.join("");
      })
   });
})
