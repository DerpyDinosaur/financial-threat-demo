/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				'slide-green': '#00fdc8',
				'slide-purple': '#7c7ce0'
			}
		}
	},
	plugins: [],
}
