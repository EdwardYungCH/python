"""第 5 堂「While 迴圈」流程測試。python3 tools/test_lesson5.py"""
import asyncio, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from testlib import *

GUESS = 'import random\nsecret = random.randint(1, 100)\nwhile True:\n    guess = int(input("猜一個數："))\n    if guess > secret:\n        print("太大")\n    elif guess < secret:\n        print("太小")\n    else:\n        print("恭喜")\n        break'
GUESS2 = 'import random\nsecret = random.randint(1, 100)\ncount = 0\nwhile True:\n    guess = int(input("猜一個數："))\n    count += 1\n    if guess > secret:\n        print("太大")\n    elif guess < secret:\n        print("太小")\n    else:\n        print("恭喜，你猜了", count, "次")\n        break'
GUESS3 = 'import random\nsecret = random.randint(1, 100)\ncount = 0\nwhile count < 5:\n    guess = int(input("猜一個數："))\n    count += 1\n    if guess > secret:\n        print("太大")\n    elif guess < secret:\n        print("太小")\n    else:\n        print("恭喜，你猜了", count, "次")\n        break\nif guess != secret:\n    print("失敗，答案是", secret)'

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(pg)
        await pg.goto(url_of(5)); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('標題是第 5 堂', '第 5 堂' in await pg.text_content('.topbar'))
        await register(pg); check('進入第 1 章', await current(pg) == 's1')
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 0)
        await check_ex(pg, ex1, 'n = 1\nwhile n <= 5:\n    print(n)')
        sh = await ex1.locator('.shell').text_content(); at = await ex1.locator('.assist').text_content()
        check('無限迴圈自動停止並由 Assistant 解釋', '無限迴圈' in sh and '無限迴圈' in at, at[:80])
        await check_ex(pg, ex1, 'n = 1\nwhile n <= 5:\n    print(n)\n    n += 1'); check('練習 1 完成', '5 分' in await fb(ex1))
        await go_next(pg)
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 2); check('估錯顯示答案 B', '答案是 B' in await c2.nth(0).locator('.fb').text_content())
        await ex2.locator('details.help summary').click(); await ex2.locator('[data-a]').click()
        await check_ex(pg, ex2, 'count = 0\nn = 1\nwhile n <= 10:\n    if n % 2 == 0:\n        count += 1\n    n += 1\nprint(count)'); check('練習 2 看答案後只得 1 分', '1 分' in await fb(ex2))
        await go_next(pg)
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 2, inputs=['0', '200', '50'])
        sh = await c3.nth(0).locator('.shell').text_content(); check('試一試 3 餵入 0、200、50 後印兩次不對', sh.count('不對') == 2 and '你輸入了 50' in sh, sh[-80:])
        await check_ex(pg, ex3, 'while True:\n    pw = input("密碼：")\n    if pw == "1234":\n        print("ok")\n    print("錯誤")\nprint("歡迎")', inputs=['0000', '1234'])
        check('練習 3 沒有 break 被捉到', '問' in await fb(ex3) or '錯誤' in await fb(ex3), await fb(ex3))
        await check_ex(pg, ex3, 'while True:\n    pw = input("密碼：")\n    if pw == "1234":\n        break\n    print("錯誤")\nprint("歡迎")', inputs=['0000', '1234']); check('練習 3 完成', '5 分' in await fb(ex3))
        await go_next(pg)
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        await predict(pg, c4.nth(0), 0); await predict(pg, c4.nth(1), 1)
        await check_ex(pg, ex4, 'import random\ndice = random.randint(1, 7)\nprint("擲出", dice)'); check('練習 4 範圍錯被拒', '1 至 6' in await fb(ex4), await fb(ex4))
        await check_ex(pg, ex4, 'import random\ndice = random.randint(1, 6)\nprint("擲出", dice)'); check('練習 4 完成', '5 分' in await fb(ex4))
        check('第 4 章 13 / 13', '13 / 13' in await pg.text_content('#navStatus'))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        t = pg.locator('#tiers .tier')
        await check_ex(pg, t.nth(0), GUESS.replace('        break', '        pass'), inputs=['50', '25', '42'])
        check('必做猜中不結束被捉到', '結束' in await fb(t.nth(0)) or '問' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), GUESS, inputs=['50', '25', '42'])
        check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'), await fb(t.nth(0)))
        await check_ex(pg, t.nth(1), GUESS2, inputs=['50', '25', '42']); check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'), await fb(t.nth(1)))
        await check_ex(pg, t.nth(2), GUESS2, inputs=['1', '2', '3', '4', '5', '6', '7']); check('挑戰無上限被捉到', '5 次' in await fb(t.nth(2)), await fb(t.nth(2)))
        await check_ex(pg, t.nth(2), GUESS3, inputs=['1', '2', '3', '4', '5']); check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await fb(t.nth(2)))
        await go_next(pg); await submit_quiz(pg, [2, 2, 0], '我忘記了 n += 1，Assistant 說是無限迴圈。')
        check('提交後進入報告', await current(pg) == 's7')
        # 9 + (0+1) + 9 + 13 + 40 + (5+5+0+5) = 87
        await common_tail(pg, b, 5, 87, 'while True:、break', mobile_chapter=3)
        await b.close()
    finish()

asyncio.run(main())
