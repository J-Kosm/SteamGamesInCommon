import { defineStore } from "pinia";

export const useMyStore = defineStore('myStore', {
    state: () => ({
        username: "",
        user_steam_id: "",
        friendslist: {},
        selected_friends: new Set(),
        shared_games: {},
    }),
    getters: {
        get_selected_friends(state) {
            return state.selected_friends
        },
        get_user_steam_id(state) {
            return state.user_steam_id
        },
        get_shared_games(state) {
            return state.shared_games
        },
        get_shared_multiplayer_games(state) {
            const shared_multiplayer_games = []
            const mutliplayer_tags = ["Multiplayer", "Co-op", "Online Co-Op", "Local Co-Op", "PvP", "Team-Based"]

            for (let i = 0; i < state.shared_games.length; i++) {

                if (state.shared_games[i]["tags"].some(j => mutliplayer_tags.includes(j))) {
                    shared_multiplayer_games.push(state.shared_games[i])
                }
            }
            return shared_multiplayer_games
        },
        get_selected_friends_usernames(state) {
            const data = []
            for (const user of state.selected_friends) {
                data.push(state.friendslist[user].username)
            }
            return data
        }

    },
    actions: {
        
    },
})