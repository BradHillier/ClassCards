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
           <div class="deck" data-deck-id="${deck.id}">
             <div class="deck-body">
               <h5 class="deck-title"><a href="#">${deck.name}</a></h5>
             </div>
           </div>
         `
            })
            deckContainer.innerHTML = deckCards.join("");


            const decks = document.querySelectorAll(".deck");
            decks.forEach((deck) => {
               deck.addEventListener("click", () => {
                  const deckId = deck.dataset.deckId;
                  fetch(`/api/decks/${deckId}/cards`)
                     .then((response) => response.json())
                     .then((cards) => {
                        const cardItems = cards.map((card) => {
                           return `
                <div class="card" onclick="this.classList.toggle('back')">
                  <div class="card-inner">
                    <div class="card-front">
                      <div class="card-body">
                        <h5 class="card-title">${card.front}</h5>
                      </div>
                    </div>
                    <div class="card-back">
                      <div class="card-body">
                        <p class="card-text">${card.back}</p>
                      </div>
                    </div>
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
   });
})
