<script>
import { mapStores } from 'pinia';
import { useMyStore } from '../stores/myStore';
import api from '@/axios';

export default {
    data() {
        return {
            user_steam_id: "",
            is_invalid: false,
        }
    },
    computed: {
        ...mapStores(useMyStore)
    },
    methods: {
        async submitGet() {
            const url = "/api/"
            try {
                const response = await api.get(url, {
                    params: {
                        user_steam_id: this.user_steam_id
                    }
                })
                // update store
                this.myStoreStore.friendslist = response.data
                this.myStoreStore.user_steam_id = this.user_steam_id
                // change view
                this.$router.push('/select_friends')
            } catch (error) {
                this.is_invalid = true
            }
        },
        validateInput() {
            this.user_steam_id = this.user_steam_id.trim()

            // just checks to make sure the user has input a whole number.
            if (/^\d+$/.test(this.user_steam_id)) {
                this.is_invalid = false
                this.submitGet()
            }
            else {
                this.is_invalid = true
            }
        }
    }
}
</script>


<template>
    <div class="view">
        <div class="panel">
            <h1>Steam Games In Common</h1>
            <p>A tool that helps you determine which games you and your friends already own and can play together.</p>
        </div>
        <br>
        
        <div class="panel">
            <p>Enter your Steam ID to begin the search.</p>
            <p>Please note: your account, and your friends' accounts must be public in order to use this tool successfully.</p>

            <p v-if="is_invalid" class="error">The Steam ID you provided is invalid, or may belong to an account this is set to Private.</p>

            <div>
                <input
                    id="steam_id_input"
                    v-model="user_steam_id"
                    placeholder="Steam ID"
                    required
                />
                <button type="button" v-on:click="validateInput">Submit</button>
            </div>
        </div>
    </div>
</template>

<style>
</style>
