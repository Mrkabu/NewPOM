slownik = {}
slownik['zaloguj'] = '//*[@id="top"]/div/div/div/div/nav/ul/li[2]/a'
slownik['terazwtv'] = '//*[@id="top"]/div/div/div/div/div/nav/a[1]'

def kliknij(driver, gdzie):
    Element = driver.find_element_by_xpath(slownik[gdzie])
    Element.click()
