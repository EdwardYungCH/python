"""第 2 堂「變量與輸入」流程測試。python3 tools/test_lesson2.py"""
import asyncio, sys, os
from playwright.async_api import async_playwright

URL = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lesson2', 'index.html'))
errors, res = [], []
def check(name, ok, extra=''):
    res.append((name, ok)); print(('PASS ' if ok else 'FAIL ') + name + (' — ' + extra if extra else ''))
async def current(pg): return await pg.evaluate('document.querySelector("section.card.current").id')
async def next_disabled(pg): return await pg.locator('#btnNext').is_disabled()
async def go_next(pg): await pg.click('#btnNext'); await pg.wait_for_timeout(250)
async def feed(pg, box, values):
    """回答模擬器 Shell 內的 input() 輸入格"""
    for v in values:
        for _ in range(20):
            pins = box.locator('.shell .pin input')
            if await pins.count(): break
            await pg.wait_for_timeout(100)
        pins = box.locator('.shell .pin input')
        if await pins.count() == 0: return
        await pins.first.fill(v); await pins.first.press('Enter'); await pg.wait_for_timeout(300)
async def predict(pg, box, pick, inputs=()):
    await box.locator('.opt').nth(pick).click(); await box.locator('.btn.go').click(); await pg.wait_for_timeout(600)
    await feed(pg, box, inputs); await pg.wait_for_timeout(400)
async def check_ex(pg, box, code, inputs=()):
    await box.locator('textarea').fill(code); await box.locator('[data-check]').click(); await pg.wait_for_timeout(700)
    await feed(pg, box, inputs); await pg.wait_for_timeout(400)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errors.append(str(e)))
        await pg.goto(URL); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        html = await pg.content()
        check('沒有第 1 堂殘留（Hello, World、名牌）', 'Hello, World' not in html and '名牌' not in html)
        check('沒有 Scratch／Arduino', 'Scratch' not in html and 'Arduino' not in html)
        await pg.fill('#stName', '測試同學'); await pg.fill('#stClass', '3A'); await pg.fill('#stNo', '12'); await pg.click('#btnStart'); await pg.wait_for_timeout(300)
        check('登記後進入第 1 章', await current(pg) == 's1')
        check('模擬器檔名 L02_', 'L02_測試同學.py' in await pg.locator('#c1 .th.full .ttl').text_content())
        # 第 1 章
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 1)
        sh = await c1.nth(0).locator('.shell').text_content()
        check('試一試 1 輸出', '我喜歡 魚蛋' in sh and '我喜歡 food' in sh, sh)
        await check_ex(pg, ex1, 'cls = "3A"\nprint("我讀", "3A", "班")')
        check('練習 1 直接寫 "3A" 被拒', '變量 cls' in await ex1.locator('[data-fb]').text_content())
        await check_ex(pg, ex1, 'cls = "3A"\nprint("我讀", cls, "班")')
        check('練習 1 完成 5 分', '5 分' in await ex1.locator('[data-fb]').text_content())
        vars_txt = await ex1.locator('.vars').text_content()
        check('Variables 視窗顯示 cls', 'cls' in vars_txt and '"3A"' in vars_txt, vars_txt)
        check('第 1 章 9 / 9', '9 / 9' in await pg.text_content('#navStatus'))
        await go_next(pg); check('進入第 2 章', await current(pg) == 's2')
        # 第 2 章
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 0)
        check('估錯顯示答案字母 C', '答案是 C' in await c2.nth(0).locator('.fb').text_content())
        await check_ex(pg, ex2, 'print(type("你好"))\nprint(type(15))\nprint(type(1.65))\nprint(type(true))')
        sh = await ex2.locator('.shell').text_content(); at = await ex2.locator('.assist').text_content()
        check('true 小寫 → NameError 及 Assistant', 'NameError' in sh and '不認識' in at, at)
        await check_ex(pg, ex2, 'print(type("你好"))\nprint(type(15))\nprint(type(1.65))\nprint(type(True))')
        check('練習 2 完成', '5 分' in await ex2.locator('[data-fb]').text_content())
        check('第 2 章 5 / 9', '5 / 9' in await pg.text_content('#navStatus'))
        await go_next(pg); check('進入第 3 章', await current(pg) == 's3')
        # 第 3 章（有 input）
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 0, inputs=['小明'])
        sh = await c3.nth(0).locator('.shell').text_content()
        check('試一試 3 互動輸入後印出 你好，小明！', '你好，小明！' in sh, sh)
        await check_ex(pg, ex3, 'subject = input("你最喜歡哪一科？")\nprint("我最喜歡 subject 科")', inputs=['電腦'])
        check('練習 3 變量放在引號內被拒', '電腦' in await ex3.locator('[data-fb]').text_content())
        await check_ex(pg, ex3, 'subject = input("你最喜歡哪一科？")\nprint("我最喜歡", subject, "科")', inputs=['電腦'])
        check('練習 3 完成', '5 分' in await ex3.locator('[data-fb]').text_content())
        await go_next(pg); check('進入第 4 章', await current(pg) == 's4')
        # 第 4 章
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        await predict(pg, c4.nth(0), 1, inputs=['3', '4'])
        check('試一試 4a 印出 34', '34' in await c4.nth(0).locator('.shell').text_content())
        await predict(pg, c4.nth(1), 1, inputs=['15'])
        check('試一試 4b 印出 明年你 16 歲', '明年你 16 歲' in await c4.nth(1).locator('.shell').text_content())
        await check_ex(pg, ex4, 'a = input("第一個數：")\nb = input("第二個數：")\nprint("和是", a + b)', inputs=['3', '4'])
        check('練習 4 未轉換被拒（和是 34）', '34' in await ex4.locator('[data-fb]').text_content(), await ex4.locator('[data-fb]').text_content())
        await check_ex(pg, ex4, 'a = int(input("第一個數："))\nb = int(input("第二個數："))\nprint("和是", a + b)', inputs=['3', '4'])
        check('第 4 章 13 / 13', '13 / 13' in await pg.text_content('#navStatus'), await pg.text_content('#navStatus'))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        # 作品
        t = pg.locator('#tiers .tier')
        await check_ex(pg, t.nth(0), 'name = input("你叫甚麼名字？")\ncls = input("你讀哪一班？")\nprint("你好，", name)\nprint("你讀", cls, "班")', inputs=['小明', '3A'])
        check('必做只問 2 條被拒', '只問了 2' in await t.nth(0).locator('[data-fb]').text_content())
        good = 'name = input("你叫甚麼名字？")\ncls = input("你讀哪一班？")\nhobby = input("你的興趣是甚麼？")\nprint("你好，", name)\nprint("你讀", cls, "班")\nprint("你的興趣是", hobby)'
        await check_ex(pg, t.nth(0), good, inputs=['小明', '3A', '打籃球'])
        check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'))
        check('可去小測', not await next_disabled(pg))
        await check_ex(pg, t.nth(1), good + '\nage = input("你幾歲？")\nprint("明年你", age + 1, "歲")', inputs=['小明', '3A', '打籃球', '15'])
        check('進階未 int() 出錯被指出', '轉成數字' in await t.nth(1).locator('[data-fb]').text_content(), await t.nth(1).locator('[data-fb]').text_content())
        await check_ex(pg, t.nth(1), good + '\nage = int(input("你幾歲？"))\nprint("明年你", age + 1, "歲")', inputs=['小明', '3A', '打籃球', '15'])
        check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'))
        await check_ex(pg, t.nth(2), good + '\nyear = int(input("你哪一年出生？"))\nprint("你今年", 2026 - year, "歲")', inputs=['小明', '3A', '打籃球', '2011'])
        check('挑戰沒有 str() 被提醒', 'str()' in await t.nth(2).locator('[data-fb]').text_content())
        await check_ex(pg, t.nth(2), good + '\nyear = int(input("你哪一年出生？"))\nprint("你今年 " + str(2026 - year) + " 歲")', inputs=['小明', '3A', '打籃球', '2011'])
        check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'))
        await go_next(pg); check('進入小測', await current(pg) == 's6')
        q = pg.locator('#quiz .predict')
        await predict(pg, q.nth(0), 1); await predict(pg, q.nth(1), 2); await predict(pg, q.nth(2), 0)
        await pg.fill('#reflect', 'TypeError 出現時我想起要加 int()。'); await pg.click('#btnExit'); await pg.wait_for_timeout(800)
        check('提交後進入報告', await current(pg) == 's7')
        # 9 + 5 + 9 + 13 + 40 + (5+5+0+5) = 91
        check('總分 91', await pg.text_content('#scoreNow') == '91', await pg.text_content('#scoreNow'))
        check('報告標題為第 2 堂', '第 2 堂 變量與輸入' in await pg.text_content('#reportBox'))
        await pg.reload(); await pg.wait_for_timeout(800)
        check('重新載入後分數保留', await pg.text_content('#scoreNow') == '91')
        await pg.click('#btnTeacher'); await pg.fill('#pin', 'py2026'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
        check('老師區答案為第 2 堂', 'cls = "3A"' in await pg.text_content('#tpanel'))
        await pg.locator('#pinX').click()
        await pg.click('#steps button[data-i="4"]'); await pg.wait_for_timeout(300)
        await pg.screenshot(path='/tmp/py3_l2_desktop.png', full_page=True)
        m = await b.new_page(viewport={'width': 390, 'height': 844})
        await m.goto(URL); await m.wait_for_timeout(800)
        await m.click('#btnTeacher'); await m.fill('#pin', 'py2026'); await m.click('#pinGo'); await m.wait_for_timeout(200); await m.click('#tpanel [data-j="2"]'); await m.wait_for_timeout(300)
        sw = await m.evaluate('document.documentElement.scrollWidth')
        check('手機闊度無橫向捲動（第 2 章有表格）', sw <= 392, str(sw))
        await m.screenshot(path='/tmp/py3_l2_mobile.png', full_page=True)
        await b.close()
    real = [e for e in errors if 'ERR_TUNNEL_CONNECTION_FAILED' not in e and 'ERR_INTERNET_DISCONNECTED' not in e]
    check('沒有 console 錯誤（不計 Google Fonts）', not real, '; '.join(real)[:300])
    fails = [r for r in res if not r[1]]
    print(f'\n{len(res)-len(fails)} / {len(res)} 通過')
    sys.exit(1 if fails else 0)

asyncio.run(main())
