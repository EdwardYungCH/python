# -*- coding: utf-8 -*-
"""第 4 堂「If…Else」。python3 tools/make_lesson4.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build

CH_HTML = r'''<!-- 1 If -->
<section class="card" id="s1" data-title="if：如果…就…" data-short="1 if">
  <header><div class="chapter">第 1 章</div><h2>if：如果條件成立，就做</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>寫 <code>if 條件:</code>，記得冒號和縮排</li><li>知道縮排的行才屬於 if</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">程式第一次會「揀路」</div>
    <p>到目前為止，程式每一行都會執行。<code>if</code> 讓程式<b>只在條件成立時</b>才執行某些行。條件就是上一堂的比較，答案是 <code>True</code> 或 <code>False</code>。</p>
    <pre class="ex">age = 15
if age &lt; 18:
    print("你是未成年人")   <span class="cm"># 縮排 4 格：屬於 if，條件成立才執行</span>
print("多謝使用")           <span class="cm"># 沒有縮排：不屬於 if，一定執行</span></pre>
    <ul class="steps-list">
      <li><code>if</code> 那一行結尾要有<b>冒號 <code>:</code></b>。</li>
      <li>屬於 if 的行要<b>縮排 4 格</b>（Thonny 會自動幫你縮）。可以有很多行。</li>
      <li>縮排結束，就是 if 結束。</li>
    </ul>
    <div class="key">第 1 堂說過縮排是語法的一部分，就是為了這一刻：縮排告訴 Python 哪些行屬於 <code>if</code>。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>if 條件:</code> 加冒號；縮排的行只在條件為 <code>True</code> 時執行。</div>
</section>

<!-- 2 Else / Elif -->
<section class="card" id="s2" data-title="else 與 elif：否則" data-short="2 elif">
  <header><div class="chapter">第 2 章</div><h2>else 與 elif：否則呢？</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>else</code> 處理「條件不成立」</li><li>用 <code>elif</code> 一次分三條或更多路</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">兩條路：if … else</div>
    <pre class="ex">age = 20
if age &lt; 18:
    print("兒童票")
else:
    print("成人票")      <span class="cm"># 條件不成立就走這邊</span></pre>
    <p><code>else</code> 不用寫條件，它就是「其餘情況」。<code>else</code> 和 <code>if</code> 要對齊，不縮排。</p>
    <div class="lead" style="margin-top:16px">三條或更多路：elif</div>
    <pre class="ex">score = 85
if score &gt;= 80:
    print("優")
elif score &gt;= 50:     <span class="cm"># elif = else if：上面不成立，再試這個</span>
    print("合格")
else:
    print("不合格")</pre>
    <p>Python 由上至下試，<b>第一個成立的就執行，之後的全部跳過</b>。所以 85 只會印「優」，雖然 85 也 ≥ 50。</p>
    <div class="key">次序很重要：如果先寫 <code>score &gt;= 50</code>，85 分就會被判為「合格」。由最嚴格（最大或最小）的條件開始寫。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>if</code> → <code>elif</code>（可多個）→ <code>else</code>；只走第一個成立的路。</div>
</section>

<!-- 3 Logical operators -->
<section class="card" id="s3" data-title="and、or、not" data-short="3 and/or">
  <header><div class="chapter">第 3 章</div><h2>and、or、not：把條件合起來</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>and</code>（都要）、<code>or</code>（其中一個）、<code>not</code>（相反）</li><li>看懂真假值表</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">兩個條件一起問</div>
    <pre class="ex">age = 15
if age &gt;= 12 and age &lt;= 17:      <span class="cm"># 兩個都要 True</span>
    print("青少年")
if age &lt; 12 or age &gt;= 65:        <span class="cm"># 其中一個 True 就可以</span>
    print("半價")
if not age &gt;= 18:                <span class="cm"># not 把 True 變 False、False 變 True</span>
    print("未成年")</pre>
    <div class="tablewrap"><table>
      <thead><tr><th>A</th><th>B</th><th><code>A and B</code></th><th><code>A or B</code></th><th><code>not A</code></th></tr></thead>
      <tbody>
        <tr><td>True</td><td>True</td><td>True</td><td>True</td><td>False</td></tr>
        <tr><td>True</td><td>False</td><td>False</td><td>True</td><td>False</td></tr>
        <tr><td>False</td><td>True</td><td>False</td><td>True</td><td>True</td></tr>
        <tr><td>False</td><td>False</td><td>False</td><td>False</td><td>True</td></tr>
      </tbody>
    </table></div>
    <p>記法：<code>and</code> 只有「兩個都 True」才 True；<code>or</code> 只有「兩個都 False」才 False。</p>
    <div class="key">常見錯誤：<code>if age == 12 or 13:</code> 不是「12 或 13」。要寫 <code>age == 12 or age == 13</code>，每邊都是完整的比較。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　<code>and</code> 都要、<code>or</code> 其一、<code>not</code> 相反；每邊都寫完整的比較。</div>
</section>

<!-- 4 Nested if -->
<section class="card" id="s4" data-title="巢狀 if：判斷裏面再判斷" data-short="4 巢狀">
  <header><div class="chapter">第 4 章</div><h2>巢狀 if：判斷裏面再判斷</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>在 if 裏面再放一個 if，縮排 8 格</li><li>知道甚麼時候用巢狀、甚麼時候用 and</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">一層一層問</div>
    <pre class="ex">age = 15
member = True
if age &lt; 18:
    print("兒童票")
    if member:                 <span class="cm"># 在 if 裏面再問：縮排 4 格</span>
        print("會員再九折")    <span class="cm"># 屬於裏面的 if：縮排 8 格</span>
else:
    print("成人票")</pre>
    <p>裏面的 <code>if</code> 只有在外面的條件成立時才會被問。看縮排就知道誰屬於誰。</p>
    <p>如果只是「兩個條件都要」，用 <code>and</code> 一行就夠；要在裏面<b>做不同的事</b>（例如先印兒童票，再決定折扣）才用巢狀。</p>
    <div class="key"><code>if member:</code> 不用寫 <code>== True</code>，因為 <code>member</code> 本身已經是 True 或 False。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　巢狀 if 每多一層多縮排 4 格；只是「都要」就用 <code>and</code>。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a'],c3:['c3_a','c3_b'],c4:['c4_a']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','哪些行屬於 if？','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'temp = 31\nif temp > 33:\n    print("酷熱警告")\n    print("多喝水")\nprint("今天氣溫", temp)',options:['酷熱警告\n多喝水\n今天氣溫 31','今天氣溫 31','多喝水\n今天氣溫 31','甚麼都不印'],answer:1,why:'31 > 33 是 False，兩行縮排的都跳過；最後一行沒有縮排，一定印。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'補上冒號和縮排，令分數 ≥ 50 時印出「合格」，然後印出「完」。（分數 60 時兩行都印）',code:'score = 60\nif score >= 50\nprint("合格")\nprint("完")',expect:'合格\n完\n',answer:'score = 60\nif score >= 50:\n    print("合格")\nprint("完")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。if 那行結尾要有冒號，下一行要縮排。'};if(res.out!=='合格\n完\n')return {ok:false,msg:'應印出「合格」和「完」兩行。'};if(!/^\s+print\("合格"\)/m.test(code))return {ok:false,msg:'輸出對了，但 print("合格") 要縮排才屬於 if。'};if(/^\s+print\("完"\)/m.test(code))return {ok:false,msg:'print("完") 不屬於 if，不要縮排。'};return {ok:true,msg:'正確。'};},
    hints:['if score >= 50 後面加冒號 :。','print("合格") 前面加 4 個空格。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t=step(h,'try','次序錯了會怎樣？','估對 4 分');
  makePredict(t,{id:'c2_a',q:'這個程式會印出甚麼？',code:'score = 85\nif score >= 50:\n    print("合格")\nelif score >= 80:\n    print("優")\nelse:\n    print("不合格")',options:['優','合格','合格\n優','不合格'],answer:1,why:'85 ≥ 50 已經成立，印「合格」後就跳過其餘的 elif 和 else，所以永遠不會印「優」。條件要由最嚴格的開始寫。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上缺少的關鍵字，令程式按氣溫分三路：≥ 28 印「熱」、≥ 18 印「舒適」、其餘印「冷」。（氣溫 22 時印 舒適）',code:'temp = 22\n____ temp >= 28:\n    print("熱")\n____ temp >= 18:\n    print("舒適")\n____:\n    print("冷")',expect:'舒適\n',answer:'temp = 22\nif temp >= 28:\n    print("熱")\nelif temp >= 18:\n    print("舒適")\nelse:\n    print("冷")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.out!=='舒適\n')return {ok:false,msg:'氣溫 22 時應只印「舒適」。'};if(!/^elif /m.test(code)||!/^else:/m.test(code))return {ok:false,msg:'輸出對了，但要用 if、elif、else 三個關鍵字。'};return {ok:true,msg:'正確。'};},
    hints:['第一路用 if。','中間的路用 elif（有條件）。','最後一路用 else（沒有條件，只有冒號）。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t1=step(h,'try','and 和 or','估對 4 分');
  makePredict(t1,{id:'c3_a',q:'這個程式會印出甚麼？',code:'a = 5\nb = 10\nprint(a > 3 and b > 20)\nprint(a > 3 or b > 20)\nprint(not a > 3)',options:['True\nTrue\nFalse','False\nTrue\nFalse','False\nFalse\nTrue','True\nFalse\nFalse'],answer:1,why:'a > 3 是 True、b > 20 是 False：and 要兩個都 True → False；or 一個 True 就夠 → True；not True → False。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','常見陷阱','估對 4 分');
  makePredict(t2,{id:'c3_b',q:'這個程式會印出甚麼？',code:'day = "星期三"\nif day == "星期六" or day == "星期日":\n    print("假期")\nelse:\n    print("返學")',options:['假期','返學','假期\n返學','出錯'],answer:1,why:'兩邊都是完整的比較，星期三兩邊都 False，or 之後是 False，走 else。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上 and 或 or：年齡 12 至 17 歲（包括兩端）印「青少年票」，否則印「普通票」。（15 歲時印 青少年票）',code:'age = 15\nif age >= 12 ____ age <= 17:\n    print("青少年票")\nelse:\n    print("普通票")',expect:'青少年票\n',answer:'age = 15\nif age >= 12 and age <= 17:\n    print("青少年票")\nelse:\n    print("普通票")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.out!=='青少年票\n')return {ok:false,msg:'15 歲時應印「青少年票」。'};if(!/ and /.test(code))return {ok:false,msg:'輸出對了，但「12 至 17」兩個條件都要成立，用 and；用 or 的話 5 歲也會變青少年。'};return {ok:true,msg:'正確。'};},
    hints:['≥ 12 和 ≤ 17 兩個條件都要成立。','都要成立是 and。']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t=step(h,'try','裏面的 if 會被問嗎？','估對 4 分');
  makePredict(t,{id:'c4_a',q:'這個程式會印出甚麼？',code:'age = 20\nmember = True\nif age < 18:\n    print("兒童票")\n    if member:\n        print("會員九折")\nelse:\n    print("成人票")',options:['兒童票\n會員九折','成人票\n會員九折','成人票','會員九折'],answer:2,why:'20 < 18 是 False，整個 if 區塊（包括裏面的 if）都跳過，只走 else。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'補上正確的縮排：下雨時印「帶傘」；下雨而且風大時再印「小心」；不下雨印「好天」。（下雨＋風大時印兩行）',code:'raining = True\nwindy = True\nif raining:\nprint("帶傘")\nif windy:\nprint("小心")\nelse:\nprint("好天")',expect:'帶傘\n小心\n',answer:'raining = True\nwindy = True\nif raining:\n    print("帶傘")\n    if windy:\n        print("小心")\nelse:\n    print("好天")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。if 下面的行要縮排。'};if(res.out!=='帶傘\n小心\n')return {ok:false,msg:'應印出「帶傘」和「小心」。注意裏面的 if 要縮排 4 格，它的 print 縮排 8 格。'};if(!/^    if windy:/m.test(code)||!/^        print\("小心"\)/m.test(code))return {ok:false,msg:'輸出對了，但 if windy: 要縮排 4 格，print("小心") 要縮排 8 格。'};return {ok:true,msg:'正確。'};},
    hints:['print("帶傘") 和 if windy: 都屬於外面的 if，縮排 4 格。','print("小心") 屬於裏面的 if，縮排 8 格。','else 和最外面的 if 對齊，它的 print 縮排 4 格。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'戲院票價計算器',
   desc:'問年齡，然後印出票價：12 歲以下「兒童票 40 元」、65 歲或以上「長者票 40 元」、其餘「成人票 80 元」。用 <code>if</code>、<code>elif</code>、<code>else</code>。',
   hints:['age = int(input("你幾歲？"))','if age < 12: … elif age >= 65: … else: …','每一路一個 print。'],inputs:['10'],
   check:async(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};const cases=[['10','兒童'],['30','成人'],['70','長者'],['65','長者'],['12','成人']];
     for(const [inp,want] of cases){const r=await runSilent(code,[inp]);if(r.err)return {ok:false,msg:`輸入 ${inp} 時出錯：${r.err.split('\n').pop()}`};if(!r.out.includes(want))return {ok:false,msg:`輸入 ${inp} 歲時應印「${want}票」，現在印了：${r.out.trim().split('\n').pop()}`};}
     if(!/elif/.test(code))return {ok:false,msg:'要用 elif 分三路。'};return {ok:true,msg:'五組測試（10、30、70、65、12 歲）全部正確。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'BMI 分類',
   desc:'問 BMI（小數），印出分類：18.5 以下「過輕」、18.5 至 22.9「正常」、23 至 24.9「過重」、25 或以上「肥胖」（香港衞生署的亞洲成人標準）。',
   hints:['bmi = float(input("BMI："))','由最小的開始：if bmi < 18.5: … elif bmi < 23: … elif bmi < 25: … else: …'],inputs:['20'],
   check:async(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};const cases=[['17','過輕'],['20','正常'],['22.9','正常'],['23','過重'],['24','過重'],['27','肥胖']];
     for(const [inp,want] of cases){const r=await runSilent(code,[inp]);if(r.err)return {ok:false,msg:`輸入 ${inp} 時出錯。`};if(!r.out.includes(want))return {ok:false,msg:`BMI ${inp} 應是「${want}」，現在印了：${r.out.trim().split('\n').pop()}`};}
     return {ok:true,msg:'六組測試全部正確。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'閏年判斷',
   desc:'問年份，判斷是否閏年：能被 4 整除而不能被 100 整除，或者能被 400 整除，就是閏年。印出「閏年」或「不是閏年」。',
   hints:['能被 4 整除：year % 4 == 0。','條件：(year % 4 == 0 and year % 100 != 0) or year % 400 == 0'],inputs:['2024'],
   check:async(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};const cases=[['2024',true],['2023',false],['1900',false],['2000',true]];
     for(const [inp,leap] of cases){const r=await runSilent(code,[inp]);if(r.err)return {ok:false,msg:`輸入 ${inp} 時出錯。`};const last=r.out.trim().split('\n').pop();const says=/不是/.test(last)?false:/閏年/.test(last);if(says!==leap)return {ok:false,msg:`${inp} 年${leap?'是':'不是'}閏年，現在印了：${last}`};}
     return {ok:true,msg:'2024、2023、1900、2000 全部判斷正確。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'x = 7\nif x > 5:\n    print("大")\nprint("完")',options:['大','大\n完','完','甚麼都不印'],answer:1,why:'7 > 5 成立印「大」；「完」沒有縮排，一定印。'},
  {id:'q2',q:'印出甚麼？',code:'n = 50\nif n > 100:\n    print("A")\nelif n > 40:\n    print("B")\nelif n > 20:\n    print("C")\nelse:\n    print("D")',options:['B','B\nC','C','D'],answer:0,why:'由上試落：n > 100 不成立，n > 40 成立印 B，之後全部跳過。'},
  {id:'q3',q:'印出甚麼？',code:'a = 3\nprint(a > 1 and a > 5)\nprint(a > 1 or a > 5)',options:['True\nTrue','False\nTrue','True\nFalse','False\nFalse'],answer:1,why:'a > 5 是 False：and 要兩個都 True → False；or 有一個 True → True。'},
];
'''

build(4, 'If…Else', '四章：if、else 與 elif、and／or／not、巢狀 if。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：if、elif／else、and／or／not、巢狀 if，每章都是「學 → 試 → 練」三步，然後做戲院票價計算器和小測。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:9,3:13,4:9}',
      "['第 1 章 if',sc.c[1],9],['第 2 章 else 與 elif',sc.c[2],9],['第 3 章 and、or、not',sc.c[3],13],['第 4 章 巢狀 if',sc.c[4],9],",
      "[['c1_a','B 今天氣溫 31'],['c2_a','B 合格'],['c3_a','B False / True / False'],['c3_b','B 返學'],['c4_a','C 成人票']]",
      """[['練習 1','if score >= 50: 加冒號，print("合格") 縮排'],['練習 2','if、elif、else'],['練習 3','and'],['練習 4','if windy: 縮排 4 格，print("小心") 縮排 8 格']]""",
      '<a href="https://www.w3schools.com/python/python_conditions.asp" target="_blank" rel="noopener">If…Else</a>',
      '例如：我忘記了冒號，Shell 出現 SyntaxError 我才發現……', '戲院票價計算器')
