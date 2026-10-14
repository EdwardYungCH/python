# -*- coding: utf-8 -*-
"""共用產生器：由第 1 堂模板產生第 N 堂原始碼。每堂的 make_lessonN.py 只提供內容。"""
import re, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def between(s, a, b):
    i = s.index(a); j = s.index(b, i); return i, j

def build(n, title, subtitle, intro, ch_html, ch_js, tiers, quiz, ch_max, rows, preds, exs, links, placeholder, work_title, work_short='5 作品'):
    src = open(os.path.join(ROOT, 'src/lesson1/lesson1.src.html'), encoding='utf8').read()
    i, j = between(src, '<!-- 1 Get Started -->', '<!-- 5 作品 -->'); src = src[:i] + ch_html + src[j:]
    src = src.replace('<section class="card" id="s5" data-title="作品：我的名牌" data-short="5 作品">\n  <header><div class="chapter">作品</div><h2>我的名牌</h2>',
                      f'<section class="card" id="s5" data-title="作品：{work_title}" data-short="{work_short}">\n  <header><div class="chapter">作品</div><h2>{work_title}</h2>')
    i, j = between(src, '/* ---------- 章節 ---------- */', '/* ---------- 作品三層 ---------- */'); src = src[:i] + ch_js + src[j:]
    src = src.replace("const res=await runSilent(code,[]);let ok,msg;\n    if(cfg.check)", "const res=await runSilent(code,cfg.inputs||[]);let ok,msg;\n    if(cfg.check)")
    i, j = between(src, 'const TIERS=[', 'TIERS.forEach('); src = src[:i] + tiers + src[j:]
    src = src.replace("const res=await runSilent(code,[]);const c=t.check(code,res);await r.run();", "const res=await runSilent(code,t.inputs||[]);const c=t.check(code,res);await r.run();")
    i, j = between(src, 'const QUIZ=[', 'QUIZ.forEach('); src = src[:i] + quiz + src[j:]
    src = src.replace('<title>開始寫 Python</title>', f'<title>{title}</title>')
    src = src.replace('<div class="lesson">中三 Python 編程 · 第 1 堂</div><h1>開始寫 Python</h1>', f'<div class="lesson">中三 Python 編程 · 第 {n} 堂</div><h1>{title}</h1>')
    src = src.replace("const KEY='py3:L1v2', PIN='py2026', SIGN='py3-l1-sign-2026', APP='PY3-L1';", f"const KEY='py3:L{n}v2', PIN='py2026', SIGN='py3-l{n}-sign-2026', APP='PY3-L{n}';")
    src = src.replace("const CH_MAX={1:9,2:9,3:13,4:9};", "const CH_MAX=" + ch_max + ";")
    src = src.replace("cfg.filename||('L01_'", f"cfg.filename||('L{n:02d}_'")
    src = src.replace("const rows=[['第 1 章 開始',sc.c[1],9],['第 2 章 語法',sc.c[2],9],['第 3 章 輸出',sc.c[3],13],['第 4 章 註解',sc.c[4],9],", "const rows=[" + rows)
    src = src.replace('中三 Python 第 1 堂 開始寫 Python', f'中三 Python 第 {n} 堂 {title}')
    src = src.replace("const preds=[['c1_a','A Hello, World!'],['c2_a','C 出錯，兩行都不印'],['c3_a','C 7 / 3 + 4'],['c3_b','B 分數： 95'],['c4_a','B 2 行']];", "const preds=" + preds + ";")
    src = src.replace("""const exs=[['練習 1','print("Hello, Python!")'],['練習 2','print("Python 分大小寫") / print("行首不可以有空格")'],['練習 3','print(10) / print("一共", 10, "件")'],['練習 4','# 練習 4 / # print("測試中，之後刪去")']];""", "const exs=" + exs + ";")
    src = re.sub(r'<p class="small">課後重溫（英文）：.*?</p>', '<p class="small">課後重溫（英文）：' + links + '</p>', src)
    src = src.replace('<p class="small">四章：開始、語法、輸出、註解。每章先讀，再「試一試」，最後做「練習」。</p>', f'<p class="small">{subtitle}</p>')
    src = src.replace('中三 Python 編程 · 第 1 堂 · 版本 2.2', f'中三 Python 編程 · 第 {n} 堂 · 版本 1.0')
    src = src.replace('placeholder="例如：我先看 Shell 紅字最後一行的英文名稱和行號，再看 Assistant……"', f'placeholder="{placeholder}"')
    src = src.replace('這一堂有四章，每章都是「學 → 試 → 練」三步，然後做一個作品和小測。', intro)
    for leftover in ('Get Started', 'demo1', '名牌', 'Hello, World'):
        assert leftover not in src, '模板殘留：' + leftover
    os.makedirs(os.path.join(ROOT, f'src/lesson{n}'), exist_ok=True)
    out = os.path.join(ROOT, f'src/lesson{n}/lesson{n}.src.html')
    open(out, 'w', encoding='utf8').write(src)
    print('written', out, len(src))
