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
const errors = ref([])

const submitHandler = async () => {
    errors.value = []
    if (data.value.password == data.value.password1){
        try{
            const response = await HTTP.post("/auth/users/",data.value)
            router.push({path: "/",query:{success_reg:true}})
        }
        catch (error){
            Object.keys(error.response.data).forEach(item=>{
                errors.value.push(error.response.data[item][0])
            })
        }
    }
    else{
        errors.value.push("Passwords are not matching")
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
                <h1>Sign Up Form</h1>
                <div v-if="errors.length > 0" class="errors">
                    <span v-for="(item, index) in errors" :key="index">{{ item }}</span>
                </div>
                <Input name="username" type="text" @change="inputHandler" placeholder="Enter username" required/>
                <Input name="email" type="email" @change="inputHandler" placeholder="Enter email" required/>
                <Input name="password" type="password" @change="inputHandler" placeholder="Enter password" required/>
                <Input name="password1" type="password" @change="inputHandler" placeholder="Repeat password" required/>
                
                <ResetButton>Sign Up</ResetButton>
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