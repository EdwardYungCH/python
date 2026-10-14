"""各堂 Playwright 測試共用的小工具。"""
import os, sys

errors, res = [], []
def check(name, ok, extra=''):
    res.append((name, ok)); print(('PASS ' if ok else 'FAIL ') + name + (' — ' + extra if extra else ''))
def url_of(n):
    return 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', f'lesson{n}', 'index.html'))
async def current(pg): return await pg.evaluate('document.querySelector("section.card.current").id')
async def next_disabled(pg): return await pg.locator('#btnNext').is_disabled()
async def go_next(pg): await pg.click('#btnNext'); await pg.wait_for_timeout(250)
async def feed(pg, box, values):
    for v in values:
        for _ in range(20):
            if await box.locator('.shell .pin input').count(): break
            await pg.wait_for_timeout(100)
        pins = box.locator('.shell .pin input')
        if await pins.count() == 0: return
        await pins.first.fill(str(v)); await pins.first.press('Enter'); await pg.wait_for_timeout(300)
async def predict(pg, box, pick, inputs=()):
    await box.locator('.opt').nth(pick).click(); await box.locator('.btn.go').click(); await pg.wait_for_timeout(600)
    await feed(pg, box, inputs); await pg.wait_for_timeout(400)
async def check_ex(pg, box, code, inputs=(), wait=8000):
    fbl = box.locator('[data-fb]'); old = await fbl.text_content() if await fbl.count() else ''
    await box.locator('textarea').fill(code); await box.locator('[data-check]').click(); await pg.wait_for_timeout(700)
    await feed(pg, box, inputs)
    # 等檢查結果出現（海龜等較慢的檢查可能要幾秒）
    for _ in range(int(wait / 200)):
        if await fbl.count() and (await fbl.text_content()) not in ('', old): break
        await pg.wait_for_timeout(200)
    await pg.wait_for_timeout(300)
async def fb(box): return await box.locator('[data-fb]').text_content()
async def register(pg):
    await pg.fill('#stName', '測試同學'); await pg.fill('#stClass', '3A'); await pg.fill('#stNo', '12'); await pg.click('#btnStart'); await pg.wait_for_timeout(300)
async def submit_quiz(pg, picks, text):
    q = pg.locator('#quiz .predict')
    for i, pk in enumerate(picks): await predict(pg, q.nth(i), pk)
    await pg.fill('#reflect', text); await pg.click('#btnExit'); await pg.wait_for_timeout(800)
async def common_tail(pg, b, n, expect_score, teacher_marker, mobile_chapter=2):
    check(f'總分 {expect_score}', await pg.text_content('#scoreNow') == str(expect_score), await pg.text_content('#scoreNow'))
    check('報告有驗證碼', '驗證碼' in await pg.text_content('#reportBox'))
    await pg.reload(); await pg.wait_for_timeout(800)
    check('重新載入後分數保留', await pg.text_content('#scoreNow') == str(expect_score))
    await pg.click('#btnTeacher'); await pg.fill('#pin', 'wrong'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
    check('錯 PIN 拒絕', 'PIN 不正確' in await pg.text_content('#tpanel'))
    await pg.fill('#pin', 'py2026'); await pg.click('#pinGo'); await pg.wait_for_timeout(200)
    check('老師區答案正確', teacher_marker in await pg.text_content('#tpanel'))
    await pg.locator('#pinX').click()
    await pg.click('#steps button[data-i="2"]'); await pg.wait_for_timeout(300)
    await pg.screenshot(path=f'/tmp/py3_l{n}_desktop.png', full_page=True)
    m = await b.new_page(viewport={'width': 390, 'height': 844})
    await m.goto(url_of(n)); await m.wait_for_timeout(800)
    await m.click('#btnTeacher'); await m.fill('#pin', 'py2026'); await m.click('#pinGo'); await m.wait_for_timeout(200); await m.click(f'#tpanel [data-j="{mobile_chapter}"]'); await m.wait_for_timeout(300)
    sw = await m.evaluate('document.documentElement.scrollWidth')
    check('手機闊度無橫向捲動', sw <= 392, str(sw))
    top = await m.evaluate('document.querySelector(".topbar").getBoundingClientRect().height')
    check('頂部欄不超過 110px', top <= 110, str(top))
    await m.screenshot(path=f'/tmp/py3_l{n}_mobile.png', full_page=True)
def finish():
    real = [e for e in errors if 'ERR_TUNNEL_CONNECTION_FAILED' not in e and 'ERR_INTERNET_DISCONNECTED' not in e]
    check('沒有 console 錯誤（不計 Google Fonts）', not real, '; '.join(real)[:300])
    fails = [r for r in res if not r[1]]
    print(f'\n{len(res)-len(fails)} / {len(res)} 通過')
    sys.exit(1 if fails else 0)
def wire(pg):
    pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errors.append(str(e)))
