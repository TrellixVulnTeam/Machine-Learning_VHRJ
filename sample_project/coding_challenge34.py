{
                kind: "method",
                key: "loadDeckType",
                value: function() {
                    this.deckType = {
                        "#friends": "friends",
                        "#lovers": "lovers"
                    }[location.hash] || "friends"
                }
            }, {
                kind: "method",
                key: "onFriendsNav",
                value: function({detail: {hash: e, direction: t}}) {
                    this.lastFriendsCard = e, It.save(this.store, "friends", e)
                }
            }, {
                kind: "method",
                key: "onLoversNav",
                value: function({detail: {hash: e, direction: t}}) {
                    this.lastLoversCard = e, It.save(this.store, "lovers", e)






                    



                    #########333

                    {
                kind: "method",
                key: "loadDeckType",
                value: function() {
                    this.deckType = {
                        "#friends": "friends",
                        "#lovers": "lovers"
                    }[location.hash] || "friends"
                }
            }, {
                kind: "method",
                key: "onFriendsNav",
                value: function({detail: {hash: e, direction: t}}) {
                    this.lastFriendsCard = e, It.save(this.store, "friends", e)
                }
            }, {
                kind: "method",
                key: "onLoversNav",
                value: function({detail: {hash: e, direction: t}}) {
                    this.lastLoversCard = e, It.save(this.store, "lovers", e)