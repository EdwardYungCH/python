# -*- coding: utf-8 -*-
"""第 9 堂「函數入門與除錯」。python3 tools/make_lesson9.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build, ROOT

CH_HTML = r'''<!-- 1 def -->
<section class="card" id="s1" data-title="函數：把一段程式包起來" data-short="1 函數">
  <header><div class="chapter">第 1 章</div><h2>函數：把一段程式包起來，改個名，隨時叫</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>def</code> 定義函數，用名字呼叫它</li><li>用參數把資料交給函數</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">定義一次，用很多次</div>
    <p>你早已用過函數：<code>print()</code>、<code>len()</code>、<code>input()</code> 都是別人寫好的函數。現在自己寫一個。</p>
    <pre class="ex">def greet():            <span class="cm"># def 定義函數，名字叫 greet，括號後要有冒號</span>
    print("你好！")      <span class="cm"># 縮排的行是函數的內容（這時不會執行）</span>
    print("歡迎來到中三")

greet()                 <span class="cm"># 呼叫：這時才執行裏面的兩行</span>
greet()                 <span class="cm"># 再呼叫一次，又印兩行</span></pre>
    <p>函數可以有<b>參數</b>：括號裏的變量，呼叫時把值交進去。</p>
    <pre class="ex">def greet(name):        <span class="cm"># name 是參數</span>
    print("你好，" + name + "！")

greet("小明")           <span class="cm"># name 變成 "小明"</span>
greet("小芳")           <span class="cm"># name 變成 "小芳"</span></pre>
    <div class="key">定義只是「教」電腦這個函數做甚麼，<b>不會執行</b>；要寫 <code>greet()</code> 呼叫才會執行。定義要放在呼叫之前。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>def 名字(參數):</code> 定義；<code>名字(值)</code> 呼叫；參數在函數裏當變量用。</div>
</section>

<!-- 2 return -->
<section class="card" id="s2" data-title="return：把結果交回來" data-short="2 return">
  <header><div class="chapter">第 2 章</div><h2>return：把結果交回來</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>return</code> 讓函數交回一個值</li><li>分辨「印出來」和「交回來」</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">交回來的值可以存起來再用</div>
    <pre class="ex">def area(w, h):         <span class="cm"># 兩個參數</span>
    return w * h        <span class="cm"># 計完交回結果，函數就結束</span>

a = area(3, 4)          <span class="cm"># a = 12：把交回的值存起來</span>
print(a)
print(area(5, 2) + 1)   <span class="cm"># 11：交回的值可以直接計算</span></pre>
    <p>只用 <code>print</code> 的函數，結果印在螢幕就沒有了；用 <code>return</code> 的函數，結果可以存入變量、再計算、再交給另一個函數。</p>
    <pre class="ex">def is_pass(score):     <span class="cm"># 交回 True 或 False 的函數</span>
    return score >= 50

if is_pass(63):
    print("合格")</pre>
    <div class="key"><code>return</code> 一執行，函數立即結束，後面的行不會跑。沒有 <code>return</code> 的函數交回 <code>None</code>。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>return 值</code> 交回結果並結束函數；<code>x = f(…)</code> 把結果存起來。</div>
</section>

<!-- 3 三類錯誤 -->
<section class="card" id="s3" data-title="三類錯誤" data-short="3 錯誤">
  <header><div class="chapter">第 3 章</div><h2>三類錯誤：語法、運行、邏輯</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>分辨語法錯誤、運行錯誤、邏輯錯誤</li><li>知道每一類怎樣找出來</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">最難找的是沒有紅字的那種</div>
    <div class="tablewrap"><table>
      <thead><tr><th>類別</th><th>甚麼時候發現</th><th>例子</th><th>怎樣找</th></tr></thead>
      <tbody>
        <tr><td><b>語法錯誤</b><br>SyntaxError、IndentationError</td><td>程式<b>開始前</b>，Python 讀不懂</td><td>漏冒號、引號不成對、縮排錯</td><td>看紅字的行號，檢查那一行的符號</td></tr>
        <tr><td><b>運行錯誤</b><br>NameError、TypeError、ValueError、ZeroDivisionError、IndexError</td><td>程式<b>執行到那一行時</b>才出錯，之前的行已執行</td><td>變量名打錯、<code>int("abc")</code>、除以 0、索引超出</td><td>看 Traceback 最後一行的名稱和行號；用測試數據找出哪種輸入會出錯</td></tr>
        <tr><td><b>邏輯錯誤</b><br>沒有紅字</td><td>程式<b>跑完了</b>，但答案不對</td><td><code>&gt;</code> 寫成 <code>&gt;=</code>、range 終點少 1、print 縮排錯放進迴圈</td><td>用已知答案的測試數據對一對；用「逐步執行」看變量每一步的變化</td></tr>
      </tbody>
    </table></div>
    <pre class="ex"><span class="cm"># 這個程式想計 1 至 10 的總和，沒有紅字，但答案是 45：邏輯錯誤</span>
total = 0
for i in range(1, 10):   <span class="cm"># 終點應是 11</span>
    total += i
print(total)</pre>
    <div class="key">測試數據要有三種：<b>正常</b>（例如 60 分）、<b>邊界</b>（剛好 50 分、0 分、100 分）、<b>錯誤</b>（-5、abc）。邊界最容易暴露邏輯錯誤。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　語法錯誤：開始前；運行錯誤：執行到才出；邏輯錯誤：沒有紅字但答案錯，用測試數據和逐步執行找。</div>
</section>

<!-- 4 逐步執行 -->
<section class="card" id="s4" data-title="逐步執行" data-short="4 逐步">
  <header><div class="chapter">第 4 章</div><h2>逐步執行：一行一行看變量怎樣變</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 🐞 逐步執行，每按一下「下一步」執行一行</li><li>看 Variables 視窗找出邏輯錯誤發生在哪一行</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">黃色是「準備執行」的那一行，右邊變量變了會標黃</div>
    <ol class="steps-list">
      <li>按工具列的 <b>🐞 逐步執行</b>。第 1 行會變黃，表示「準備執行它」。</li>
      <li>按 <b>下一步 ▶</b>：執行黃色那一行，黃色移到下一行，Variables 顯示新的值，變了的會標黃。</li>
      <li>迴圈裏的行會重複變黃，每圈一次。<code>input()</code> 會在 Shell 等你輸入。</li>
      <li>按 <b>■ 停止</b> 可以隨時離開。</li>
    </ol>
    <p>試試下面這個程式：它想找最大值，但答案錯了。逐步執行，看 <code>biggest</code> 甚麼時候應該變但沒有變。</p>
    <div id="demo4"></div>
    <div class="key">邏輯錯誤的找法：先在紙上寫下你<b>預期</b>每一步變量應是甚麼，再逐步執行對照；第一個不同的地方就是錯處。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　逐步執行＝一行一行看；預期值和實際值第一次不同的那行就是錯處。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a','c2_b'],c3:['c3_a'],c4:['c4_a']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','定義不執行，呼叫才執行','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出幾行？',code:'def hello(name):\n    print("你好，" + name)\n\nprint("開始")\nhello("Amy")\nhello("Ben")\nprint("完")',options:['2 行','3 行','4 行','5 行'],answer:2,why:'開始、你好，Amy、你好，Ben、完：定義本身不印，兩次呼叫各印一行。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上缺少的部分：定義一個函數 line(n)，印出 n 個 =；然後呼叫它印 5 個和 10 個。',code:'____ line(n):\n    print("=" * n)\n\nline(____)\nline(____)',expect:'=====\n==========\n',answer:'def line(n):\n    print("=" * n)\n\nline(5)\nline(10)',
    hints:['定義函數的關鍵字是 def。','呼叫時把數字放進括號：line(5)。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t1=step(h,'try','return 之後的行','估對 4 分');
  makePredict(t1,{id:'c2_a',q:'這個程式會印出甚麼？',code:'def double(x):\n    return x * 2\n    print("這行會印嗎？")\n\nprint(double(4))',options:['8','8\n這行會印嗎？','這行會印嗎？\n8','出錯'],answer:0,why:'return 一執行函數就結束，後面的 print 永遠不會跑。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','印出來 vs 交回來','估對 4 分');
  makePredict(t2,{id:'c2_b',q:'這個程式會印出甚麼？',code:'def add(a, b):\n    print(a + b)\n\nx = add(2, 3)\nprint(x)',options:['5\n5','5\nNone','5','None'],answer:1,why:'add 只印 5，沒有 return，交回的是 None，所以 x 是 None。要用結果就要 return。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上缺少的部分：函數 bmi(w, h) 交回體重 ÷ 身高²，保留一位小數；然後印出 bmi(50, 1.6)。',code:'def bmi(w, h):\n    ____ round(w / (h * h), 1)\n\nprint(____(50, 1.6))',expect:'19.5\n',answer:'def bmi(w, h):\n    return round(w / (h * h), 1)\n\nprint(bmi(50, 1.6))',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(!/return\s+round/.test(code))return {ok:false,msg:'函數要用 return 交回結果。'};if(res.out!=='19.5\n')return {ok:false,msg:'應印出 19.5。'};return {ok:true,msg:'正確。'};},
    hints:['交回結果用 return。','呼叫函數就是寫它的名字加括號：bmi(50, 1.6)。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t=step(h,'try','是哪一類錯誤？','估對 4 分');
  makePredict(t,{id:'c3_a',q:'這個程式想印合格（50 分或以上）人數，應是 2，執行後卻印出 3，沒有紅字。這是哪一類錯誤？',code:'scores = [50, 49, 80]\nn = 0\nfor s in scores:\n    if s >= 49:\n        n += 1\nprint(n)',options:['語法錯誤','運行錯誤','邏輯錯誤','沒有錯誤'],answer:2,why:'程式跑完、沒有紅字，但答案錯：條件寫成 >= 49，49 分也被當合格。這就是邏輯錯誤，只有用測試數據對答案才找得到。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'這個程式有一個邏輯錯誤：它想印 1 至 5 的乘積（120），卻印出 0。改好它。',code:'p = 0\nfor i in range(1, 6):\n    p *= i\nprint(p)',expect:'120\n',answer:'p = 1\nfor i in range(1, 6):\n    p *= i\nprint(p)',
    hints:['沒有紅字，所以是邏輯錯誤；用逐步執行看 p 每一步的值。','乘法的初值應是 1，不是 0。']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  makeThonny($('#demo4'),{id:'demo4',code:'scores = [60, 95, 70]\nbiggest = scores[0]\nfor s in scores:\n    if s > biggest:\n        biggest = biggest\nprint(biggest)',label:'按 🐞 逐步執行，看 biggest',debug:true});
  const t=step(h,'try','逐步執行後再答','估對 4 分');
  makePredict(t,{id:'c4_a',q:'上面的程式印出 60 而不是 95。錯在第幾行？',code:'1 scores = [60, 95, 70]\n2 biggest = scores[0]\n3 for s in scores:\n4     if s > biggest:\n5         biggest = biggest\n6 print(biggest)',options:['第 2 行','第 4 行','第 5 行','第 6 行'],answer:2,why:'第 5 行應是 biggest = s，把更大的 s 存入；寫成 biggest = biggest 等於沒有改。逐步執行時會見到第 5 行執行後 biggest 沒有變。'},S.pred,PRED_PTS,null,true);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'這個程式想數 1 至 10 之中有幾多個偶數（應是 5），但印出 10。用逐步執行找出錯處並改好。',code:'count = 0\nfor i in range(1, 11):\n    if i % 2 == 0:\n        count += 1\n    count += 1\nprint(count)',expect:'5\n',answer:'count = 0\nfor i in range(1, 11):\n    if i % 2 == 0:\n        count += 1\nprint(count)',debug:true,
    hints:['逐步執行，看 count 在哪一行多加了。','第 5 行多了一個 count += 1，刪去它。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'捉蟲比賽：修正三個程式',debug:true,
   desc:'下面三段程式各有<b>一個</b>錯誤（一個語法錯誤、一個運行錯誤、一個邏輯錯誤）。把三段都修好，令輸入 <code>80</code> 時依次印出 <code>合格</code>、<code>你輸入了 80</code>、<code>平均 60.0</code>。用「逐步執行」幫你找第三段。',
   hints:['第一段：看紅字的行號，if 後面漏了甚麼？','第二段：input 交回的是文字，要 int() 才可以比較。','第三段：平均 = 總和 ÷ 項數；用逐步執行看 total 最後是幾多。'],inputs:['80'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'仍有錯誤：'+res.err.split('\n').pop()};const o=res.out;if(!/合格/.test(o))return {ok:false,msg:'第一段應印「合格」。'};if(!/你輸入了 80/.test(o))return {ok:false,msg:'第二段應印「你輸入了 80」。'};if(!/平均 60\.0/.test(o))return {ok:false,msg:'第三段應印「平均 60.0」（50、60、70 的平均）。檢查 total 的初值和除數。'};return {ok:true,msg:'三個蟲都捉到了。'};},
   code:'# 第一段：語法錯誤\nscore = 80\nif score >= 50\n    print("合格")\n\n# 第二段：運行錯誤\nn = input("數字：")\nif n > 50:\n    print("你輸入了", n)\n\n# 第三段：邏輯錯誤\nscores = [50, 60, 70]\ntotal = 0\nfor s in scores:\n    total = s\nprint("平均", total / len(scores))'},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'把成績查詢器拆成函數',debug:true,
   desc:'寫兩個函數：<code>average(scores)</code> 交回平均（保留一位小數）、<code>biggest(scores)</code> 交回最大值（自己用迴圈找，不可用 max）。然後問 5 個分數放進列表，印出 <code>平均 71.4</code> 和 <code>最高 92</code>。',
   hints:['def average(scores): total = 0 … return round(total / len(scores), 1)','def biggest(scores): b = scores[0] … return b','主程式：scores = []，問 5 次 append，再 print("平均", average(scores))。'],inputs:['80','65','92','47','73'],
   check:(code,res)=>{if(/\bmax\(|\bsum\(/.test(code))return {ok:false,msg:'不可以用 max() 或 sum()。'};if(!/def\s+average\s*\(/.test(code)||!/def\s+biggest\s*\(/.test(code))return {ok:false,msg:'要定義 average(scores) 和 biggest(scores) 兩個函數。'};if((code.match(/\breturn\b/g)||[]).length<2)return {ok:false,msg:'average 和 biggest 都要用 return 交回結果，不是 print。'};if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};if(/None/.test(res.out))return {ok:false,msg:'印出了 None：函數沒有 return，交回的是 None。'};if(res.asked!==5)return {ok:false,msg:'要問 5 個分數。'};if(!/71\.4/.test(res.out)||!/92/.test(res.out))return {ok:false,msg:'80、65、92、47、73 的平均是 71.4，最高 92。'};return {ok:true,msg:'進階完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'閏年函數',debug:true,
   desc:'寫函數 <code>is_leap(year)</code>：能被 4 整除但不能被 100 整除，或能被 400 整除，交回 True，否則 False。然後對 2000、1900、2024、2023 各印一行「年份 True/False」。',
   hints:['return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0','for y in [2000, 1900, 2024, 2023]: print(y, is_leap(y))'],inputs:[],
   check:(code,res)=>{if(!/def\s+is_leap\s*\(/.test(code))return {ok:false,msg:'要定義 is_leap(year)。'};if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};for(const [y,w] of [[2000,'True'],[1900,'False'],[2024,'True'],[2023,'False']]){if(!new RegExp(y+'\\s+'+w).test(res.out))return {ok:false,msg:`${y} 應是 ${w}。`};}return {ok:true,msg:'挑戰完成。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'def f(x):\n    return x + 1\n\nprint(f(f(1)))',options:['2','3','f(2)','出錯'],answer:1,why:'f(1) 交回 2，f(2) 交回 3。'},
  {id:'q2',q:'執行到哪一行才出錯？',code:'a = 10\nb = 0\nprint("開始")\nprint(a / b)\nprint("完")',options:['第 1 行，程式不會開始','第 4 行，「開始」已印出','第 5 行','不會出錯'],answer:1,why:'除以 0 是運行錯誤，執行到第 4 行才發生，之前的「開始」已經印了。'},
  {id:'q3',q:'這個程式想印 1 至 3 的總和（6），卻印出 1 3 6 三行。錯在哪？',code:'t = 0\nfor i in range(1, 4):\n    t += i\n    print(t)',options:['range 終點錯','t 初值錯','print 縮排了，放進了迴圈','沒有錯'],answer:2,why:'print 有縮排，每圈都印；把它移出迴圈（刪去縮排）就只印一次 6。這是邏輯錯誤。'},
];
'''

build(9, '函數入門與除錯', '四章：函數、return、三類錯誤、逐步執行。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：函數、return、三類錯誤、逐步執行，每章都是「學 → 試 → 練」三步，然後做捉蟲比賽和小測。小測之後要填下一堂專題的規劃表。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:13,3:9,4:9}',
      "['第 1 章 函數',sc.c[1],9],['第 2 章 return',sc.c[2],13],['第 3 章 三類錯誤',sc.c[3],9],['第 4 章 逐步執行',sc.c[4],9],",
      "[['c1_a','C 4 行'],['c2_a','A 8'],['c2_b','B 5 / None'],['c3_a','C 邏輯錯誤'],['c4_a','C 第 5 行']]",
      """[['練習 1','def、line(5)、line(10)'],['練習 2','return、bmi'],['練習 3','p = 1'],['練習 4','刪去第 5 行的 count += 1']]""",
      '<a href="https://www.w3schools.com/python/python_functions.asp" target="_blank" rel="noopener">Functions</a>、<a href="https://www.w3schools.com/python/python_functions_return.asp" target="_blank" rel="noopener">Return Values</a>',
      '例如：我用逐步執行看到 biggest 沒有變，才發現寫錯了……', '捉蟲比賽與函數')

# ---- 後處理：必做作品預載有錯的程式；小測後加「專題規劃表」 ----
p = os.path.join(ROOT, 'src/lesson9/lesson9.src.html')
s = open(p, encoding='utf8').read()
s = s.replace("const r=makeThonny(box,{id:t.id,code:rec.code||'',", "const r=makeThonny(box,{id:t.id,code:rec.code||t.code||'',")
# 專題規劃表：取代自評
s = s.replace('<div class="lead">自評<small>5 分</small></div>\n    <p class="small">今天程式出錯時，你是怎樣找到原因的？寫一兩句。</p>',
              '<div class="lead">專題規劃表<small>5 分</small></div>\n    <p class="small">下一堂要做迷你專題（問答遊戲、小食部收銀機、文字冒險、海龜藝術，或自訂）。先寫好規劃：</p>\n    <ol class="steps-list small"><li><b>題目</b>：一句話</li><li><b>輸入</b>：程式會問使用者甚麼</li><li><b>處理</b>：用到的 if、迴圈、列表、函數</li><li><b>輸出</b>：印出甚麼</li><li><b>測試數據</b>：兩組（一組正常、一組邊界或錯誤），寫明預期結果</li></ol>')
s = s.replace('<textarea id="reflect" rows="3"', '<textarea id="reflect" rows="8"')
s = s.replace("if(t.length<6){$('#exitFb').textContent='自評請最少寫一句。';return;}", "if(t.length<40){$('#exitFb').textContent='規劃表要寫齊題目、輸入、處理、輸出和測試數據（最少 40 字）。';return;}")
s = s.replace('<p class="small">自評：${esc(S.quiz.reflect)}</p>', '<p class="small">專題規劃表：${esc(S.quiz.reflect)}</p>')
s = s.replace('自評：${S.quiz.reflect}', '專題規劃表：${S.quiz.reflect}')
s = s.replace("rows.map(r=>`${r[0]}：${r[1]} / ${r[2]}`).join('\\n')+`\\n總分", "rows.map(r=>`${r[0]}：${r[1]} / ${r[2]}`).join('\\n')+`\\n總分")
assert '專題規劃表' in s and 't.code||' in s
open(p, 'w', encoding='utf8').write(s)
print('post-processed')
