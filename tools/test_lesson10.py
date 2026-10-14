"""第 10 堂「迷你專題及選科導航」流程測試。python3 tools/test_lesson10.py"""
import asyncio, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from testlib import *

PROJ = '''# 題目：小食部收銀機　作者：測試同學
# 輸入：三樣食物價錢和付款額
prices = []
for i in range(3):
    prices.append(int(input("價錢：")))
pay = int(input("付款："))
# 處理：累加總數
total = 0
for p in prices:
    total += p
# 輸出
print("總數", total)
if pay >= total:
    print("找續", pay - total)
else:
    print("不夠錢")'''
NO_IF = PROJ.replace('if pay >= total:\n    print("找續", pay - total)\nelse:\n    print("不夠錢")', 'print("找續", pay - total)\nprint("找續", pay - total)\nprint("找續", pay - total)\nprint("找續", pay - total)')
FEW_COMMENTS = PROJ.replace('# 輸入：三樣食物價錢和付款額\n', '').replace('# 輸出\n', '')

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(pg)
        await pg.goto(url_of(10)); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('標題是第 10 堂', '第 10 堂' in await pg.text_content('.topbar'))
        await register(pg); check('進入第 1 章', await current(pg) == 's1')
        check('第 1 章顯示規劃表提示區', await pg.locator('#planBox').count() == 1)
        await pg.click('#btnPlan'); check('四格空白被拒', '四格' in await pg.text_content('#planFb'))
        await pg.fill('#t1in', '10\n20\n30\n100'); await pg.fill('#t1out', '找續 40'); await pg.fill('#t2in', '10\n20\n30\n100'); await pg.fill('#t2out', '不夠錢')
        await pg.click('#btnPlan'); check('兩組相同被拒', '不同' in await pg.text_content('#planFb'))
        await pg.fill('#t2in', '10\n20\n30\n50'); await pg.click('#btnPlan'); await pg.wait_for_timeout(300)
        check('測試數據儲存 5 分', '5 分' in await pg.text_content('#planFb'))
        await go_next(pg); check('進入第 2 章', await current(pg) == 's2')
        c2 = pg.locator('#c2 .predict')
        await predict(pg, c2.nth(0), 0); check('估錯顯示答案 B', '答案是 B' in await c2.nth(0).locator('.fb').text_content())
        await predict(pg, c2.nth(1), 1); await predict(pg, c2.nth(2), 1)
        check('第 2 章 8 / 12', '8 / 12' in await pg.text_content('#navStatus'), await pg.text_content('#navStatus'))
        await go_next(pg); check('進入第 3 章', await current(pg) == 's3')
        cb = pg.locator('#thonnyChecks input')
        check('四個清單項目', await cb.count() == 4)
        await cb.nth(0).check(); await cb.nth(1).check(); await pg.click('#btnThonny'); check('只剔兩項被拒', '頭三項' in await pg.text_content('#thonnyFb'))
        await cb.nth(2).check(); await pg.fill('#thonnyDiff', '太短'); await pg.click('#btnThonny'); check('分別太短被拒', '20 字' in await pg.text_content('#thonnyFb'))
        await pg.fill('#thonnyDiff', '真 Thonny 要自己開檔案和儲存，錯誤訊息是英文，沒有中文 Assistant 解釋；Variables 視窗要自己在 View 開。'); await pg.click('#btnThonny'); await pg.wait_for_timeout(300)
        check('真 Thonny 體驗 8 分', '8 分' in await pg.text_content('#thonnyFb'))
        await go_next(pg); check('進入第 4 章', await current(pg) == 's4')
        for i in range(5): await pg.check(f'input[name="sq{i}"][value="4"]')
        await pg.click('#btnSelf'); check('漏答被拒', '六條' in await pg.text_content('#selfFb'))
        await pg.check('input[name="sq5"][value="2"]'); await pg.click('#btnSelf'); await pg.wait_for_timeout(300)
        check('自我檢視 15 分', '15 分' in await pg.text_content('#selfFb'))
        r = await pg.text_content('#selfResult'); check('結果顯示總分 22 / 24 及較低範疇', '22 / 24' in r and '主動性' in r, r[:80])
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        t = pg.locator('#tiers .tier')
        check('作品 Thonny 有逐步執行和海龜', await t.nth(0).locator('[data-dbg]').count() == 1)
        await check_ex(pg, t.nth(0), NO_IF); check('沒有 if 被拒', '要有 if' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), PROJ.replace('pay - total', 'pay + total')); check('輸出不符預期被捉到', '找續 40' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), PROJ); check('必做用第 1 組數據通過 25 分', '25 分' in await pg.text_content('#tfb_t1'), await fb(t.nth(0)))
        await check_ex(pg, t.nth(1), PROJ.replace('print("不夠錢")', 'print("錢不夠")')); check('第 2 組輸出不符被捉到', '不夠錢' in await fb(t.nth(1)), await fb(t.nth(1)))
        await check_ex(pg, t.nth(1), PROJ); check('進階邊界測試通過 10 分', '10 分' in await pg.text_content('#tfb_t2'), await fb(t.nth(1)))
        await check_ex(pg, t.nth(2), FEW_COMMENTS); check('註解不足被拒', '註解' in await fb(t.nth(2)), await fb(t.nth(2)))
        await check_ex(pg, t.nth(2), PROJ); check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await fb(t.nth(2)))
        await go_next(pg); check('進入小測', await current(pg) == 's6')
        check('小測後是互評紀錄', '互評紀錄' in await pg.text_content('#s6'))
        q = pg.locator('#quiz .predict')
        for i, pk in enumerate([0, 0, 1]): await predict(pg, q.nth(i), pk)
        await pg.fill('#reflect', '太短'); await pg.click('#btnExit'); await pg.wait_for_timeout(200); check('互評紀錄太短被拒', '30 字' in await pg.text_content('#exitFb'))
        await submit_quiz(pg, [], '互評同學：李小明。建議一：付款少於總數時可以提示還差幾多錢。建議二：價錢用小數也可以計算。')
        check('提交後進入報告', await current(pg) == 's7')
        rep = await pg.text_content('#reportBox')
        check('報告載有互評、自我檢視、測試數據', '互評紀錄' in rep and '22 / 24' in rep and '10 / 20 / 30 / 100' in rep, rep[:200])
        # 5 + 8 + 8 + 15 + 40 + (15 + 5) = 96
        await common_tail(pg, b, 10, 96, '免除真 Thonny', mobile_chapter=4)
        # 老師免除第 3 章
        w = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(w)
        await w.goto(url_of(10)); await w.wait_for_timeout(800); await register(w)
        await w.click('#btnTeacher'); await w.fill('#pin', 'py2026'); await w.click('#pinGo'); await w.wait_for_timeout(200); await w.click('#waive3'); await w.wait_for_timeout(300)
        check('老師免除後第 3 章 8 分', await w.text_content('#scoreNow') == '8', await w.text_content('#scoreNow'))
        await w.click('#steps button[data-i="3"]'); await w.wait_for_timeout(300)
        check('免除後第 3 章顯示完成', '8 分' in await w.text_content('#thonnyFb'))
        await b.close()
    finish()

asyncio.run(main())
