<script>
import chart_exp from '@/components/chart_exp.vue';
import chart_area from '@/components/chart_area.vue';
import chart_salary from '@/components/chart_salary.vue';
import chart_skill from '@/components/chart_skill.vue';
import chart_degree from '@/components/chart_degree.vue';
import chart_all_key from "@/components/chart_all_key.vue";
import loader from '@/components/loader.vue';
import axios from "axios";
import api from '../api/api.js';


export default {
  data() {
    return {
      items: [],
      items_count:[],
      selectedIndex: 0,
      chart_name: 'main',
      is_loading: true,
      query_key: '',
      query_type: ''
    }
  }, mounted() {
    this.get_keywords()
  },
  methods: {
    //实现导航点击变色
    getTopic(index, id) {
      this.selectedIndex = index;
    },
    //实现页面内平滑跳转
    scrollToAnchor(anchor) {
      const element = document.getElementById(anchor);
      if (element) {
        element.scrollIntoView({behavior: 'smooth'});
      }
    },
    get_keywords() {
      axios({
        method: 'post',
        url: api.basePath+api.get_key,
        data: {
          keyword: 'all'
        }
      }).then(res => {
        // 返回请求到的数据
        this.items = Object.values(res.data.keyword)
        this.items_count = Object.values(res.data.count)
        this.is_loading = false
      }).catch(err => {
        // 返回错误信息
        console.log('出现错误：')
        if (err.response.status === 500)
          window.alert("500\n网络异常，请稍后再试");
        this.is_loading = false
        console.log(err)
      })
    }
  },
  components: {
    loader,
    chart_all_key,
    chart_area,
    chart_exp,
    chart_salary,
    chart_skill,
    chart_degree
  }
}

</script>

<template>
  <div v-if="is_loading" class="loader">
    <loader></loader>
  </div>
  <div class="charts-page">
    <div class="left-container" id="left-container">
      <ul>
        <li v-for="(item,index) in items">
          <a :href="'#'+item" :class="selectedIndex === index ? 'active':''"
             @click="getTopic(index, item.topicClassId); chart_name='main'"
             @click.prevent="scrollToAnchor(item)">{{ item }}</a>
        </li>
      </ul>
    </div>
    <div class="charts" id="charts">
      <div v-if=" chart_name === 'area'">
        <button @click="chart_name='main'; selectedIndex = 0">
          <span class="shadow"></span>
          <span class="edge"></span>
          <span class="front text">返回</span>
        </button>
        <chart_area :q_keyword="query_key" :q_type="query_type"></chart_area>
      </div>
      <div v-if=" chart_name === 'salary'">
        <button @click="chart_name='main'; selectedIndex = 0">
          <span class="shadow"></span>
          <span class="edge"></span>
          <span class="front text">返回</span>
        </button>
        <chart_salary :q_keyword="query_key" :q_type="query_type"></chart_salary>
      </div>
      <div v-if=" chart_name === 'degree'">
        <button @click="chart_name='main'; selectedIndex = 0">
          <span class="shadow"></span>
          <span class="edge"></span>
          <span class="front text">返回</span>
        </button>
        <chart_degree :q_keyword="query_key" :q_type="query_type"></chart_degree>
      </div>
      <div v-if=" chart_name === 'exp'">
        <button @click="chart_name='main'; selectedIndex = 0">
          <span class="shadow"></span>
          <span class="edge"></span>
          <span class="front text">返回</span>
        </button>
        <chart_exp :q_keyword="query_key" :q_type="query_type"></chart_exp>
      </div>
      <div v-if=" chart_name === 'technique'">
        <button @click="chart_name='main'; selectedIndex = 0">
          <span class="shadow"></span>
          <span class="edge"></span>
          <span class="front text">返回</span>
        </button>
        <chart_skill :q_keyword="query_key" :q_type="query_type"></chart_skill>
      </div>
      <div v-if="chart_name === 'main'">
        <chart_all_key></chart_all_key>
      </div>
      <div class="charts-list" v-for="item in items" v-if=" chart_name === 'main'">
        <div>
          <h3 class="tech_type" :id="item">{{ item }}</h3>
          <div id="same-type-charts">
            <div id="chart" class="col-2 col-3 col-4" @click="chart_name='area';query_type='area';query_key=item">
              <div class="card" style="background: rgba(238, 102, 102);">
                地区
              </div>
            </div>
            <div id="chart" class="col-2 col-3 col-4" @click="chart_name='salary';query_type='salary';query_key=item">
              <div class="card" style="background: rgba(126, 211, 244);">
                薪资
              </div>
            </div>
            <div id="chart" class="col-2 col-3 col-4" @click="chart_name='degree';query_type='degree';query_key=item">
              <div class="card" style="background: rgba(250, 200, 88);">
                学历
              </div>
            </div>
            <div id="chart" class="col-2 col-3 col-4" @click="chart_name='exp';query_type='exp';query_key=item">
              <div class="card" style="background: rgba(92, 123, 217);">
                工作经验
              </div>
            </div>
            <div id="chart" class="col-2 col-3 col-4"
                 @click="chart_name='technique';query_type='technique';query_key=item">
              <div class="card" style="background: rgba(145, 204, 117);">
                相关技能
              </div>
            </div>
          </div>
        </div>
        <p class="split"></p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.loader {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

a {
  color: #484848;
}

.charts-page {
  position: absolute;
  left: 0;
  right: 0;
  top: 50px;
  bottom: 0;
  overflow-y: auto;
}

#left-container {
  position: sticky;
  left: 0;
  top: 0;
  float: left;
  height: calc(100%);
  width: 200px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  overscroll-behavior: contain;
}

@media (max-width: 768px) {
  #left-container {
    display: none;
  }
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

#left-container li a {
  height: 45px;
  padding: 10px 0 10px 40px;
  display: block;
  text-decoration: none;
  color: #6e7079;
}

#left-container li a.active {
  background-color: #da5454;
  color: #fff;
}

#same-type-charts {
  margin-right: -15px;
  margin-left: -15px;
  overflow: hidden;
}

#charts {
  margin-left: 220px;
  padding: 10px 10px;
}

@media (max-width: 768px) {
  #charts {
    margin-left: 0;
  }
}

button {
  position: relative;
  border: none;
  background: transparent;
  padding: 0;
  margin-bottom: 15px;
  cursor: pointer;
  outline-offset: 4px;
  transition: filter 250ms;
  user-select: none;
  touch-action: manipulation;
}

.shadow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  background: hsl(0deg 0% 0% / 0.25);
  will-change: transform;
  transform: translateY(2px);
  transition: transform 600ms cubic-bezier(.3, .7, .4, 1);
}

.edge {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  background: linear-gradient(
      to left,
      hsl(340deg 100% 16%) 0%,
      hsl(340deg 100% 32%) 8%,
      hsl(340deg 100% 32%) 92%,
      hsl(340deg 100% 16%) 100%
  );
}

.front {
  display: block;
  position: relative;
  padding: 12px 27px;
  border-radius: 12px;
  font-size: 1.1rem;
  color: white;
  background: hsl(345deg 100% 47%);
  will-change: transform;
  transform: translateY(-4px);
  transition: transform 600ms cubic-bezier(.3, .7, .4, 1);
}

button:hover {
  filter: brightness(110%);
}

button:hover .front {
  transform: translateY(-6px);
  transition: transform 250ms cubic-bezier(.3, .7, .4, 1.5);
}

button:active .front {
  transform: translateY(-2px);
  transition: transform 34ms;
}

button:hover .shadow {
  transform: translateY(4px);
  transition: transform 250ms cubic-bezier(.3, .7, .4, 1.5);
}

button:active .shadow {
  transform: translateY(1px);
  transition: transform 34ms;
}

button:focus:not(:focus-visible) {
  outline: none;
}

.charts-list {
  margin: 25px 15px 25px 15px;
}

.tech_type {
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e1e5f2;
  font-weight: normal;
  color: #010415;
  font-size: 30px;
}

#chart {
  position: relative;
  min-height: 1px;
  padding-right: 15px;
  padding-left: 15px;
}

@media (min-width: 768px) {
  #chart {
    float: left;
  }
}

@media (min-width: 768px) {
  .col-2 {
    width: 50%;
  }
}

@media (min-width: 992px) {
  .col-3 {
    width: 33.33333333%;
  }
}

@media (min-width: 1200px) {
  .col-4 {
    width: 25%;
  }
}

.card {
  box-sizing: border-box;
  margin-top: 10px;
  margin-bottom: 10px;
  width: 100%;
  height: 254px;
  border: 1px solid white;
  backdrop-filter: blur(6px);
  border-radius: 17px;
  text-align: center;
  cursor: pointer;
  transition: all 0.5s;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  font-weight: bolder;
  color: black;
  font-size: 20px;
}

.card:hover {
  border: 1px solid black;
  transform: scale(1.05);
  font-size: 40px;
}

.card:active {
  transform: scale(0.95) rotateZ(1.7deg);
  font-size: 40px;
}

</style>