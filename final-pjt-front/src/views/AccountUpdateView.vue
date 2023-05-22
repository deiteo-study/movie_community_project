<template>
  <div>
    <div v-if="!check">
      <h1>비밀번호 확인</h1>
      <p>회원정보 수정을 위해 비밀번호를 입력해 주세요.</p>
      <form @submit.prevent="password_check">
        <label for="">비밀번호 : </label>
        <input type="password" v-model="password" />
        <button>확인</button>
      </form>
    </div>
    <div v-else>
        <h1>회원정보수정</h1>
        <div class="ff">
            <div class='set_box'>
                <h1>프로필 변경</h1>
                <p>프로필 변경에 대한것 추가...</p>
            </div>
            <div class='set_box'>
                <h1>비밀번호 변경</h1>
                <label for="">아이디 : </label>
                <input type="text" :value='user.username' disabled/>
                <br>
                <label for="">비밀번호 : </label>
                <input type="password" v-model="password1" />
                <br>
                <label for="">비밀번호 확인 : </label>
                <input type="password" v-model="password2" @keyup.enter="change_password"/>
                <br>
                <button @click='change_password'>확인</button>
            </div>
        </div>
        <button @click='accountdelete'>회원탈퇴</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'AccountUpdateView',
    data(){
        return {
            check:false,
            user:null,
            password:null,

            password1:null,
            password2:null
        }
    },
    created(){
        axios({
            method:'get',
            url: `http://127.0.0.1:8000/accounts/user/`,
            headers : {
                Authorization: ` Token ${this.$store.state.token }`}
        })
        .then(res => {
            this.user=res.data
        })
        },
    methods:{
        password_check(){
            const username=this.user.username
            const password=this.password

            axios({
                method: 'post',
                url: `http://127.0.0.1:8000/accounts/login/`,
                data:{username,password}
            })
            .then(res => {
                if (this.$store.state.token==res.data.key) {
                    this.check=true
                }
            })
            .catch((err) => console.log(err))
        },
        change_password(){
            if (!this.password1 || !this.password2) {
                return alert('변경할 비밀번호를 입력해주세요')
            }
            if (this.password1 != this.password2) {
                return alert('비밀번호를 확인해주세요.')
            }

            const new_password1=this.password1
            const new_password2=this.password2
            // const old_password=this.password

            const payload={
                new_password1,new_password2
            }
            this.$store.dispatch('change_password', payload)
        },
        accountdelete(){
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/accounts/delete/`,
                headers : {
                    Authorization: ` Token ${this.$store.state.token }`}
            })
            .then(res => {
                console.log(res)
                this.$store.commit('LOGOUT')
            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style scoped>
.ff {
    display: flex;
    justify-content: space-between;
    margin:0 10%
}
.set_box {
    border: 2px solid blue;
    width: 80%;
    margin: 20px;
    padding: 50px;
}
</style>