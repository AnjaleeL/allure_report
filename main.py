# selenium 4
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_binary='binaries/Google Chrome for Testing116.app/Contents/MacOS/Google Chrome for Testing'
options=webdriver.ChromeOptions()
options.binary_location=chrome_binary
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)



def verify_title():
    driver.get("https://sdetunicorns.com")

    title = driver.title

    expected_title = "Master Software Testing and Automation Online | SDET Unicorns"
    if title == expected_title:
        print("Title verification successful !")
    else:
        print(f"Title verification failed. Expected '{expected_title}',but got '{title}',")

    driver.quit()

if __name__ == '__main__':
    verify_title()
