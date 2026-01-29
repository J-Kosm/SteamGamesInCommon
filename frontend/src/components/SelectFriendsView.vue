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
                if (!this.myStoreStore.selected_friends.includes(id)) {
                    this.myStoreStore.selected_friends.push(id)
                }
                else {
                    this.myStoreStore.selected_friends.pop(id)
                }
            },
            async submitFriends() {
                // const url = "http://localhost:8000/shared/"
                // console.log(this.myStoreStore.get_selected_friends)
                // const data = {
                //     selected_friends: this.myStoreStore.get_selected_friends
                // }
                // const response = await api.post(url, data, { headers: { 'Content-Type': 'multipart/form-data' } })
                this.$router.push('/shared')
            },
        }
    }
</script>

<template>
    <div>
        <p>Your friendslist</p>
        <p>Select your friends and then press "Submit" to see what games you have in common.</p>
        <button type="button" v-on:click="submitFriends">Submit</button>
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
    position: relative;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 200px));
    gap: 10px;
}

</style>