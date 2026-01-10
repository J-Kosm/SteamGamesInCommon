<script>
export default {
    data() {
        return {
            steam_id: ""
        }
    },
    methods: {
        async submitGet(e) {
            const url = "http://localhost:8000/"
            const params = new URLSearchParams({
                steam_id: this.steam_id
            })

            try {
                const response = await fetch((url + "?" + params.toString()), {
                    method: "GET",
                })
                if (!response.ok) {
                    throw new Error("Request Failed")
                }

                this.result = await response.text()
            } catch (err) {
                console.log("Error")
                console.log(err)
            }
        },
    }
}

</script>


<template>
    <label for="steam_id_input">Enter Your Steam ID: </label>
    <input
        id="steam_id_input"
        v-model="steam_id"
        placeholder="Steam ID"
        required
    />
    <br>
    <button type="button" v-on:click="submitGet">Submit</button>
</template>

<style></style>
