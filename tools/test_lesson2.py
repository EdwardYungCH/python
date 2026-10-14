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
async def predict(pg, box, pick):
    await box.locator('.opt').nth(pick).click(); await box.locator('.btn.go').click(); await pg.wait_for_timeout(900)
async def answer_pins(pg, box, values):
    for v in values:
        pin = box.locator('.shell .pin input')
        if await pin.count():
            await pin.first.fill(v); await pin.first.press('Enter'); await pg.wait_for_timeout(500)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errors.append(str(e)))
        await pg.goto(URL); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        html = await pg.content()
        check('頁面沒有 Scratch／Arduino 字眼', 'Scratch' not in html and 'Arduino' not in html)
        check('標題是第 2 堂', '第 2 堂' in await pg.text_content('.topbar'))
        await pg.fill('#stName', '測試同學'); await pg.fill('#stClass', '3A'); await pg.fill('#stNo', '12'); await pg.click('#btnStart'); await pg.wait_for_timeout(300)
        check('登記後進入第 1 章', await current(pg) == 's1')
        # 第 1 章
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 1)
        sh = await c1.nth(0).locator('.shell').text_content()
        check('試一試 1 印出 name 和 陳大文', 'name' in sh and '陳大文' in sh)
        await ex1.locator('textarea').fill('cls = "3A"\nprint("我讀", "cls", "班")'); await ex1.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 1 引號包變量被拒', '不一樣' in await ex1.locator('[data-fb]').text_content())
        await ex1.locator('textarea').fill('cls = "3A"\nprint("我讀", cls, "班")'); await ex1.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 1 完成；Variables 顯示 cls', '5 分' in await ex1.locator('[data-fb]').text_content() and 'cls' in await ex1.locator('.vars').text_content())
        await go_next(pg); check('進入第 2 章', await current(pg) == 's2')
        # 第 2 章
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 0)
        check('估錯顯示答案 B', '答案是 B' in await c2.nth(0).locator('.fb').text_content())
        await ex2.locator('textarea').fill('print(type("早晨"))\nprint(type(7))\nprint(type(2.5))\nprint(type(False))'); await ex2.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 2 完成', '5 分' in await ex2.locator('[data-fb]').text_content())
        await go_next(pg); check('進入第 3 章', await current(pg) == 's3')
        # 第 3 章
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 1); await predict(pg, c3.nth(1), 2)
        sh = await c3.nth(1).locator('.shell').text_content()
        check('TypeError 以 Thonny 格式顯示', 'Traceback' in sh and 'TypeError' in sh, sh[:120])
        await ex3.locator('textarea').fill('chi = "85"\neng = "85"\ntotal = int(chi) + int(eng)\nprint("總分：", total)'); await ex3.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('練習 3 不用 str() 被拒', 'str(total)' in await ex3.locator('[data-fb]').text_content(), await ex3.locator('[data-fb]').text_content())
        await ex3.locator('textarea').fill('chi = "85"\neng = "85"\ntotal = int(chi) + int(eng)\nprint("總分：" + str(total))'); await ex3.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('第 3 章 13 分', '13 / 13' in await pg.text_content('#navStatus'))
        await go_next(pg); check('進入第 4 章', await current(pg) == 's4')
        # 第 4 章
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        await predict(pg, c4.nth(0), 2)
        await answer_pins(pg, c4.nth(0), ['15'])
        sh = await c4.nth(0).locator('.shell').text_content()
        check('input 試一試：輸入後出 TypeError', 'TypeError' in sh, sh[:150])
        await ex4.locator('textarea').fill('name = input("你叫甚麼名字？")\nyear = input("你哪一年出生？")\nprint(name, "今年", 2026 - year, "歲")'); await ex4.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        fbt = await ex4.locator('[data-fb]').text_content()
        check('練習 4 未轉換出錯被拒', '出錯' in fbt, fbt)
        sh = await ex4.locator('.shell').text_content()
        check('檢查用測試輸入並顯示於 Shell', '測試輸入' in sh and '小明' in sh, sh[:150])
        await ex4.locator('textarea').fill('name = input("你叫甚麼名字？")\nyear = int(input("你哪一年出生？"))\nprint(name, "今年", 2026 - year, "歲")'); await ex4.locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('第 4 章 9 分', '9 / 9' in await pg.text_content('#navStatus'), await pg.text_content('#navStatus'))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        # 作品
        t = pg.locator('#tiers .tier')
        await t.nth(0).locator('textarea').fill('name = input("名字？")\ncls = input("班別？")\nprint("你好，" + name)\nprint("你讀 " + cls + " 班")'); await t.nth(0).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('必做只問 2 條被拒', '只問了 2' in await t.nth(0).locator('[data-fb]').text_content())
        good = 'name = input("名字？")\ncls = input("班別？")\nhobby = input("興趣？")\nprint("你好，" + name + "！")\nprint("你讀 " + cls + " 班。")\nprint("原來你喜歡" + hobby + "。")'
        await t.nth(0).locator('textarea').fill(good); await t.nth(0).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'))
        check('作品 Shell 顯示測試輸入及回話', '小明' in await t.nth(0).locator('.shell').text_content())
        await t.nth(1).locator('textarea').fill(good + '\nyear = input("出生年份？")\nprint("你今年", 2026 - int(year), "歲。")'); await t.nth(1).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'), await t.nth(1).locator('[data-fb]').text_content())
        await t.nth(2).locator('textarea').fill(good + '\nyear = int(input("出生年份？"))\nh = float(input("身高？"))\nw = float(input("體重？"))\nprint("身高", h, "米，體重", w, "公斤")\nprint(type(h))'); await t.nth(2).locator('[data-check]').click(); await pg.wait_for_timeout(900)
        check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await t.nth(2).locator('[data-fb]').text_content())
        await go_next(pg); check('進入小測', await current(pg) == 's6')
        q = pg.locator('#quiz .predict')
        await predict(pg, q.nth(0), 1); await predict(pg, q.nth(1), 3); await predict(pg, q.nth(2), 0)
        await pg.fill('#reflect', '我先看 Traceback 最後一行，再看 Assistant。'); await pg.click('#btnExit'); await pg.wait_for_timeout(800)
        check('提交後進入報告', await current(pg) == 's7')
        # 9 + 5 + 13 + 9 + 40 + (5+5+0+5) = 91
        check('總分 91', await pg.text_content('#scoreNow') == '91', await pg.text_content('#scoreNow'))
        check('報告標題是第 2 堂', '第 2 堂 變量與輸入' in await pg.text_content('#reportBox'))
        await pg.reload(); await pg.wait_for_timeout(800)
        check('重新載入後分數保留', await pg.text_content('#scoreNow') == '91')
        await pg.click('#btnTeacher'); await pg.fill('#pin', 'py2026'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
        check('老師區答案是第 2 堂的', 'int(chi)' in await pg.text_content('#tpanel'))
        await pg.locator('#pinX').click()
        await pg.click('#steps button[data-i="4"]'); await pg.wait_for_timeout(300)
        await pg.screenshot(path='/tmp/py3_l2_desktop.png', full_page=True)
        m = await b.new_page(viewport={'width': 390, 'height': 844})
        await m.goto(URL); await m.wait_for_timeout(800)
        await m.click('#btnTeacher'); await m.fill('#pin', 'py2026'); await m.click('#pinGo'); await m.wait_for_timeout(200); await m.click('#tpanel [data-j="2"]'); await m.wait_for_timeout(300)
        sw = await m.evaluate('document.documentElement.scrollWidth')
        check('手機闊度無橫向捲動（第 2 章表格）', sw <= 392, str(sw))
        top = await m.evaluate('document.querySelector(".topbar").getBoundingClientRect().height')
        check('頂部欄不超過 110px', top <= 110, str(top))
        await b.close()
    real = [e for e in errors if 'ERR_TUNNEL_CONNECTION_FAILED' not in e and 'ERR_INTERNET_DISCONNECTED' not in e]
    check('沒有 console 錯誤（不計 Google Fonts）', not real, '; '.join(real)[:300])
    fails = [r for r in res if not r[1]]
    print(f'\n{len(res)-len(fails)} / {len(res)} 通過')
    sys.exit(1 if fails else 0)

asyncio.run(main())
