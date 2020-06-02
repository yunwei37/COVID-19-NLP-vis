<script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/world.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts-wordcloud.min.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/china.js"></script>

## 疫情数据可视化交互分析看板

---
### 疫情态势数据可视化看板：

<div>
    <div id="current-maps" style="border: 20px;border-color: black;">
        <div>
            <label>请选择地图类型:     </label>
            <select name="select-map" id="mapselecter">
                <option value="0" >现存确诊人数</option>
                <option value="1" >累计死亡人数</option>
                <option value="2" >死亡率（死亡/确诊）</option>
            </select>
        </div>
        <div>
            <label>拖动滑块即可切换日期:</label>
            <input id='slider' style="width: 400px;vertical-align: middle;" type='range' min='0' max='121' step='1'/>
        </div>
        <div id="worldMap" class="maps" style="width:500px; height:500px;display: inline-block;"></div>
        <div id="chinaMap" class="maps" style="width:500px; height:500px;display: inline-block;"></div>
    </div>  
    <div>
        <label>请选择国家：    </label>
        <select id="selectCountrys">
        {% for cate in cates %}
            <option value="{{cate}}" >{{cate}}</option>
        {% endfor %}
        </select>
        <div id="lines" style="width:500px; height:300px;display: inline-block;"></div>
        <div id="04cd225d9bb642288bef9788ed998f30" class="chart-container" style="width:500px; height:300px;display: inline-block;"></div>
        <script type="text/javascript" src="{{ url_for('static',filename='calendar.js') }}"></script>
    </div>
</div>

---
### 疫情舆情分析可视化：



<script type="text/javascript" src="{{ url_for('static',filename='render.js') }}"></script>
