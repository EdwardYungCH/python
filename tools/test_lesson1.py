import asyncio, sys, json
from playwright.async_api import async_playwright

import os
URL = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lesson1', 'index.html'))
errors = []
res = []
def check(name, ok, extra=''):
    res.append((name, ok, extra)); print(('PASS ' if ok else 'FAIL ') + name + (' — ' + extra if extra else ''))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 900})
        pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errors.append(str(e)))
        await pg.goto(URL)
        await pg.wait_for_timeout(800)
        st = await pg.text_content('#pyStatus')
        check('Skulpt 載入', '就緒' in st, st)
        # s0
        await pg.fill('#stName', '測試同學'); await pg.fill('#stClass', '3A'); await pg.fill('#stNo', '12')
        await pg.click('#btnStart'); await pg.wait_for_timeout(300)
        check('登記後解鎖第 1 節', not await pg.locator('#s1').evaluate('e=>e.classList.contains("locked")'))
        # s1 matching: 4 right, 1 wrong
        ans = ['print("你好")', 'name = input("你叫甚麼名字？")', 'score = 0', 'if score > 50:', 'while True:']
        for i, a in enumerate(ans):
            await pg.select_option(f'#match_{i}', a)
        await pg.click('#btnMatch'); await pg.wait_for_timeout(300)
        fb = await pg.text_content('#matchFb')
        check('配對 4/5 得 8 分', '4 / 5' in fb and '8 分' in fb, fb)
        check('第 2 節解鎖', not await pg.locator('#s2').evaluate('e=>e.classList.contains("locked")'))
        # s2 predictions: answer all; one wrong on purpose
        preds2 = await pg.locator('#pred2 .predict').all()
        correct = [0, 1, 2, 1]
        for i, box in enumerate(preds2):
            pick = correct[i] if i != 1 else 0
            await box.locator('.opt').nth(pick).click()
            await box.locator('.btn.go').click()
            await pg.wait_for_timeout(1200)
        out0 = await preds2[0].locator('.out').last.text_content()
        check('執行器印出 你好，中三', '你好，中三' in out0, out0.strip())
        out2 = await preds2[2].locator('.out').last.text_content()
        check('3+4 與 "3 + 4" 輸出', '7' in out2 and '3 + 4' in out2, out2.strip())
        score = await pg.text_content('#scoreNow')
        check('分數 8 + 7.5 = 15.5', score == '15.5', score)
        check('第 3 節解鎖', not await pg.locator('#s3').evaluate('e=>e.classList.contains("locked")'))
        # s3: interactive input test on first runner
        preds3 = await pg.locator('#pred3 .predict').all()
        box = preds3[0]
        await box.locator('.opt').nth(1).click(); await box.locator('.btn.go').click()
        await pg.wait_for_timeout(800)
        pin = box.locator('.out .pin input')
        check('input() 顯示輸入框', await pin.count() == 1)
        await pin.fill('小明'); await pin.press('Enter'); await pg.wait_for_timeout(800)
        out = await box.locator('.out').last.text_content()
        check('輸入小明後印出 你好，小明！', '你好，小明！' in out, out.strip())
        for i, box in enumerate(preds3[1:], start=1):
            await box.locator('.opt').nth([1, 1, 0][i-1]).click(); await box.locator('.btn.go').click()
            await pg.wait_for_timeout(600)
            # answer any pending inputs
            for _ in range(3):
                pins = box.locator('.out .pin input')
                if await pins.count():
                    await pins.first.fill('3'); await pins.first.press('Enter'); await pg.wait_for_timeout(500)
        check('第 4 節解鎖', not await pg.locator('#s4').evaluate('e=>e.classList.contains("locked")'))
        # s4 bugs
        tiers4 = await pg.locator('#bugs .tier').all()
        # bug1: run wrong first to see hint
        await tiers4[0].locator('.btn.run').click(); await pg.wait_for_timeout(600)
        o = await tiers4[0].locator('.out').text_content()
        check('錯誤一執行顯示 SyntaxError 及中文提示', 'SyntaxError' in o and '引號' in o, o.strip()[:120])
        await tiers4[0].locator('textarea').fill('print("歡迎來到中三 Python")')
        await tiers4[0].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('錯誤一修正 5 分', '5 分' in await pg.text_content('#bugfb_b1'))
        # bug2 reveal then fix -> 1 point
        await tiers4[1].locator('[data-h="2"]').click()
        await tiers4[1].locator('textarea').fill('print("第一堂完成")')
        await tiers4[1].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('錯誤二看答案後只得 1 分', '1 分' in await pg.text_content('#bugfb_b2'), await pg.text_content('#bugfb_b2'))
        # bug3 wrong fix first
        await tiers4[2].locator('textarea').fill('name = input("你叫甚麼名字？")\nprint("你好，" + name')
        await tiers4[2].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('錯誤三未修正不給分', '仍未' in await pg.text_content('#bugfb_b3'))
        await tiers4[2].locator('textarea').fill('name = input("你叫甚麼名字？")\nprint("你好，" + name)')
        await tiers4[2].locator('[data-check]').click(); await pg.wait_for_timeout(800)
        # the run() will show an input box; answer it
        pins = tiers4[2].locator('.out .pin input')
        if await pins.count():
            await pins.first.fill('小明'); await pins.first.press('Enter'); await pg.wait_for_timeout(500)
        check('錯誤三修正 5 分', '5 分' in await pg.text_content('#bugfb_b3'))
        check('第 5 節解鎖', not await pg.locator('#s5').evaluate('e=>e.classList.contains("locked")'))
        # s5 tiers
        t = await pg.locator('#tiers .tier').all()
        await t[0].locator('[data-check]').click(); await pg.wait_for_timeout(500)
        check('必做未填 ____ 被拒', '____' in await t[0].text_content())
        await t[0].locator('textarea').fill('name = input("你叫甚麼名字？")\ncls = input("你讀哪一班？")\nhobby = input("你的興趣是甚麼？")\nprint("你好，" + name + "！")\nprint("你讀 " + cls + " 班。")\nprint("你的興趣是" + hobby + "。")')
        await t[0].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('必做完成 20 分', '20 分' in await pg.text_content('#tfb_t1'))
        check('第 6 節解鎖（必做即可）', not await pg.locator('#s6').evaluate('e=>e.classList.contains("locked")'))
        await t[1].locator('textarea').fill('a=input("1")\nb=input("2")\nc=input("3")\nprint(a,b,c)')
        await t[1].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('進階只問 3 條被拒', '只問了 3' in await t[1].text_content())
        await t[1].locator('textarea').fill('a=input("1")\nb=input("2")\nc=input("3")\nd=input("4")\nprint(a,b,c)\nprint("科目："+d)')
        await t[1].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'))
        await t[2].locator('textarea').fill('f=input("食物？")\np=input("地方？")\nprint("我最喜歡在"+p+"吃"+f+"。")')
        await t[2].locator('[data-check]').click(); await pg.wait_for_timeout(1000)
        check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'))
        # s6 exit
        ex = await pg.locator('#exitq .predict').all()
        check('出口卡預測沒有執行器', await ex[0].locator('.runner').count() == 0)
        await ex[0].locator('.opt').nth(0).click(); await ex[0].locator('.btn.go').click()
        await ex[1].locator('.opt').nth(2).click(); await ex[1].locator('.btn.go').click()
        await pg.wait_for_timeout(300)
        await ex[2].locator('textarea').fill('print("今天是第 1 堂")')
        await ex[2].locator('.btn.go').click(); await pg.wait_for_timeout(800)
        check('出口卡改錯正確', '+5' in await ex[2].locator('.row span').text_content())
        await pg.click('#btnExit'); await pg.wait_for_timeout(200)
        check('自評太短被拒', '一句' in await pg.text_content('#exitFb'))
        await pg.fill('#reflect', '我先看錯誤訊息最後一行，再找行號。')
        await pg.click('#btnExit'); await pg.wait_for_timeout(800)
        rep = await pg.text_content('#reportBox')
        score = await pg.text_content('#scoreNow')
        # expected: warm 8 + p2 7.5 + p3 10 + bugs 11 + tiers 35 + exit (5+0+5+5)=15 -> 86.5
        check('總分 86.5', score == '86.5', score)
        check('報告有驗證碼', '驗證碼' in rep)
        # persistence
        await pg.reload(); await pg.wait_for_timeout(800)
        check('重新載入後分數保留', await pg.text_content('#scoreNow') == '86.5')
        check('重新載入後出口卡鎖定', await pg.locator('#btnExit').is_disabled())
        # teacher PIN
        await pg.click('#btnTeacher'); await pg.fill('#pin', 'wrong'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
        check('錯 PIN 拒絕', 'PIN 不正確' in await pg.text_content('#tpanel'))
        await pg.fill('#pin', 'py2026'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
        check('正確 PIN 顯示答案', '配對 1' in await pg.text_content('#tpanel'))
        await pg.screenshot(path='/tmp/py3_shot_desktop.png', full_page=True)
        # mobile
        m = await b.new_page(viewport={'width': 390, 'height': 844})
        await m.goto(URL); await m.wait_for_timeout(800)
        sw = await m.evaluate('document.documentElement.scrollWidth')
        check('手機闊度無橫向捲動', sw <= 392, str(sw))
        await m.screenshot(path='/tmp/py3_shot_mobile.png', full_page=True)
        await b.close()
    real=[e for e in errors if 'ERR_TUNNEL_CONNECTION_FAILED' not in e and 'ERR_INTERNET_DISCONNECTED' not in e]
    check('沒有 console 錯誤（不計 Google Fonts 載入失敗）', not real, '; '.join(real)[:300])
    fails = [r for r in res if not r[1]]
    print(f'\n{len(res)-len(fails)} / {len(res)} 通過')
    sys.exit(1 if fails else 0)

asyncio.run(main())
