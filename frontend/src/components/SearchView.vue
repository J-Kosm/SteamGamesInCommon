<script>
import { mapStores } from 'pinia';
import { useMyStore } from '../stores/myStore';
import api from '@/axios';

export default {
    data() {
        return {
            user_steam_id: ""
        }
    },
    computed: {
        ...mapStores(useMyStore)
    },
    methods: {
        async submitGet() {
            const url = "http://localhost:8000/"
            try {
                const response = await api.get(url, {
                    params: {
                        user_steam_id: this.user_steam_id
                    }
                })
                // update store
                console.log(response.data)
                this.myStoreStore.friendslist = response.data
                this.myStoreStore.user_steam_id = this.user_steam_id
                // change view
                this.$router.push('/select_friends')
            } catch (error) {
                console.error(error)
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
