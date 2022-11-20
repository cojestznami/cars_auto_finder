from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import Navigation_Main
from page_object_model.main_script import driver


class SearchCarNew:
    def __init__(self):
        self.driver = driver
        yield
        driver.quit()

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def first_search(self):
        self.driver.get("https://www.allegro.pl")
        searching_car = Navigation_Main(self.driver)
        searching_car.decline_gdpr()
        searching_car.car_adverts_path()
        searching_car.car_brand_and_model_define("Renault", "Clio")
        searching_car.set_up_age(2005, 2015)
        searching_car.set_up_price(100, 28000)
        searching_car.choose_petrol("Benzyna")
        searching_car.perform_search()
        searching_car.choose_lift_version()


e = 1

list1 = driver.find_elements(By.XPATH, "//article//div/a")
list_url = [link.get_attribute("href") for link in list1]
i = 1
f = open("new_car_test.txt", 'w')
for url in list_url:
    driver.get(url)
    f.write("Auction nr " + str(e) + "\n")
    f.write(url + "\n")
    auction_name = driver.find_element(By.XPATH, "//div[1]/div/div/div/div/div/div[1]/div/div[1]/h4")
    f.write(auction_name.get_attribute('textContent') + "\n")
    price_tag = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/span")
    f.write("Price for this car is: " + price_tag.text + "00 PLN." + "\n")
    number_show = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div[5]/div[2]/button")
    number_show.click()
    number_copy = driver.find_element(By.XPATH, "//div/div[2]/div/div/div/div/div/div/div/div[2]/div[5]/div[2]/div/div/a")
    f.write(number_copy.get_attribute('textContent') + "\n")
    ssname = ("Auction name " + str(e))
    driver.get_screenshot_as_file(f'/Users/bartoszwrobel/PycharmProjects/cars_auto_finder/scrensh/{str(ssname)}.png')
    f.write("\n\n")
    e = e + 1
    driver.switch_to.new_window()
f.close()
