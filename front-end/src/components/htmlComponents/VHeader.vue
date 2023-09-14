<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useStore()
const user = useStore().state.user
const burger_active = ref(false);

const open_menu = () =>{
    burger_active.value = !burger_active.value;
    document.body.classList.toggle('lock');
}

const redirectToPage = (path) => {
    router.push({path:path})
}

</script>
<template>
    <header class="header">
        <div class="header__container">
            <div class="header__logo" @click="redirectToPage('/')"><a href="#"><span class="newcolor">A</span>Movie</a></div>
            <div v-if="!user.name" class="header__reg">
                <div style="cursor: pointer;" class="log-up" @click="redirectToPage('/sign-up/')" >Sign<span class="newcolor">Up</span></div>
                <div class="slash">|</div>
                <div style="cursor: pointer;" class="log-in" @click="redirectToPage('/login/')" >Log<span class="newcolor">In</span></div>
            </div>
            <div class="header__reg" v-else>
                <div class="newcolor">{{ user.name }}</div>
                <div class="slash">|</div>
                <div style="cursor: pointer;" @click="redirectToPage('/favorite/')">Favorite</div>
                <div class="slash">|</div>
                <div style="cursor: pointer;" class="newcolor" @click="()=>{store.dispatch('logout')}">Logout</div>
            </div>
            <div class="burger__btn" @click="open_menu()" :class="{burger__btn_active: burger_active}"><span></span></div>
        </div>
    </header>
    <div class="header__reg_burger" >
        <div v-if="!user.name" class="burger__row" :class="{burger__row_active: burger_active}">
            <div class="log-up">Log<span class="newcolor">Up</span></div>
            <div class="log-in">Log<span class="newcolor">In</span></div>
        </div>
        <div v-else class="burger__row" :class="{burger__row_active: burger_active}">
            <div class="newcolor">{{ user.name }}</div>
            <div>Favorite</div>
            <div style="cursor: pointer;" class="newcolor" @click="()=>{store.dispatch('logout')}">Logout</div>
        </div>
    </div>
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
.header {
    width: 100%;
    height: 80px;
    position: fixed;
    z-index: 100;
    background-color: $colorGrey;
    &__container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 80px;
        @extend %limiter;
        padding: 00px 20px;
    }
    &__logo {
        font-size: 48px;
    }
    &__reg {
        display: flex;
        align-items: center ;
        *{
            font-size: 32px;
        }
        .slash{
            margin: 0px 10px;
        }
    }
    &__reg_burger{
        display: none;
        align-items: center;
        *{
            font-size: 32px;
        }
    }
    *{
        font-family: $fontES;
    }
}
.burger__btn{
    display: none;
}
.newcolor{
    color: $colorBlue;
}
@media (max-width:581px) {
    .header{
        &__reg{
            display: none;
        }
        &__reg_burger{
            display: block;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    }
    .burger{
        &__row{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            min-height: 100vh;
            position: relative;
            z-index: 10;
            background-color: #3e3e3e;
            transform: translateY(-100%);
            transition: transform 300ms;
            & div{
                margin-bottom: 20px;
            }
            & div:last-child{
                margin-bottom: 0px;
            }
            &_active{
                transform: translate(0);
            }
        }
        &__btn{
            display: block;
            position: relative;
            width: 30px;
            height: 16px;
            cursor: pointer;
            &::before{
                content: '';
                transition: all 300ms;
                left: 0;
                top: 0;
                position: absolute;
                height: 10%;
                width: 100%;
                background-color: #fff;
            }
            &::after{
                content: '';
                transition: all 300ms;
                left: 0;
                bottom: 0;
                position: absolute;
                height: 10%;
                width: 100%;
                background-color: #fff;
            }
            & span{
                transition: all 300ms;
                left: 0;
                top: 50%;
                transform: scale(1) translate(0px, -50%);
                position: absolute;
                height: 10%;
                width: 100%;
                background-color: $colorBlue;
            }
        }
        &__btn_active{
            &::before{
                transform: rotate(-45deg);
                top: 8px;
            }
            &::after{
                content: '';
                transform: rotate(45deg);
                bottom: 6px;
            }
            & span{
                transform: scale(0) translate(0px, -50%);
            }
        }
    }
}

</style>
