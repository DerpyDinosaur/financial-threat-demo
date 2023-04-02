<template>
	<Login v-if="!$authenticated"/>
	<main class="p-8 mb-8 relative grid grid-rows-[.1fr_.1fr_1fr] bg-yellow-900/10 rounded" v-else>
		<div class="flex justify-between items-center">
			<h4 class="text-4xl capitalize">Welcome, {{$profile.username}}</h4>
			<button class="px-2 py-1 my-4 text-xl outline outline-4 outline-amber-900/30 bg-amber-900/50" @click="logout()">Logout</button>
		</div>
		<div class="flex justify-between items-center">
			<button class="px-2 py-1 my-4 text-xl outline outline-4 outline-amber-900/30 bg-amber-900/50">Payment</button>
			<button class="px-2 py-1 my-4 text-xl outline outline-4 outline-amber-900/30 bg-amber-900/50">Buy FOMO</button>
		</div>
		<div class="text-center">
			<h2><span class="display text-2xl">FOMO</span> {{$profile.wallet}}</h2>
			<div class="p-4 grid grid-cols-4 justify-center items-center">
				<h3 class="p-2 text-xl font-bold">Date</h3>
				<h3 class="p-2 text-xl font-bold">Action</h3>
				<h3 class="p-2 text-xl font-bold">Amount</h3>
				<h3 class="p-2 text-xl font-bold">Total</h3>
				<template v-for="item in $profile['history']">
					<p class="p-1">{{item["date"]}}</p>
					<p class="p-1">{{item["action"]}}</p>
					<p :class="{'text-red-900':item['action']=='debit','text-green-900':item['action']=='credit'}" class="p-1">{{item["amount"]}}</p>
					<p class="p-1">{{item["total"]}}</p>
				</template>
			</div>
		</div>
	</main>
</template>

<script setup lang='ts'>
	import { watch } from 'vue'
	import { authenticated, hydrate, profile } from '../store'
	import { useStore } from '@nanostores/vue'
	//||
	import Login from './Login.vue'

	// Variables
	const $authenticated = useStore(authenticated)
	const $profile = useStore(profile)

	// Methods
	const logout = () => authenticated.set(false);

	// Computed
	watch($authenticated, (n) => {
		if(n) hydrate()
	})
</script>