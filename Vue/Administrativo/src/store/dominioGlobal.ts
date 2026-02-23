import {defineStore} from 'pinia'

export const UrlGlobal = defineStore('dominio', {
    state: () => ({
        //urlGlobal: 'https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host'
        urlGlobal: 'http://127.0.0.1:8000'
    })

})
