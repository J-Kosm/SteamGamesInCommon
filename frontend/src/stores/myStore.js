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
            console.log(state.shared_games)
            return state.shared_games
        },
        get_selected_friends_usernames(state) {
            const data = []
            for (let i = 0; i < state.selected_friends.length; i++) {
                data.push(state.friendslist[state.selected_friends[i]].username)
            }
            return data
        }

    },
    actions: {
        
    },
})