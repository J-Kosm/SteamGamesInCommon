import { defineStore } from "pinia";

export const useMyStore = defineStore('myStore', {
    state: () => ({
        username: "",
        user_steam_id: "",
        friendslist: {},
        selected_friends: [],
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
        }

    },
    actions: {
        
    },
})