import { AnkiConnectDAO } from "./anki_connect.js"

const deckContainer = document.querySelector("#deck-container");
const myDAO = new AnkiConnectDAO()
const modal = document.querySelector(".modal")
let modalEventListener = null


document.addEventListener("DOMContentLoaded", async () => {

    deckContainer.innerHTML += `
        <div style="text-align: center">
            wating for permission to access Anki Connect
        </div>
        <div style="text-align: center">
            Please ensure Anki is open and the AnkiConnect addon is installed    
        </div>`

    // request permission to access anki connect
    const request = await myDAO.requestPermission()
    if (await request.permission === "granted") {
        deckContainer.innerHTML = ''
        createDeckElements()
    } else {
        deckContainer.innerHTML = `
            <div style="text-align: center">
                Permission denied, please refresh the page to try again 
            </div>`
    }


    const closeModal = () => { modal.style.display = "none" }
    // get the 'X' on the modal and set it to hide the modal
    const closeButton = document.querySelector(".close");
    closeButton.addEventListener('click', closeModal)

    // get the 'No' button on the modal and bind it to hide the modal
    const noButton = document.querySelector("#cancelButton");
    noButton.addEventListener('click', closeModal)
});


/**
 *
 */
async function createDeckElements() {
    await myDAO.getDeckNames()
        .then(names => names.map(name => {

            // create element was used to easily add the event listener
            const deck = document.createElement('div')
            deck.classList = "deck"
            deck.innerHTML = `
                     <div class="deck-body">
                         <h5 class="deck-title">${name}</h5>
                     </div>`
            deckContainer.appendChild(deck)

            // open modal confirming intent to upload when clicked
            deck.addEventListener('click', () => {
                showModal(name)
            })

        }))
}


function showModal(deckName) {

    // show the modal and update it's text
    modal.style.display = "block";
    modal.querySelector("p").innerHTML = `
        Are you sure you want to upload <b>${deckName}</b>`

    // unbind the old eventlistener if one exists
    const confirmButton = document.querySelector("#confirmButton")
    if (modalEventListener != null) {
        confirmButton.removeEventListener('click', modalEventListener)
    }
    // bind uploading the current deck to the 'Yes' button
    modalEventListener = async () => {
        const cards = await getCardData(deckName)
        const json = await uploadDeck(deckName, await cards)
        console.log(json)
    }
    confirmButton.addEventListener('click', modalEventListener)
}


async function getCardData(deckName) {

    const cards = await myDAO.getCards(deckName)

    // ensure only cards using the Basic note type are uploaded
    const cardData = await cards.filter(card => card.modelName === "Basic")
        .map(card => {
            return {
                front: card.fields.Front.value,
                back: card.fields.Back.value,
                tags: card.tags
            }
        })
    return await cardData
}


async function uploadDeck(deckName, cardData) {

    const body_content = {
            name: deckName,
            isPublic: true,
            authorID: 1,
            cards: cardData
    }
    console.log(body_content)
    const response = await fetch("/api/decks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body_content)
    })
    return await response.json()
}
