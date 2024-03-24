from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def seleniumScraper(linkToScrape):
    """method to scrape a link using selenium"""
    
    #opens the link in chrome
    driver = webdriver.Chrome()
    driver.get(linkToScrape)
    #takes all of the text from the webpage
    all_text = driver.find_element(By.TAG_NAME, "body").get_attribute("innerText")
    driver.quit
    #return all of the text
    return all_text


#SIC codes------------------------------------------------------    
def sicSearchCompaniesHouse(company_name,SIC):
    """method to scrape companies house based on sic code"""
    #opens the link in chrome
    driver = webdriver.Chrome()
    #loading companies house web page
    driver.get("https://find-and-update.company-information.service.gov.uk/advanced-search")
    #accepting cookies
    driver.find_element(By.ID,"accept-cookies-button").click()
    #expanding company status button
    driver.find_element(By.ID,"accordion-default-heading-4").click()
    #selecting active companies
    driver.find_element(By.ID,"activeCompanies").click()
    #expanding nature of business section
    driver.find_element(By.ID,"accordion-default-heading-5").click()
    #fidning the search bar
    search_bar = driver.find_element(By.ID, "sicCodes")
    #search for sic code
    search_bar.send_keys(SIC)
    # Submit the search 
    driver.find_element(By.ID,"advanced-search-button").click()  # Submit the form containing the search bar
    wait = WebDriverWait(driver, 10)  # Set reasonable wait time
    for x in range(1):
      search_result = driver.find_element(By.CLASS_NAME,"govuk-table__row").get_attribute("innerText")
    driver.quit
    return search_result
