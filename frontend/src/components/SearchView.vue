<script>
import { mapStores } from 'pinia';
import { useMyStore } from '../stores/myStore';

export default {
    data() {
        return {
            steam_id: ""
        }
    },
    computed: {
        ...mapStores(useMyStore)
    },
    methods: {
        async submitGet(e) {
            const url = "http://localhost:8000/"
            const params = new URLSearchParams({
                user_steam_id: this.user_steam_id
            })
            try {
                const response = await fetch((url + "?" + params.toString()), {
                    method: "GET",
                })
                if (!response.ok) {
                    throw new Error("Request Failed")
                }
                if (this.myStore) {
                    console.log("store is loaded")
                }
                if (this.myStoreStore) {
                    console.log("storestore is loaded")
                }
                // update store
                this.myStoreStore.friendslist = await response.json()
                this.myStoreStore.user_steam_id = this.user_steam_id
                // change view
                this.$router.push('/select_friends')

            } catch (err) {
                console.log("Error")
                console.log(err)
            }
        },
    }
}
</script>


<template>
    <label for="steam_id_input">Enter Your Steam ID: </label>
    <input
        id="steam_id_input"
        v-model="user_steam_id"
        placeholder="Steam ID"
        required
    />
    <br>
    <button type="button" v-on:click="submitGet">Submit</button>
</template>

<style>
    
</style>
