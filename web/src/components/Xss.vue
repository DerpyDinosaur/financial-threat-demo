<template>
    <form @submit.prevent="submit">
        <label>Input</label>
        <input type="text"/>
        <button type="submit">Submit</button>
    </form>

    <div id="box" class=""></div>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { useStore } from '@nanostores/vue'
    import { users } from '../store'

    const input = ref('');
    const $users = useStore(users);

    const submit = () => {
        alert($users);
    }
</script>