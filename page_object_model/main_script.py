from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(15)


def decline_gdpr():
    driver.find_element(By.XPATH, "//div/div[2]/div/div[2]/button[2]").click()  # decline rodo


def choosing_car_market():
    driver.find_element(By.XPATH, "//div[contains(text(), 'Motoryzacja')]").click()  # choosing car market


def choosing_adverts_box_board():
    driver.find_element(By.XPATH, "//div[@class='mh85_0 mr3m_1']//a/div[1]").click()  # choosing adverts box board


def select_car_brand_list():
    driver.find_element(By.XPATH, "//form/div[1]/div/div/select").click()


def choosing_car_from_list(car_name):
    Select(driver.find_element(By.XPATH, "//form/div[1]/div/div/select")).select_by_visible_text(car_name)


def select_car_model_from_list():
    driver.find_element(By.XPATH, "//form/div[2]/div/div/select").click()


def choosing_model_from_list(car_model):
    Select(driver.find_element(By.XPATH, "//form/div[2]/div/div/select")).select_by_visible_text(car_model)


def production_start_date(year1):
    driver.find_element(By.XPATH, "//div[3]/div/div/div/div/div[1]/div/input").send_keys(year1)


def production_end_date(year2):
    driver.find_element(By.XPATH, "//div/div/div[2]/div/input").send_keys(year2)


def min_price(minprice):
    driver.find_element(By.XPATH, "//div[4]/div/div/div/div/div[1]/div/input").send_keys(minprice)


def max_price(maxprice):
    driver.find_element(By.XPATH, "//div[4]/div/div/div/div/div[2]/div/input").send_keys(maxprice)


def petrol_type_choosing_list():
    driver.find_element(By.XPATH, "//form/div[5]/div/div/select").click()


def petrol_type(petroltype):
    Select(driver.find_element(By.XPATH, "//form/div[5]/div/div/select")).select_by_visible_text(petroltype)


def search_results():
    driver.find_element(By.XPATH, "//div/form/div[6]/div/input").click()


def choosing_version():
    driver.find_element(By.XPATH, "//div[2]/ul/li[3]/div/a").click()


driver.maximize_window()
driver.get("https://www.allegro.pl")  # open car website

decline_gdpr()
choosing_car_market()
choosing_adverts_box_board()
select_car_brand_list()
choosing_car_from_list("Renault")
select_car_model_from_list()
choosing_model_from_list("Clio")
production_start_date(2005)
production_end_date(2015)
min_price(200)
max_price(26000)
petrol_type_choosing_list()
petrol_type("Benzyna")
search_results()
choosing_version()

list1 = driver.find_elements(By.XPATH, "//article//div/a")
list_url = [link.get_attribute("href") for link in list1]

i = 1
f = open("new_car_test.txt", 'w')
for url in list_url:
    driver.get(url)
    f.write("Auction nr " + str(i) + "\n")
    f.write(url + "\n")
    auction_name = driver.find_element(By.XPATH, "//div[1]/div/div/div/div/div/div[1]/div/div[1]/h4")
    f.write(auction_name.get_attribute('textContent') + "\n")
    price_tag = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/span")
    f.write("Price for this car is: " + price_tag.text + "00 PLN." + "\n")
    number_show = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div[5]/div[2]/button")
    number_show.click()
    number_copy = driver.find_element(By.XPATH, "//div/div[2]/div/div/div/div/div/div/div/div[2]/div[5]/div[2]/div/div/a")
    f.write(number_copy.get_attribute('textContent') + "\n")
    ssname = ("Auction name " + str(i))
    driver.get_screenshot_as_file(f'/Users/bartoszwrobel/PycharmProjects/cars_auto_finder/scrensh/{str(ssname)}.png')
    f.write("\n\n")
    i = i + 1
    driver.switch_to.new_window()
f.close()
