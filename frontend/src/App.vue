<script setup>
import { ref } from "vue"

const count = ref(0)

console.log("APP SCRIPT SETUP RUN")
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="count++">Increment</button>
  </div>
</template>
