<script>
import { mapStores } from 'pinia';
import { useMyStore } from '../stores/myStore';
import FriendCard from './FriendCard.vue';


    export default {
        components: {
            FriendCard
        },
        data() {
            return {
                selected_friends: []
            }
        },
        computed: {
            ...mapStores(useMyStore)
        },
        methods: {
            // keep track of which friends were selected.
            onFriend_selected(id) {
                if (!this.myStoreStore.selected_friends.includes(id)) {
                    this.myStoreStore.selected_friends.push(id)
                }
                else {
                    this.myStoreStore.selected_friends.pop(id)
                }
            },
            async submitFriends() {
                const url = "http://localhost:8000/shared/"
                // const params = url + ? + 
                const response = await fetch(url, {
                    method: "POST"
                })


                // const response = await fetch((url + "?" + params.toString()), {
                //     method: "GET",
                // })
            },
        }
    }
</script>

<template>
    <p>Your friendslist</p>
    <p>Select your friends and then press "Submit" to see what games you have in common.</p>
    <button type="button" v-on:click="submitFriends">Submit</button>

    <FriendCard
        @friend_selected="onFriend_selected"
        v-for="friend in this.myStoreStore.friendslist"
        :steam_id="friend.steam_id"
        :username="friend.username"
        :avatarfull="friend.avatarfull"
    />

</template>

<style>

</style>