# -*- coding: utf-8 -*-
"""第 7 堂「字串」。python3 tools/make_lesson7.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build

CH_HTML = r'''<!-- 1 索引 -->
<section class="card" id="s1" data-title="字串、長度與索引" data-short="1 索引">
  <header><div class="chapter">第 1 章</div><h2>字串是一串字符，每個都有編號</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>len()</code> 數字串有幾多個字符</li><li>用 <code>s[0]</code>、<code>s[-1]</code> 取出某一個字符</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">由 0 開始數</div>
    <p>字串（string）就是引號裏的文字。它由一個個<b>字符</b>組成，每個字符有一個編號叫<b>索引</b>，<b>由 0 開始</b>。</p>
    <div class="tablewrap"><table>
      <thead><tr><th>字符</th><td>P</td><td>y</td><td>t</td><td>h</td><td>o</td><td>n</td></tr></thead>
      <tbody><tr><th>索引</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
      <tr><th>負索引</th><td>-6</td><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr></tbody>
    </table></div>
    <pre class="ex">s = "Python"
print(len(s))        <span class="cm"># 6：一共 6 個字符</span>
print(s[0])          <span class="cm"># P：第一個</span>
print(s[5])          <span class="cm"># n：最後一個（索引 = 長度 − 1）</span>
print(s[-1])         <span class="cm"># n：-1 也是最後一個，由後數起</span>
print("th" in s)     <span class="cm"># True：s 裏面有沒有 "th"</span></pre>
    <div class="key">最後一個字符的索引是 <code>len(s) - 1</code>，不是 <code>len(s)</code>；<code>s[6]</code> 會出 <code>IndexError</code>。空格和標點都算一個字符。</div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　<code>len(s)</code> 長度；<code>s[i]</code> 第 i 個（由 0 起）；<code>s[-1]</code> 最後一個；<code>x in s</code> 有沒有。</div>
</section>

<!-- 2 切片 -->
<section class="card" id="s2" data-title="切片：取一段" data-short="2 切片">
  <header><div class="chapter">第 2 章</div><h2>切片：取一段出來</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>s[a:b]</code> 取索引 a 至 b − 1 的一段</li><li>省略 a 或 b 的意思</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">和 range 一樣：終點不包括</div>
    <pre class="ex">s = "Hello, Kowloon"
print(s[0:5])        <span class="cm"># Hello：索引 0 至 4</span>
print(s[7:14])       <span class="cm"># Kowloon</span>
print(s[:5])         <span class="cm"># Hello：省略起點 = 由 0 開始</span>
print(s[7:])         <span class="cm"># Kowloon：省略終點 = 直到結尾</span>
print(s[-7:])        <span class="cm"># Kowloon：最後 7 個</span></pre>
    <p>切片不會改變原本的字串，只是取一份出來。要記住：<code>s[2:5]</code> 取 3 個字符（5 − 2），不是 4 個。</p>
    <div class="key">電話號碼、身份證、日期都常常要切：<code>"2026-10-14"[0:4]</code> 是年份 <code>"2026"</code>。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　<code>s[a:b]</code> 由 a 到 b − 1；<code>s[:b]</code> 開頭起；<code>s[a:]</code> 到結尾。</div>
</section>

<!-- 3 方法與 f-string -->
<section class="card" id="s3" data-title="字串方法與 f-string" data-short="3 方法">
  <header><div class="chapter">第 3 章</div><h2>字串方法與 f-string</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>upper()</code>、<code>lower()</code>、<code>strip()</code>、<code>replace()</code>、<code>count()</code></li><li>用 f-string 把變量放進句子</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">方法：字串自帶的工具，用一點叫出來</div>
    <pre class="ex">s = "  Hello, Kowloon  "
print(s.upper())            <span class="cm"># "  HELLO, KOWLOON  "：全部大寫</span>
print(s.lower())            <span class="cm"># 全部小寫</span>
print(s.strip())            <span class="cm"># "Hello, Kowloon"：刪去頭尾的空格</span>
print(s.replace("l", "L"))  <span class="cm"># 把所有 l 換成 L</span>
print(s.count("l"))         <span class="cm"># 3：l 出現了幾多次</span></pre>
    <p>方法<b>不會改變</b>原本的 <code>s</code>，它只是交回一個新字串。要保留結果，就賦值回去：<code>s = s.strip()</code>。</p>
    <h3>f-string：把變量放進句子最方便的寫法</h3>
    <pre class="ex">name = "小明"
score = 95
print("你好，" + name + "，你有 " + str(score) + " 分")   <span class="cm"># 用 + 要自己轉 str，很麻煩</span>
print(f"你好，{name}，你有 {score} 分")                   <span class="cm"># f-string：引號前加 f，變量放在 {}</span>
print(f"下次目標 {score + 5} 分")                         <span class="cm"># {} 裏可以計算</span></pre>
    <div class="key">記住引號前的 <code>f</code>，沒有它 <code>{name}</code> 會照字印出來。</div>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　<code>s.upper()</code> 等方法交回新字串；<code>f"…{變量}…"</code> 把變量放進句子。</div>
</section>

<!-- 4 逐字處理 -->
<section class="card" id="s4" data-title="逐字處理" data-short="4 逐字">
  <header><div class="chapter">第 4 章</div><h2>用 for 逐個字符處理</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>用 <code>for ch in s:</code> 逐個字符看</li><li>用 <code>isdigit()</code>、<code>isupper()</code>、<code>isalpha()</code> 判斷字符種類</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">for 不只可以數數字，也可以逐個字符走</div>
    <pre class="ex">for ch in "abc":
    print(ch)            <span class="cm"># a、b、c 各一行</span></pre>
    <p>配合計數器，就可以統計字串裏有幾多個某種字符：</p>
    <pre class="ex">pw = "ab12cd3"
digits = 0
for ch in pw:
    if ch.isdigit():     <span class="cm"># 這個字符是不是數字？</span>
        digits += 1
print("有", digits, "個數字")   <span class="cm"># 3</span></pre>
    <div class="tablewrap"><table>
      <thead><tr><th>方法</th><th>True 的情況</th></tr></thead>
      <tbody>
        <tr><td><code>ch.isdigit()</code></td><td>是 0 至 9 的數字</td></tr>
        <tr><td><code>ch.isalpha()</code></td><td>是英文字母（或中文字）</td></tr>
        <tr><td><code>ch.isupper()</code></td><td>是大寫字母</td></tr>
        <tr><td><code>ch.islower()</code></td><td>是小寫字母</td></tr>
        <tr><td><code>ch.isspace()</code></td><td>是空格</td></tr>
      </tbody>
    </table></div>
    <div class="key">這些方法用在單一字符或整個字串都可以：<code>"123".isdigit()</code> 是 True，<code>"12a".isdigit()</code> 是 False。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　<code>for ch in s:</code> 逐個字符；<code>ch.isdigit()</code> 等判斷種類；配合計數器統計。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:['c1_a'],c2:['c2_a'],c3:['c3_a','c3_b'],c4:['c4_a']};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}

(function(){const h=$('#c1');const done=chapterDone(1);
  const t=step(h,'try','索引由 0 開始','估對 4 分');
  makePredict(t,{id:'c1_a',q:'這個程式會印出甚麼？',code:'s = "Hong Kong"\nprint(len(s))\nprint(s[0], s[4], s[-1])',options:['8\nH K g','9\nH   g','9\nH K g','8\nH o g'],answer:1,why:'空格也算一個字符，長度是 9；s[4] 是第 5 個字符，就是那個空格。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c1_ex',ch:'c1',q:'填上索引，令程式印出 P 和 n（Python 的第一個和最後一個字符）。',code:'s = "Python"\nprint(s[____])\nprint(s[____])',expect:'P\nn\n',answer:'s = "Python"\nprint(s[0])\nprint(s[-1])',
    hints:['第一個字符的索引是 0。','最後一個可以用 -1，或者 len(s) - 1 = 5。']},done);
})();
(function(){const h=$('#c2');const done=chapterDone(2);
  const t=step(h,'try','終點不包括','估對 4 分');
  makePredict(t,{id:'c2_a',q:'這個程式會印出甚麼？',code:'s = "ABCDEFG"\nprint(s[1:4])\nprint(s[4:])',options:['BCD\nEFG','BCDE\nEFG','ABCD\nDEFG','BCD\nDEFG'],answer:0,why:'s[1:4] 是索引 1、2、3 → BCD；s[4:] 由索引 4 到尾 → EFG。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c2_ex',ch:'c2',q:'用切片把日期拆開：印出年份 2026 和月份 10。',code:'d = "2026-10-14"\nprint(d[____:____])\nprint(d[____:____])',expect:'2026\n10\n',answer:'d = "2026-10-14"\nprint(d[0:4])\nprint(d[5:7])',
    hints:['年份是索引 0 至 3，寫 [0:4]。','月份在「-」之後：索引 5 和 6，寫 [5:7]。']},done);
})();
(function(){const h=$('#c3');const done=chapterDone(3);
  const t1=step(h,'try','方法不改變原本的字串','估對 4 分');
  makePredict(t1,{id:'c3_a',q:'這個程式會印出甚麼？',code:'s = "hello"\ns.upper()\nprint(s)\nprint(s.upper())',options:['HELLO\nHELLO','hello\nHELLO','hello\nhello','出錯'],answer:1,why:'第 2 行的 s.upper() 交回新字串但沒有存起來，s 仍是 hello；第 4 行才印大寫。'},S.pred,PRED_PTS,done);
  const t2=step(h,'try','有沒有 f？','估對 4 分');
  makePredict(t2,{id:'c3_b',q:'這個程式會印出甚麼？',code:'n = 3\nprint("{n} 個")\nprint(f"{n} 個")',options:['3 個\n3 個','{n} 個\n3 個','{n} 個\n{n} 個','出錯'],answer:1,why:'第一句沒有 f，{n} 只是普通文字；第二句有 f，{n} 被換成 3。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c3_ex',ch:'c3',q:'填上缺少的部分：把輸入的名字刪去頭尾空格、改成大寫，再用 f-string 印出「歡迎，AMY！」（測試輸入是「  amy  」）。',code:'name = input("名字：")\nname = name.____().____()\nprint(____"歡迎，{name}！")',answer:'name = input("名字：")\nname = name.strip().upper()\nprint(f"歡迎，{name}！")',inputs:['  amy  '],
    check:(code,res)=>{if(res.err)return {ok:false,msg:'程式出錯，看看 Shell 的錯誤訊息。'};if(!/歡迎，AMY！/.test(res.out))return {ok:false,msg:'輸入「  amy  」後應印出「歡迎，AMY！」，現在印出：'+res.out.split('\n').filter(l=>l.includes('歡迎')).join(' ')};if(!/\.strip\(\)/.test(code)||!/\.upper\(\)/.test(code))return {ok:false,msg:'要用 strip() 和 upper()。'};if(!/print\(\s*f"/.test(code))return {ok:false,msg:'要用 f-string：print(f"…")。'};return {ok:true,msg:'正確。'};},
    hints:['刪頭尾空格是 strip()，大寫是 upper()，可以連着用。','f-string 要在引號前加 f。']},done);
})();
(function(){const h=$('#c4');const done=chapterDone(4);
  const t=step(h,'try','數有幾多個大寫','估對 4 分');
  makePredict(t,{id:'c4_a',q:'這個程式會印出甚麼？',code:'s = "Hello World"\nn = 0\nfor ch in s:\n    if ch.isupper():\n        n += 1\nprint(n)',options:['0','1','2','11'],answer:2,why:'逐個字符看，H 和 W 是大寫，一共 2 個。'},S.pred,PRED_PTS,done);
  const e=step(h,'ex','練習','答對 5 分');
  makeExercise(e,{id:'c4_ex',ch:'c4',q:'填上缺少的部分，數出字串裏有幾多個數字（應印出 4）。',code:'s = "a1b22c3"\ncount = 0\nfor ____ in s:\n    if ch.____():\n        count += 1\nprint(count)',expect:'4\n',answer:'s = "a1b22c3"\ncount = 0\nfor ch in s:\n    if ch.isdigit():\n        count += 1\nprint(count)',
    hints:['for 後面的變量名要和下面 if 用的一樣：ch。','判斷是不是數字的方法是 isdigit()。']},done);
})();

'''

TIERS = r'''const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'密碼強度檢查器',
   desc:'問使用者輸入密碼。如果<b>長度最少 8</b>、<b>有數字</b>、<b>有大寫字母</b>三樣都符合，印「強」；否則印「弱」，並印出缺了甚麼（例如「太短」「沒有數字」「沒有大寫」）。',
   hints:['用 len(pw) >= 8 檢查長度。','用 for ch in pw: 配合 ch.isdigit() 和 ch.isupper() 找有沒有數字和大寫，可以用兩個計數器或 True/False 變量。','最後 if 三樣都 True 印「強」，否則印「弱」和原因。'],inputs:['abc'],
   check:async(code,res)=>{if(!/for\s+\w+\s+in/.test(code))return {ok:false,msg:'要用 for 逐個字符檢查。'};if(!/isdigit\(\)/.test(code)||!/isupper\(\)/.test(code))return {ok:false,msg:'要用 isdigit() 和 isupper()。'};
     const cases=[['abc','弱',/太短|不夠|長度|沒有數字|沒有大寫/],['Abcdefg1','強',null],['abcdefg1','弱',/大寫/],['ABCDEFGH','弱',/數字/]];
     for(const [inp,want,re] of cases){const r=await runSilent(code,[inp]);if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};if(r.asked!==1)return {ok:false,msg:'要問一次密碼。'};const o=r.out.replace(/密碼[^\n]*\n/,'');if(!o.includes(want))return {ok:false,msg:`輸入「${inp}」應印「${want}」，現在印出：${o.trim().split('\n').join(' / ')||'（沒有）'}`};if(re&&!re.test(o))return {ok:false,msg:`輸入「${inp}」是弱密碼，要印出原因（例如太短、沒有數字、沒有大寫）。`};}
     return {ok:true,msg:'密碼強度檢查器完成，四組測試都通過。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'統計元音',
   desc:'問使用者一句英文，數出裏面有幾多個元音（a、e、i、o、u，大小寫都算），印「元音：N 個」。例如 Hello World 有 3 個。',
   hints:['先 s = s.lower()，就不用理大小寫。','for ch in s: if ch in "aeiou": count += 1'],inputs:['Hello World'],
   check:async(code,res)=>{for(const [inp,n] of [['Hello World',3],['PYTHON is FUN',3],['xyz',0]]){const r=await runSilent(code,[inp]);if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};const o=r.out.replace(/^[^\n]*：[^\n]*\n/,'');if(!new RegExp('\\b'+n+'\\b').test(r.out.split('\n').slice(-2).join(' ')))return {ok:false,msg:`「${inp}」有 ${n} 個元音，程式印出：${r.out.trim().split('\n').pop()}`};}return {ok:true,msg:'統計元音完成。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'凱撒密碼',
   desc:'問一段小寫英文和一個數字 k，把每個字母向後移 k 個（z 之後回到 a），印出密文。例如 abc 移 1 是 bcd，xyz 移 2 是 zab。提示：<code>ord("a")</code> 是 97，<code>chr(98)</code> 是 "b"；用 <code>(ord(ch) - 97 + k) % 26 + 97</code>。',
   hints:['result = ""，然後 for ch in text: 逐個字符算新字符，result += 新字符。','新字符 = chr((ord(ch) - 97 + k) % 26 + 97)。','% 26 令 z 之後回到 a。'],inputs:['abc','1'],
   check:async(code,res)=>{for(const [t,k,want] of [['abc','1','bcd'],['xyz','2','zab'],['hello','13','uryyb']]){const r=await runSilent(code,[t,k]);if(r.err)return {ok:false,msg:'程式出錯：'+r.err.split('\n').pop()};if(r.asked!==2)return {ok:false,msg:'要問文字和數字兩次。'};if(!r.out.includes(want))return {ok:false,msg:`「${t}」移 ${k} 應是 ${want}，程式印出：${r.out.trim().split('\n').pop()}`};}return {ok:true,msg:'凱撒密碼完成。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'印出甚麼？',code:'s = "apple"\nprint(s[1:3], len(s))',options:['ap 5','pp 5','ppl 5','pp 4'],answer:1,why:'s[1:3] 是索引 1 和 2 → pp；長度 5。'},
  {id:'q2',q:'印出甚麼？',code:'s = "Hi"\nprint(s.lower() + s.upper())',options:['HiHi','hihi','hiHI','HIhi'],answer:2,why:'lower() 交回 hi，upper() 交回 HI，+ 把兩個接起來。'},
  {id:'q3',q:'印出甚麼？',code:'n = 0\nfor ch in "a1b2c3":\n    if ch.isalpha():\n        n += 1\nprint(f"{n} 個")',options:['3 個','6 個','{n} 個','a b c'],answer:0,why:'isalpha() 只有 a、b、c 是 True；f-string 把 n 換成 3。'},
];
'''

build(7, '字串', '四章：索引、切片、字串方法與 f-string、逐字處理。每章先讀，再「試一試」，最後做「練習」。',
      '這一堂有四章：索引、切片、字串方法與 f-string、逐字處理，每章都是「學 → 試 → 練」三步，然後做密碼強度檢查器和小測。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:9,2:9,3:13,4:9}',
      "['第 1 章 索引',sc.c[1],9],['第 2 章 切片',sc.c[2],9],['第 3 章 方法與 f-string',sc.c[3],13],['第 4 章 逐字處理',sc.c[4],9],",
      "[['c1_a','B 9 / H 空格 g'],['c2_a','A BCD / EFG'],['c3_a','B hello / HELLO'],['c3_b','B {n} 個 / 3 個'],['c4_a','C 2']]",
      """[['練習 1','s[0]、s[-1]'],['練習 2','d[0:4]、d[5:7]'],['練習 3','strip().upper()、f"…"'],['練習 4','for ch in s、isdigit()']]""",
      '<a href="https://www.w3schools.com/python/python_strings.asp" target="_blank" rel="noopener">Strings</a>、<a href="https://www.w3schools.com/python/python_strings_slicing.asp" target="_blank" rel="noopener">Slicing</a>、<a href="https://www.w3schools.com/python/python_strings_methods.asp" target="_blank" rel="noopener">String Methods</a>、<a href="https://www.w3schools.com/python/python_string_formatting.asp" target="_blank" rel="noopener">f-string</a>',
      '例如：我忘記了索引由 0 開始，s[5] 出了 IndexError……', '密碼強度檢查器')
