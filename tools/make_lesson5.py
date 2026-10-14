# -*- coding: utf-8 -*-
"""第 5 堂「While 迴圈」。python3 tools/make_lesson5.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build

CH_HTML = r'''<!-- 1 While -->
<section class="card" id="s1" data-title="while：條件成立就一直重複" data-short="1 while">
  <header><div class="chapter">第 1 章</div><h2>while：條件成立就一直重複</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>寫 <code>while 條件:</code> 重複執行縮排的行</li><li>知道迴圈裏一定要有東西令條件最後變 False</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">像 if，但做完會再問一次</div>
    <p><code>if</code> 問一次，成立就做一次。<code>while</code> 問一次，成立就做一次，<b>然後回頭再問</b>，直至條件變成 <code>False</code> 才離開。</p>
    <pre class="ex">n = 1
while n &lt;= 3:        <span class="cm"># 每次先問：n 仍然 ≤ 3 嗎？</span>
    print(n)
    n += 1           <span class="cm"># 令 n 變大，否則永遠 ≤ 3</span>
print("完")          <span class="cm"># 沒有縮排：迴圈結束後才執行</span></pre>
    <p>執行過程：n = 1 印 1 → n = 2 印 2 → n = 3 印 3 → n = 4，4 ≤ 3 不成立，離開 → 印「完」。</p>
    <div class="key"><b>無限迴圈</b>：如果忘記 <code>n += 1</code>，n 永遠是 1，條件永遠成立，程式永遠不停。在這裏執行會自動停止並報錯；在真 Thonny 要按紅色「停止」。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>while 條件:</code> 條件 True 就重複；迴圈裏要改變條件用到的變量。</div>
</section>

<!-- 2 Counter & accumulator -->
<section class="card" id="s2" data-title="計數器與累加器" data-short="2 累加">
  <header><div class="chapter">第 2 章</div><h2>計數器與累加器：迴圈最常做的兩件事</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>count += 1</code> 數做了幾次</li><li>用 <code>total += x</code> 把每次的數加起來</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">兩個固定寫法</div>
    <p>很多程式都是「開始時設為 0，迴圈裏每次加一點，結束後印出來」。</p>
    <pre class="ex"><span class="cm"># 累加器：1 + 2 + 3 + 4 + 5</span>
total = 0            <span class="cm"># 迴圈前先設為 0</span>
n = 1
while n &lt;= 5:
    total += n       <span class="cm"># 每次把 n 加進 total</span>
    n += 1
print("總和", total) <span class="cm"># 15</span></pre>
    <pre class="ex"><span class="cm"># 計數器：數有幾多個 3 的倍數</span>
count = 0
n = 1
while n &lt;= 10:
    if n % 3 == 0:
        count += 1   <span class="cm"># 符合條件才加 1</span>
    n += 1
print(count)         <span class="cm"># 3（3、6、9）</span></pre>
    <div class="key">三步：迴圈<b>前</b>設 0 → 迴圈<b>裏</b>加 → 迴圈<b>後</b>印。印的那行不要縮排，否則每次都印。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>total = 0</code> 在迴圈前；<code>total += x</code> 在迴圈裏；<code>print(total)</code> 在迴圈後。</div>
</section>

<!-- 3 break & validation -->
<section class="card" id="s3" data-title="break 與重複輸入" data-short="3 break">
  <header><div class="chapter">第 3 章</div><h2>break：問到對為止</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>while True:</code> 加 <code>break</code> 寫「做到某個情況才停」</li><li>用迴圈重複問，直至輸入有效</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">不知道要重複幾多次</div>
    <p>有時事先不知道要問幾次，例如要使用者輸入 1 至 100 的數，輸入錯就再問。寫法是 <code>while True:</code>（永遠成立），裏面用 <code>break</code> 跳出。</p>
    <pre class="ex">while True:
    n = int(input("輸入 1 至 100 的數："))
    if n &gt;= 1 and n &lt;= 100:
        break               <span class="cm"># 有效：立刻離開迴圈</span>
    print("不對，再試")     <span class="cm"># 無效：印提示，回頭再問</span>
print("你輸入了", n)</pre>
    <p><code>break</code> 一執行，整個 <code>while</code> 立刻結束，跳到迴圈後的第一行。</p>
    <div class="key">這叫<b>數據驗證</b>：不信任使用者的輸入，先檢查範圍。之後很多程式都會用到。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　<code>while True:</code> ＋ <code>break</code>：條件在迴圈裏面判斷，符合才離開。</div>
</section>

<!-- 4 random -->
<section class="card" id="s4" data-title="random：讓電腦抽數字" data-short="4 random">
  <header><div class="chapter">第 4 章</div><h2>random：讓電腦抽一個數字</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>import random</code> 載入模組</li><li>用 <code>random.randint(a, b)</code> 抽 a 至 b 之間的整數</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">模組是別人寫好的工具箱</div>
    <p>Python 本身不會抽數字，但有一個叫 <code>random</code> 的<b>模組</b>會。用之前要先 <code>import</code>（載入）它，通常放在程式最頂。</p>
    <pre class="ex">import random                  <span class="cm"># 載入工具箱</span>
dice = random.randint(1, 6)    <span class="cm"># 1 至 6 之間抽一個整數（包括 1 和 6）</span>
print("擲出", dice)</pre>
    <p>每次執行結果都可能不同。<code>randint(a, b)</code> 兩端都包括：<code>randint(1, 6)</code> 可以是 1、2、3、4、5 或 6。</p>
    <pre class="ex">import random
n = 0
while n &lt; 3:
    print(random.randint(1, 10))   <span class="cm"># 抽三次</span>
    n += 1</pre>
    <div class="key">寫法是 <code>random.randint</code>：先寫模組名、一點、再寫工具名。漏了 <code>import random</code> 會出 <code>NameError</code>。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　<code>import random</code> 放最頂；<code>random.randint(a, b)</code> 抽 a 至 b。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a'],c3:['c3_a'],c4:['c4_a','c4_b']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','迴圈會走幾次？','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'n = 5\nwhile n > 2:\n    print(n)\n    n -= 1\nprint("完")',options:['5\n4\n3\n完','5\n4\n3\n2\n完','5\n4\n完','永遠不停'],answer:0,why:'5、4、3 都 > 2 會印；n 變 2 時 2 > 2 不成立就離開，印「完」。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上缺少的部分，令程式印出 1 至 5 每個數一行。',code:'n = 1\nwhile n ____ 5:\n    print(n)\n    n ____ 1',expect:'1\n2\n3\n4\n5\n',answer:'n = 1\nwhile n <= 5:\n    print(n)\n    n += 1',
    hints:['n 由 1 數到 5，條件是 n <= 5。','每次要令 n 大 1：n += 1。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t=step(h,'try','累加器','估對 4 分');
  makePredict(t,{id:'c2_a',q:'這個程式會印出甚麼？',code:'total = 0\nn = 1\nwhile n <= 4:\n    total += n\n    n += 1\nprint(total)',options:['4','10','1\n3\n6\n10','15'],answer:1,why:'1 + 2 + 3 + 4 = 10。print 在迴圈外，只印一次。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上缺少的部分，計出 1 至 10 之中偶數的個數（應印出 5）。',code:'count = ____\nn = 1\nwhile n <= 10:\n    if n % 2 == 0:\n        count ____ 1\n    n += 1\nprint(count)',expect:'5\n',answer:'count = 0\nn = 1\nwhile n <= 10:\n    if n % 2 == 0:\n        count += 1\n    n += 1\nprint(count)',
    hints:['計數器開始時是 0。','符合條件時加 1：count += 1。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t=step(h,'try','輸入 0、200、50，會印幾多次「不對」？','估對 4 分');
  makePredict(t,{id:'c3_a',q:'執行時依次輸入 0、200、50。「不對，再試」會印幾多次？',code:'while True:\n    n = int(input("輸入 1 至 100："))\n    if n >= 1 and n <= 100:\n        break\n    print("不對，再試")\nprint("你輸入了", n)',options:['0 次','1 次','2 次','3 次'],answer:2,why:'0 和 200 都無效，各印一次；50 有效就 break，不印。執行時試試自己輸入。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上缺少的部分：重複問密碼，直至輸入 1234 才印「歡迎」。',code:'while ____:\n    pw = input("密碼：")\n    if pw == "1234":\n        ____\n    print("錯誤")\nprint("歡迎")',answer:'while True:\n    pw = input("密碼：")\n    if pw == "1234":\n        break\n    print("錯誤")\nprint("歡迎")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.asked!==2)return {ok:false,msg:`測試輸入 0000、1234：程式應問兩次，現在問了 ${res.asked} 次。`};if(!/歡迎\s*$/.test(res.out))return {ok:false,msg:'輸入 1234 後應印「歡迎」並結束。'};if((res.out.match(/錯誤/g)||[]).length!==1)return {ok:false,msg:'輸入 0000 時應印一次「錯誤」。'};return {ok:true,msg:'正確。'};},
    hints:['不知道要問幾次，用 while True:。','密碼對了就 break 離開。'],inputs:['0000','1234']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t1=step(h,'try','抽到甚麼？','估對 4 分');
  makePredict(t1,{id:'c4_a',q:'這個程式會印出甚麼？',code:'import random\nprint(random.randint(7, 7))',options:['7','0 至 7 之間的一個數','每次不同','出錯'],answer:0,why:'randint(7, 7) 由 7 至 7 之間抽，只可能是 7。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','會印幾行？','估對 4 分');
  makePredict(t2,{id:'c4_b',q:'這個程式會印出幾行？',code:'import random\nn = 0\nwhile n < 3:\n    print(random.randint(1, 10))\n    n += 1',options:['1 行','3 行','10 行','不一定'],answer:1,why:'迴圈走 3 次，每次印一個 1 至 10 的數；數字每次不同，但行數一定是 3。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'填上缺少的部分，擲一粒骰子（1 至 6），並印出結果。',code:'____ random\ndice = random.randint(____, ____)\nprint("擲出", dice)',answer:'import random\ndice = random.randint(1, 6)\nprint("擲出", dice)',
    check:async(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。第一行要 import random。'};if(!/random\.randint\(\s*1\s*,\s*6\s*\)/.test(code))return {ok:false,msg:'骰子是 1 至 6：randint(1, 6)。'};for(let i=0;i<5;i++){const r=await runSilent(code,[]);const m=/擲出\s+(\d+)/.exec(r.out);if(!m||+m[1]<1||+m[1]>6)return {ok:false,msg:'應印出「擲出」和一個 1 至 6 的數。'};}return {ok:true,msg:'正確。執行幾次看看結果會變。'};},
    hints:['載入模組的關鍵字是 import。','骰子最小 1、最大 6。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'猜數字遊戲',
   desc:'電腦用 <code>random.randint(1, 100)</code> 抽一個秘密數字。重複問玩家猜一個數：猜大了印「太大」，猜小了印「太小」，猜中印「恭喜」並結束。',
   hints:['secret = random.randint(1, 100)，然後 while True:。','guess = int(input("猜一個數："))','if guess > secret: 太大 / elif guess < secret: 太小 / else: 恭喜 + break'],inputs:['50','25','42'],
   check:async(code,res)=>{if(!/import random/.test(code)||!/random\.randint\(\s*1\s*,\s*100\s*\)/.test(code))return {ok:false,msg:'要用 random.randint(1, 100) 抽秘密數字。'};if(!/while/.test(code))return {ok:false,msg:'要用 while 迴圈重複問。'};
     const fixed=code.replace(/random\.randint\(\s*1\s*,\s*100\s*\)/,'42');const r=await runSilent(fixed,['50','25','42']);if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};
     if(r.asked!==3)return {ok:false,msg:`秘密數字是 42 時，依次猜 50、25、42 應問 3 次，程式問了 ${r.asked} 次（猜中後要結束）。`};const lines=r.out.split('\n');const i1=lines.findIndex(l=>/大/.test(l)),i2=lines.findIndex(l=>/小/.test(l)),i3=lines.findIndex(l=>/恭喜|中/.test(l));
     if(i1<0||i2<0||i3<0||!(i1<i2&&i2<i3))return {ok:false,msg:'猜 50 應印「太大」，猜 25 應印「太小」，猜 42 應印「恭喜」。'};return {ok:true,msg:'猜數字遊戲完成。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'數一數猜了幾次',
   desc:'加一個計數器，每猜一次加 1；猜中時印出「你猜了 __ 次」。',
   hints:['迴圈前 count = 0。','每次 input 之後 count += 1。','恭喜那行印 count。'],inputs:['50','25','42'],
   check:async(code,res)=>{const fixed=code.replace(/random\.randint\(\s*1\s*,\s*100\s*\)/,'42');const r=await runSilent(fixed,['50','25','42']);if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};if(!/3\s*次/.test(r.out))return {ok:false,msg:'猜 50、25、42 三次後應印出「你猜了 3 次」。'};return {ok:true,msg:'進階完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'最多猜 5 次',
   desc:'只可以猜 5 次。5 次都猜不中就印「失敗，答案是 __」並結束。',
   hints:['條件改為 while count < 5:，或在迴圈裏 if count == 5: break。','迴圈後判斷：如果最後一次 guess != secret 就印失敗。'],inputs:['1','2','3','4','5'],
   check:async(code,res)=>{const fixed=code.replace(/random\.randint\(\s*1\s*,\s*100\s*\)/,'42');const r=await runSilent(fixed,['1','2','3','4','5','6','7']);if(r.asked!==5)return {ok:false,msg:`五次都猜錯時應只問 5 次，程式問了 ${r.asked} 次。`};if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};if(r.asked!==5)return {ok:false,msg:`五次都猜錯時應只問 5 次，程式問了 ${r.asked} 次。`};if(!/失敗/.test(r.out)||!/42/.test(r.out))return {ok:false,msg:'5 次猜不中應印「失敗，答案是 42」。'};
     const r2=await runSilent(fixed,['42']);if(r2.asked!==1||!/恭喜|中/.test(r2.out))return {ok:false,msg:'第一次就猜中時仍應印「恭喜」並結束。'};return {ok:true,msg:'挑戰完成。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'n = 0\nwhile n < 3:\n    n += 1\nprint(n)',options:['0','2','3','0\n1\n2'],answer:2,why:'n 變 1、2、3，3 < 3 不成立離開；print 在迴圈外只印最後的 3。'},
  {id:'q2',q:'這個程式會怎樣？',code:'n = 5\nwhile n > 0:\n    print(n)',options:['印 5 到 1','只印一次 5','永遠印 5，不會停','出錯'],answer:2,why:'迴圈裏沒有改變 n，5 > 0 永遠成立，這是無限迴圈。'},
  {id:'q3',q:'印出甚麼？',code:'total = 0\nk = 1\nwhile k <= 3:\n    total += k\n    k += 1\n    print(total)',options:['6','1\n3\n6','1\n2\n3','3'],answer:1,why:'print 縮排了，在迴圈裏，每次都印：1、1+2=3、3+3=6。'},
];
'''

build(5, 'While 迴圈', '四章：while、計數器與累加器、break 與重複輸入、random。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：while、計數器與累加器、break、random，每章都是「學 → 試 → 練」三步，然後做猜數字遊戲和小測。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:9,3:9,4:13}',
      "['第 1 章 while',sc.c[1],9],['第 2 章 計數器與累加器',sc.c[2],9],['第 3 章 break',sc.c[3],9],['第 4 章 random',sc.c[4],13],",
      "[['c1_a','A 5 4 3 完'],['c2_a','B 10'],['c3_a','C 2 次'],['c4_a','A 7'],['c4_b','B 3 行']]",
      """[['練習 1','n <= 5、n += 1'],['練習 2','count = 0、count += 1'],['練習 3','while True:、break'],['練習 4','import、randint(1, 6)']]""",
      '<a href="https://www.w3schools.com/python/python_while_loops.asp" target="_blank" rel="noopener">While Loops</a>、<a href="https://www.w3schools.com/python/ref_random_randint.asp" target="_blank" rel="noopener">random.randint()</a>',
      '例如：我忘記了 n += 1，程式停不了，Assistant 提醒我是無限迴圈……', '猜數字遊戲')
