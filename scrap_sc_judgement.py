import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome()
url = "https://indiankanoon.org/search/?formInput=doctypes:supremecourt%20fromdate:1-1-2024%20todate:%2031-12-2024"
driver.get(url)

result_title = driver.find_elements(by="xpath", value='//div[@class="result_title"]')

# all_case_link_array
case_links = [result_t.find_element(by="xpath", value="a").get_attribute("href") for result_t in result_title]

for case_link in case_links:
    driver.get(case_link)
    case_data = {}
    
    case_data['court_name'] = driver.find_element(by="xpath", value='//h2[@class="docsource_main"]').text
    case_data['case_title'] = driver.find_element(by="xpath", value='//h2[@class="doc_title"]').text
    case_data['case_meta_box'] = driver.find_element(by="xpath", value='//pre[@id="pre_1"]').text
    case_data['full_judgement'] = driver.find_element(by="xpath", value='//div[@class="judgments"]').text
    
    # Issue filter section
    case_data['issues'] = [issue.text for issue in driver.find_elements(By.CSS_SELECTOR, '[title="Issue"]')]
    
    # Fact filter section
    case_data['facts'] = [fact.text for fact in driver.find_elements(By.CSS_SELECTOR, '[title="Fact"]')]
    
    # Petitioner's Argument filter section
    case_data['petitioners_arguments'] = [pa.text for pa in driver.find_elements(By.CSS_SELECTOR, '[title="Petitioner\'s Argument"]')]
    
    # Court's Reasoning filter section
    case_data['courts_reasoning'] = [cr.text for cr in driver.find_elements(By.CSS_SELECTOR, '[title="Court\'s Reasoning"]')]
    
    # Precedent Analysis filter section
    case_data['precedent_analysis'] = [pa.text for pa in driver.find_elements(By.CSS_SELECTOR, '[title="Precedent Analysis"]')]
    
    # Analysis of the law filter section
    case_data['analysis_of_the_law'] = [al.text for al in driver.find_elements(By.CSS_SELECTOR, '[title="Analysis of the law"]')]
    
    # Respondent's Argument filter section
    case_data['respondents_arguments'] = [ra.text for ra in driver.find_elements(By.CSS_SELECTOR, '[title="Respondent\'s Argument"]')]
    
    # Conclusion filter section
    case_data['conclusion'] = [conclusion.text for conclusion in driver.find_elements(By.CSS_SELECTOR, '[title="Conclusion"]')]
    
    # Negative view of court
    case_data['negative_view'] = [nv.text for nv in driver.find_elements(By.CSS_SELECTOR, '[data-sentiment="Neg"]')]
    
    # Accepted by court
    case_data['accepted_by_court'] = [ac.text for ac in driver.find_elements(By.CSS_SELECTOR, '[data-sentiment="Pos"]')]
    
    # Relied on Party
    case_data['relied_on_party'] = [rp.text for rp in driver.find_elements(By.CSS_SELECTOR, '[data-sentiment="PARTY"]')]
    
    # No clear sentiment
    case_data['no_clear_sentiment'] = [ncs.text for ncs in driver.find_elements(By.CSS_SELECTOR, '[data-sentiment="Neutral"]')]
    
    # Generate a filename-safe version of the case title
    safe_case_title = re.sub(r'[^\w\s-]', '', case_data['case_title']).strip().replace(' ', '_')
    
    # Save the data to a JSON file
    with open(f'/home/rifa/Desktop/SCC/{safe_case_title}.json', 'w', encoding='utf-8') as json_file:
        json.dump(case_data, json_file, ensure_ascii=False, indent=4)
    
    driver.back()

driver.quit()
