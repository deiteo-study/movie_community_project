<template>
  <div>
    <div v-if="!check">
      
      <div class="pw">
        <h1>Check Password</h1>
        <p>회원정보 수정을 위해 비밀번호를 입력해 주세요.</p>
        <br>
        <div class="form1">
            <form class="form" @submit.prevent="password_check">
                <label for="">PW : </label>
                <input type="password" v-model="password" />
                <button class="check"> 확인</button>
            </form>
        </div>
            
      </div>
     
    </div>
    <div v-else>
        <div class='changediv'>
        <h1>회원정보수정</h1>
        <div class="ff">
            <div class='set_box'>
                <h2>Change Profile</h2>
                <br>
                <br>         
                <br>       
                <img class="img" src="@/assets/gongsa.png" alt="-ing" >
                <br>
                <br>
                <h6>프로필 업데이트 기능 준비중 입니다..⌛️</h6>
                <p></p>
                <!-- <img src="@/assets/open.png" alt=""> -->
            </div>
            <div class='set_box'>
                <h2>Change Password</h2>
                <br>
                <label for="">username</label>
                <input type="text" :value='user.username' disabled/>
                <br>
                <label for="">password</label>
                <input type="password" v-model="password1" />
                <br>
                <label for="">password confirmation</label>
                <input type="password" v-model="password2" @keyup.enter="change_password"/>
                <br>
                <button  class="check" @click='change_password'>확인</button>
            </div>
        </div>
        <br>
        <button @click='accountdelete'>회원탈퇴</button>
    </div>
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
                alert('회원탈퇴가 완료되었습니다!')
            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style scoped>
.changediv {
    margin-top: 10%;
}
.ff {
    display: flex;
    justify-content: center ;
    margin:0 10%
}
.set_box {
    border: 1.5px solid rgb(156, 166, 171);
    border-radius: 0.9rem;
    width: 38%;
    margin: 30px;
    padding: 50px;
    box-shadow: 6px 6px 3px 3px gray;

}
.form{
    top: 20px;
    /* background-color: black; */
    /* width: 500px;
    margin: 10px auto 10px auto; */
}
input {
    border: solid 2px rgb(217, 221, 223);
    border-radius: 0.7rem;
    width: 320px;
    margin-left: 5px;
    margin-bottom: 10px;
    height: 40px;
    padding-left: 10px;
}
/* 확인 버튼 */
.check{
    border: none;
    background-color: rgb(185, 219, 228);
    border-radius: 0.7rem;
    margin-left: 5px;
}
.pw {
    margin-top: 20%;
}
label{
    font-size: 20px;
}
button{
    border: solid 1.5px rgb(159, 188, 188);
    background-color: rgb(255, 255, 255);
    border-radius: 0.7rem;
    margin-left: 5px;
    height: 35px;
    width: 75px;
}
button:hover {
  /* background-color:#edeee3; */
   background-color:#d2e3e7;
   border: solid rgb(181, 183, 184);
  outline: 0;
}
.img{
    width: 60px;
    height: 60px;
}
</style>