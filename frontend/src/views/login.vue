<script>
export default{
  data() {
    return {
      account: "",
      password: ""
    }
  },
  methods:{
    input(){
      console.log(this.account,this.password)
    }
  }
}
</script>

<template>
  <div class="form-container">
    <p>登录</p>
    <form class="form">
      <label>账号</label>
      <input type="text" v-model="account" class="input" placeholder="Enter yout email">
      <label>密码</label>
      <input type="password" v-model="password" class="input" placeholder="Password">
      <button @click="input">登入</button>
    </form>
  </div>
<!--  <p>account is :{{account}}</p>-->
<!--  <p>password is :{{password}}</p>-->
</template>

<style scoped>
.form-container {
  margin-top: 150px;
  left: 40%;
  width: 300px;
  background: linear-gradient(180deg,rgb(0, 183, 255) 25%,rgb(255, 255, 255) 20%);
  height: 350px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  box-shadow: 0 0 20px rgb(1, 4, 21);
}

.form {
  width: 80%;
  display: flex;
  flex-direction: column;
  margin-top: 40px;
}

.form-container p {
  position: absolute;
  top: 10%;
  left: 10%;
  font-size: 30px;
  font-weight: 900;
  color: rgb(255, 255, 255);
}

.form-container label {
  color: rgb(40, 42, 44);
  margin-top: 15px;
  margin-bottom: 5px;
  font-size: 15px;
}

.form-container .input {
  padding: 10px;
  height: 35px;
  border: none;
  background-color: rgb(224, 231, 236);
}

.form-container .input:focus {
  outline: none;
}

.form-container button {
  border: none;
  height: 35px;
  margin-top: 30px;
  background-color: rgb(0, 183, 255);
  color: white;
  font-size: 16px;
}

</style>