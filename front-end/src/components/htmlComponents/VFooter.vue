<script setup>

</script>
<template>
    <footer class="footer">
        <div class="footer__info">
            <div class="author">@site</div>
            <div class="contacts">
                <div>Contacts</div>
                <div class="contacts__data">
                    <div class="contacts__tel">tel:+380980944511</div>
                    <div class="contacts__email">email: email.ore</div>
                </div>
            </div>
        </div>
    </footer>
</template>
<style scoped lang="scss">
@import "../../scss/variables.scss";
.footer {

    position: relative;
    z-index: 2;
    background-color: $colorGrey;
    padding: 10px 0px;
    &__info {
        @extend %limiter;
        padding: 0px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    *{
        font-size: 20px;
    }
}
.contacts {
    display: flex;
    align-items: center;
    &__data {
        margin-left: 20px;
    }
}

</style>
