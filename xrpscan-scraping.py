from selenium.webdriver import Chrome

import time
import json

browser= Chrome()
browser.get("https://xrpscan.com/account/ryBANkk28Mj71jRKAkt13U1X9ubztsGWZ")
time.sleep(1)


xrpscan_table_index = ["3", "4", "6", "7"]
xrpdata_dict = {'tx_hash':[], 'from':[], "to":[], "amount":[]}
for i in range(50):
    for index in xrpscan_table_index:
        tbody = browser.find_elements_by_xpath("//*[@id=\"account-transactions-tabpane-transactions\"]/div/div[1]/table/tbody/tr/td["+index+"]")
        for td in tbody:
            if index == '3': xrpdata_dict.setdefault("tx_hash").append(td.text)
            if index == '4': xrpdata_dict.setdefault("from").append(td.text.split()[0])
            if index == '6': xrpdata_dict.setdefault("to").append(td.text.split()[0])
            if index == '7': xrpdata_dict.setdefault("amount").append(td.text)

    table_pagination = browser.find_element_by_xpath("//*[@id=\"account-transactions-tabpane-transactions\"]/div/div[2]/ul/li[2]/a")
    table_pagination.click()
    time.sleep(1)
        
with open("xrpdata.json", "w") as f:
    json.dump(xrpdata_dict, f)

browser.close()

