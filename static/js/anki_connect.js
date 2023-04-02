/**
 * For the below functions to work, the user must have Anki open with the Anki Connect
 * plugin installed
 *
 * all method should be called using the `await` keyword
 * e.g.
 *    const deckNames = await localGetDecks()
 *
 * TODO: add error handling
 */

class DeckAnkiConnectDAO {

   constructor() {
      this.url = "http://localhost:8765"
   }

   /** 
    * As Anki connect uses a single endpoint for various actions, the data for a specific
    * action can be passed to this method, which will then execute it and return the resulting
    * json
    */
   async call(action) {
      const response = await fetch(this.url, {
         method: "POST",
         body: JSON.stringify(action)
      })
      const json = await response.json()
      return json.result
   }

   /**
    * Get the complete list of deck names for the current user
    */
   async localGetDecks() {
      const data = {
         action: "deckNames",
         version: 6
      }
      return await this.call(data)
   }

   /**
    * Create a new empty deck. Will not overwrite a deck that exists with the same name
    */
   async localCreateDeck(deckName) {

      const data = {
         action: "createDeck",
         version: 6,
         params: {
            deck: deckName
         }
      }
      return await this.call(data)
   }
}
