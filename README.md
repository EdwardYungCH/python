# 中三 Python 編程

中三 Python 自學課程（10 堂 × 80 分鐘）。每堂是一個獨立的 HTML 檔，Python 執行器（[Skulpt](https://skulpt.org)，MIT 授權）已內嵌，不需要網絡也能執行。

學生網址（需在 Settings → Pages 開啟 main / root）：`https://edwardyungch.github.io/python/`

## 課堂進度

| 堂 | 主題 | 狀態 |
|---|---|---|
| 1 | 由積木到文字 | 完成 |
| 2 | 變量與運算 | 規劃 |
| 3 | 程式會判斷 | 規劃 |
| 4 | 海龜繪圖與 for 迴圈 | 規劃 |
| 5 | 累加與計數 | 規劃 |
| 6 | while 迴圈與數據驗證 | 規劃 |
| 7 | 列表與標準算法 | 規劃 |
| 8 | 字串、除錯與測試 | 規劃 |
| 9 | 迷你專題（一） | 規劃 |
| 10 | 迷你專題（二）及選科導航 | 規劃 |

## 結構

```
index.html                 首頁：LESSONS 陣列列出各堂（href 留空 = 準備中）
lessonN/index.html         第 N 堂成品（單一檔案，含 Skulpt，約 1 MB）
src/lessonN/lessonN.src.html   第 N 堂原始碼（Skulpt 由 CDN 載入，約 46 KB，改這個）
tools/test_lessonN.py      Playwright 流程測試
```

## 每堂的設計

- 登記 → 熱身 → 示範（先估後執行）→ 改錯 → 三層實作（必做／進階／挑戰）→ 出口卡 → 成績報告。
- 進度自動儲存在瀏覽器（localStorage）；階段順序解鎖。
- 實作在 Thonny 完成，貼回網頁由 Skulpt 以測試輸入自動檢查。
- 成績報告帶驗證碼（HMAC-SHA256），老師區（PIN）可核對答案和驗證碼。
- 課堂頁沒有返回首頁的連結。

## 測試

```
python3 tools/test_lesson1.py
```

需要 Playwright 及 Chromium。測試會走完整個流程（含故意答錯、看答案扣分、重新載入後保留、老師 PIN、手機闊度）。

## 注意

- 公開 repo 內的老師 PIN（`py2026`）和報告密鑰任何人都看得到；驗證碼只防學生隨手改報告，不防有心人。
- 同一部電腦輪流使用時，要按頁底「清除進度」。
- 重新建置離線版：把原始碼中兩行 Skulpt CDN `<script src>` 換成內嵌的 `skulpt.min.js` 和 `skulpt-stdlib.js`（取自 [skulpt](https://github.com/skulpt/skulpt) 的建置檔）。
