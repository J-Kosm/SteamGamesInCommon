import { defineStore } from "pinia";

export const useMyStore = defineStore('myStore', {
    state: () => ({
        username: "",
        user_steam_id: "",
        friendslist: {},
        selected_friends: [],
    }),
    getters: {
        get_selected_friends(state) {
            return state.selected_friends
        }
    },
    actions: {
        
    },
})