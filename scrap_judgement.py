import time
import json
from selenium import webdriver
url = "https://indiankanoon.org/"
sub_url = f"{url}/search/?formInput=scc%20online%20%20%20%20%20doctypes%3A%20judgments&pagenum=1"
driver = webdriver.Chrome()
driver.get(sub_url)

jdm_title = driver.find_elements(by='xpath', value='//div[@class="result_title"]')
jdm_source = driver.find_elements(by='xpath', value='//span[@class="docsource"]')

res_list = []
for title, source in zip(jdm_title, jdm_source):
    jdm_json_f = {
        "title": title.text,
        "docsource": source.text
    }
    res_list.append(jdm_json_f)

json_format = json.dumps(res_list, indent=3)
print(json_format)