"""第 9 堂「函數入門與除錯」流程測試。python3 tools/test_lesson9.py"""
import asyncio, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from testlib import *

BUGS_FIXED = '# 第一段\nscore = 80\nif score >= 50:\n    print("合格")\n\n# 第二段\nn = int(input("數字："))\nif n > 50:\n    print("你輸入了", n)\n\n# 第三段\nscores = [50, 60, 70]\ntotal = 0\nfor s in scores:\n    total += s\nprint("平均", total / len(scores))'
FUNC = 'def average(scores):\n    total = 0\n    for s in scores:\n        total += s\n    return round(total / len(scores), 1)\n\ndef biggest(scores):\n    b = scores[0]\n    for s in scores:\n        if s > b:\n            b = s\n    return b\n\nscores = []\nfor i in range(5):\n    scores.append(int(input("分數：")))\nprint("平均", average(scores))\nprint("最高", biggest(scores))'
LEAP = 'def is_leap(year):\n    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0\n\nfor y in [2000, 1900, 2024, 2023]:\n    print(y, is_leap(y))'

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(pg)
        await pg.goto(url_of(9)); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('標題是第 9 堂', '第 9 堂' in await pg.text_content('.topbar'))
        await register(pg); check('進入第 1 章', await current(pg) == 's1')
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 2)
        await check_ex(pg, ex1, 'def line(n):\n    print("=" * n)\n\nline(5)\nline(8)'); check('練習 1 第二次呼叫錯被拒', '不一樣' in await fb(ex1))
        await check_ex(pg, ex1, 'def line(n):\n    print("=" * n)\n\nline(5)\nline(10)'); check('練習 1 完成', '5 分' in await fb(ex1))
        await go_next(pg)
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 1); check('估錯顯示答案 A', '答案是 A' in await c2.nth(0).locator('.fb').text_content())
        await predict(pg, c2.nth(1), 1)
        await check_ex(pg, ex2, 'def bmi(w, h):\n    print(round(w / (h * h), 1))\n\nprint(bmi(50, 1.6))'); check('練習 2 用 print 代替 return 被拒', 'return' in await fb(ex2), await fb(ex2))
        await check_ex(pg, ex2, 'def bmi(w, h):\n    return round(w / (h * h), 1)\n\nprint(bmi(50, 1.6))'); check('練習 2 完成', '5 分' in await fb(ex2))
        check('第 2 章 9 / 13（估錯一題）', '9 / 13' in await pg.text_content('#navStatus'), await pg.text_content('#navStatus'))
        await go_next(pg)
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 2)
        await ex3.locator('details.help summary').click(); await ex3.locator('[data-a]').click()
        await check_ex(pg, ex3, 'p = 1\nfor i in range(1, 6):\n    p *= i\nprint(p)'); check('練習 3 看答案後只得 1 分', '1 分' in await fb(ex3))
        await go_next(pg)
        # 第 4 章：逐步執行示範
        d = pg.locator('#demo4 .th')
        check('示範有逐步執行按鈕', await d.locator('[data-dbg]').count() == 1)
        await d.locator('[data-dbg]').click(); await pg.wait_for_timeout(400)
        check('開始逐步執行：第 1 行變黃', '1' in (await d.locator('.dbgview .ln.cur').text_content()).split()[0])
        for _ in range(4): await d.locator('[data-step]').click(); await pg.wait_for_timeout(250)
        vars_txt = await d.locator('.vars').text_content()
        check('四步後 Variables 顯示 biggest 與 s', 'biggest' in vars_txt and 's' in vars_txt, vars_txt[:60])
        for _ in range(12):
            if '完畢' in await d.locator('.dbgstat').text_content(): break
            await d.locator('[data-step]').click(); await pg.wait_for_timeout(200)
        check('逐步執行可走到完畢', '完畢' in await d.locator('.dbgstat').text_content(), await d.locator('.dbgstat').text_content())
        check('完畢後 Shell 印出 60', '60' in await d.locator('.shell').text_content())
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        await predict(pg, c4.nth(0), 2)
        check('練習 4 的 Thonny 有逐步執行', await ex4.locator('[data-dbg]').count() == 1)
        await check_ex(pg, ex4, 'count = 0\nfor i in range(1, 11):\n    if i % 2 == 0:\n        count += 1\nprint(count)'); check('練習 4 完成', '5 分' in await fb(ex4))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        t = pg.locator('#tiers .tier')
        code0 = await t.nth(0).locator('textarea').input_value(); check('必做預載三段有錯的程式', '第一段' in code0 and 'total = s' in code0)
        check('作品 Thonny 有逐步執行', await t.nth(0).locator('[data-dbg]').count() == 1)
        await check_ex(pg, t.nth(0), BUGS_FIXED.replace('total += s', 'total = s'), inputs=['80']); check('第三段未修被捉到', '60.0' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), BUGS_FIXED, inputs=['80']); check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'), await fb(t.nth(0)))
        await check_ex(pg, t.nth(1), FUNC.replace('return round(total / len(scores), 1)', 'print(round(total / len(scores), 1))'), inputs=['80', '65', '92', '47', '73']); check('進階沒有 return 平均被捉到', '71.4' in await fb(t.nth(1)) or 'return' in await fb(t.nth(1)), await fb(t.nth(1)))
        await check_ex(pg, t.nth(1), FUNC, inputs=['80', '65', '92', '47', '73']); check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'), await fb(t.nth(1)))
        await check_ex(pg, t.nth(2), LEAP.replace(' and year % 100 != 0', '')); check('挑戰漏 100 被 1900 捉到', '1900' in await fb(t.nth(2)), await fb(t.nth(2)))
        await check_ex(pg, t.nth(2), LEAP); check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await fb(t.nth(2)))
        await go_next(pg)
        check('小測後是專題規劃表', '專題規劃表' in await pg.text_content('#s6'))
        q = pg.locator('#quiz .predict')
        for i, pk in enumerate([1, 1, 2]): await predict(pg, q.nth(i), pk)
        await pg.fill('#reflect', '太短'); await pg.click('#btnExit'); await pg.wait_for_timeout(200); check('規劃表太短被拒', '40 字' in await pg.text_content('#exitFb'))
        await pg.fill('#reflect', '題目：小食部收銀機。輸入：三樣食物的價錢和付款額。處理：用 for 累加總數，用 if 判斷夠不夠錢。輸出：總數和找續。測試數據：10、20、30 付 100 → 找 40；付 50 → 不夠錢。'); await pg.click('#btnExit'); await pg.wait_for_timeout(800)
        check('提交後進入報告', await current(pg) == 's7')
        check('報告載有規劃表', '專題規劃表' in await pg.text_content('#reportBox'))
        # 9 + (0+4+5) + (4+1) + 9 + 40 + (5+5+5+5) = 92
        await common_tail(pg, b, 9, 92, 'p = 1', mobile_chapter=4)
        await b.close()
    finish()

asyncio.run(main())
