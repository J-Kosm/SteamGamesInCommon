<script>
export default {
    props: ['app_id', 'name', 'img_icon_url'],
    
}
</script>

<template>
    <div>
        <img src="https://cdn.fastly.steamstatic.com/steamcommunity/public/images/apps/{{this.app_id}}/{{this.img_icon_url}}.jpg" alt="">
        <p>{{ this.name }}</p>
    </div>
</template>

<style>

</style>