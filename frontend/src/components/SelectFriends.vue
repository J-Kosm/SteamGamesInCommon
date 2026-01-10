<script>
    export default {
        data() {
            return {
                username: ""
            }
        },
        methods: {
            submitFriends() {

            }
        }
    }
</script>

<template>
    <p>var's friendslist</p>
    <p>Select your friends to see what games you have in common, then press "Submit"</p>
    <button type="button" v-on:click="submitFriends">Submit</button>
</template>

<style>

</style>