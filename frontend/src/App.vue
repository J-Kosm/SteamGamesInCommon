<script>
import { mapStores } from 'pinia'
import { useMyStore } from './stores/myStore';

export default {
  data() {
    return {

    }
  },
  computed: {
    ...mapStores(useMyStore)
  }
}


console.log("APP SCRIPT SETUP RUN")
</script>

<template>
  <main>
    <RouterView />
  </main>
</template>
