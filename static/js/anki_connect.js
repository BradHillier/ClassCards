/**
 * For the below functions to work, the user must have Anki open with the Anki Connect
 * plugin installed
 *
 * all method should be called using the `await` keyword
 * e.g.
 *    const deckNames = await myDeckAnkiConnectDAO.getDeckNames()
 *
 * Documentation is mostly taken from Anki-Connect's offical documentation which can be found 
 * at: 
 *    https://foosoft.net/projects/anki-connect/index.html
 *
 * TODO: add error handling
 */

class DeckAnkiConnectDAO {

   constructor() {

      // The url of the server started by Anki-Connect
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
    * Requests permission to use the API exposed by Anki Connect. This method does not require 
    * the API key, and is the only one that accepts requests from any origin; the other methods 
    * only accept requests from trusted origins, which are listed under webCorsOriginList in 
    * Anki Connect's add-on config. localhost is trusted by default.

    * Calling this method from an untrusted origin will display a popup in Anki asking the 
    * user whether they want to allow your origin to use the API; calls from trusted origins 
    * will return the result without displaying the popup. When denying permission, the user 
    * may also choose to ignore further permission requests from that origin. These origins 
    * end up in the ignoreOriginList, editable via the add-on config.
    *
    * The result always contains the permission field, which in turn contains either the 
    * string granted or denied, corresponding to whether your origin is trusted. If your 
    * origin is trusted, the fields requireApiKey (true if required) and version will also be 
    * returned.
    *
    * This should be the first call you make to make sure that your application and 
    * Anki-Connect are able to communicate properly with each other. New versions of 
    * Anki-Connect are backwards compatible; as long as you are using actions which are 
    * available in the reported Anki-Connect version or earlier, everything should work fine.
    */
   async requestPermission() {
      const data = {
         action: "requestPermission",
         version: 6
      }
      return await this.call(data)
   }

   /**
    * Get the complete list of deck names for the current user
    */
   async getDeckNames() {
      const data = {
         action: "deckNames",
         version: 6
      }
      return await this.call(data)
   }

   /**
    * Create a new empty deck. Will not overwrite a deck that exists with the same name
    */
   async createDeck(deckName) {

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
