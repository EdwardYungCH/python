"""第 7 堂「字串」流程測試。python3 tools/test_lesson7.py"""
import asyncio, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from testlib import *

PW = 'pw = input("密碼：")\nhas_digit = False\nhas_upper = False\nfor ch in pw:\n    if ch.isdigit():\n        has_digit = True\n    if ch.isupper():\n        has_upper = True\nif len(pw) >= 8 and has_digit and has_upper:\n    print("強")\nelse:\n    print("弱")\n    if len(pw) < 8:\n        print("太短")\n    if not has_digit:\n        print("沒有數字")\n    if not has_upper:\n        print("沒有大寫")'
VOW = 's = input("一句英文：").lower()\ncount = 0\nfor ch in s:\n    if ch in "aeiou":\n        count += 1\nprint(f"元音：{count} 個")'
CAE = 'text = input("文字：")\nk = int(input("移幾多：")) \nresult = ""\nfor ch in text:\n    result += chr((ord(ch) - 97 + k) % 26 + 97)\nprint(result)'

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(pg)
        await pg.goto(url_of(7)); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('標題是第 7 堂', '第 7 堂' in await pg.text_content('.topbar'))
        await register(pg); check('進入第 1 章', await current(pg) == 's1')
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 1)
        await check_ex(pg, ex1, 's = "Python"\nprint(s[1])\nprint(s[6])')
        sh = await ex1.locator('.shell').text_content(); check('s[6] 出 IndexError', 'IndexError' in sh, sh[-120:])
        await check_ex(pg, ex1, 's = "Python"\nprint(s[0])\nprint(s[5])'); check('練習 1 完成（s[5] 亦可）', '5 分' in await fb(ex1))
        await go_next(pg)
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 1); check('估錯顯示答案 A', '答案是 A' in await c2.nth(0).locator('.fb').text_content())
        await check_ex(pg, ex2, 'd = "2026-10-14"\nprint(d[0:4])\nprint(d[5:6])'); check('練習 2 月份切錯被拒', '不一樣' in await fb(ex2))
        await check_ex(pg, ex2, 'd = "2026-10-14"\nprint(d[0:4])\nprint(d[5:7])'); check('練習 2 完成', '5 分' in await fb(ex2))
        await go_next(pg)
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 1); await predict(pg, c3.nth(1), 1)
        await check_ex(pg, ex3, 'name = input("名字：")\nname = name.strip().upper()\nprint("歡迎，{name}！")', inputs=['  amy  ']); check('練習 3 漏 f 被拒', '歡迎' in await fb(ex3), await fb(ex3))
        await check_ex(pg, ex3, 'name = input("名字：")\nname = name.strip().upper()\nprint(f"歡迎，{name}！")', inputs=['  amy  ']); check('練習 3 完成', '5 分' in await fb(ex3), await fb(ex3))
        check('第 3 章 13 / 13', '13 / 13' in await pg.text_content('#navStatus'))
        await go_next(pg)
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        await predict(pg, c4.nth(0), 2)
        await ex4.locator('details.help summary').click(); await ex4.locator('[data-a]').click()
        await check_ex(pg, ex4, 's = "a1b22c3"\ncount = 0\nfor ch in s:\n    if ch.isdigit():\n        count += 1\nprint(count)'); check('練習 4 看答案後只得 1 分', '1 分' in await fb(ex4))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        t = pg.locator('#tiers .tier')
        await check_ex(pg, t.nth(0), PW.replace('and has_upper', 'and True'), inputs=['abc']); check('必做漏大寫檢查被 abcdefg1 捉到', 'abcdefg1' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), PW, inputs=['abc']); check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'), await fb(t.nth(0)))
        await check_ex(pg, t.nth(1), VOW.replace('.lower()', ''), inputs=['Hello World']); check('進階不理大小寫被捉到', 'PYTHON' in await fb(t.nth(1)), await fb(t.nth(1)))
        await check_ex(pg, t.nth(1), VOW, inputs=['Hello World']); check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'), await fb(t.nth(1)))
        await check_ex(pg, t.nth(2), CAE.replace('% 26 + 97', '+ 97'), inputs=['abc', '1']); check('挑戰沒有回到 a 被 xyz 捉到', 'xyz' in await fb(t.nth(2)), await fb(t.nth(2)))
        await check_ex(pg, t.nth(2), CAE, inputs=['abc', '1']); check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await fb(t.nth(2)))
        await go_next(pg); await submit_quiz(pg, [1, 2, 1], '我忘記了 f-string 要加 f，印出 {n}。')
        check('提交後進入報告', await current(pg) == 's7')
        # 9 + (0+5) + 13 + (4+1) + 40 + (5+5+0+5) = 87
        await common_tail(pg, b, 7, 87, 'strip().upper()', mobile_chapter=3)
        await b.close()
    finish()

asyncio.run(main())
