<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="createAccount">Create Account</button>
    <button>Log in</button>
    <form>
      <input v-model="username" placeholder="Username"/>
      <input v-model="password" placeholder="Password" type="password"/>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'HelloWorld',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  props: {
    msg: String
  },
  methods: {
    createAccount(event) {
      // `this` inside methods points to the current active instance
      // `event` is the native DOM event
      if (event) {
        //alert(this.username + this.password)
        axios.post("http://192.168.2.38:5000/create-account", {
          email: this.username,
          password: this.password
        })
        .then((response) => {
          if(response.status === 200) {
            alert("Account created");
          } else {
            alert("Something went wrong");
          }
        })
      }


    }

      
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
button {
  padding: 5px;
  margin: 5px;
}
input {
  padding: 5px;
  margin: 5px;
}
</style>
