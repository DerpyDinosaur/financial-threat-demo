<template>
	<Login v-if="!$authenticated"/>
	<main v-else>
		<button @click="hydrate()">Hydrate</button>
	</main>
</template>

<script setup lang='ts'>
	import { authenticated, hydrate } from '../store';
	import { useStore } from '@nanostores/vue';
	//||
	import Login from './Login.vue'

	// Variables
	const $authenticated = useStore(authenticated)
</script>