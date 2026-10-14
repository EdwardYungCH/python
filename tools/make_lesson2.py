# -*- coding: utf-8 -*-
"""由第 1 堂模板產生第 2 堂原始碼。python3 tools/make_lesson2.py"""
import re, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = open(os.path.join(ROOT, 'src/lesson1/lesson1.src.html'), encoding='utf8').read()

def between(s, a, b):
    i = s.index(a); j = s.index(b, i); return i, j

# ---------- 章節 HTML ----------
CH_HTML = r'''<!-- 1 Variables -->
<section class="card" id="s1" data-title="變量：給資料一個名字" data-short="1 變量">
  <header><div class="chapter">第 1 章</div><h2>變量：給資料一個名字</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>=</code> 把資料放進一個變量</li><li>把變量印出來，也可以改它的值</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">變量（variable）是一個有名字的盒子</div>
    <p>上一堂每次都把文字直接寫在 <code>print</code> 裏。如果同一樣東西要用很多次，先把它放進一個<b>變量</b>，之後叫名字就可以。</p>
    <pre class="ex">name = "陳大文"     <span class="cm"># 把文字放進叫 name 的變量</span>
print(name)         <span class="cm"># 印出盒子裏的東西：陳大文</span>
print("你好，", name)
name = "李小明"     <span class="cm"># 盒子裏的東西可以換</span>
print(name)         <span class="cm"># 李小明</span></pre>
    <p>一個 <code>=</code> 的意思是「把右邊放進左邊」，不是數學的「等於」。</p>
    <h3>名字怎樣改</h3>
    <ul class="steps-list">
      <li>用英文字母、數字和底線 <code>_</code>；不可以用空格，不可以由數字開頭。</li>
      <li>分大小寫：<code>name</code> 和 <code>Name</code> 是兩個盒子。</li>
      <li>名字要有意思：<code>score</code> 比 <code>s</code> 好，<code>my_name</code> 比 <code>mn</code> 好。</li>
    </ul>
    <h3>印變量</h3>
    <p>變量<b>不加引號</b>。加了引號就變成印那幾個字母。</p>
    <pre class="ex">cls = "3A"
print("我讀", cls, "班")     <span class="cm"># 我讀 3A 班（逗號會加空格）</span>
print("我讀" + cls + "班")   <span class="cm"># 我讀3A班（+ 直接黐在一起）</span>
print("我讀 cls 班")          <span class="cm"># 我讀 cls 班（引號裏的 cls 只是文字）</span></pre>
    <div class="key">執行後看右邊 <b>Variables</b> 視窗：每個變量和它現在的值都列出來。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>名字 = 值</code> 放進盒子；印變量不加引號；逗號加空格，<code>+</code> 直接相連。</div>
</section>

<!-- 2 Data Types -->
<section class="card" id="s2" data-title="數據類型：文字還是數字" data-short="2 類型">
  <header><div class="chapter">第 2 章</div><h2>數據類型：文字還是數字</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>分辨 <code>str</code>、<code>int</code>、<code>float</code>、<code>bool</code> 四種類型</li><li>用 <code>type()</code> 查一個值是甚麼類型</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">Python 會記住每個值是哪一種</div>
    <div class="tablewrap"><table>
      <thead><tr><th>類型</th><th>英文</th><th>例子</th><th>怎樣認</th></tr></thead>
      <tbody>
        <tr><td>字串（文字）</td><td><code>str</code></td><td><code>"你好"</code>、<code>"3A"</code>、<code>"15"</code></td><td>有引號</td></tr>
        <tr><td>整數</td><td><code>int</code></td><td><code>15</code>、<code>-3</code>、<code>2026</code></td><td>沒有引號，沒有小數點</td></tr>
        <tr><td>小數</td><td><code>float</code></td><td><code>1.65</code>、<code>49.5</code></td><td>沒有引號，有小數點</td></tr>
        <tr><td>布爾（真假）</td><td><code>bool</code></td><td><code>True</code>、<code>False</code></td><td>只有這兩個，開頭大寫</td></tr>
      </tbody>
    </table></div>
    <p>最容易混淆的是 <code>"15"</code> 和 <code>15</code>：有引號的是文字 15，沒引號的是數字 15。文字只能「黐」，數字才能「計」。</p>
    <pre class="ex">print(15 + 1)       <span class="cm"># 16（數字相加）</span>
print("15" + "1")   <span class="cm"># 151（文字相連）</span>
print(type(15))     <span class="cm"># &lt;class 'int'&gt;</span>
print(type("15"))   <span class="cm"># &lt;class 'str'&gt;</span></pre>
    <div class="key"><code>type(x)</code> 會告訴你 <code>x</code> 是甚麼類型。不肯定時就用它查一查。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　有引號是 <code>str</code>；數字分 <code>int</code>（整數）和 <code>float</code>（小數）；<code>True</code>／<code>False</code> 是 <code>bool</code>。</div>
</section>

<!-- 3 User Input -->
<section class="card" id="s3" data-title="輸入：問使用者" data-short="3 輸入">
  <header><div class="chapter">第 3 章</div><h2>輸入：問使用者一條問題</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>input()</code> 問問題，把答案放進變量</li><li>知道 <code>input()</code> 給的永遠是文字</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">input() 會停下來等你打字</div>
    <pre class="ex">name = input("你叫甚麼名字？")   <span class="cm"># 括號內是問題，會印出來</span>
print("你好，" + name + "！")</pre>
    <p>執行時 Shell 會印出問題，然後<b>停住</b>等你打字。你按 Enter 之後，打的字就放進 <code>name</code>，程式才繼續。</p>
    <ul class="steps-list">
      <li>問題後面不會自動換行，你打的字會緊接在問題後面。</li>
      <li>問題文字最好以「？」或「：」結尾，再加一個空格，看起來才整齊。</li>
      <li><b>不論你打甚麼，<code>input()</code> 給的都是文字（<code>str</code>）</b>。打 15，得到的是 <code>"15"</code>。</li>
    </ul>
    <div class="key">想自己試：在模擬器執行後，Shell 會出現一個黃色輸入格，打字後按 Enter。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　<code>變量 = input("問題")</code>；答案是文字；程式會等你按 Enter 才繼續。</div>
</section>

<!-- 4 Casting -->
<section class="card" id="s4" data-title="類型轉換：文字變數字" data-short="4 轉換">
  <header><div class="chapter">第 4 章</div><h2>類型轉換：把文字變成數字</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>int()</code>、<code>float()</code> 把輸入變成數字再計算</li><li>用 <code>str()</code> 把數字變成文字再相連</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">input 給文字，計算要數字</div>
    <p>上一章說過 <code>input()</code> 給的是文字。所以這樣寫會出錯：</p>
    <pre class="ex">age = input("你幾歲？")
print(age + 1)      <span class="cm"># TypeError：文字不可以加數字</span></pre>
    <p>解決方法是先把文字<b>轉換</b>成數字：</p>
    <pre class="ex">age = int(input("你幾歲？"))   <span class="cm"># int() 把 "15" 變成 15</span>
print(age + 1)                  <span class="cm"># 16</span></pre>
    <div class="tablewrap"><table>
      <thead><tr><th>函數</th><th>作用</th><th>例子</th></tr></thead>
      <tbody>
        <tr><td><code>int()</code></td><td>變成整數</td><td><code>int("15")</code> → <code>15</code>；<code>int(3.9)</code> → <code>3</code>（直接去掉小數）</td></tr>
        <tr><td><code>float()</code></td><td>變成小數</td><td><code>float("1.65")</code> → <code>1.65</code>；<code>float(5)</code> → <code>5.0</code></td></tr>
        <tr><td><code>str()</code></td><td>變成文字</td><td><code>str(16)</code> → <code>"16"</code>，之後可以用 <code>+</code> 和文字相連</td></tr>
      </tbody>
    </table></div>
    <pre class="ex">age = 15
print("明年你 " + str(age + 1) + " 歲")   <span class="cm"># 數字要先 str() 才可以用 + 相連</span>
print("明年你", age + 1, "歲")            <span class="cm"># 用逗號就不用轉換</span></pre>
    <div class="key"><code>int("abc")</code> 會出錯（ValueError），因為 abc 不是數字。之後學了判斷才處理這情況。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　<code>int(input(...))</code> 是最常用的寫法；數字要 <code>str()</code> 才可以用 <code>+</code> 黐文字，用逗號則不用。</div>
</section>

'''
i, j = between(src, '<!-- 1 Get Started -->', '<!-- 5 作品 -->')
src = src[:i] + CH_HTML + src[j:]

# ---------- 作品 header ----------
src = src.replace('<section class="card" id="s5" data-title="作品：我的名牌" data-short="5 作品">\n  <header><div class="chapter">作品</div><h2>我的名牌</h2>',
                  '<section class="card" id="s5" data-title="作品：自我介紹機械人" data-short="5 作品">\n  <header><div class="chapter">作品</div><h2>自我介紹機械人</h2>')

# ---------- 章節 JS ----------
CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a'],c3:['c3_a'],c4:['c4_a','c4_b']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','變量換了值之後印甚麼？','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'food = "魚蛋"\nprint("我喜歡", food)\nfood = "燒賣"\nprint("我喜歡 food")',options:['我喜歡 魚蛋\n我喜歡 燒賣','我喜歡 魚蛋\n我喜歡 food','我喜歡 燒賣\n我喜歡 燒賣','出錯'],answer:1,why:'第 2 行印變量（不加引號）得到 魚蛋；第 4 行的 food 在引號裏面，只是四個字母。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上缺少的部分：把班別 3A 放進變量 cls，然後印出「我讀 3A 班」。',code:'____ = "3A"\nprint("我讀", ____, "班")',expect:'我讀 3A 班\n',answer:'cls = "3A"\nprint("我讀", cls, "班")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.out!=='我讀 3A 班\n')return {ok:false,msg:'輸出應該是「我讀 3A 班」。'};if(!/^\s*cls\s*=/m.test(code))return {ok:false,msg:'輸出對了，但變量要叫 cls。'};if(/print\([^)]*"3A"[^)]*\)/.test(code))return {ok:false,msg:'輸出對了，但 print 裏要用變量 cls，不要直接寫 "3A"。'};return {ok:true,msg:'正確。'};},
    hints:['第 1 行左邊是變量的名字 cls。','第 2 行中間放變量 cls，不加引號。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t=step(h,'try','文字和數字相加有甚麼分別？','估對 4 分');
  makePredict(t,{id:'c2_a',q:'這個程式會印出甚麼？',code:'a = "20"\nb = "26"\nc = 20\nd = 26\nprint(a + b)\nprint(c + d)',options:['46\n46','2026\n2026','2026\n46','出錯'],answer:2,why:'a、b 有引號是文字，+ 把它們黐成 2026；c、d 是數字，+ 計出 46。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'填上四個值，令程式印出四種類型：第一個是文字、第二個是整數、第三個是小數、第四個是布爾值。',code:'print(type(____))\nprint(type(____))\nprint(type(____))\nprint(type(____))',expect:"<class 'str'>\n<class 'int'>\n<class 'float'>\n<class 'bool'>\n",answer:'print(type("你好"))\nprint(type(15))\nprint(type(1.65))\nprint(type(True))',
    hints:['文字要有引號，例如 "你好"。','整數沒有小數點（15），小數有（1.65）。','布爾值只有 True 和 False，開頭大寫。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t=step(h,'try','執行時輸入「小明」，最後印出甚麼？','估對 4 分');
  makePredict(t,{id:'c3_a',q:'這個程式最後一行會印出甚麼？（執行時請輸入 小明）',code:'name = input("你叫甚麼名字？")\nprint("你好，" + name + "！")',options:['你好，小明！','你好，name！','你好，+ name +！','出錯'],answer:0,why:'input 把你打的字放進 name；+ 把三段文字黐起來。執行時試試打自己的名字。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上缺少的部分：問使用者最喜歡的科目，然後印出「我最喜歡 ___ 科」。',code:'subject = ____("你最喜歡哪一科？")\nprint("我最喜歡", ____, "科")',answer:'subject = input("你最喜歡哪一科？")\nprint("我最喜歡", subject, "科")',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.asked<1)return {ok:false,msg:'程式要用 input() 問一條問題。'};if(!res.out.includes('我最喜歡 電腦 科'))return {ok:false,msg:'測試輸入「電腦」時，應印出「我最喜歡 電腦 科」。'};return {ok:true,msg:'正確。'};},
    hints:['問問題的指令是 input。','第 2 行中間放變量 subject。'],inputs:['電腦']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t1=step(h,'try','先輸入 3，再輸入 4，印出甚麼？','估對 4 分');
  makePredict(t1,{id:'c4_a',q:'執行時先輸入 3，再輸入 4。最後印出甚麼？',code:'a = input("第一個數：")\nb = input("第二個數：")\nprint(a + b)',options:['7','34','3 + 4','出錯'],answer:1,why:'input 給的是文字，"3" + "4" 是黐起來，變成 34。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','加了 int() 之後呢？','估對 4 分');
  makePredict(t2,{id:'c4_b',q:'執行時輸入 15。最後印出甚麼？',code:'age = int(input("你幾歲？"))\nprint("明年你", age + 1, "歲")',options:['明年你 151 歲','明年你 16 歲','明年你 age + 1 歲','出錯'],answer:1,why:'int() 把 "15" 變成數字 15，15 + 1 = 16；用逗號印數字不用轉換。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'這個程式想計算兩個數的和，但執行會出錯或得到錯的答案。加上轉換，令輸入 3 和 4 時印出 7。',code:'a = input("第一個數：")\nb = input("第二個數：")\nprint("和是", a + b)',answer:'a = int(input("第一個數："))\nb = int(input("第二個數："))\nprint("和是", a + b)',
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.asked<2)return {ok:false,msg:'要問兩個數。'};if(!/和是 7\s*$/m.test(res.out))return {ok:false,msg:'輸入 3 和 4 時，應印出「和是 7」，現在印了：'+res.out.trim().split('\n').pop()};return {ok:true,msg:'正確。'};},
    hints:['input() 外面包一層 int()：int(input("…"))。','兩個輸入都要轉換。'],inputs:['3','4']},done);
})();

'''
i, j = between(src, '/* ---------- 章節 ---------- */', '/* ---------- 作品三層 ---------- */')
src = src[:i] + CH_JS + src[j:]

# makeExercise：支援 inputs（有 input 的練習）；練習的互動執行也要有輸入
src = src.replace("const res=await runSilent(code,[]);let ok,msg;\n    if(cfg.check)", "const res=await runSilent(code,cfg.inputs||[]);let ok,msg;\n    if(cfg.check)")

# ---------- TIERS ----------
TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'問三條問題，介紹自己',
   desc:'程式要用 <code>input()</code> 問三條問題：姓名、班別、興趣，然後印出三行，每行都用到一個答案。例如：「你好，陳大文！」「你讀 3A 班。」「你的興趣是打籃球。」',
   hints:['三個 input，三個 print。','每個 input 的答案放進一個變量，例如 name、cls、hobby。','print 裏用逗號或 + 把文字和變量連起來。'],inputs:['小明','3A','打籃球'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(res.asked<3)return {ok:false,msg:`程式只問了 ${res.asked} 條問題，要問 3 條。`};
     const miss=['小明','3A','打籃球'].filter(x=>!res.out.split('\n').some(l=>l.includes(x)&&!l.includes('？')&&!l.includes('?')));
     if(miss.length)return {ok:false,msg:'輸出沒有用到答案：'+miss.join('、')+'（測試輸入：小明、3A、打籃球）'};return {ok:true,msg:'三條問題都用上了。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'多問年齡，計出明年幾歲',
   desc:'在必做的程式上加第四條問題「你幾歲？」，用 <code>int()</code> 轉成數字，然後印出「明年你 __ 歲」。',
   hints:['age = int(input("你幾歲？"))','print("明年你", age + 1, "歲")'],inputs:['小明','3A','打籃球','15'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。輸入 15 時 age + 1 要先把文字轉成數字。'};if(res.asked<4)return {ok:false,msg:`程式只問了 ${res.asked} 條問題，要問 4 條。`};if(!/16/.test(res.out))return {ok:false,msg:'輸入 15 歲時，應印出 16（明年）。'};if(!/int\(/.test(code))return {ok:false,msg:'要用 int() 把輸入轉成數字。'};return {ok:true,msg:'進階完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'由出生年份計年齡',
   desc:'改為問「你哪一年出生？」，用今年（2026）減去出生年份，印出「你今年 __ 歲」。要用 <code>+</code> 把句子黐起來，所以數字要 <code>str()</code>。',
   hints:['year = int(input("你哪一年出生？"))','age = 2026 - year','print("你今年 " + str(age) + " 歲")：用 + 就要 str()。'],inputs:['小明','3A','打籃球','2011'],
   check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。用 + 黐數字要先 str()。'};if(!/你今年 ?15 ?歲/.test(res.out))return {ok:false,msg:'輸入 2011 時，應印出「你今年 15 歲」。'};if(!/str\(/.test(code))return {ok:false,msg:'輸出對了，但這題要練習 str()：用 + 把句子黐起來。'};return {ok:true,msg:'挑戰完成。'};}},
];
'''
i, j = between(src, 'const TIERS=[', 'TIERS.forEach(')
src = src[:i] + TIERS + src[j:]
# tiers check: runSilent with inputs
src = src.replace("const res=await runSilent(code,[]);const c=t.check(code,res);await r.run();", "const res=await runSilent(code,t.inputs||[]);const c=t.check(code,res);await r.run();")

# ---------- QUIZ ----------
QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'x = 5\nx = x + 2\nprint(x)',options:['5','7','x + 2','出錯'],answer:1,why:'第 2 行把 5 + 2 = 7 放回 x。'},
  {id:'q2',q:'印出甚麼？',code:'print("3" + "4")\nprint(3 + 4)',options:['7\n7','34\n34','34\n7','7\n34'],answer:2,why:'有引號是文字相連，沒有引號是數字相加。'},
  {id:'q3',q:'執行時輸入 15，會怎樣？',code:'age = input("你幾歲？")\nprint(age + 1)',options:['印出 16','印出 151','出錯（TypeError）','印出 15'],answer:2,why:'input 給的是文字 "15"，文字不可以加數字 1，所以 TypeError。要先 int()。'},
];
'''
i, j = between(src, 'const QUIZ=[', 'QUIZ.forEach(')
src = src[:i] + QUIZ + src[j:]

# ---------- 常數、標題、報告、老師區 ----------
src = src.replace('<title>開始寫 Python</title>', '<title>變量與輸入</title>')
src = src.replace('<div class="lesson">中三 Python 編程 · 第 1 堂</div><h1>開始寫 Python</h1>', '<div class="lesson">中三 Python 編程 · 第 2 堂</div><h1>變量與輸入</h1>')
src = src.replace("const KEY='py3:L1v2', PIN='py2026', SIGN='py3-l1-sign-2026', APP='PY3-L1';", "const KEY='py3:L2v2', PIN='py2026', SIGN='py3-l2-sign-2026', APP='PY3-L2';")
src = src.replace("const CH_MAX={1:9,2:9,3:13,4:9};", "const CH_MAX={1:9,2:9,3:9,4:13};")
src = src.replace("cfg.filename||('L01_'", "cfg.filename||('L02_'")
src = src.replace("const rows=[['第 1 章 開始',sc.c[1],9],['第 2 章 語法',sc.c[2],9],['第 3 章 輸出',sc.c[3],13],['第 4 章 註解',sc.c[4],9],", "const rows=[['第 1 章 變量',sc.c[1],9],['第 2 章 數據類型',sc.c[2],9],['第 3 章 輸入',sc.c[3],9],['第 4 章 類型轉換',sc.c[4],13],")
src = src.replace('中三 Python 第 1 堂 開始寫 Python', '中三 Python 第 2 堂 變量與輸入')
src = src.replace("const preds=[['c1_a','A Hello, World!'],['c2_a','C 出錯，兩行都不印'],['c3_a','C 7 / 3 + 4'],['c3_b','B 分數： 95'],['c4_a','B 2 行']];",
                  "const preds=[['c1_a','B 我喜歡 魚蛋 / 我喜歡 food'],['c2_a','C 2026 / 46'],['c3_a','A 你好，小明！'],['c4_a','B 34'],['c4_b','B 明年你 16 歲']];")
src = src.replace("""const exs=[['練習 1','print("Hello, Python!")'],['練習 2','print("Python 分大小寫") / print("行首不可以有空格")'],['練習 3','print(10) / print("一共", 10, "件")'],['練習 4','# 練習 4 / # print("測試中，之後刪去")']];""",
                  """const exs=[['練習 1','cls = "3A" / print("我讀", cls, "班")'],['練習 2','type("你好") type(15) type(1.65) type(True)'],['練習 3','input("…") / print("我最喜歡", subject, "科")'],['練習 4','a = int(input(…)) b = int(input(…))']];""")
src = re.sub(r'<p class="small">課後重溫（英文）：.*?</p>',
             '<p class="small">課後重溫（英文）：<a href="https://www.w3schools.com/python/python_variables.asp" target="_blank" rel="noopener">Variables</a>、<a href="https://www.w3schools.com/python/python_datatypes.asp" target="_blank" rel="noopener">Data Types</a>、<a href="https://www.w3schools.com/python/python_user_input.asp" target="_blank" rel="noopener">User Input</a>、<a href="https://www.w3schools.com/python/python_casting.asp" target="_blank" rel="noopener">Casting</a></p>', src)
src = src.replace('<p class="small">四章：開始、語法、輸出、註解。每章先讀，再「試一試」，最後做「練習」。</p>', '<p class="small">四章：變量、數據類型、輸入、類型轉換。每章先讀，再「試一試」，最後做「練習」。</p>')
src = src.replace('中三 Python 編程 · 第 1 堂 · 版本 2.2', '中三 Python 編程 · 第 2 堂 · 版本 1.0')
src = src.replace('placeholder="例如：我先看 Shell 紅字最後一行的英文名稱和行號，再看 Assistant……"', 'placeholder="例如：TypeError 出現時我想起 input 給的是文字，要加 int()……"')
src = src.replace('這一堂有四章，每章都是「學 → 試 → 練」三步，然後做一個作品和小測。', '這一堂有四章：變量、數據類型、輸入、類型轉換，每章都是「學 → 試 → 練」三步，然後做一個會問問題的作品和小測。')

assert 'Get Started' not in src and 'demo1' not in src, '模板殘留'
out = os.path.join(ROOT, 'src/lesson2/lesson2.src.html')
open(out, 'w', encoding='utf8').write(src)
print('written', out, len(src))
