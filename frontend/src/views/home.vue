<script setup>

</script>

<template>
  <div class="main-page">
    <section class="home-section">
      <div class="home-container">
        <div class="home-info">
          <div class="info-title">Home</div>
          <div class="info-subtitle">这是一个关于招聘数据可视化的平台</div>
          <div class="home-to-view-btn">
            <router-link to="/charts" class="btn">所有图表</router-link>
          </div>
        </div>
        <div class="pic_div">
          <img src="/src/assets/picture.jpg" class="wordcloud">
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.main-page {
  position: absolute;
  top: 50px;
  left: 0;
  right: 0;
  bottom: 0;
  overflow-y: auto;
}

.home-section {
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.home-section .home-container {
  margin: 0 auto;
  height: 100%;
  padding: 0 30px;
  position: relative;
}

@media (min-width: 992px) {
  .home-container {
    width: 1080px;
  }
}


@media (max-width: 480px) {
  .home-container {
    text-align: center;
  }
}

.home-info {
  margin-top: 15vh;
}

@media (max-width: 992px) {
  .home-info {
    width: 100%;
    left: 0;
    margin-left: 0;
    text-align: center;
  }
}

@media (max-width: 768px) {
  .home-info {
    margin-top: 10vh;
  }
}

.info-title {
  font-size: 75px;
  font-weight: 800;
  color: #081642;
  line-height: 1.2em;
}

.info-subtitle {
  font-size: 21px;
  color: #1d2b5a;
  margin-top: 15px;
}

@media (max-width: 768px) {
  .info-subtitle {
    font-size: 14px;
    margin-top: 10px;
  }
}

.btn {
  margin-top: 5vh;
  display: inline-block;
  padding: 0.9rem 1.8rem;
  font-size: 16px;
  font-weight: 700;
  color: rgb(72, 72, 72);
  border: 3px solid rgb(252, 70, 100);
  border-radius: 30px;
  cursor: pointer;
  position: relative;
  background-color: transparent;
  text-decoration: none;
  overflow: hidden;
  z-index: 1;
  font-family: inherit;
}

.btn::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgb(252, 70, 100);
  transform: translateX(-100%);
  transition: all .3s;
  z-index: -1;
}

.btn:hover::before {
  transform: translateX(0);
}
.pic_div{
  height: 75%;
  top: 0;
  position: absolute;
  right: 20px;
}
@media (max-width: 1000px){
  .pic_div{
    height: 70%;
    top: 30%;
    right: 0;
  }
}


.wordcloud{
  width: 700px;
  height: 700px;
  max-width: 100%;
  max-height: 100%;
  position: relative;
  z-index: -100;
  overflow: hidden;
}
</style>