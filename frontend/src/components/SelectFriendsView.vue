<script>
import { mapStores } from 'pinia';
import Cookies from "js-cookie"
import { useMyStore } from '../stores/myStore';
import FriendCard from './FriendCard.vue';
import api from '@/axios';

const csrfToken = Cookies.get("csrftoken")
api.defaults.headers.common["X-CSRFToken"] = csrfToken


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
                if (!this.myStoreStore.selected_friends.has(id)) {
                    console.log("Selected: " + id)
                    this.myStoreStore.selected_friends.add(id)
                }
                else {
                    console.log("Deselected: " + id)
                    this.myStoreStore.selected_friends.delete(id)
                }
            },
            async submitFriends() {
                this.$router.push('/shared')
            },
        }
    }
</script>

<template>
    <div class="view">
        <div class="panel">
            <p>Select your friends and then press "Submit" to see what games you have in common.</p>
        </div>

        <div class="panel">
            <p>You have selected:</p>
            <p>{{ this.myStoreStore.get_selected_friends_usernames.join(", ")}}</p>
            <button type="button" v-on:click="submitFriends">Submit</button>
        </div>
    </div>
    <div class="friend-menu">
        <FriendCard
            @friend_selected="onFriend_selected"
            v-for="friend in this.myStoreStore.friendslist"
            :steam_id="friend.steam_id"
            :username="friend.username"
            :avatarfull="friend.avatarfull"
        />
    </div>
</template>

<style>
.friend-menu {
    position:relative;
    justify-content: center;
    min-width: 200px;
    max-width: 900px;
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 200px));
    gap: 10px;
}

</style>