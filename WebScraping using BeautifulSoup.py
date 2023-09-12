import requests
import csv
from bs4 import BeautifulSoup

URL = ['https://en.wikipedia.org/wiki/Aabar_Investments',
       'https://en.wikipedia.org/wiki/Abu_Dhabi_Aviation',
       'https://en.wikipedia.org/wiki/Abu_Dhabi_Commercial_Bank',
       'https://en.wikipedia.org/wiki/Abu_Dhabi_Islamic_Bank',
       'https://en.wikipedia.org/wiki/ADNOC_Gas_Processing',
       'https://en.wikipedia.org/wiki/Abu_Dhabi_Media',
       'https://en.wikipedia.org/wiki/TAQA',
       'https://en.wikipedia.org/wiki/Abu_Dhabi_National_Hotels',
       'https://en.wikipedia.org/wiki/Abu_Dhabi_National_Oil_Company',
       'https://en.wikipedia.org/wiki/ADPC',
       'https://en.wikipedia.org/wiki/Air_Arabia',
       'https://en.wikipedia.org/wiki/Al_Dahra_Agricultural_Company',
       'https://en.wikipedia.org/wiki/Al_Ghurair_Group',
       'https://en.wikipedia.org/wiki/Al_Tayer_Group',
       'https://en.wikipedia.org/wiki/Aldar_Properties',
       'https://en.wikipedia.org/wiki/Alpha_Data',
       'https://en.wikipedia.org/wiki/Arab_Center_for_Consultancy_%26_Economic_Studies',
       'https://en.wikipedia.org/wiki/Aramex',
       'https://en.wikipedia.org/wiki/Armada_Group',
       'https://en.wikipedia.org/wiki/Dana_Gas',
       'https://en.wikipedia.org/wiki/Du_(telco)',
       'https://en.wikipedia.org/wiki/Dubai_Bank',
       'https://en.wikipedia.org/wiki/Dubai_Financial_Market',
       'https://en.wikipedia.org/wiki/Dubai_Holding',
       'https://en.wikipedia.org/wiki/Dubai_Islamic_Bank',
       'https://en.wikipedia.org/wiki/Dubai_Media_Incorporated',
       'https://en.wikipedia.org/wiki/DP_World',
       'https://en.wikipedia.org/wiki/Easa_Saleh_Al_Gurg_Group_LLC',
       'https://en.wikipedia.org/wiki/Emaar_Properties',
       'https://en.wikipedia.org/wiki/Emirates_(airline)',
       'https://en.wikipedia.org/wiki/Emirates_Global_Aluminium',
       'https://en.wikipedia.org/wiki/Etihad_Airways',
       'https://en.wikipedia.org/wiki/Etisalat',
       'https://en.wikipedia.org/wiki/First_Gulf_Bank',
       'https://en.wikipedia.org/wiki/Information_Systems_Associates_FZE',
       'https://en.wikipedia.org/wiki/Julphar',
       'https://en.wikipedia.org/wiki/Jumeirah_(hotel_chain)',
       'https://en.wikipedia.org/wiki/Mashreqbank',
       'https://en.wikipedia.org/wiki/National_Bank_of_Abu_Dhabi',
       'https://en.wikipedia.org/wiki/National_Bank_of_Dubai',
       'https://en.wikipedia.org/wiki/NewBoy',
       'https://en.wikipedia.org/wiki/Noor_Islamic_Bank',
       'https://en.wikipedia.org/wiki/RAKBANK',
       'https://en.wikipedia.org/wiki/Sharjah_Islamic_Bank',
       'https://en.wikipedia.org/wiki/SHUAA_Capital',
       'https://en.wikipedia.org/wiki/Souq.com',
       'https://en.wikipedia.org/wiki/Sorouh_Real_Estate',
       'https://en.wikipedia.org/wiki/Spacetoon',
       'https://en.wikipedia.org/wiki/Tamweel',
       'https://en.wikipedia.org/wiki/The_Emirates_Group',
       'https://en.wikipedia.org/wiki/Thuraya',
       'https://en.wikipedia.org/wiki/Unibeton_Ready_Mix',
       'https://en.wikipedia.org/wiki/Union_National_Bank',
       'https://en.wikipedia.org/wiki/Ureed',
       'https://en.wikipedia.org/wiki/Warid_Telecom']

csv_headers = set()
csv_rows = []

for url in URL:
    csv_row = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    credit_union_name = soup.find('h1', id="firstHeading")
    table = soup.find('table', class_='infobox')
    data_rows = table.find_all('tr')
    for data_row in data_rows:
        label = data_row.find('th')
        value = data_row.find('td')
        if label is None or value is None:
            continue
        beautified_label = label.text.strip()
        beautified_value = value.text.strip()
        csv_row[beautified_label] = beautified_value
        csv_headers.add(beautified_label)
    csv_row["name"] = credit_union_name.text.strip()
    csv_row["url"] = url
    csv_rows.append(csv_row)
    print(csv_rows)

with open(r'uae.csv', 'a+', newline="", encoding="utf-8") as output:
    headers = ["name", "url"]
    headers += sorted(csv_headers)
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(csv_rows)