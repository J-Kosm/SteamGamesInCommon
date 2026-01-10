<script>
export default {
    data() {
        return {
            count: 0
        }
    },
    methods: {
        counter(e) {
            this.count = this.count + 1
            console.log("Counting!")
            console.log(this.count)
        }
    }
}

console.log("APP SCRIPT SETUP RUN")
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <button v-on:click="counter">Increment</button>
  </div>
</template>
