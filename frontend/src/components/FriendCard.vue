<script>
export default {
    data() {
        return {
            isSelected: false
        }
    },
    props: ['steam_id', 'username', 'avatarfull'],
    methods: {
        onClicked() {
            this.isSelected = !this.isSelected
            this.$emit('friend_selected', this.steam_id)
        },

    }
}
</script>

<template>
    <div 
        class="card"
        :class="{ selected: isSelected }"
        @click=onClicked
    >
        <img :src="this.avatarfull" alt="" >
        <p>
            {{ this.username }}
        </p>
    </div>
</template>

<style>
.card {
  position: relative;
  display: inline-block;
  text-align: center;
  border-style: solid;
  margin: auto;
  background-color: var(--panel-color);
}
.selected {
    border-color: blue;
    background-color: rgb(126, 171, 255);
}

</style>