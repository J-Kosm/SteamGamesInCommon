<script>
export default {
    props: ['app_id', 'name', 'img_icon_url'],
    data() {
        return {
            img_src: `https://cdn.fastly.steamstatic.com/steamcommunity/public/images/apps/${this.app_id}/${this.img_icon_url}.jpg`
        }
    },
    
}
</script>

<template>
    <div class="game-card">
        <img :src="img_src" alt="">
        <span>{{ this.name }}</span>
    </div>
</template>

<style>
.game-card {
  position: relative;
  display: flex;
  border-style:solid;
  width: auto;
  height: auto;
  align-items: center;
  background-color: var(--panel-color);
}
.game-card img {
    max-height: 32px;
    max-width: 32px;
}
.game-card span {
    padding: 4px;
    margin: auto;
    
}

</style>