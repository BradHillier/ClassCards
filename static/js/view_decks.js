// view_decks.js

const deckContainer = document.querySelector("#deck-container");

fetch("/api/decks")
  .then((response) => response.json())
  .then((data) => {
    const deckCards = data.map((deck) => {
      return `
        <div class="deck" data-deck-id="${deck.id}">
          <div class="deck-body">
            <h5 class="deck-title"><a href="#">${deck.name}</a></h5>
          </div>
        </div>
      `;
    });

    deckContainer.innerHTML = deckCards.join("");

    // add event listeners to the deck elements
    const decks = document.querySelectorAll(".deck");
    decks.forEach((deck) => {
      deck.addEventListener("click", () => {
        const deckId = deck.dataset.deckId;
        fetch(`/api/decks/${deckId}/cards`)
          .then((response) => response.json())
          .then((cards) => {
            const cardItems = cards.map((card) => {
              return `
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">${card.front}</h5>
                    <p class="card-text">${card.back}</p>
                  </div>
                </div>
              `;
            });
            deckContainer.innerHTML = cardItems.join("");
          })
          .catch((error) => {
            console.error(error);
          });
      });
    });
  })
  .catch((error) => {
    console.error(error);
  });

