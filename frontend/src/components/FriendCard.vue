<script>
export default {
    props: ['steam_id', 'username', 'avatarfull'],
}
</script>

<template>
    <li>
        <input @click="$emit('friend_selected', this.steam_id)" type="checkbox" name="" id="">
        <img :src="this.avatarfull" alt="">
        {{ this.username }}
    </li>
</template>

<style>

</style>