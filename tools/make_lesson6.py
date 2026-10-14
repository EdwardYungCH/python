# -*- coding: utf-8 -*-
"""第 6 堂「For 迴圈與 Range」。python3 tools/make_lesson6.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build

CH_HTML = r'''<!-- 1 for -->
<section class="card" id="s1" data-title="for：數住做幾次" data-short="1 for">
  <header><div class="chapter">第 1 章</div><h2>for：數住做幾次</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>for i in range(n):</code> 重複 n 次</li><li>知道 i 每次會變：0、1、2 …</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">已經知道要做幾次，就用 for</div>
    <p>上一堂的 <code>while</code> 要自己寫計數器、自己加 1。如果事先知道要重複幾次，<code>for</code> 會幫你數：</p>
    <pre class="ex">for i in range(5):     <span class="cm"># i 依次是 0、1、2、3、4</span>
    print(i)
print("完")            <span class="cm"># 沒有縮排：迴圈完結後才執行</span></pre>
    <p><code>range(5)</code> 產生 0 至 4 共 5 個數（<b>由 0 開始，不包括 5</b>）。每一圈 <code>i</code> 拿一個數，縮排的行執行一次。</p>
    <pre class="ex"><span class="cm"># 同一件事，while 要三行，for 只要一行</span>
n = 0                  <span class="cm"># while 版</span>
while n &lt; 3:
    print("你好")
    n += 1

for i in range(3):     <span class="cm"># for 版</span>
    print("你好")</pre>
    <div class="key">不用 <code>i</code> 的時候也要寫它；<code>range(3)</code> 就是「3 次」。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>for i in range(n):</code> 重複 n 次，i 由 0 數到 n − 1。</div>
</section>

<!-- 2 range -->
<section class="card" id="s2" data-title="range 的三種寫法" data-short="2 range">
  <header><div class="chapter">第 2 章</div><h2>range 的三種寫法</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li><code>range(a, b)</code> 由 a 數到 b − 1</li><li><code>range(a, b, step)</code> 每次跳 step</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">起點、終點、步長</div>
    <div class="tablewrap"><table>
      <thead><tr><th>寫法</th><th>產生的數</th><th>說明</th></tr></thead>
      <tbody>
        <tr><td><code>range(5)</code></td><td>0 1 2 3 4</td><td>由 0 開始，不包括 5</td></tr>
        <tr><td><code>range(1, 6)</code></td><td>1 2 3 4 5</td><td>由 1 開始，不包括 6</td></tr>
        <tr><td><code>range(2, 11, 2)</code></td><td>2 4 6 8 10</td><td>由 2 開始，每次加 2，不包括 11</td></tr>
        <tr><td><code>range(10, 0, -1)</code></td><td>10 9 … 1</td><td>步長是負數就倒數</td></tr>
      </tbody>
    </table></div>
    <pre class="ex">for i in range(1, 6):
    print(i)           <span class="cm"># 1 2 3 4 5，每個一行</span>

for i in range(10, 0, -2):
    print(i)           <span class="cm"># 10 8 6 4 2</span></pre>
    <div class="key">終點永遠<b>不包括</b>：要印到 5，就寫 <code>range(1, 6)</code>。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>range(起點, 終點, 步長)</code>；終點不包括在內；步長可以是負數。</div>
</section>

<!-- 3 累加累乘 -->
<section class="card" id="s3" data-title="用 for 累加和累乘" data-short="3 累加">
  <header><div class="chapter">第 3 章</div><h2>用 for 累加和累乘</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>total += i</code> 把 range 的數加起來</li><li>用 <code>p *= i</code> 乘起來，和算年年加息</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">迴圈前設初值，迴圈裏加或乘，迴圈後印</div>
    <pre class="ex"><span class="cm"># 1 + 2 + … + 10</span>
total = 0
for i in range(1, 11):
    total += i
print(total)           <span class="cm"># 55</span>

<span class="cm"># 1 × 2 × 3 × 4</span>
p = 1                  <span class="cm"># 乘法的初值是 1，不是 0</span>
for i in range(1, 5):
    p *= i
print(p)               <span class="cm"># 24</span></pre>
    <p>年年加息也是累乘：每年的錢是上一年乘 1.05（利率 5%）。</p>
    <pre class="ex">money = 1000
for year in range(1, 4):
    money *= 1.05
    print(year, "年後：", round(money, 2))</pre>
    <div class="key">加法初值 0，乘法初值 1。<code>round(x, 2)</code> 保留兩位小數。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　累加 <code>total += i</code>（初值 0）；累乘 <code>p *= i</code>（初值 1）。</div>
</section>

<!-- 4 turtle -->
<section class="card" id="s4" data-title="turtle：用迴圈畫圖" data-short="4 海龜">
  <header><div class="chapter">第 4 章</div><h2>turtle：用迴圈畫圖</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>turtle</code> 模組叫海龜前進和轉彎</li><li>用 <code>for</code> 重複「前進、轉彎」畫出多邊形</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">海龜走過的路就是線</div>
    <p><code>turtle</code> 是 Python 內置的畫圖模組。畫布中央有一隻小海龜，你叫它前進，它走過的地方就留下一條線。</p>
    <pre class="ex">import turtle
t = turtle.Turtle()    <span class="cm"># 造一隻海龜，叫它 t</span>
t.forward(100)         <span class="cm"># 前進 100 步</span>
t.left(90)             <span class="cm"># 向左轉 90 度</span>
t.forward(100)</pre>
    <p>畫正方形要「前進、左轉 90°」四次，正好用 <code>for</code>：</p>
    <pre class="ex">import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(80)
    t.left(90)</pre>
    <div class="tablewrap"><table>
      <thead><tr><th>指令</th><th>作用</th></tr></thead>
      <tbody>
        <tr><td><code>t.forward(d)</code></td><td>前進 d 步</td></tr>
        <tr><td><code>t.backward(d)</code></td><td>後退 d 步</td></tr>
        <tr><td><code>t.left(a)</code>／<code>t.right(a)</code></td><td>左轉／右轉 a 度</td></tr>
        <tr><td><code>t.penup()</code>／<code>t.pendown()</code></td><td>提筆（移動不畫線）／落筆</td></tr>
        <tr><td><code>t.color("red")</code></td><td>改線的顏色</td></tr>
      </tbody>
    </table></div>
    <div class="key">多邊形的規律：有 n 條邊，每次轉 <code>360 / n</code> 度。正方形 4 邊轉 90°，三角形 3 邊轉 120°。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　<code>import turtle</code>、<code>t = turtle.Turtle()</code>；n 邊形：<code>for i in range(n):</code> 前進、轉 <code>360 / n</code> 度。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a'],c3:['c3_a'],c4:['c4_a','c4_b']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','i 會是甚麼？','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'for i in range(3):\n    print("第", i, "次")\nprint("完")',options:['第 1 次\n第 2 次\n第 3 次\n完','第 0 次\n第 1 次\n第 2 次\n完','第 0 次\n第 1 次\n第 2 次\n第 3 次\n完','完'],answer:1,why:'range(3) 是 0、1、2；print("完") 沒有縮排，迴圈完結後印一次。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上 range 內的數字，令程式印出 0 至 4 每個一行。',code:'for i in range(____):\n    print(i)',expect:'0\n1\n2\n3\n4\n',answer:'for i in range(5):\n    print(i)',
    hints:['0 至 4 一共有幾多個數？','range(n) 由 0 數到 n − 1。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t=step(h,'try','起點、終點、步長','估對 4 分');
  makePredict(t,{id:'c2_a',q:'這個程式會印出甚麼？',code:'for i in range(2, 11, 3):\n    print(i)',options:['2\n5\n8','2\n5\n8\n11','3\n6\n9','2\n3\n4\n5\n6\n7\n8\n9\n10'],answer:0,why:'由 2 開始每次加 3：2、5、8；下一個 11 不小於終點 11，不印。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上三個數字，令程式印出 10、20、30、40、50（每個一行）。',code:'for i in range(____, ____, ____):\n    print(i)',expect:'10\n20\n30\n40\n50\n',answer:'for i in range(10, 51, 10):\n    print(i)',
    hints:['起點 10，每次加 10。','終點不包括在內，要大過 50，例如 51 或 60。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t=step(h,'try','累乘','估對 4 分');
  makePredict(t,{id:'c3_a',q:'這個程式會印出甚麼？',code:'p = 1\nfor i in range(1, 5):\n    p *= i\nprint(p)',options:['10','24','4','1\n2\n6\n24'],answer:1,why:'1 × 2 × 3 × 4 = 24；print 在迴圈外只印一次。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上缺少的部分，計出 1 至 100 的總和（應印出 5050）。',code:'total = ____\nfor i in range(1, ____):\n    total += i\nprint(total)',expect:'5050\n',answer:'total = 0\nfor i in range(1, 101):\n    total += i\nprint(total)',
    hints:['加法的初值是 0。','要加到 100，終點要寫 101。']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t1=step(h,'try','畫出甚麼？','估對 4 分');
  makePredict(t1,{id:'c4_a',q:'這個程式會畫出甚麼？估完按 ▶ 看畫布。',code:'import turtle\nt = turtle.Turtle()\nfor i in range(3):\n    t.forward(100)\n    t.left(120)',options:['正方形','三角形','六邊形','一條直線'],answer:1,why:'重複 3 次、每次轉 120°（360 ÷ 3），三條邊接成三角形。',turtle:true},S.pred,PRED_PTS,done);
  const t2=step(h,'try','轉幾多度？','估對 4 分');
  makePredict(t2,{id:'c4_b',q:'要畫正六邊形，每次應轉幾多度？',code:'import turtle\nt = turtle.Turtle()\nfor i in range(6):\n    t.forward(50)\n    t.left(____)',options:['30','45','60','90'],answer:2,why:'360 ÷ 6 = 60。執行器內把 ____ 換成 60 試試。',turtle:true},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'填上缺少的部分，畫一個正五邊形。',code:'import turtle\nt = turtle.Turtle()\nfor i in range(____):\n    t.forward(70)\n    t.left(____)',answer:'import turtle\nt = turtle.Turtle()\nfor i in range(5):\n    t.forward(70)\n    t.left(72)',turtle:true,
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(!/range\(\s*5\s*\)/.test(code))return {ok:false,msg:'五邊形有 5 條邊：range(5)。'};if(!/left\(\s*72\s*\)|right\(\s*72\s*\)|360\s*\/\s*5/.test(code))return {ok:false,msg:'每次要轉 360 ÷ 5 = 72 度。'};if(res.ink<50)return {ok:false,msg:'畫布上沒有線，檢查 forward 有沒有執行。'};return {ok:true,msg:'正五邊形完成。'};},
    hints:['五邊形有 5 條邊。','每次轉 360 ÷ 5 度。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'乘數表',
   desc:'問使用者一個數 n，然後用 <code>for</code> 印出 n 的乘數表：<code>n x 1 = n</code> 到 <code>n x 9 = 9n</code>，共 9 行。例如輸入 7，第三行是 <code>7 x 3 = 21</code>。',
   hints:['n = int(input("哪一個數？"))','for i in range(1, 10):','print(n, "x", i, "=", n * i)'],inputs:['7'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};if(res.asked!==1)return {ok:false,msg:'要問一次使用者輸入數字。'};if(!/for\s+\w+\s+in\s+range/.test(code))return {ok:false,msg:'要用 for 迴圈。'};
     const lines=res.out.split('\n').filter(l=>/=/.test(l));if(lines.length<9)return {ok:false,msg:`輸入 7 應印 9 行乘數表，只找到 ${lines.length} 行有「=」。`};for(let k=1;k<=9;k++){if(!lines.some(l=>l.includes('7')&&new RegExp('\\b'+k+'\\b').test(l)&&new RegExp('=\\s*'+(7*k)+'\\b').test(l)))return {ok:false,msg:`找不到 7 x ${k} = ${7*k} 那一行。`};}return {ok:true,msg:'乘數表完成。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'儲蓄計算機',
   desc:'問本金、年利率（%）和年數，然後每年印一行「第 y 年：餘額」，餘額保留兩位小數。例如本金 1000、利率 5、3 年，第 3 年應是 1157.63。',
   hints:['rate = float(input("年利率（%）：")) / 100','for year in range(1, years + 1): money *= 1 + rate','print("第", year, "年：", round(money, 2))'],inputs:['1000','5','3'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};if(res.asked!==3)return {ok:false,msg:`要問本金、利率、年數三次，程式問了 ${res.asked} 次。`};const lines=res.out.split('\n').filter(l=>/\d+\.\d/.test(l));if(lines.length<3)return {ok:false,msg:'3 年應印 3 行餘額。'};if(!/1050\.0|1102\.5|1157\.6/.test(res.out))return {ok:false,msg:'本金 1000、利率 5%：第 1 年 1050.0，第 2 年 1102.5，第 3 年 1157.63。檢查 money *= 1 + rate。'};if(!/1157\.6/.test(res.out))return {ok:false,msg:'第 3 年應是 1157.63，檢查迴圈有沒有走 3 次。'};return {ok:true,msg:'儲蓄計算機完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'任何多邊形',
   desc:'問使用者邊數 n，然後用海龜畫出正 n 邊形（每邊 60 步）。提示：每次轉 <code>360 / n</code> 度。',
   hints:['n = int(input("幾多條邊？"))','for i in range(n):','t.forward(60) 然後 t.left(360 / n)'],inputs:['5'],turtle:true,
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};if(res.asked!==1)return {ok:false,msg:'要問一次邊數。'};if(!/import turtle/.test(code))return {ok:false,msg:'要 import turtle。'};if(!/360\s*\/\s*\w+/.test(code))return {ok:false,msg:'轉的角度要用 360 / n 計出來。'};if(!/range\(\s*\w+\s*\)/.test(code))return {ok:false,msg:'迴圈次數要跟邊數：range(n)。'};if(res.ink<50)return {ok:false,msg:'畫布上沒有線。'};return {ok:true,msg:'多邊形完成。試試輸入 8 或 12。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'for i in range(2, 6):\n    print(i)',options:['2\n3\n4\n5','2\n3\n4\n5\n6','1\n2\n3\n4\n5','0\n1\n2\n3\n4\n5'],answer:0,why:'由 2 開始，終點 6 不包括：2、3、4、5。'},
  {id:'q2',q:'印出幾行？',code:'for i in range(2):\n    print("A")\nprint("B")',options:['A\nB\nA\nB','A\nA\nB','A\nB','B'],answer:1,why:'迴圈兩次印 A；print("B") 沒有縮排，最後印一次。'},
  {id:'q3',q:'印出甚麼？',code:'p = 1\nfor i in range(3):\n    p *= 2\nprint(p)',options:['6','8','2','2\n4\n8'],answer:1,why:'p 乘 2 三次：2、4、8；print 在迴圈外只印 8。'},
];
'''

build(6, 'For 迴圈與 Range', '四章：for、range、累加與累乘、turtle 畫圖。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：for、range、累加與累乘、turtle 畫圖，每章都是「學 → 試 → 練」三步，然後做乘數表、儲蓄計算機和海龜多邊形，再做小測。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:9,3:9,4:13}',
      "['第 1 章 for',sc.c[1],9],['第 2 章 range',sc.c[2],9],['第 3 章 累加與累乘',sc.c[3],9],['第 4 章 turtle',sc.c[4],13],",
      "[['c1_a','B 第 0 次 第 1 次 第 2 次 完'],['c2_a','A 2 5 8'],['c3_a','B 24'],['c4_a','B 三角形'],['c4_b','C 60']]",
      """[['練習 1','range(5)'],['練習 2','range(10, 51, 10)'],['練習 3','total = 0、range(1, 101)'],['練習 4','range(5)、left(72)']]""",
      '<a href="https://www.w3schools.com/python/python_for_loops.asp" target="_blank" rel="noopener">For Loops</a>、<a href="https://www.w3schools.com/python/ref_func_range.asp" target="_blank" rel="noopener">range()</a>',
      '例如：我把終點寫成 5，少印了一個數，看 Shell 才發現 range 不包括終點……', '乘數表、儲蓄計算機與海龜')
