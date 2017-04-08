from selenium import webdriver

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('http://meblilem.com.ua')
products = browser.find_elements_by_xpath('//div[@class="item"]/a[2]')
print('Found', len(products), 'items on page')
for product in products:
    print(product.text)
browser.quit()
