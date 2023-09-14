import {createStore} from 'vuex';

const store = createStore({
    state:{
        user:{
            "name":localStorage.getItem("username"),
            "id":localStorage.getItem("id"),
            "token":localStorage.getItem("token"),
        }
    },
    actions:{
        login(context, payload){
            context.state.user.name = payload.name
            context.state.user.id = payload.id
            context.state.user.token = payload.token
        },
        logout(context, payload){
            localStorage.removeItem("username")
            localStorage.removeItem("id")
            localStorage.removeItem("token")
            context.state.user.name = undefined
            context.state.user.id = undefined
            context.state.user.token = undefined
        }
    }
})

export default store