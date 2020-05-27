<script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/world.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts-wordcloud.min.js"></script>
<script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/china.js"></script>

<div id="links" style="line-height: 36px; background-color: rgb(84, 105, 104);">
    <a href="/" style="display: inline-block; text-align: center" >数据分析与可视化</a>
    <a href="/document" style="display: inline-block; text-align: center" >技术文档</a>
</div>


# 疫情空间数据与舆情数据分析可视化

新型冠状病毒肺炎（COVID-19，简称“新冠肺炎”）疫情肆虐全球多个国家，2020年3月11日，世界卫生组织 (WHO) 正式宣布将新冠肺炎列为全球性大流行病。

在全球抗击新型冠状病毒疫情的过程中，产生了前所未有的大规模疫情数据，利用大数据分析技术和方法能够协助发现病毒传染源、监测疫情发展、调配救援物资，从而更好地进行疫情防控工作。空间数据分析作为大数据分析的重要组成，将数据智能处理、直观展示和交互分析有机地结合，使机器智能和人类智慧深度融合、优势互补，为疫情防控中的分析、指挥和决策提供有效依据和指南。

本项目希望能利用交互式空间数据分析技术，预测疫情发展趋势与关键节点、分析社交媒体话题与情感的动态演变、对社会舆情进行态势感知。

## 所使用的数据集：

- 疫情统计时空数据，分为国内各省市疫情统计数据及世界各国疫情统计数据，包括从1.19至5.19四个月时间的确诊人数、现存确诊人数、治愈人数、死亡人数等
- 中国社会组织公共服务平台疫情防控专区新闻1400+篇，包含时间、标题、正文内容、作者等
- 依据与“新冠肺炎”相关的230个主题关键词进行数据采集的2020年1月1日—2020年2月20日期间共计100万条微博数据

部分数据经爬虫采集，部分数据采用公开数据集；

## Part 1：疫情空间数据数据可视化及趋势分析：

### 疫情数据动态交互可视化地图

共有三种地图类型：现存确诊率地图、累计死亡人数地图、死亡率（累计死亡人数/累计确诊人数）地图，可以通过下拉框进行选择；

可以拖动时间轴上的滑块改变地图显示日期，范围为 1.19-5.19；

<div id="current-maps" >
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

通过交互分析可以发现：

- 现存确诊人数
  - 在1.20日左右，全国公布的疫情一开始出现在广东、湖北、北京上海等地，此时湖北的疫情确诊人数已经突破200；
  - 此后，疫情从湖北开始向四周身份成扩散趋势，在1.26日湖北的确诊人数已经突破1000；除湖北外，浙江与广东确诊人数也到达三位数；国外在美国、澳大利亚、法国和泰国等东南亚国家也出现确诊病例；
  - 在2.2日前后，湖北的确诊人数突破五位数，其他地区疫情人数继续增加；国外疫情也在欧洲、东南亚、美洲呈缓慢扩散趋势
  - 在2月中旬，西藏成为国内首个清零的省份；国外继续缓慢增长；国内疫情迎来拐点，现存确诊人数趋于平缓、不再增加，并开始缓慢减少；现存确诊人数约为50000左右，其中大部分集中在湖北；
  - 二月底三月初，国内确诊人数逐渐减少，国外此时开始大规模出现感染并扩散到多个国家；此时意大利、伊朗疫情较为严重；疫情开始扩散到非洲、南美洲；
  - 三月中旬后，国内疫情已经基本得到控制，大多省份恢复到个位数或清零，绝大多数现存确诊病例集中在湖北；而世界上大部分国家都已出现确诊报告，许多国家突破五位数确诊；其中欧洲和伊朗、美国较为严重；
  - 四月初，国内确诊人数继续减少，但有部分省份出现略微反扑；国外疫情几乎已经扩散到世界所有国家，其中美国确诊人数已经突破20万，是世界最严重的地区；
  - 从四月中旬开始，由于外来输入原因，国内黑龙江及东北地区出现了一次比较严重的疫情反扑，确诊人数接近500，但在五月初逐步得到控制；
  - 国外疫情在四五月份继续趋向严重，在5.8美国的确诊人数突破百万；但部分早期疫情严重的国家由于采取了有效的控制手段导致疫情缓解；
  
- 累计死亡人数
  - 二月初，世界各国开始出现死亡病例；
  - 国内的死亡病例数在二月中旬趋向平缓；
  - 在三月中旬，世界各国死亡病例陆续出现或开始明显增多；
  - 在五月份，报告的死亡数以美国、欧洲最为严重，许多国家死亡人数已经远远超过了中国；

- 死亡率：
  - 死亡率也可以反应出疫情的控制程度，死亡率越低表明患者得到救治的概率越大；
  - 在医疗资源充足的地区，死亡率可以降低到1%左右；医疗资源不足的地区，死亡率可以高达10%；
  - 国内死亡率数据分析：
    - 在一月下旬，中国的死亡率以黑龙江、湖北、湖南河南较为严重，但在一月底二月初除湖北外，其他省份呈下降趋势；
    - 在国内疫情确诊人数峰值的二月中旬，国内平均死亡率为2.5，死亡率相对较高的是湖北、黑龙江、海南、台湾等地；
    - 此后，国内湖北的死亡率继续升高，可能是由于医疗资源不足，无法给予患者有效救治，同时此前积累的确诊患者也陆续出现死亡；同样升高的有新疆、黑龙江；
    - 三月中旬后，在国内疫情基本得到控制的情况下，全国平均死亡率在4%，湖北死亡率达到4.7左右；
    - 在四月中旬补统计了一下之前因为新冠去世但未计入死亡率数据的死亡人数，最后湖北的死亡率为6.6，国内平均死亡率在5.5
  - 国外死亡率数据分析：
    - 从三月下旬开始，伴随着疫情的大规模扩散，各国疫情死亡率也逐步增高；
    - 值得注意的是，许多国家的统计数据表明在其疫情刚开始出现的数日内死亡率是一个高峰，可能表明了在初始阶段未能对患者作出良好的检测和发现，只能从新冠重症患者处得到资料；
    - 虽然非洲等某些不发达国家的疫情报告数据较少，但死亡率较高；可能表明了对于新冠的轻症患者，并没有良好的检测能力；
    - 死亡率较高的国家显著集中在欧洲地区，表明了医疗资源的相对短缺；墨西哥的死亡率也较高；

总体来看：
- 中国在三月份就逐步控制住了疫情趋势，为世界抗疫事业做出了卓越的典范；
- 欧洲和美洲等发达国家疫情数据较为严重，可能是发达国家在世界范围内流动的人口较大，但更可能是发达国家能得到有效的检测并报告病例；

### 世界疫情数据曲线图

通过曲线图可直观地表现出确诊数据、死亡数据、治愈数据等的变化趋势，可以通过下拉框进行选择所显示的国家：

<div>
    <label>请选择国家：    </label>
    <select id="selectCountrys">
    {% for cate in cates %}
        <option value="{{cate}}" >{{cate}}</option>
    {% endfor %}
    </select>
    <div id="lines" style="width:1000px; height:600px;"></div>
</div>

通过交互分析，可以将疫情数据趋势分为几种类别：

- 疫情已经得到控制，如中国：
- 疫情数据还在保持增长趋势，如美国、俄罗斯；
- 疫情基本得到控制，现存确诊数在逐步减少，如意大利；
- 数据太少，如多米尼克；

同时也可以发现：

- 由于检测技术或标准变化，可能出现确诊数据在短时间内的大量增多，也有的国家是每隔一段时间集中增加一次确诊数据；
- 截止5.20，大多数国家的疫情还在上升趋势；

### 疫情趋势预测分析

- logistic回归算法

## part 2: 疫情舆情数据分析与可视化

### 新闻数据分析与可视化

#### 中国社会组织公共服务平台疫情防控专区新闻词云可视化(全部文章)：



<div>
    <div id="c61d88ede2df46799724e4ef261fa76f" class="chart-container" style="width:900px; height:500px;"></div>
    <script type="text/javascript" src="{{ url_for('static',filename='wordcloud.js') }}"></script>
</div>

#### 部分新闻词云图：

可通过拖动滑块改变日期范围，每个日期范围内有约100篇新闻；

<div>
    <div>
        <label>拖动滑块即可切换日期:</label>
        <input id='sliderWord' style="width: 400px;vertical-align: middle;" type='range' min='0' max='90' step='1'/>
    </div>
    <div id="wordcloud" style="width:1000px; height:600px;"></div>
</div>

### TF-IDF

<img src="{{ url_for('static',filename='results/tfidf.png') }}" style="width:1000px; height:600px;">

# 层次聚类分析

<img src="{{ url_for('static',filename='results/tree_word_50.png') }}" style="width:1000px;">

### 微博舆情分析与数据可视化




<script type="text/javascript" src="{{ url_for('static',filename='render.js') }}"></script>