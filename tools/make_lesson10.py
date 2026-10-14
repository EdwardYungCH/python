# -*- coding: utf-8 -*-
"""第 10 堂「迷你專題及選科導航」。python3 tools/make_lesson10.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lessongen import build, ROOT

CH_HTML = r'''<!-- 1 規劃 -->
<section class="card" id="s1" data-title="專題規劃與測試數據" data-short="1 規劃">
  <header><div class="chapter">第 1 章</div><h2>專題規劃與測試數據</h2>
    <div class="goal"><b>這一堂你會：</b><ul><li>按上一堂的規劃表完成一個自己的程式</li><li>先定好測試數據，做完用它檢查</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">先定測試，後寫程式</div>
    <p>上一堂你寫的專題規劃表：</p>
    <pre class="ex" id="planBox">（找不到上一堂的規劃表。如果你在另一部電腦做第 9 堂，請把規劃表重新寫在下面的測試數據旁。）</pre>
    <p>專題要求：<b>有 input、有 if、有迴圈</b>，最少 12 行；可選題目：問答遊戲、小食部收銀機、文字冒險、海龜藝術，或自訂。進階要用到<b>列表或函數</b>。</p>
    <div class="key">程式做好後，網頁會用你下面寫的測試數據自動執行一次；所以輸入要和程式問的次序一樣，每行一個。預期輸出寫一個一定會出現的字或數。</div>
  </div>
  <div class="step make"><span class="mark">做</span>
    <div class="lead">寫兩組測試數據<small>5 分</small></div>
    <div class="row">
      <label class="f">第 1 組：正常情況的輸入（每行一個）<textarea id="t1in" rows="4" placeholder="例如：&#10;10&#10;20&#10;100"></textarea></label>
      <label class="f">第 1 組：預期輸出會出現的字或數<input type="text" id="t1out" placeholder="例如：找續 70"></label>
    </div>
    <div class="row">
      <label class="f">第 2 組：邊界或錯誤情況的輸入（每行一個）<textarea id="t2in" rows="4" placeholder="例如：&#10;10&#10;20&#10;5"></textarea></label>
      <label class="f">第 2 組：預期輸出會出現的字或數<input type="text" id="t2out" placeholder="例如：不夠錢"></label>
    </div>
    <div class="row"><button class="btn go" id="btnPlan">儲存測試數據</button><span class="small" id="planFb"></span></div>
  </div>
  <div id="c1"></div>
  <div class="summary"><b>小結</b>　測試數據先定好：一組正常、一組邊界或錯誤，各寫明預期輸出。</div>
</section>

<!-- 2 ICT -->
<section class="card" id="s2" data-title="ICT 高中讀甚麼" data-short="2 ICT">
  <header><div class="chapter">第 2 章</div><h2>ICT 高中讀甚麼？</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>知道高中「資訊及通訊科技」科不只是編程</li><li>知道必修、選修和校本評核的比重</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">編程佔三分之一，其餘是理論和應用</div>
    <div class="tablewrap"><table>
      <thead><tr><th>部分</th><th>內容</th><th>時數</th></tr></thead>
      <tbody>
        <tr><td rowspan="5"><b>必修</b><br>144 小時</td><td>資訊處理：資訊系統、數據表示（二進制、字符、圖像）、試算表、數據庫</td><td>37</td></tr>
        <tr><td>電腦系統基礎：硬件、記憶體、操作系統</td><td>20</td></tr>
        <tr><td>互聯網及其應用：網絡、IP、網頁、網上保安</td><td>31</td></tr>
        <tr><td><b>計算思維與程式編寫</b>：你這十堂學的東西，再加流程圖、偽代碼、追蹤表</td><td><b>48</b></td></tr>
        <tr><td>資訊及通訊科技對社會的影響：科技創新、健康與道德、知識產權</td><td>8</td></tr>
        <tr><td><b>選修</b><br>76 小時</td><td>三選二：數據庫（SQL）／網絡應用程式開發（HTML、CSS、JavaScript、PHP）／算法與程式編寫（Python 進階：排序、搜尋、檔案）</td><td>76</td></tr>
        <tr><td><b>校本評核</b><br>30 小時</td><td>中五至中六做一個真實的小型系統：設計、實施、測試、評估</td><td>30</td></tr>
      </tbody>
    </table></div>
    <p>公開考試：卷一考必修（55%）、卷二考選修（25%）、校本評核（20%）。程式語言是 <b>Python</b>，和你這十堂一樣。</p>
    <p>出路：大學的計算機科學、資訊工程、數據科學、人工智能、資訊系統、數碼媒體等；也是很多理科、商科課程的加分科目。</p>
    <div class="key">適合讀 ICT 的人：喜歡動手解難、不怕程式出錯慢慢找；也要不介意讀理論（網絡、硬件、數據表示）。</div>
  </div>
  <div id="c2"></div>
  <div class="summary"><b>小結</b>　必修 144 小時（編程 48）、選修三選二 76 小時、校本評核 30 小時；卷一 55%、卷二 25%、校本評核 20%。</div>
</section>

<!-- 3 真 Thonny -->
<section class="card" id="s3" data-title="真 Thonny 體驗" data-short="3 Thonny">
  <header><div class="chapter">第 3 章</div><h2>開一次真正的 Thonny</h2>
    <div class="goal"><b>學完這章你會：</b><ul><li>在電腦室開啟真正的 Thonny，貼上你的程式執行</li><li>知道真 Thonny 和網頁模擬器的分別</li></ul></div></header>
  <div class="step learn"><span class="mark">學</span>
    <div class="lead">中四用的就是它</div>
    <ol class="steps-list">
      <li>在電腦室的電腦開啟 <b>Thonny</b>（開始選單搜尋 Thonny）。</li>
      <li>把你在這個網頁寫好的專題程式全選複製，貼到 Thonny 上面的編輯器。</li>
      <li>按綠色 ▶（或 F5）。第一次會叫你儲存：檔名用 <code>L10_你的名字.py</code>，存到老師指定的資料夾。</li>
      <li>在 Shell 輸入你的測試數據，看結果是否一樣。</li>
      <li>試試 Thonny 的 <b>View → Variables</b>，和 <b>Debug</b>（蟲仔圖示）→ <b>Step over</b>，和這裏的逐步執行是同一件事。</li>
    </ol>
    <p>真 Thonny 的分別：程式存成 <code>.py</code> 檔案在電腦裏；錯誤訊息是英文（沒有 Assistant 的中文）；可以安裝其他模組；沒有執行時間限制，無限迴圈要按紅色「停止」。</p>
  </div>
  <div class="step make"><span class="mark">做</span>
    <div class="lead">完成後剔選<small>8 分</small></div>
    <div id="thonnyChecks"></div>
    <label class="f">真 Thonny 和這裏的模擬器，你發現有甚麼不同？（最少 20 字）<textarea id="thonnyDiff" rows="3"></textarea></label>
    <div class="row"><button class="btn go" id="btnThonny">提交</button><span class="small" id="thonnyFb"></span></div>
    <p class="small">如果今天不能用電腦室，老師可以用 PIN 免除這一章。</p>
  </div>
  <div id="c3"></div>
  <div class="summary"><b>小結</b>　真 Thonny 存 .py 檔、英文錯誤訊息、要自己按停止；其餘和這裏一樣。</div>
</section>

<!-- 4 自我檢視 -->
<section class="card" id="s4" data-title="我適合讀 ICT 嗎？" data-short="4 檢視">
  <header><div class="chapter">第 4 章</div><h2>我適合讀 ICT 嗎？</h2>
    <div class="goal"><b>這一章：</b><ul><li>回看這十堂的經歷，誠實評一評自己</li><li>結果只供你和老師參考，不設門檻</li></ul></div></header>
  <div class="step make"><span class="mark">做</span>
    <div class="lead">六條問題，每條 1 至 4 分<small>15 分（完成即得）</small></div>
    <div id="selfCheck"></div>
    <div class="row"><button class="btn go" id="btnSelf">看結果</button><span class="small" id="selfFb"></span></div>
    <div id="selfResult"></div>
    <div class="key">堅持和興趣比打字快慢重要。分數不高但享受解難的同學，同樣值得考慮 ICT。</div>
  </div>
  <div id="c4"></div>
  <div class="summary"><b>小結</b>　選科看三樣：喜不喜歡解難、介不介意讀理論、有沒有自己動手的衝動。</div>
</section>

'''

CH_JS = r'''/* ---------- 章節 ---------- */
function step(host,kind,lead,pts){const d=document.createElement('div');d.className='step '+kind;d.innerHTML=`<span class="mark">${kind==='try'?'試':kind==='ex'?'練':'做'}</span><div class="lead">${esc(lead)}${pts?`<small>${esc(pts)}</small>`:''}</div>`;host.appendChild(d);return d;}
const PRED_IDS={c1:[],c2:['c2_a','c2_b','c2_c'],c3:[],c4:[]};
function chapterDone(i){return()=>{refreshScore();if(chapterComplete(i))advance(i+1);};}
function setEx(ch,score,extra){S.ex[ch]=Object.assign({ok:true,score},extra||{});save();refreshScore();}

/* 第 1 章：讀取上一堂的規劃表；儲存兩組測試數據 */
(function(){
  try{const r=localStorage.getItem('py3:L9v2');if(r){const o=JSON.parse(r);if(o&&o.quiz&&o.quiz.reflect)$('#planBox').textContent=o.quiz.reflect;}}catch(e){}
  const rec=S.ex.c1;if(rec&&rec.ok){$('#t1in').value=rec.t1in;$('#t1out').value=rec.t1out;$('#t2in').value=rec.t2in;$('#t2out').value=rec.t2out;$('#planFb').innerHTML='<span class="badge">✓ 已儲存，5 分</span>';}
  $('#btnPlan').addEventListener('click',()=>{const t1in=$('#t1in').value.trim(),t1out=$('#t1out').value.trim(),t2in=$('#t2in').value.trim(),t2out=$('#t2out').value.trim();
    if(!t1in||!t1out||!t2in||!t2out){$('#planFb').textContent='四格都要填。';return;}
    if(t1in===t2in){$('#planFb').textContent='兩組輸入要不同：第 2 組應是邊界或錯誤情況。';return;}
    setEx('c1',5,{t1in,t1out,t2in,t2out});$('#planFb').innerHTML='<span class="badge">✓ 已儲存，5 分</span>';renderNav();if(chapterComplete(1))advance(2);});
})();

/* 第 2 章：三題 */
(function(){const h=$('#c2');const done=()=>{if(PRED_IDS.c2.every(id=>S.pred[id]))setEx('c2',0);refreshScore();if(chapterComplete(2))advance(3);};
  const t1=step(h,'try','編程佔必修幾多？','估對 4 分');
  makePredict(t1,{id:'c2_a',q:'高中 ICT 必修 144 小時中，「計算思維與程式編寫」佔幾多？',code:'資訊處理 37\n電腦系統基礎 20\n互聯網及其應用 31\n計算思維與程式編寫 48\n社會影響 8',options:['約一半','約三分之一','約四分之一','全部'],answer:1,why:'48 ÷ 144 = 三分之一。其餘三分之二是理論和應用，所以讀 ICT 不只是寫程式。'},S.pred,PRED_PTS,done,true);
  const t2=step(h,'try','選修','估對 4 分');
  makePredict(t2,{id:'c2_b',q:'選修部分有三個選項，學生要讀幾多個？',code:'A 數據庫\nB 網絡應用程式開發\nC 算法與程式編寫',options:['1 個','2 個','3 個','不用讀'],answer:1,why:'三選二，由學校決定開哪兩個組合。'},S.pred,PRED_PTS,done,true);
  const t3=step(h,'try','評核','估對 4 分');
  makePredict(t3,{id:'c2_c',q:'校本評核（中五至中六做的小型系統）佔總分幾多？',code:'卷一（必修）55%\n卷二（選修）25%\n校本評核 ?',options:['10%','20%','30%','45%'],answer:1,why:'卷一 55% + 卷二 25% + 校本評核 20% = 100%。'},S.pred,PRED_PTS,done,true);
})();

/* 第 3 章：真 Thonny 清單 */
(function(){
  const items=['我在電腦室開啟了 Thonny','我把專題程式貼到 Thonny 並儲存為 L10_姓名.py','我在真 Thonny 執行並輸入了測試數據','我試過 View → Variables 或 Debug'];
  const rec=S.ex.c3||{};const host=$('#thonnyChecks');
  host.innerHTML=items.map((t,i)=>`<label style="display:flex;gap:8px;align-items:center;margin:4px 0"><input type="checkbox" data-i="${i}" ${rec.checks&&rec.checks[i]?'checked':''} ${rec.ok?'disabled':''} style="width:20px;height:20px"> ${esc(t)}</label>`).join('');
  if(rec.ok){$('#thonnyDiff').value=rec.diff||'';$('#thonnyDiff').readOnly=true;$('#btnThonny').disabled=true;$('#thonnyFb').innerHTML=`<span class="badge">✓ 完成，${rec.score} 分</span>`;}
  $('#btnThonny').addEventListener('click',()=>{const checks=$$('#thonnyChecks input').map(c=>c.checked);const diff=$('#thonnyDiff').value.trim();
    if(checks.filter(Boolean).length<3){$('#thonnyFb').textContent='最少要完成頭三項。';return;}if(diff.length<20){$('#thonnyFb').textContent='分別最少寫 20 字。';return;}
    setEx('c3',8,{checks,diff});$$('#thonnyChecks input').forEach(c=>c.disabled=true);$('#thonnyDiff').readOnly=true;$('#btnThonny').disabled=true;$('#thonnyFb').innerHTML='<span class="badge">✓ 完成，8 分</span>';renderNav();if(chapterComplete(3))advance(4);});
})();

/* 第 4 章：自我檢視 */
const SELFQ=[['解難態度','程式出錯時，我願意自己試幾次找原因'],['拆解問題','我享受想辦法把大問題拆成小步驟'],['邏輯準確','「先估後執行」的題目，我大多估得對'],['完成作品','我的迷你專題能運作，並通過自己的測試數據'],['理論學習','我不介意理解和記憶理論，例如網絡、硬件、數據表示'],['主動性','我曾在課堂以外自己試寫或修改程式']];
(function(){
  const rec=S.ex.c4||{};const host=$('#selfCheck');
  host.innerHTML=`<div class="tablewrap"><table><thead><tr><th>範疇</th><th>題目</th><th>1 不同意</th><th>2</th><th>3</th><th>4 很同意</th></tr></thead><tbody>${SELFQ.map((q,i)=>`<tr><td>${q[0]}</td><td>${q[1]}</td>${[1,2,3,4].map(v=>`<td style="text-align:center"><input type="radio" name="sq${i}" value="${v}" ${rec.ans&&rec.ans[i]===v?'checked':''} ${rec.ok?'disabled':''} style="width:20px;height:20px"></td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  function result(ans){const total=ans.reduce((a,b)=>a+b,0);const low=SELFQ.filter((q,i)=>ans[i]<=2).map(q=>q[0]);let msg;if(total>=19)msg='你在解難和動手方面的評分很高，ICT 應該很適合你。';else if(total>=13)msg='你有不少適合的特質，可以認真考慮 ICT；留意一下評分較低的範疇是否你介意的。';else msg='你對編程的興趣暫時未算強烈。選科時多想想：你喜歡的是哪一部分？興趣比分數重要。';
    return `<div class="fb neutral"><b>總分 ${total} / 24。</b>${msg}${low.length?`<br>評分較低：${low.join('、')}。`:''}</div>`;}
  if(rec.ok){$('#selfResult').innerHTML=result(rec.ans);$('#btnSelf').disabled=true;$('#selfFb').innerHTML='<span class="badge">✓ 完成，15 分</span>';}
  $('#btnSelf').addEventListener('click',()=>{const ans=SELFQ.map((q,i)=>{const r=$(`input[name="sq${i}"]:checked`);return r?+r.value:0;});if(ans.some(v=>!v)){$('#selfFb').textContent='六條都要選。';return;}
    setEx('c4',15,{ans});$('#selfResult').innerHTML=result(ans);$$('#selfCheck input').forEach(c=>c.disabled=true);$('#btnSelf').disabled=true;$('#selfFb').innerHTML='<span class="badge">✓ 完成，15 分</span>';renderNav();if(chapterComplete(4))advance(5);});
})();

'''

TIERS = r'''function hasLoop(c){return /\bfor\s+\w+\s+in\b|\bwhile\b/.test(c);}
function lineCount(c){return c.split('\n').filter(l=>l.trim()&&!l.trim().startsWith('#')).length;}
function tset(k){const r=S.ex.c1||{};return (r[k]||'').split('\n').map(s=>s.trim()).filter(Boolean);}
const TIERS=[
  {id:'t1',pill:'必做',cls:'',pts:25,title:'專題可以運作',debug:true,turtle:true,
   desc:'按規劃表寫你的專題。要求：有 <code>input</code>、有 <code>if</code>、有迴圈，最少 12 行。按「檢查」時會用第 1 章的<b>第 1 組測試數據</b>自動執行，不可以出錯，而且輸出要見到你寫的預期字句。',
   hints:['先把規劃表的「輸入」變成幾行 input()。','再寫「處理」：if 判斷和迴圈。','最後 print 輸出；每寫幾行就按 ▶ 試一次。'],
   check:async(code,res)=>{if(!/input\(/.test(code))return {ok:false,msg:'專題要有 input()。'};if(!/\bif\b/.test(code))return {ok:false,msg:'專題要有 if。'};if(!hasLoop(code))return {ok:false,msg:'專題要有 for 或 while 迴圈。'};if(lineCount(code)<12)return {ok:false,msg:`程式只有 ${lineCount(code)} 行（不計註解），最少 12 行。`};
     const r=await runSilent(code,tset('t1in'));if(r.err)return {ok:false,msg:'用第 1 組測試數據執行時出錯：'+r.err.split('\n').pop()};const want=(S.ex.c1||{}).t1out||'';if(want&&!r.out.includes(want))return {ok:false,msg:`輸出沒有見到你預期的「${want}」。檢查程式，或回第 1 章改測試數據。`};return {ok:true,msg:'第 1 組測試通過，專題可以運作。'};}},
  {id:'t2',pill:'進階',cls:'g',pts:10,title:'用到列表或函數，邊界測試也通過',debug:true,turtle:true,
   desc:'程式要用到<b>列表</b>或<b>自己定義的函數</b>，並且用第 1 章的<b>第 2 組測試數據</b>（邊界或錯誤情況）執行也不出錯、輸出見到預期字句。把程式貼到這裏再檢查。',
   hints:['把重複的部分抽成 def 函數，或把多個值放進列表。','邊界情況常見是 0、負數、剛好等於某個數；用 if 處理它。'],
   check:async(code,res)=>{if(!/\bdef\s+\w+\(|\[\s*[^\]]*\]|\.append\(/.test(code))return {ok:false,msg:'要用到列表（[ ]）或函數（def）。'};const r=await runSilent(code,tset('t2in'));if(r.err)return {ok:false,msg:'用第 2 組測試數據執行時出錯：'+r.err.split('\n').pop()};const want=(S.ex.c1||{}).t2out||'';if(want&&!r.out.includes(want))return {ok:false,msg:`輸出沒有見到你預期的「${want}」。`};return {ok:true,msg:'邊界測試通過。'};}},
  {id:'t3',pill:'挑戰',cls:'y',pts:5,title:'有註解、有程式風格',debug:true,turtle:true,
   desc:'最頂一行註解寫題目和你的名字；最少再加 3 行註解說明各部分做甚麼；變量名要有意思（不可以全部叫 a、b、x）。把最終版貼到這裏檢查。',
   hints:['# 題目：小食部收銀機　作者：陳大文','每個主要部分前加一行 # 說明。'],
   check:(code,res)=>{const lines=code.split('\n');if(!/^\s*#/.test(lines[0]||''))return {ok:false,msg:'最頂一行要是註解。'};const cm=lines.filter(l=>/^\s*#/.test(l)).length;if(cm<4)return {ok:false,msg:`只有 ${cm} 行註解，最少 4 行（頂行加 3 行）。`};const names=[...new Set((code.match(/^\s*([a-zA-Z_]\w*)\s*=/gm)||[]).map(m=>m.trim().split(/\s*=/)[0]))];const good=names.filter(n=>n.length>=3);if(names.length&&good.length<Math.ceil(names.length/2))return {ok:false,msg:'變量名要有意思，最少一半要 3 個字母以上（例如 price、total）。'};return {ok:true,msg:'挑戰完成。'};}},
];
'''

QUIZ = r'''const QUIZ=[
  {id:'q1',q:'高中 ICT 公開考試卷一考甚麼？',code:'卷一 55%\n卷二 25%\n校本評核 20%',options:['必修部分','選修部分','校本評核','只考編程'],answer:0,why:'卷一考必修五個單元，卷二考兩個選修。'},
  {id:'q2',q:'高中 ICT 的程式語言是甚麼？',code:'這十堂學的語言',options:['Python','Scratch','Java','C++'],answer:0,why:'公開考試用 Python（或 C++），和這十堂一樣。'},
  {id:'q3',q:'以下哪一樣這十堂沒有教，是中四才學的？',code:'變量、if、迴圈、列表、函數',options:['列表','流程圖和偽代碼','while 迴圈','字串切片'],answer:1,why:'流程圖、偽代碼、追蹤表是中四「算法設計」的內容；這十堂先學會寫程式，到時會較易上手。'},
];
'''

build(10, '迷你專題及選科導航', '四章：專題規劃與測試數據、ICT 高中讀甚麼、真 Thonny 體驗、自我檢視；然後完成專題、小測與互評。',
      '這一堂先定測試數據，再看 ICT 高中讀甚麼、開一次真 Thonny、做自我檢視，然後用 55 分鐘完成專題，最後小測和互評。',
      CH_HTML, CH_JS, TIERS, QUIZ, '{1:5,2:12,3:8,4:15}',
      "['第 1 章 規劃與測試數據',sc.c[1],5],['第 2 章 ICT 高中讀甚麼',sc.c[2],12],['第 3 章 真 Thonny 體驗',sc.c[3],8],['第 4 章 自我檢視',sc.c[4],15],",
      "[['c2_a','B 約三分之一'],['c2_b','B 2 個'],['c2_c','B 20%']]",
      """[['第 1 章','兩組測試數據（第 2 組要不同）'],['第 3 章','頭三項剔選＋分別 20 字'],['第 4 章','六條都選']]""",
      '<a href="https://www.edb.gov.hk/tc/curriculum-development/kla/technology-edu/curriculum-doc/index.html" target="_blank" rel="noopener">教育局：資訊及通訊科技課程及評估指引</a>、<a href="https://www.w3schools.com/python/" target="_blank" rel="noopener">W3Schools Python Tutorial（課後自學）</a>',
      '例如：同學 陳大文 試我的程式時輸入了負數，程式出錯，我加了 if 檢查……', '迷你專題')

# ---- 後處理 ----
p = os.path.join(ROOT, 'src/lesson10/lesson10.src.html')
s = open(p, encoding='utf8').read()
# 作品區說明
s = s.replace('<div class="goal"><b>直接在下面的 Thonny 寫。</b>先按 ▶ 試行，看 Shell 的結果滿意了才按「檢查」。三層可以只做第一層；進階和挑戰留給有時間的同學。</div>',
              '<div class="goal"><b>約 55 分鐘。</b>在下面的 Thonny 寫你的專題，寫幾行就按 ▶ 試一次；卡住可用 🐞 逐步執行。做好按「檢查」，網頁會用你第 1 章寫的測試數據執行。進階和挑戰把同一個程式貼過去再檢查。</div>')
# 小測後：互評紀錄取代自評
s = s.replace('<div class="lead">自評<small>5 分</small></div>\n    <p class="small">今天程式出錯時，你是怎樣找到原因的？寫一兩句。</p>',
              '<div class="lead">互評紀錄<small>5 分</small></div>\n    <p class="small">和一位同學交換試玩對方的專題。寫下：同學的名字、你給對方的一個建議、對方給你的一個建議（最少 30 字）。</p>')
s = s.replace("if(t.length<6){$('#exitFb').textContent='自評請最少寫一句。';return;}", "if(t.length<30){$('#exitFb').textContent='互評紀錄要寫同學名字和兩個建議（最少 30 字）。';return;}")
s = s.replace('<p class="small">自評：${esc(S.quiz.reflect)}</p>', '<p class="small">互評紀錄：${esc(S.quiz.reflect)}</p><p class="small">自我檢視：${S.ex.c4&&S.ex.c4.ans?S.ex.c4.ans.map((v,i)=>SELFQ[i][0]+v).join("、")+"（總分 "+S.ex.c4.ans.reduce((a,b)=>a+b,0)+" / 24）":"未做"}</p><p class="small">測試數據：第 1 組 ${esc((S.ex.c1||{}).t1in||"").replace(/\\n/g," / ")} → ${esc((S.ex.c1||{}).t1out||"")}；第 2 組 ${esc((S.ex.c1||{}).t2in||"").replace(/\\n/g," / ")} → ${esc((S.ex.c1||{}).t2out||"")}</p>')
s = s.replace('自評：${S.quiz.reflect}', '互評紀錄：${S.quiz.reflect}')
# 老師區：免除第 3 章
s = s.replace("<h3>跳到任何一章（會在報告標示）</h3>", "<h3>免除第 3 章（不能用電腦室時）</h3><div class=\"row\"><button class=\"btn\" id=\"waive3\">免除真 Thonny 體驗（給 8 分）</button></div><h3>跳到任何一章（會在報告標示）</h3>")
s = s.replace("$$('[data-j]',p).forEach(b=>b.addEventListener('click',()=>{", "$('#waive3',p).addEventListener('click',()=>{S.teacherUsed=true;S.ex.c3={ok:true,score:8,checks:[],diff:'（老師免除）'};save();refreshScore();if(S.stage<4)S.stage=4;S.view=3;save();location.reload();});\n    $$('[data-j]',p).forEach(b=>b.addEventListener('click',()=>{")
assert '互評紀錄' in s and 'waive3' in s and '約 55 分鐘' in s
open(p, 'w', encoding='utf8').write(s)
print('post-processed')
