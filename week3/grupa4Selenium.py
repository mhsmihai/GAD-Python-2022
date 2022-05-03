from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
ziua_numarul = [20, 21, 22, 23, 24, 25, 26]
for k in ziua_numarul:
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{k}-ianuarie-ora-13-00/")
    table = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody')
    rows = table.find_elements(by=By.TAG_NAME, value="tr")
    dictionary = {}
    for i, row in enumerate(rows):
        cells = row.find_elements(by=By.TAG_NAME, value="td")
        for j, cell in enumerate(cells):
            if i == 0:
                dictionary[j] = [cell.text]
            else:
                dictionary[j].append(cell.text)
dictionary[4].append('')
print(dictionary)
df = pd.DataFrame(dictionary)
df.to_csv('InformareCovid.xls')
