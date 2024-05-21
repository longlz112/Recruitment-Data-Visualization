<script>
import axios from "axios";
import * as echarts from 'echarts';
import loader from '@/components/loader.vue'
import api from "@/api/api.js";

export default {
  data() {
    return {
      responseData: [],
      is_loading:true
    };
  },
  mounted() {
    //this.sendDataToServer();
    this.initBarChart()
  },
  methods:{
    initBarChart() {
      this.barChart = echarts.init(document.getElementById('myecharts'));
      axios({
        method: 'post',
        url: api.basePath+api.get_data,
        data: {
          keyword: this.q_keyword,
          type: this.q_type
        }
      }).then(res => {
        // 返回请求到的数据
        const res_data = res.data
        this.is_loading = false
        const option = {
          title: {
            text: this.q_keyword+'相关技能统计'
          },
          xAxis: {
            type: 'value'
          },
          yAxis: {
            axisLabel:{
              interval: 0,//Y轴信息全部展示
            },
            type: 'category',
            data:  Object.values(res_data.skill),
            inverse: true//从高到低排列
          },
          series: [{
            data:  Object.values(res_data.count),
            emphasis: {
              label: {
                show: true,
                fontSize: 20,
                fontWeight: 'bold'
              }
            },
            type: 'bar',
            label: {
              position:'center',
              formatter: '{b} : {c}'
            },
          }]
        };

        this.barChart.setOption(option);
      }).catch(err => {
        // 返回错误信息
        console.log('出现错误：')
        if (err.response.status === 500)
            window.alert("500\n网络异常，请稍后再试");
        this.is_loading = false
        console.log(err)
      })
    },
  },
  components:{
    loader
  },
  props:["q_keyword","q_type"]
}


</script>

<template>
  <div v-if="is_loading" class="loader">
    <loader></loader>
  </div>
  <div id="myecharts" :style="{width: '100%', height: '70vh'}"></div>
</template>

<style scoped>
.loader {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>