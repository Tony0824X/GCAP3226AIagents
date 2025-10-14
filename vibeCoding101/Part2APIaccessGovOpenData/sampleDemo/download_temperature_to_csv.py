import requests
import csv

# API 連結
API_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

# 取得資料
response = requests.get(API_URL)
data = response.json()

# 以溫度資料為例，轉存為 CSV
csv_filename = "temperature_data.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # 寫入標題
    writer.writerow(["place", "value", "unit", "recordTime"])
    # 寫入資料
    for entry in data["temperature"]["data"]:
        writer.writerow([
            entry["place"],
            entry["value"],
            entry["unit"],
            data["temperature"]["recordTime"]
        ])
print(f"已下載並儲存為 {csv_filename}")
