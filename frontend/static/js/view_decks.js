// view_decks.js


const deckContainer = document.querySelector("#deck-container");

fetch("/api/decks")
  .then((response) => response.json())
  .then((data) => {
    const deckCards = data.decks.map((deck) => {
      return `
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">${deck.title}</h5>
          </div>
        </div>
      `;
    });

    deckContainer.innerHTML = deckCards.join("");
  });
