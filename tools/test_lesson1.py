"""第 1 堂「開始寫 Python」流程測試（第 2 版）。python3 tools/test_lesson1.py"""
import asyncio, sys, os
from playwright.async_api import async_playwright

URL = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lesson1', 'index.html'))
errors, res = [], []
def check(name, ok, extra=''):
    res.append((name, ok)); print(('PASS ' if ok else 'FAIL ') + name + (' — ' + extra if extra else ''))
def locked(pg, sid): return pg.locator('#' + sid).evaluate('e=>e.classList.contains("locked")')

async def predict(pg, box, pick):
    await box.locator('.opt').nth(pick).click(); await box.locator('.btn.go').click(); await pg.wait_for_timeout(900)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errors.append(str(e)))
        await pg.goto(URL); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('頁面沒有 Scratch／Arduino 字眼', 'Scratch' not in await pg.content() and 'Arduino' not in await pg.content())
        await pg.fill('#stName', '測試同學'); await pg.fill('#stClass', '3A'); await pg.fill('#stNo', '12'); await pg.click('#btnStart'); await pg.wait_for_timeout(300)
        check('登記後解鎖第 1 章', not await locked(pg, 's1'))
        # 第 1 章
        c1 = pg.locator('#c1 .predict')
        await predict(pg, c1.nth(0), 0)
        check('試一試 1 執行印出 Hello, World!', 'Hello, World!' in await c1.nth(0).locator('.out').text_content())
        check('試一試後仍鎖第 2 章（練習未做）', await locked(pg, 's2'))
        ex1 = c1.nth(1)
        await ex1.locator('[data-check]').click(); await pg.wait_for_timeout(300)
        check('練習 1 未填 ____ 被拒', '____' in await ex1.text_content())
        await ex1.locator('textarea').fill('Print("Hello, Python!")'); await ex1.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 1 大小寫錯誤顯示 NameError 提示', 'NameError' in await ex1.locator('.out').text_content() and '大小寫' in await ex1.locator('.out').text_content())
        await ex1.locator('textarea').fill('print("Hello, Python!")'); await ex1.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 1 完成 5 分', '5 分' in await ex1.locator('[data-fb]').text_content())
        check('第 1 章 9 分', await pg.text_content('#m1') == '9 / 9 分', await pg.text_content('#m1'))
        check('第 2 章解鎖', not await locked(pg, 's2'))
        # 第 2 章：估錯
        c2 = pg.locator('#c2 .predict')
        await predict(pg, c2.nth(0), 0)
        o = await c2.nth(0).locator('.out').text_content()
        check('縮排錯誤執行出錯並有中文提示', 'Error' in o and '縮排' in o, o[:100])
        ex2 = c2.nth(1)
        await ex2.locator('[data-a]').click()
        await ex2.locator('textarea').fill('print("Python 分大小寫")\nprint("行首不可以有空格")'); await ex2.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 2 看答案後只得 1 分', '1 分' in await ex2.locator('[data-fb]').text_content())
        check('第 2 章 1 分', await pg.text_content('#m2') == '1 / 9 分', await pg.text_content('#m2'))
        # 第 3 章
        c3 = pg.locator('#c3 .predict')
        await predict(pg, c3.nth(0), 2); await predict(pg, c3.nth(1), 1)
        ex3 = c3.nth(2)
        await ex3.locator('textarea').fill('print("你好")\nprint("10")\nprint("一共", 10, "件")'); await ex3.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 3 用引號包數字被拒', '不要用引號' in await ex3.text_content())
        await ex3.locator('textarea').fill('print("你好")\nprint(10)\nprint("一共", 10, "件")'); await ex3.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('第 3 章 13 分', await pg.text_content('#m3') == '13 / 13 分', await pg.text_content('#m3'))
        # 第 4 章
        c4 = pg.locator('#c4 .predict')
        await predict(pg, c4.nth(0), 1)
        ex4 = c4.nth(1)
        await ex4.locator('textarea').fill('print("開始")\nprint("完結")'); await ex4.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 4 刪行而非註解被拒', '最頂' in await ex4.text_content() or '註解掉' in await ex4.text_content())
        await ex4.locator('textarea').fill('# 練習 4\nprint("開始")\n# print("測試中，之後刪去")\nprint("完結")'); await ex4.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('第 4 章 9 分', await pg.text_content('#m4') == '9 / 9 分', await pg.text_content('#m4'))
        check('第 5 節作品解鎖', not await locked(pg, 's5'))
        # 作品
        t = pg.locator('#tiers .tier')
        await t.nth(0).locator('textarea').fill('print("==========")\nprint("陳大文")\nprint("3A")\nprint("==========")'); await t.nth(0).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('必做內容不足 5 行被拒', '最少要 5 行' in await t.nth(0).text_content())
        good = 'print("==========")\nprint("陳大文")\nprint("3A")\nprint("興趣：打籃球")\nprint("食物：魚蛋")\nprint("想去：日本")\nprint("==========")'
        await t.nth(0).locator('textarea').fill(good); await t.nth(0).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'))
        check('第 6 節小測解鎖', not await locked(pg, 's6'))
        await t.nth(1).locator('textarea').fill('# 名牌 陳大文\n' + good + '\nprint("出生年份：", "2026 - 15")  # 計算'); await t.nth(1).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('進階計算放在引號內被拒', '不在引號內' in await t.nth(1).text_content())
        await t.nth(1).locator('textarea').fill('# 名牌 陳大文\n' + good + '\nprint("出生年份：", 2026 - 15)  # 計算'); await t.nth(1).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'))
        await t.nth(2).locator('textarea').fill('print("   *   ")\nprint("  ***  ")\nprint(" ***** ")\nprint("*******")\nprint("  |||  ")\nprint("  |||  ")'); await t.nth(2).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'))
        # 小測
        q = pg.locator('#quiz .predict')
        check('小測沒有執行器', await q.nth(0).locator('.runner').count() == 0)
        await predict(pg, q.nth(0), 0); await predict(pg, q.nth(1), 1); await predict(pg, q.nth(2), 2)
        await pg.click('#btnExit'); await pg.wait_for_timeout(200)
        check('自評太短被拒', '一句' in await pg.text_content('#exitFb'))
        await pg.fill('#reflect', '我先看 Shell 紅字最後一行，再找行號。'); await pg.click('#btnExit'); await pg.wait_for_timeout(800)
        # 9 + 1 + 13 + 9 + 40 + (5+5+0+5) = 87
        check('總分 87', await pg.text_content('#scoreNow') == '87', await pg.text_content('#scoreNow'))
        check('報告有驗證碼', '驗證碼' in await pg.text_content('#reportBox'))
        await pg.reload(); await pg.wait_for_timeout(800)
        check('重新載入後分數保留', await pg.text_content('#scoreNow') == '87')
        check('重新載入後小測鎖定', await pg.locator('#btnExit').is_disabled())
        await pg.click('#btnTeacher'); await pg.fill('#pin', 'wrong'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
        check('錯 PIN 拒絕', 'PIN 不正確' in await pg.text_content('#tpanel'))
        await pg.fill('#pin', 'py2026'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
        check('正確 PIN 顯示答案', '練習 1' in await pg.text_content('#tpanel'))
        await pg.keyboard.press('Escape'); await pg.locator('#pinX').click()
        await pg.screenshot(path='/tmp/py3_shot_desktop.png', full_page=True)
        m = await b.new_page(viewport={'width': 390, 'height': 844})
        await m.goto(URL); await m.wait_for_timeout(800)
        sw = await m.evaluate('document.documentElement.scrollWidth')
        check('手機闊度無橫向捲動', sw <= 392, str(sw))
        await m.screenshot(path='/tmp/py3_shot_mobile.png', full_page=True)
        await b.close()
    real = [e for e in errors if 'ERR_TUNNEL_CONNECTION_FAILED' not in e and 'ERR_INTERNET_DISCONNECTED' not in e]
    check('沒有 console 錯誤（不計 Google Fonts）', not real, '; '.join(real)[:300])
    fails = [r for r in res if not r[1]]
    print(f'\n{len(res)-len(fails)} / {len(res)} 通過')
    sys.exit(1 if fails else 0)

asyncio.run(main())
