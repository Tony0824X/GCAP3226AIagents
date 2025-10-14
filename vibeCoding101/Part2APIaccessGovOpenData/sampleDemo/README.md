# 香港天文台即時天氣資料 API 說明

## 資料來源
API 連結：
https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en

## 可取得的資料類型
- 各區降雨量（rainfall）
- 天氣圖示（icon）
- 特別天氣提示（specialWxTips）
- 紫外線指數（uvindex）
- 各區溫度（temperature）
- 濕度（humidity）
- 資料更新時間（updateTime）

## 資料格式
API 回傳 JSON 格式，包含多個欄位，每個欄位都對應不同的天氣資訊。

## 進階資料探索
此 API 並不直接提供其他連結，但你可以參考香港天文台的 [Open Data 主頁](https://data.weather.gov.hk/weatherAPI/doc/) 來獲取更多 API 文件與資料型別。

## 取得資料的步驟（非程式人員易懂的偽程式碼）

1. 打開瀏覽器，進入 API 網址。
2. 你會看到一串結構化的資料（JSON 格式）。
3. 若要自動取得資料，可用下列步驟：

```
偽程式碼：
1. 設定 API 網址
2. 用工具（如 Excel、Google Sheets、或網頁）抓取網址內容
3. 解析資料（通常工具會自動幫你整理成表格）
4. 查看你需要的欄位，例如溫度、濕度、降雨量等
```

## 進階：如何遞迴探索更多資料
- 進入 [API 文件頁](https://data.weather.gov.hk/weatherAPI/doc/) 查看所有可用的 API。
- 每個 API 都有不同的 dataType，例如：天氣預報、警告、雷達圖等。
- 你可以更換網址中的 dataType 參數來取得不同資料。

## 參考連結
- [香港天文台 Open Data 主頁](https://data.weather.gov.hk/weatherAPI/doc/)
- [API 文件（英文）](https://data.weather.gov.hk/weatherAPI/doc/HKO_Open_Data_API_Documentation.pdf)

---
本說明檔自動生成，歡迎根據需要補充。
