# 中三 Python 編程

中三 Python 自學課程（10 堂 × 80 分鐘），獨立課程，章節次序跟 [W3Schools Python Tutorial](https://www.w3schools.com/python/)，只教高中 ICT 會用到的部分。每堂是一個獨立的 HTML 檔，Python 執行器（[Skulpt](https://skulpt.org)，MIT 授權）已內嵌，不需要網絡也能執行。

學生網址（需在 Settings → Pages 開啟 main / root）：`https://edwardyungch.github.io/python/`

## 課堂進度

| 堂 | 主題 | W3Schools 章節 | 狀態 |
|---|---|---|---|
| 1 | 開始寫 Python | Get Started、Syntax、Output、Comments | 完成（第 2.2 版，內置 Thonny 模擬器） |
| 2 | 變量與輸入 | Variables、Data Types、Casting、User Input | 完成 |
| 3 | 數字與運算符 | Numbers、Operators、Booleans | 完成 |
| 4 | If…Else | If…Else | 完成 |
| 5 | While 迴圈 | While Loops、Random | 完成 |
| 6 | For 迴圈與 Range | For Loops、Range；turtle | 完成（模擬器加海龜畫布） |
| 7 | 字串 | Strings、Slicing、Methods、f-string | 完成 |
| 8 | 列表 | Lists | 完成 |
| 9 | 函數入門與除錯 | Functions、Return；錯誤類型；逐步執行 | 完成（模擬器加逐步執行） |
| 10 | 迷你專題及選科導航 | — | 規劃 |

## 結構

```
index.html                 首頁：LESSONS 陣列列出各堂（href 留空 = 準備中）
lessonN/index.html         第 N 堂成品（單一檔案，含 Skulpt，約 1 MB）
src/lessonN/lessonN.src.html   第 N 堂原始碼（Skulpt 由 CDN 載入，約 46 KB，改這個）
tools/test_lessonN.py      Playwright 流程測試
tools/lessongen.py         共用產生器：由第 1 堂模板產生第 N 堂
tools/make_lessonN.py      第 N 堂的內容（章節 HTML、章節 JS、三層作品、小測），執行後再 build
tools/testlib.py           各堂測試共用工具
tools/build.py             建置：python3 tools/build.py N（把 Skulpt 內嵌進 lessonN/index.html）
tools/skulpt/              Skulpt 建置檔（skulpt.min.js、skulpt-stdlib.js）
```

## 每堂的設計

- 登記及溫習 → 每堂 2 至 3 章（解說 → 試一試：先估後執行 → 練習：填空）→ 作品（必做／進階／挑戰，在 Thonny 做）→ 小測 → 成績報告。
- 學生頁面只有 Python，不作 Scratch、Arduino 或高中課程代號的對照。
- 版面：頂部進度列（可回看已完成的章）、一次只顯示一章、底部「上一章／下一章」；每章「學 → 試 → 練」三步以左側直線串連，章首有學習目標、章末有小結。
- 進度自動儲存在瀏覽器（localStorage）；章節順序解鎖，完成本章才可按「下一章」。
- 提示和「直接看答案」收在「需要幫忙？」摺疊區內；練習答錯兩次自動出提示。
- 全部程式在網頁內的 Thonny 模擬器寫和執行（Skulpt）：標題列、工具列（▶ 執行、儲存）、行號、Shell（`>>> %Run 檔名.py`）、Thonny 格式的 Traceback、Assistant 中文解釋、Variables 視窗、🐞 逐步執行（debug:true：逐行按「下一步」，高亮現行，Variables 即時更新）、海龜畫布（turtle:true）。試一試用精簡版（編輯器＋Shell），練習和作品用完整版。檢查時以測試輸入自動評分。
- 成績報告帶驗證碼（HMAC-SHA256），老師區（PIN）可核對答案和驗證碼。
- 課堂頁沒有返回首頁的連結。

## 測試

```
python3 tools/test_lesson1.py
python3 tools/test_lesson2.py
python3 tools/test_lesson3.py
python3 tools/test_lesson4.py
python3 tools/test_lesson5.py
python3 tools/test_lesson6.py
python3 tools/test_lesson7.py
python3 tools/test_lesson8.py
python3 tools/test_lesson9.py
```

需要 Playwright 及 Chromium。測試會走完整個流程（含故意答錯、看答案扣分、重新載入後保留、老師 PIN、手機闊度）。

## 注意

- 公開 repo 內的老師 PIN（`py2026`）和報告密鑰任何人都看得到；驗證碼只防學生隨手改報告，不防有心人。
- 同一部電腦輪流使用時，要按頁底「清除進度」。
- 改動原始碼後執行 `python3 tools/build.py N` 重新建置，再跑測試。
