import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.screener.in/company/COASTCORP/consolidated/#balance-sheet"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Company Name
company = soup.find("h1").text.strip()
print("Company:", company)

# Extract top ratios
data = []

ratios = soup.select("ul#top-ratios li")

for item in ratios:
    name = item.find("span", class_="name")
    value = item.find("span", class_="number")

    if name and value:
        data.append({
            "Metric": name.text.strip(),
            "Value": value.text.strip()
        })

df = pd.DataFrame(data)

print(df)

df.to_csv("coastcorp.csv", index=False)