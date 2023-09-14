<script setup>
import VHeader from '../components/htmlComponents/VHeader.vue';
import VFooter from '../components/htmlComponents/VFooter.vue';
import VMain from '../components/htmlComponents/VMain.vue';
import Input from '../components/Input.vue';
import ResetButton from '../components/ResetButton.vue';
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { HTTP } from '../api'

const router = useRouter()
const store = useStore()
const data = ref({})
const errors = ref("")

const submitHandler = async () => {
    try{
        const response = await HTTP.post("/jwt/token/",data.value)
        const response_detail = await HTTP.get("/jwt/user/", {
            headers:{
                Authorization: `Bearer ${response.data.access}`
            }
        })
        localStorage.setItem("username",response_detail.data?.username)
        localStorage.setItem("id",response_detail.data?.id)
        localStorage.setItem("token",response.data?.access)
        store.dispatch('login',{name:response_detail.data?.username,token:response.data?.access,id:response_detail.data?.id})
        router.push({path: "/"})
    }
    catch (error){
        console.log(error)
    }
}

const inputHandler = (e) => {
    data.value[e.target.name] = e.target.value
}

</script>
<template>
    <VHeader/>
    <VMain>
        <div class="form-container">
            <form @submit.prevent="submitHandler">
                <h1>Login Form</h1>
                <p v-if="errors">Errors</p>
                <Input name="username" type="text" @change="inputHandler" placeholder="Enter username" />
                <Input name="password" type="password" @change="inputHandler" placeholder="Enter password" />
                <ResetButton>Log In</ResetButton>
            </form>
        </div>
    </VMain>
    <VFooter/>
</template>

<style scoped lang="scss">
@import "../scss/variables.scss";

.form{
    &-container{
        padding-top: 80px;
        min-height: calc(100vh - 160px);
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        h1{
            text-align: center;
            font-family: $fontES;
            font-size: 40px;
            letter-spacing: 2px;
            margin-bottom: 0.5em;
        }
    }
}
</style>