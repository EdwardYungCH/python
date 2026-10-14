# -*- coding: utf-8 -*-
"""第 8 堂「列表」。python3 tools/make_lesson8.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build

CH_HTML = r'''<!-- 1 列表 -->
<section class="card" id="s1" data-title="列表：一個變量裝很多值" data-short="1 列表">
  <header><div class="chapter">第 1 章</div><h2>列表：一個變量裝很多值</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>[ ]</code> 建立列表，用索引取出和修改其中一項</li><li>用 <code>len()</code> 數有幾多項</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">五個分數，不用五個變量</div>
    <p>要記住全班的分數，不可能寫 <code>s1</code>、<code>s2</code>、<code>s3</code> … 一個個變量。<b>列表（list）</b>讓一個變量裝很多個值，用方括號和逗號寫：</p>
    <pre class="ex">scores = [80, 65, 92, 47, 73]
print(len(scores))     <span class="cm"># 5：有 5 項</span>
print(scores[0])       <span class="cm"># 80：第一項，索引由 0 開始（和字串一樣）</span>
print(scores[-1])      <span class="cm"># 73：最後一項</span>
scores[3] = 50         <span class="cm"># 把第 4 項改成 50（字串不可以這樣改，列表可以）</span>
print(scores)          <span class="cm"># [80, 65, 92, 50, 73]</span></pre>
    <p>列表可以裝文字：<code>names = ["Amy", "Ben", "Cat"]</code>；也可以是空的：<code>names = []</code>，之後再加。</p>
    <div class="key">索引由 0 開始；<code>scores[5]</code> 不存在，會出 <code>IndexError</code>。印整個列表會連方括號一起印。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>x = [a, b, c]</code>；<code>x[i]</code> 取或改第 i 項；<code>len(x)</code> 項數。</div>
</section>

<!-- 2 加減 -->
<section class="card" id="s2" data-title="加項、刪項" data-short="2 加減">
  <header><div class="chapter">第 2 章</div><h2>加項、刪項</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>append()</code> 在尾加一項，用迴圈逐個輸入</li><li>用 <code>remove()</code>、<code>pop()</code> 刪項</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">列表會隨程式執行而變長變短</div>
    <pre class="ex">names = []                 <span class="cm"># 空列表</span>
names.append("Amy")        <span class="cm"># 尾加一項 → ["Amy"]</span>
names.append("Ben")        <span class="cm"># → ["Amy", "Ben"]</span>
names.insert(0, "Zoe")     <span class="cm"># 在索引 0 插入 → ["Zoe", "Amy", "Ben"]</span>
names.remove("Amy")        <span class="cm"># 刪去值是 "Amy" 的那項 → ["Zoe", "Ben"]</span>
last = names.pop()         <span class="cm"># 刪去最後一項並交回它 → last = "Ben"</span>
print(names)               <span class="cm"># ["Zoe"]</span></pre>
    <p>最常用的組合：用迴圈重複 <code>input</code> 和 <code>append</code>，把使用者輸入的東西逐個收進列表：</p>
    <pre class="ex">scores = []
for i in range(3):
    s = int(input("分數："))
    scores.append(s)
print(scores)              <span class="cm"># 例如 [80, 65, 92]</span></pre>
    <div class="key"><code>append</code> 真的改變了列表，不用寫 <code>names = names.append(...)</code>（那樣會變成 None）。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>x.append(v)</code> 尾加；<code>x.insert(i, v)</code> 插入；<code>x.remove(v)</code> 刪值；<code>x.pop()</code> 刪尾。</div>
</section>

<!-- 3 迴圈與最大最小 -->
<section class="card" id="s3" data-title="迴圈、總和、最大最小" data-short="3 最大">
  <header><div class="chapter">第 3 章</div><h2>用迴圈逐項看：總和、平均、最大、最小</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>for s in scores:</code> 逐項處理</li><li>自己寫「找最大值」：先假設第一項最大，逐項比較</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">先假設第一項是最大，見到更大就換</div>
    <pre class="ex">scores = [80, 65, 92, 47, 73]
total = 0
for s in scores:           <span class="cm"># s 依次是 80、65、92、47、73</span>
    total += s
print("總和", total)        <span class="cm"># 357</span>
print("平均", total / len(scores))   <span class="cm"># 71.4</span></pre>
    <pre class="ex">biggest = scores[0]        <span class="cm"># 先假設第一項最大</span>
for s in scores:
    if s > biggest:        <span class="cm"># 見到更大的</span>
        biggest = s        <span class="cm"># 就換</span>
print("最高", biggest)      <span class="cm"># 92</span></pre>
    <p>找最小值只需把 <code>&gt;</code> 改成 <code>&lt;</code>。Python 其實有 <code>max()</code>、<code>min()</code>、<code>sum()</code>，但<b>這一堂要自己寫</b>，因為「逐項比較」這個方法以後很多題目都用得着，考試也會考你追蹤這種程式。</p>
    <div class="key">起始值要用 <code>scores[0]</code>，不要用 0：如果全部分數都是負數，用 0 會找錯。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　<code>for s in x:</code> 逐項；總和用累加；最大值：先設第一項，逐項比較，更大就換。</div>
</section>

<!-- 4 搜尋與計數 -->
<section class="card" id="s4" data-title="搜尋與計數" data-short="4 搜尋">
  <header><div class="chapter">第 4 章</div><h2>搜尋與計數</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>數符合條件的項目有幾多個</li><li>逐項搜尋某個值，找到就記下位置</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">計數器加條件；搜尋就是逐項對比</div>
    <pre class="ex"><span class="cm"># 數有幾多個合格（50 分或以上）</span>
scores = [80, 65, 92, 47, 73]
passed = 0
for s in scores:
    if s >= 50:
        passed += 1
print(passed, "人合格")     <span class="cm"># 4 人合格</span></pre>
    <pre class="ex"><span class="cm"># 搜尋：Cat 的分數是幾多？</span>
names = ["Amy", "Ben", "Cat", "Dan", "Eve"]
scores = [80, 65, 92, 47, 73]
target = "Cat"
found = -1                   <span class="cm"># -1 代表未找到</span>
for i in range(len(names)):  <span class="cm"># i 是索引 0 至 4</span>
    if names[i] == target:
        found = i            <span class="cm"># 記下位置</span>
if found == -1:
    print("找不到")
else:
    print(target, "的分數是", scores[found])   <span class="cm"># 兩個列表用同一個索引對應</span></pre>
    <div class="key">用 <code>for i in range(len(x))</code> 而不是 <code>for s in x</code>，是因為要知道<b>位置</b>，才可以到另一個列表取對應的項。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　計數：條件成立才 <code>+= 1</code>；搜尋：<code>for i in range(len(x))</code> 逐項比對，找到記下 i。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a'],c3:['c3_a','c3_b'],c4:['c4_a']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','索引與修改','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'x = [10, 20, 30, 40]\nx[1] = 25\nprint(x[1], x[-1], len(x))',options:['25 40 4','20 40 4','25 30 3','10 40 4'],answer:0,why:'x[1] 改成 25；x[-1] 是最後一項 40；長度仍是 4。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上缺少的部分：把列表第 3 項改成 "Cat"，再印出列表的項數和第一項。',code:'names = ["Amy", "Ben", "Cas"]\nnames[____] = "Cat"\nprint(len(names))\nprint(names[____])',expect:'3\nAmy\n',answer:'names = ["Amy", "Ben", "Cas"]\nnames[2] = "Cat"\nprint(len(names))\nprint(names[0])',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(!/names\[\s*2\s*\]\s*=/.test(code))return {ok:false,msg:'第 3 項的索引是 2。'};if(res.out!=='3\nAmy\n')return {ok:false,msg:'應印出 3 和 Amy 兩行。'};return {ok:true,msg:'正確。'};},
    hints:['第 3 項的索引是 2（由 0 開始數）。','第一項是 names[0]。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t=step(h,'try','append 與 pop','估對 4 分');
  makePredict(t,{id:'c2_a',q:'這個程式會印出甚麼？',code:'x = [1, 2]\nx.append(3)\nx.pop()\nx.append(4)\nprint(x)',options:['[1, 2, 3, 4]','[1, 2, 4]','[1, 2, 3]','[4]'],answer:1,why:'加 3 → [1,2,3]；pop 刪尾 → [1,2]；加 4 → [1,2,4]。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上缺少的部分：問 3 次名字，逐個加入列表，最後印出列表（測試輸入：Amy、Ben、Cat）。',code:'names = ____\nfor i in range(3):\n    n = input("名字：")\n    names.____(n)\nprint(names)',answer:'names = []\nfor i in range(3):\n    n = input("名字：")\n    names.append(n)\nprint(names)',inputs:['Amy','Ben','Cat'],
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(!/\['Amy', 'Ben', 'Cat'\]/.test(res.out))return {ok:false,msg:"應印出 ['Amy', 'Ben', 'Cat']。"};return {ok:true,msg:'正確。'};},
    hints:['開始時是空列表 []。','尾加一項用 append。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t1=step(h,'try','逐項累加','估對 4 分');
  makePredict(t1,{id:'c3_a',q:'這個程式會印出甚麼？',code:'x = [3, 5, 2]\nt = 0\nfor v in x:\n    t += v\nprint(t, t / len(x))',options:['10 3.3333333333333335','10 3','3 1.0','10 2'],answer:0,why:'3+5+2=10；10 除以 3 項是 3.333…（/ 是小數除法）。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','找最大值的追蹤','估對 4 分');
  makePredict(t2,{id:'c3_b',q:'執行完畢後 biggest 是甚麼？如果把第 1 行的 biggest = x[0] 改成 biggest = 0 又如何？',code:'x = [-5, -2, -9]\nbiggest = x[0]\nfor v in x:\n    if v > biggest:\n        biggest = v\nprint(biggest)',options:['-5；改成 0 仍是 -5','-2；改成 0 會變 0','-9；改成 0 會變 0','-2；改成 0 仍是 -2'],answer:1,why:'逐項比較，-2 最大；如果起始值是 0，沒有一項大過 0，會錯誤地印 0。所以起始值要用 x[0]。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上缺少的部分，自己寫出找最小值（應印出 47）。不可以用 min()。',code:'scores = [80, 65, 92, 47, 73]\nsmallest = ____\nfor s in scores:\n    if s ____ smallest:\n        smallest = s\nprint(smallest)',expect:'47\n',answer:'scores = [80, 65, 92, 47, 73]\nsmallest = scores[0]\nfor s in scores:\n    if s < smallest:\n        smallest = s\nprint(smallest)',
    check:(code,res)=>{if(/min\(/.test(code))return {ok:false,msg:'這一題要自己用迴圈寫，不可以用 min()。'};if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(!/smallest\s*=\s*scores\[\s*0\s*\]/.test(code))return {ok:false,msg:'起始值要用 scores[0]。'};if(res.out!=='47\n')return {ok:false,msg:'應印出 47，檢查比較符號。'};return {ok:true,msg:'正確。'};},
    hints:['起始值用第一項 scores[0]。','找最小值：見到更小的就換，用 <。']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t=step(h,'try','搜尋','估對 4 分');
  makePredict(t,{id:'c4_a',q:'這個程式會印出甚麼？',code:'names = ["Amy", "Ben", "Cat"]\nfound = -1\nfor i in range(len(names)):\n    if names[i] == "Ben":\n        found = i\nprint(found)',options:['Ben','1','2','-1'],answer:1,why:'Ben 在索引 1；找到就把 i 記入 found。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'填上缺少的部分，數出有幾多個分數不合格（低於 50），應印出 2。',code:'scores = [80, 35, 92, 47, 73]\nfailed = 0\nfor s in scores:\n    if ____:\n        failed ____ 1\nprint(failed)',expect:'2\n',answer:'scores = [80, 35, 92, 47, 73]\nfailed = 0\nfor s in scores:\n    if s < 50:\n        failed += 1\nprint(failed)',
    hints:['不合格的條件是 s < 50。','符合就 failed += 1。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'班級成績查詢器',
   desc:'問 5 個分數並放進列表，然後印出<b>總和</b>、<b>平均</b>（保留一位小數）和<b>最高分</b>。最高分要自己用迴圈找，不可以用 <code>max()</code>、<code>sum()</code>。',
   hints:['scores = []，用 for i in range(5): 問 5 次並 append。','總和用累加；平均 = 總和 / len(scores)，用 round(x, 1)。','最高分：biggest = scores[0]，逐項比較。'],inputs:['80','65','92','47','73'],
   check:(code,res)=>{if(/\bmax\(|\bsum\(/.test(code))return {ok:false,msg:'這一題要自己寫，不可以用 max() 或 sum()。'};if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};if(res.asked!==5)return {ok:false,msg:`要問 5 個分數，程式問了 ${res.asked} 次。`};if(!/append\(/.test(code))return {ok:false,msg:'要用 append 把分數放進列表。'};
     const o=res.out;if(!/357/.test(o))return {ok:false,msg:'80、65、92、47、73 的總和是 357。'};if(!/71\.4/.test(o))return {ok:false,msg:'平均應是 71.4（保留一位小數）。'};if(!/92/.test(o))return {ok:false,msg:'最高分應是 92。'};return {ok:true,msg:'成績查詢器完成。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'合格人數與最高分是第幾位',
   desc:'在必做之上，再印出<b>合格人數</b>（50 分或以上）和<b>最高分是第幾位同學</b>（第 1 位是列表第一項）。測試分數 80、65、92、47、73 應印「4 人合格」和「第 3 位」。',
   hints:['合格人數：計數器加條件 s >= 50。','要知道位置，改用 for i in range(len(scores))，見到更大就記下 i。','印 i + 1 才是「第幾位」。'],inputs:['80','65','92','47','73'],
   check:(code,res)=>{if(/\bmax\(|\bsum\(|\.index\(/.test(code))return {ok:false,msg:'不可以用 max()、sum() 或 index()。'};if(res.err)return {ok:false,msg:'程式出錯：'+res.err.split('\n').pop()};const o=res.out;if(!/4\s*人/.test(o))return {ok:false,msg:'應印「4 人合格」。'};if(!/第\s*3\s*位/.test(o))return {ok:false,msg:'最高分 92 是第 3 位同學，應印「第 3 位」。'};return {ok:true,msg:'進階完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'按名字查分數',
   desc:'名單固定是 <code>["Amy", "Ben", "Cat", "Dan", "Eve"]</code>。問 5 個分數後，再問一個名字：找到就印「名字 的分數是 N」，找不到就印「找不到」。',
   hints:['found = -1，然後 for i in range(len(names)): if names[i] == target: found = i','找到時分數是 scores[found]。'],inputs:['80','65','92','47','73','Cat'],
   check:async(code,res)=>{if(/\.index\(/.test(code))return {ok:false,msg:'要自己用迴圈搜尋，不可以用 index()。'};for(const [nm,want] of [['Cat','92'],['Eve','73'],['Zoe','找不到']]){const r=await runSilent(code,['80','65','92','47','73',nm]);if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};if(r.asked!==6)return {ok:false,msg:'要問 5 個分數再問 1 個名字。'};const last=r.out.trim().split('\n').pop();if(!last.includes(want))return {ok:false,msg:`查「${nm}」應見到「${want}」，程式印出：${last}`};}return {ok:true,msg:'挑戰完成。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'x = [5, 8, 3]\nx.append(1)\nprint(x[1], len(x))',options:['5 4','8 4','8 3','1 4'],answer:1,why:'x[1] 是第二項 8；append 後有 4 項。'},
  {id:'q2',q:'印出甚麼？',code:'x = [4, 9, 2]\nb = x[0]\nfor v in x:\n    if v > b:\n        b = v\nprint(b)',options:['4','9','2','15'],answer:1,why:'逐項比較，9 最大。'},
  {id:'q3',q:'印出甚麼？',code:'x = [3, 7, 7, 1]\nn = 0\nfor v in x:\n    if v == 7:\n        n += 1\nprint(n)',options:['1','2','7','4'],answer:1,why:'等於 7 的有兩項。'},
];
'''

build(8, '列表', '四章：列表、加項刪項、迴圈與最大最小、搜尋與計數。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：列表、加項刪項、迴圈與最大最小、搜尋與計數，每章都是「學 → 試 → 練」三步，然後做班級成績查詢器和小測。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:9,3:13,4:9}',
      "['第 1 章 列表',sc.c[1],9],['第 2 章 加項刪項',sc.c[2],9],['第 3 章 迴圈與最大最小',sc.c[3],13],['第 4 章 搜尋與計數',sc.c[4],9],",
      "[['c1_a','A 25 40 4'],['c2_a','B [1, 2, 4]'],['c3_a','A 10 3.333…'],['c3_b','B -2；改成 0 會變 0'],['c4_a','B 1']]",
      """[['練習 1','names[2]、names[0]'],['練習 2','[]、append'],['練習 3','scores[0]、<'],['練習 4','s < 50、+=']]""",
      '<a href="https://www.w3schools.com/python/python_lists.asp" target="_blank" rel="noopener">Lists</a>、<a href="https://www.w3schools.com/python/python_lists_add.asp" target="_blank" rel="noopener">Add Items</a>、<a href="https://www.w3schools.com/python/python_lists_remove.asp" target="_blank" rel="noopener">Remove Items</a>、<a href="https://www.w3schools.com/python/python_lists_loop.asp" target="_blank" rel="noopener">Loop Lists</a>',
      '例如：我把最大值的起始值設成 0，負數測試時出錯……', '班級成績查詢器')
