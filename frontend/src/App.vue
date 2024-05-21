<script setup>
</script>

<template>
  <nav class="navbar-default">
    <div class="navbar-header">
      招聘数据可视化
    </div>
    <div class="navbar-collapse">
      <ul>
        <li class="left-li">
          <router-link to="/">首页</router-link>
        </li>
        <li class="left-li">
          <router-link to="/charts">图表</router-link>
        </li>
      </ul>
<!--      <ul>-->
<!--        <li class="right-li">-->
<!--          <router-link to="/login">登录</router-link>-->
<!--        </li>-->
<!--      </ul>-->
    </div>

  </nav>

  <main>
    <router-view></router-view>
  </main>

</template>

<style scoped>

.navbar-default {
  top: 0;
  right: 0;
  left: 0;
  background-color: #ffffff;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  height: 50px;
  margin-bottom: 20px;
  z-index: 10000;
}

.navbar-header {
  font-weight: bolder;
  font-size: 20px;
  color: #65d2f3;
  float: left;
  padding: 8px 8px;
}

.navbar-default li {
  text-decoration: none;
  list-style: none;
}

.navbar-default a {
  text-decoration: none;
  padding: 10px 20px;
  color: #181818;
  display: block;
}

.navbar-collapse {
  height: auto !important;
  padding-right: 10px;
}

.navbar-collapse .left-li {
  height: 50px;
  float: left;
}

.navbar-collapse .right-li {
  height: 50px;
  float: right;
}

.left-li::before, .right-li::before {
  margin-left: auto;
}

.left-li::before, .right-li::before {
  content: '';
  width: 0;
  height: 2px;
  background: #f44336;
  display: block;
  transition: 0.5s;
}

.left-li:hover::before, .right-li:hover::before {
  width: 100%;
}

</style>
