<script>
import { mapStores } from 'pinia';
import { useMyStore } from '../stores/myStore';
import api from '@/axios';
import GameCard from './GameCard.vue';

export default {
    components: {
            GameCard
        },
    data() {
        return {
            loading: true,
            loaded: false,
            empty: false,
            multiplayer_only: false
        }
    },
    created() {
        this.getSharedGames()
    },
    computed: {
        ...mapStores(useMyStore),
    },
    methods: {
        async getSharedGames() {
            const url = "http://localhost:8000/shared/"
            const data = {
                    selected_friends: this.myStoreStore.get_selected_friends,
                    user_steam_id: this.myStoreStore.get_user_steam_id
                }
            this.loading = true

            try {
                const response = await api.post(url, data, { headers: { 'Content-Type': 'multipart/form-data' } })
                this.myStoreStore.shared_games = response.data

            } catch (err) {
                this.error = err.toString()
            } finally {
                this.loading = false
                if (this.myStoreStore.shared_games.length == 0) {
                    this.empty = true
                } else {
                    this.loaded = true
                }
            }
        },
        filterMultiplayer() {
            this.multiplayer_only = true
        }
    }
}
</script>

<template>
<div v-if="loading" class="loading">
    Loading...
</div>

<div v-if="empty" class="empty">
    There were no games in common :c
</div>

<div v-if="loaded" class="content">
    <div class="head">
        Here are the games you have in common with: {{ this.myStoreStore.get_selected_friends_usernames.join(", ") }}
    </div>
    <br>
    <div>
        <button v-on:click="filterMultiplayer">
            Show Multiplayer Only
        </button>
    </div>
    <br>
    <div class="card-container">
        <GameCard
            v-if="multiplayer_only"
            v-for="game in this.myStoreStore.get_shared_multiplayer_games"
            :app_id="game['appid']"
            :name="game['name']"
            :img_icon_url="game['img_icon_url']"
        />
        <GameCard
            v-else
            v-for="game in this.myStoreStore.get_shared_games"
            :app_id="game['appid']"
            :name="game['name']"
            :img_icon_url="game['img_icon_url']"
        />
    </div>
</div>
</template>

<style>
.head {
    margin-bottom: 1fr;
}
.card-container {
    position: relative;
    display: grid;
    gap: 10px;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
}

</style>