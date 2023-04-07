// view_decks.js

const deckContainer = document.querySelector("#deck-container");

fetch("/api/decks")
  .then((response) => response.json())
  .then((data) => {
    const deckCards = data.decks.map((deck) => {
      return `
        <div class="deck">
          <div class="deck-body">
            <h5 class="deck-title"><a href="/api/decks/${deck.id}/cards">${deck.title}</a></h5>
          </div>
        </div>
      `;
    });

    deckContainer.innerHTML = deckCards.join("");
  });
