<template>
	<h1>Login</h1>
</template>

<script setup lang='ts'>
	import { onMounted, ref } from 'vue'
	import { login } from '../store'
	import { useStore } from '@nanostores/vue'

	const response = ref('')

	onMounted(() => {
		response.value = login("albalamia", "password")
	})
</script>