"""第 6 堂「For 迴圈與 Range」流程測試。python3 tools/test_lesson6.py"""
import asyncio, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from testlib import *

TABLE = 'n = int(input("哪一個數？"))\nfor i in range(1, 10):\n    print(n, "x", i, "=", n * i)'
SAVE = 'money = float(input("本金："))\nrate = float(input("年利率（%）：")) / 100\nyears = int(input("年數："))\nfor year in range(1, years + 1):\n    money *= 1 + rate\n    print("第", year, "年：", round(money, 2))'
POLY = 'import turtle\nn = int(input("幾多條邊？"))\nt = turtle.Turtle()\nfor i in range(n):\n    t.forward(60)\n    t.left(360 / n)'

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(pg)
        await pg.goto(url_of(6)); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('標題是第 6 堂', '第 6 堂' in await pg.text_content('.topbar'))
        await register(pg); check('進入第 1 章', await current(pg) == 's1')
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 0); check('估錯顯示答案 B', '答案是 B' in await c1.nth(0).locator('.fb').text_content())
        await check_ex(pg, ex1, 'for i in range(4):\n    print(i)'); check('練習 1 range(4) 不對', '不一樣' in await fb(ex1), await fb(ex1))
        await check_ex(pg, ex1, 'for i in range(5):\n    print(i)'); check('練習 1 完成', '5 分' in await fb(ex1))
        await go_next(pg)
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 0)
        await check_ex(pg, ex2, 'for i in range(10, 50, 10):\n    print(i)'); check('練習 2 終點 50 少印一個', '不一樣' in await fb(ex2))
        await check_ex(pg, ex2, 'for i in range(10, 60, 10):\n    print(i)'); check('練習 2 完成（終點 60 亦可）', '5 分' in await fb(ex2))
        await go_next(pg)
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 1)
        await ex3.locator('details.help summary').click(); await ex3.locator('[data-a]').click()
        await check_ex(pg, ex3, 'total = 0\nfor i in range(1, 101):\n    total += i\nprint(total)'); check('練習 3 看答案後只得 1 分', '1 分' in await fb(ex3))
        await go_next(pg)
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        check('第 4 章試一試有海龜畫布', await c4.nth(0).locator('.tpane').count() == 1)
        await predict(pg, c4.nth(0), 1)
        await pg.wait_for_timeout(1500)
        ink = await c4.nth(0).locator('.tpane').evaluate('el=>{let n=0;el.querySelectorAll("canvas").forEach(c=>{const d=c.getContext("2d").getImageData(0,0,c.width,c.height).data;for(let i=3;i<d.length;i+=4)if(d[i]>0)n++;});return n}')
        check('執行後畫布有線（三角形）', ink > 50, str(ink))
        await predict(pg, c4.nth(1), 2)
        await check_ex(pg, ex4, 'import turtle\nt = turtle.Turtle()\nfor i in range(5):\n    t.forward(70)\n    t.left(90)'); check('練習 4 角度錯被拒', '72' in await fb(ex4), await fb(ex4))
        await check_ex(pg, ex4, 'import turtle\nt = turtle.Turtle()\nfor i in range(5):\n    t.forward(70)\n    t.left(72)'); await pg.wait_for_timeout(800); check('練習 4 完成', '5 分' in await fb(ex4), await fb(ex4))
        check('第 4 章 13 / 13', '13 / 13' in await pg.text_content('#navStatus'))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        t = pg.locator('#tiers .tier')
        await check_ex(pg, t.nth(0), 'n = int(input("哪一個數？"))\nfor i in range(1, 9):\n    print(n, "x", i, "=", n * i)', inputs=['7'])
        check('必做只有 8 行被捉到', '9 行' in await fb(t.nth(0)) or '9' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), TABLE, inputs=['7']); check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'), await fb(t.nth(0)))
        await check_ex(pg, t.nth(1), SAVE.replace('money *= 1 + rate', 'money += money * rate / 2'), inputs=['1000', '5', '3']); check('進階計錯利息被捉到', '1157' in await fb(t.nth(1)), await fb(t.nth(1)))
        await check_ex(pg, t.nth(1), SAVE, inputs=['1000', '5', '3']); check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'), await fb(t.nth(1)))
        check('挑戰有海龜畫布', await t.nth(2).locator('.tpane').count() == 1)
        await check_ex(pg, t.nth(2), POLY.replace('360 / n', '72'), inputs=['5']); check('挑戰固定角度被拒', '360' in await fb(t.nth(2)), await fb(t.nth(2)))
        await check_ex(pg, t.nth(2), POLY, inputs=['5']); await pg.wait_for_timeout(800); check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await fb(t.nth(2)))
        await go_next(pg); await submit_quiz(pg, [0, 1, 1], '我把終點寫成 5，少印了一個數。')
        check('提交後進入報告', await current(pg) == 's7')
        # (0+5) + 9 + (4+1) + 13 + 40 + 20 = 92
        await common_tail(pg, b, 6, 92, 'range(10, 51, 10)', mobile_chapter=4)
        await b.close()
    finish()

asyncio.run(main())
