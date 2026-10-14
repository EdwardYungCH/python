"""第 8 堂「列表」流程測試。python3 tools/test_lesson8.py"""
import asyncio, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.async_api import async_playwright
from testlib import *

BASE = 'scores = []\nfor i in range(5):\n    s = int(input("分數："))\n    scores.append(s)\ntotal = 0\nfor s in scores:\n    total += s\nbiggest = scores[0]\nfor s in scores:\n    if s > biggest:\n        biggest = s\nprint("總和", total)\nprint("平均", round(total / len(scores), 1))\nprint("最高分", biggest)'
ADV = BASE + '\npassed = 0\nfor s in scores:\n    if s >= 50:\n        passed += 1\nprint(passed, "人合格")\npos = 0\nfor i in range(len(scores)):\n    if scores[i] > scores[pos]:\n        pos = i\nprint("最高分是第", pos + 1, "位")'
CHA = 'names = ["Amy", "Ben", "Cat", "Dan", "Eve"]\nscores = []\nfor i in range(5):\n    scores.append(int(input("分數：")))\ntarget = input("名字：")\nfound = -1\nfor i in range(len(names)):\n    if names[i] == target:\n        found = i\nif found == -1:\n    print("找不到")\nelse:\n    print(target, "的分數是", scores[found])'
S5 = ['80', '65', '92', '47', '73']

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 900}); wire(pg)
        await pg.goto(url_of(8)); await pg.wait_for_timeout(800)
        check('Skulpt 載入', '就緒' in await pg.text_content('#pyStatus'))
        check('標題是第 8 堂', '第 8 堂' in await pg.text_content('.topbar'))
        await register(pg); check('進入第 1 章', await current(pg) == 's1')
        c1 = pg.locator('#c1 .predict'); ex1 = pg.locator('#c1 .exbox')
        await predict(pg, c1.nth(0), 0)
        await check_ex(pg, ex1, 'names = ["Amy", "Ben", "Cas"]\nnames[3] = "Cat"\nprint(len(names))\nprint(names[0])')
        sh = await ex1.locator('.shell').text_content(); at = await ex1.locator('.assist').text_content(); check('names[3] 出 IndexError 並有 Assistant', 'IndexError' in sh and '索引' in at, at[:60])
        await check_ex(pg, ex1, 'names = ["Amy", "Ben", "Cas"]\nnames[2] = "Cat"\nprint(len(names))\nprint(names[0])'); check('練習 1 完成', '5 分' in await fb(ex1))
        await go_next(pg)
        c2 = pg.locator('#c2 .predict'); ex2 = pg.locator('#c2 .exbox')
        await predict(pg, c2.nth(0), 0); check('估錯顯示答案 B', '答案是 B' in await c2.nth(0).locator('.fb').text_content())
        await check_ex(pg, ex2, 'names = []\nfor i in range(3):\n    n = input("名字：")\n    names.append(n)\nprint(names)', inputs=['Amy', 'Ben', 'Cat']); check('練習 2 完成', '5 分' in await fb(ex2), await fb(ex2))
        await go_next(pg)
        c3 = pg.locator('#c3 .predict'); ex3 = pg.locator('#c3 .exbox')
        await predict(pg, c3.nth(0), 0); await predict(pg, c3.nth(1), 1)
        await check_ex(pg, ex3, 'scores = [80, 65, 92, 47, 73]\nprint(min(scores))'); check('練習 3 用 min() 被拒', 'min()' in await fb(ex3))
        await check_ex(pg, ex3, 'scores = [80, 65, 92, 47, 73]\nsmallest = 0\nfor s in scores:\n    if s < smallest:\n        smallest = s\nprint(smallest)'); check('練習 3 起始值 0 被拒', 'scores[0]' in await fb(ex3), await fb(ex3))
        await check_ex(pg, ex3, 'scores = [80, 65, 92, 47, 73]\nsmallest = scores[0]\nfor s in scores:\n    if s < smallest:\n        smallest = s\nprint(smallest)'); check('練習 3 完成', '5 分' in await fb(ex3))
        check('第 3 章 13 / 13', '13 / 13' in await pg.text_content('#navStatus'))
        await go_next(pg)
        c4 = pg.locator('#c4 .predict'); ex4 = pg.locator('#c4 .exbox')
        await predict(pg, c4.nth(0), 1)
        await ex4.locator('details.help summary').click(); await ex4.locator('[data-a]').click()
        await check_ex(pg, ex4, 'scores = [80, 35, 92, 47, 73]\nfailed = 0\nfor s in scores:\n    if s < 50:\n        failed += 1\nprint(failed)'); check('練習 4 看答案後只得 1 分', '1 分' in await fb(ex4))
        await go_next(pg); check('進入作品', await current(pg) == 's5')
        t = pg.locator('#tiers .tier')
        await check_ex(pg, t.nth(0), BASE.replace('biggest = scores[0]\nfor s in scores:\n    if s > biggest:\n        biggest = s', 'biggest = max(scores)'), inputs=S5); check('必做用 max() 被拒', 'max()' in await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), BASE.replace('round(total / len(scores), 1)', 'total // len(scores)'), inputs=S5); check('必做平均算錯被捉到', '71.4' in await fb(t.nth(0)), await fb(t.nth(0)))
        await check_ex(pg, t.nth(0), BASE, inputs=S5); check('必做完成 25 分', '25 分' in await pg.text_content('#tfb_t1'), await fb(t.nth(0)))
        await check_ex(pg, t.nth(1), ADV.replace('pos + 1', 'pos'), inputs=S5); check('進階第幾位少 1 被捉到', '第 3 位' in await fb(t.nth(1)), await fb(t.nth(1)))
        await check_ex(pg, t.nth(1), ADV, inputs=S5); check('進階完成 10 分', '10 分' in await pg.text_content('#tfb_t2'), await fb(t.nth(1)))
        await check_ex(pg, t.nth(2), CHA.replace('if found == -1:\n    print("找不到")\nelse:\n    print(target, "的分數是", scores[found])', 'print(target, "的分數是", scores[found])'), inputs=S5 + ['Cat']); check('挑戰找不到時出錯被捉到', 'Zoe' in await fb(t.nth(2)), await fb(t.nth(2)))
        await check_ex(pg, t.nth(2), CHA, inputs=S5 + ['Cat']); check('挑戰完成 5 分', '5 分' in await pg.text_content('#tfb_t3'), await fb(t.nth(2)))
        await go_next(pg); await submit_quiz(pg, [1, 1, 0], '我把最大值的起始值設成 0，試一試提醒了我。')
        check('提交後進入報告', await current(pg) == 's7')
        # 9 + (0+5) + 13 + (4+1) + 40 + (5+5+0+5) = 87
        await common_tail(pg, b, 8, 87, 'scores[0]、<', mobile_chapter=3)
        await b.close()
    finish()

asyncio.run(main())
