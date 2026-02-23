import {ref,Ref} from 'vue'
import axios from 'axios'
class LoginService{
    private ms:Ref<string> 

    constructor(){
    this.ms = ref('')
    }

    getMs():Ref<string>{
        return this.ms
    }


    async fetchByLogin(nombre_usuario:string,contrasena:string):Promise<void>{
        try{
            //const url = 'https://5e9147f5-145d-4231-97c5-0bdcffd88b89.clouding.host/api/seguser/login';
            const url = 'http://127.0.0.1:8000/api/seguser/login';
            const response = await axios.post(url,{
                usuario:nombre_usuario,
                contrasena:contrasena},{
                headers: {
                    'accept': 'application/json',
                    'content-type':'application/json',
                },
                withCredentials:true
                })
            this.ms.value = response.data;
        }catch(error){
            console.log(error)
        }
    }
}
export default LoginService
