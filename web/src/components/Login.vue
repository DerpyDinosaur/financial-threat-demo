<template>
	<section class="mt-20 flex flex-col gap-4">
		<h4 class="text-center text-4xl">Login</h4>
		<form class="flex flex-col gap-4" @submit.prevent="submit()" autocomplete="off">
			<label>Username</label>
			<input class="p-4 text-3xl focus:outline-none bg-amber-900/10" v-model="username">
			<label>Password</label>
			<input class="p-4 text-3xl focus:outline-none bg-amber-900/10" v-model="password">
			<button class="m-auto w-1/2 text-xl outline outline-2 outline-amber-900/30 bg-amber-900/50" type="submit">Submit</button>
		</form>
	</section>

</template>

<script setup lang='ts'>
	import { onMounted, ref } from 'vue'
	import { login } from '../store'
	import { useStore } from '@nanostores/vue'

	const username = ref('')
	const password = ref('')

	const submit = async () => {
		await login(username.value, password.value)
	}
</script>