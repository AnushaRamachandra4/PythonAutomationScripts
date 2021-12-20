import time
from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browsername = "firefox"

if browsername == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Pass the correct browsername :' +browsername)
    raise Exception('Browser is not found')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
time.sleep(3)
nametext = driver.find_element_by_xpath("//h1[normalize-space()='About you']")
driver.execute_script("arguments[0].scrollIntoView();",nametext)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='name']").send_keys('Anusha Ramachandra')
time.sleep(3)
driver.find_element_by_xpath("//a[@class='button button-block action']//div[@class='label']").click()
driver.implicitly_wait(3)
element = driver.find_element_by_xpath("//div[@class='section sign above-overlay']")
time.sleep(3)
#driver.get_screenshot_as_file("G:\\screenshot\\file.png")
location = element.location_once_scrolled_into_view
size = element.size
png = driver.get_screenshot_as_png()
im = Image.open(BytesIO(png))
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['width']
print(left, top, right,bottom)
im = im.crop((left, top, right, bottom))
im.save("G:\\screenshot\\DocumentSigned.png")  # saves new cropped image
driver.find_element_by_xpath("//a[@class='button button-block sign-button action']//div[@class='label']").click()
time.sleep(3)
element = driver.find_element_by_xpath("//span[normalize-space()='Document signed!']").text
print(element)
assert element == "Document signed!"
time.sleep(3)
driver.quit()


