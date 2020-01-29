
export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: 'murr_front',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
    "~/static/fonts/fonts.css"
    // {src: "~/static/fonts/fonts.css"}
    // '~/assets/fonts.css'

    // '~/node_modules/bulma/css/bulma.min.css'
    // '~/node_modules/normalize.css/normalize.css'
    // '~/node_modules/bootstrap/dist/css/bootstrap.min.css'
    // '~/node_modules/bootstrap/dist/css/bootstrap-grid.min.css'
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
  ],
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
