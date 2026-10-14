# -*- coding: utf-8 -*-
"""第 3 堂「數字與運算符」。python3 tools/make_lesson3.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build

CH_HTML = r'''<!-- 1 Numbers -->
<section class="card" id="s1" data-title="數字：整數和小數" data-short="1 數字">
  <header><div class="chapter">第 1 章</div><h2>數字：整數和小數</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>分辨 <code>int</code> 和 <code>float</code>，知道除法的答案一定是小數</li><li>用 <code>round()</code> 四捨五入</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">兩種數字</div>
    <p>上一堂學過：沒有小數點的是整數 <code>int</code>，有小數點的是小數 <code>float</code>。計算時要留意一條規矩：<b>用 <code>/</code> 除，答案一定是小數</b>，就算除得盡。</p>
    <pre class="ex">print(10 / 2)      <span class="cm"># 5.0（不是 5）</span>
print(7 / 2)       <span class="cm"># 3.5</span>
print(3 + 4.0)     <span class="cm"># 7.0（有一個是小數，答案就是小數）</span></pre>
    <h3>四捨五入</h3>
    <p>小數太長時用 <code>round()</code>：第二個數是保留幾個小數位，不寫就取整數。</p>
    <pre class="ex">print(round(3.14159, 2))   <span class="cm"># 3.14</span>
print(round(2.718))        <span class="cm"># 3</span>
print(round(49.95, 1))     <span class="cm"># 50.0</span></pre>
    <div class="key">之後計 BMI、平均分這類會有很多小數位的東西，記得 <code>round()</code>。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>/</code> 的答案永遠是 <code>float</code>；<code>round(x, n)</code> 保留 n 個小數位。</div>
</section>

<!-- 2 Arithmetic -->
<section class="card" id="s2" data-title="算術運算符" data-short="2 算術">
  <header><div class="chapter">第 2 章</div><h2>算術運算符：加減乘除之外</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>//</code> 取整除、<code>%</code> 取餘數、<code>**</code> 取次方</li><li>知道先乘除後加減，括號最先</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">七個算術運算符</div>
    <div class="tablewrap"><table>
      <thead><tr><th>運算符</th><th>意思</th><th>例子</th><th>答案</th></tr></thead>
      <tbody>
        <tr><td><code>+</code></td><td>加</td><td><code>7 + 2</code></td><td><code>9</code></td></tr>
        <tr><td><code>-</code></td><td>減</td><td><code>7 - 2</code></td><td><code>5</code></td></tr>
        <tr><td><code>*</code></td><td>乘</td><td><code>7 * 2</code></td><td><code>14</code></td></tr>
        <tr><td><code>/</code></td><td>除</td><td><code>7 / 2</code></td><td><code>3.5</code></td></tr>
        <tr><td><code>//</code></td><td>整除（只要商，不要餘數）</td><td><code>7 // 2</code></td><td><code>3</code></td></tr>
        <tr><td><code>%</code></td><td>餘數</td><td><code>7 % 2</code></td><td><code>1</code></td></tr>
        <tr><td><code>**</code></td><td>次方</td><td><code>7 ** 2</code></td><td><code>49</code></td></tr>
      </tbody>
    </table></div>
    <p><code>//</code> 和 <code>%</code> 是一對：17 粒糖每包 5 粒，<code>17 // 5</code> 是可以包 3 包，<code>17 % 5</code> 是剩 2 粒。</p>
    <pre class="ex">sweets = 17
print("可以包", sweets // 5, "包")    <span class="cm"># 3</span>
print("剩下", sweets % 5, "粒")      <span class="cm"># 2</span></pre>
    <h3>先後次序</h3>
    <p>和數學一樣：括號最先，然後 <code>**</code>，然後乘除（<code>* / // %</code>），最後加減。不肯定就加括號。</p>
    <pre class="ex">print(2 + 3 * 4)      <span class="cm"># 14</span>
print((2 + 3) * 4)    <span class="cm"># 20</span></pre>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>//</code> 商、<code>%</code> 餘數、<code>**</code> 次方；先乘除後加減，括號最先。</div>
</section>

<!-- 3 Assignment -->
<section class="card" id="s3" data-title="賦值運算符" data-short="3 賦值">
  <header><div class="chapter">第 3 章</div><h2>賦值運算符：把變量改一改</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>看懂 <code>x = x + 1</code> 這種「用舊值計新值」的寫法</li><li>用 <code>+=</code>、<code>-=</code>、<code>*=</code> 簡寫</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">x = x + 1 是甚麼意思</div>
    <p>數學上 <code>x = x + 1</code> 不成立，但 Python 的 <code>=</code> 是「把右邊放進左邊」：先計右邊 <code>x + 1</code>，再放回 <code>x</code>。所以 <code>x</code> 會大一。</p>
    <pre class="ex">score = 10
score = score + 5     <span class="cm"># 先計 10 + 5 = 15，放回 score</span>
print(score)          <span class="cm"># 15</span></pre>
    <p>這種寫法太常用，所以有簡寫：</p>
    <div class="tablewrap"><table>
      <thead><tr><th>簡寫</th><th>等於</th></tr></thead>
      <tbody>
        <tr><td><code>score += 5</code></td><td><code>score = score + 5</code></td></tr>
        <tr><td><code>score -= 5</code></td><td><code>score = score - 5</code></td></tr>
        <tr><td><code>score *= 2</code></td><td><code>score = score * 2</code></td></tr>
        <tr><td><code>score /= 2</code></td><td><code>score = score / 2</code></td></tr>
      </tbody>
    </table></div>
    <div class="key">之後學迴圈時，<code>count += 1</code>（計數器）和 <code>total += x</code>（累加器）會天天用。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　<code>x += 1</code> 即 <code>x = x + 1</code>：先用舊值計，再放回去。</div>
</section>

<!-- 4 Comparison & Booleans -->
<section class="card" id="s4" data-title="比較運算符與布爾值" data-short="4 比較">
  <header><div class="chapter">第 4 章</div><h2>比較運算符：答案是 True 或 False</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>==</code>、<code>!=</code>、<code>&gt;</code>、<code>&lt;</code>、<code>&gt;=</code>、<code>&lt;=</code> 比較兩個值</li><li>知道比較的結果是布爾值 <code>True</code>／<code>False</code></li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">問電腦一條是非題</div>
    <div class="tablewrap"><table>
      <thead><tr><th>運算符</th><th>意思</th><th>例子</th><th>答案</th></tr></thead>
      <tbody>
        <tr><td><code>==</code></td><td>等於（兩個 =）</td><td><code>5 == 5</code></td><td><code>True</code></td></tr>
        <tr><td><code>!=</code></td><td>不等於</td><td><code>5 != 5</code></td><td><code>False</code></td></tr>
        <tr><td><code>&gt;</code></td><td>大於</td><td><code>5 &gt; 3</code></td><td><code>True</code></td></tr>
        <tr><td><code>&lt;</code></td><td>小於</td><td><code>5 &lt; 3</code></td><td><code>False</code></td></tr>
        <tr><td><code>&gt;=</code></td><td>大於或等於</td><td><code>5 &gt;= 5</code></td><td><code>True</code></td></tr>
        <tr><td><code>&lt;=</code></td><td>小於或等於</td><td><code>5 &lt;= 3</code></td><td><code>False</code></td></tr>
      </tbody>
    </table></div>
    <p>比較的答案只有兩個：<code>True</code>（真）或 <code>False</code>（假），這就是上一堂見過的布爾值 <code>bool</code>。</p>
    <pre class="ex">age = 15
print(age &gt;= 18)      <span class="cm"># False</span>
print(age != 15)      <span class="cm"># False</span>
is_adult = age &gt;= 18  <span class="cm"># 比較的結果也可以放進變量</span>
print(is_adult)       <span class="cm"># False</span></pre>
    <div class="key">最常見的錯：<b>一個 <code>=</code> 是放進去，兩個 <code>==</code> 才是比較</b>。<code>age = 18</code> 會把 age 改成 18；<code>age == 18</code> 才是問「age 是不是 18」。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　六個比較運算符，答案是 <code>True</code>／<code>False</code>；<code>==</code> 比較，<code>=</code> 賦值。下一堂用它們來做判斷。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a','c2_b'],c3:['c3_a'],c4:['c4_a']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','除得盡也是小數？','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'print(8 / 4)\nprint(8 + 4)',options:['2\n12','2.0\n12','2.0\n12.0','2\n12.0'],answer:1,why:'/ 的答案一定是小數，所以 2.0；+ 兩個整數還是整數，所以 12。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上缺少的部分，令程式印出保留 1 個小數位的平均分 78.3。',code:'total = 235\naverage = total / 3\nprint(round(____, ____))',expect:'78.3\n',answer:'total = 235\naverage = total / 3\nprint(round(average, 1))',
    hints:['round 的第一個是要四捨五入的變量 average。','第二個數是小數位數：1。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t1=step(h,'try','// 和 % 分別給甚麼？','估對 4 分');
  makePredict(t1,{id:'c2_a',q:'這個程式會印出甚麼？',code:'print(17 // 5)\nprint(17 % 5)',options:['3.4\n2','3\n2','2\n3','3\n0.4'],answer:1,why:'17 ÷ 5 = 3 餘 2：// 給商 3，% 給餘數 2。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','先乘除後加減','估對 4 分');
  makePredict(t2,{id:'c2_b',q:'這個程式會印出甚麼？',code:'print(10 - 2 * 3)\nprint((10 - 2) * 3)\nprint(2 ** 3)',options:['24\n24\n6','4\n24\n8','4\n24\n6','24\n4\n8'],answer:1,why:'先乘：10 - 6 = 4；括號先：8 × 3 = 24；2 ** 3 = 2 × 2 × 2 = 8。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上兩個運算符，把 37 元換成十元和一元：印出「十元 3 個」和「一元 7 個」。',code:'money = 37\nprint("十元", money ____ 10, "個")\nprint("一元", money ____ 10, "個")',expect:'十元 3 個\n一元 7 個\n',answer:'money = 37\nprint("十元", money // 10, "個")\nprint("一元", money % 10, "個")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.out!=='十元 3 個\n一元 7 個\n')return {ok:false,msg:'應印出「十元 3 個」和「一元 7 個」。37 ÷ 10 的商是幾？餘數是幾？'};if(!code.includes('//')||!code.includes('%'))return {ok:false,msg:'輸出對了，但要用 // 和 % 計。'};return {ok:true,msg:'正確。'};},
    hints:['37 有幾多個十？用整除 //。','剩下的零頭是餘數 %。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t=step(h,'try','一步一步改變量','估對 4 分');
  makePredict(t,{id:'c3_a',q:'這個程式會印出甚麼？',code:'x = 10\nx += 5\nx *= 2\nx -= 1\nprint(x)',options:['29','14','30','19'],answer:0,why:'10 → +5 = 15 → ×2 = 30 → −1 = 29。每一行都用舊值計新值。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上簡寫的賦值運算符：小食部收銀，先加 12 元，再加 8 元，最後打八折（乘 0.8），印出 16.0。',code:'total = 0\ntotal ____ 12\ntotal ____ 8\ntotal ____ 0.8\nprint(total)',expect:'16.0\n',answer:'total = 0\ntotal += 12\ntotal += 8\ntotal *= 0.8\nprint(total)',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.out!=='16.0\n')return {ok:false,msg:'應印出 16.0：(12 + 8) × 0.8。'};if(!/\+=/.test(code)||!/\*=/.test(code))return {ok:false,msg:'輸出對了，但要用簡寫 += 和 *=。'};return {ok:true,msg:'正確。'};},
    hints:['加上去用 +=。','乘用 *=。']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t=step(h,'try','= 和 == 有甚麼分別？','估對 4 分');
  makePredict(t,{id:'c4_a',q:'這個程式會印出甚麼？',code:'age = 15\nprint(age == 18)\nprint(age < 18)\nage = 18\nprint(age == 18)',options:['False\nTrue\nTrue','False\nTrue\nFalse','True\nTrue\nTrue','出錯'],answer:0,why:'15 不等於 18 → False；15 小於 18 → True；第 4 行一個 = 把 age 改成 18，所以最後 True。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'填上三個比較運算符，令三行分別印出 True、False、True。',code:'score = 60\nprint(score ____ 60)   # 等於\nprint(score ____ 60)   # 不等於\nprint(score ____ 50)   # 大於',expect:'True\nFalse\nTrue\n',answer:'score = 60\nprint(score == 60)\nprint(score != 60)\nprint(score > 50)',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。括號內一個 = 不是比較，要用 ==。'};if(res.out!=='True\nFalse\nTrue\n')return {ok:false,msg:'應印出 True、False、True。'};if(!code.includes('==')||!code.includes('!='))return {ok:false,msg:'輸出對了，但第 1 行要用 ==、第 2 行要用 !=。'};return {ok:true,msg:'正確。'};},
    hints:['等於是兩個等號 ==。','不等於是 !=。','大於是 >。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'BMI 計算器',
   desc:'問身高（米，例如 1.65）和體重（公斤，例如 55），用 <code>float()</code> 轉成數字，計算 BMI = 體重 ÷ 身高<sup>2</sup>，印出保留 1 個小數位的結果，例如「你的 BMI 是 20.2」。',
   hints:['height = float(input("身高（米）："))，體重同樣。','bmi = weight / height ** 2','print("你的 BMI 是", round(bmi, 1))'],inputs:['1.65','55'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。輸入要先 float()。'};if(res.asked<2)return {ok:false,msg:'要問身高和體重兩個數。'};if(!/20\.2\b/.test(res.out))return {ok:false,msg:'輸入 1.65 和 55 時應印出 20.2（55 ÷ 1.65² = 20.20…，round 到 1 位）。現在印了：'+res.out.trim().split('\n').pop()};if(!/round\(/.test(code))return {ok:false,msg:'要用 round() 保留 1 個小數位。'};return {ok:true,msg:'BMI 計算器完成。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'找續計算機',
   desc:'問一個 100 以下的整數金額，用 <code>//</code> 和 <code>%</code> 計出要幾多張 50 元、幾多張 10 元、幾多個 1 元（用最少的張數）。例如 87 元 → 50 元 1 張、10 元 3 張、1 元 7 個。',
   hints:['fifty = money // 50，然後 money = money % 50 把剩下的放回去。','再對 10 做同樣的事。','最後剩下的就是 1 元的個數。'],inputs:['87'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.asked<1)return {ok:false,msg:'要問金額。'};const nums=(res.out.replace(/87/g,'').match(/\d+/g)||[]).map(Number);let k=0;for(const n of nums){if(n===[1,3,7][k])k++;}const ok=k===3;
     if(!ok)return {ok:false,msg:'輸入 87 時應依次印出 1（50 元）、3（10 元）、7（1 元）。'};if(!code.includes('//')||!code.includes('%'))return {ok:false,msg:'要用 // 和 % 計。'};return {ok:true,msg:'找續計算機完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'秒數換算',
   desc:'問一個秒數，換算成「__ 小時 __ 分 __ 秒」。例如 3725 秒 → 1 小時 2 分 5 秒。',
   hints:['1 小時 = 3600 秒：hours = s // 3600，剩下 s % 3600。','分鐘：再用 // 60 和 % 60。'],inputs:['3725'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};const o=res.out.replace(/3725/g,'');if(!/1\D+2\D+5\D*$/m.test(o.trim().split('\n').slice(-3).join(' ')))return {ok:false,msg:'輸入 3725 時應印出 1 小時 2 分 5 秒。'};return {ok:true,msg:'挑戰完成。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'print(9 // 2, 9 % 2, 9 / 2)',options:['4 1 4.5','4.5 1 4','4 1 4','4 0 4.5'],answer:0,why:'// 商 4，% 餘 1，/ 一定是小數 4.5。'},
  {id:'q2',q:'印出甚麼？',code:'x = 4\nx += 3\nx *= 2\nprint(x)',options:['10','14','24','7'],answer:1,why:'4 + 3 = 7，7 × 2 = 14。'},
  {id:'q3',q:'印出甚麼？',code:'n = 10\nprint(n = 10)',options:['True','10','False','出錯'],answer:3,why:'比較要用兩個 ==。括號內一個 = 會被當成設定參數，print 不認識叫 n 的參數，所以出錯（TypeError）。'},
];
'''

build(3, '數字與運算符', '四章：數字、算術運算符、賦值運算符、比較運算符。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：數字、算術、賦值、比較，每章都是「學 → 試 → 練」三步，然後做 BMI 計算器和小測。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:13,3:9,4:9}',
      "['第 1 章 數字',sc.c[1],9],['第 2 章 算術運算符',sc.c[2],13],['第 3 章 賦值運算符',sc.c[3],9],['第 4 章 比較運算符',sc.c[4],9],",
      "[['c1_a','B 2.0 / 12'],['c2_a','B 3 / 2'],['c2_b','B 4 / 24 / 8'],['c3_a','A 29'],['c4_a','A False / True / True']]",
      """[['練習 1','round(average, 1)'],['練習 2','money // 10、money % 10'],['練習 3','+= 12、+= 8、*= 0.8'],['練習 4','==、!=、>']]""",
      '<a href="https://www.w3schools.com/python/python_numbers.asp" target="_blank" rel="noopener">Numbers</a>、<a href="https://www.w3schools.com/python/python_operators.asp" target="_blank" rel="noopener">Operators</a>、<a href="https://www.w3schools.com/python/python_booleans.asp" target="_blank" rel="noopener">Booleans</a>',
      '例如：我把 // 和 % 搞混了，後來用 17 // 5 試一次就記得……', 'BMI 計算器')
