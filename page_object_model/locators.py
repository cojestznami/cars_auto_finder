from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def loop_links():
    list1 = driver.find_elements(By.XPATH, "//article//div/a")
    list_url = [link.get_attribute("href") for link in list1]
    for url in list_url:
        driver.get(url)
        f.write("Auction nr " + str(i) + "\n")
        f.write(url + "\n")
        auction_name = driver.find_element(By.XPATH, "//div[1]/div/div/div/div/div/div[1]/div/div[1]/h4")
        f.write(auction_name.get_attribute('textContent') + "\n")
        price_tag = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/span")
        f.write("Price for this car is: " + price_tag.text + "00 PLN." + "\n")
        number_show = driver.find_element(By.XPATH,
                                          "//div[2]/div/div/div/div/div/div/div/div[2]/div[5]/div[2]/button")
        number_show.click()
        number_copy = driver.find_element(By.XPATH,
                                          "//div/div[2]/div/div/div/div/div/div/div/div[2]/div[5]/div[2]/div/div/a")
        f.write(number_copy.get_attribute('textContent') + "\n")
        ssname = ("Auction name " + str(i))
        driver.get_screenshot_as_file(
            f'/Users/bartoszwrobel/PycharmProjects/cars_auto_finder/scrensh/{str(ssname)}.png')
        f.write("\n\n")
        i = i + 1
        driver.switch_to.new_window()


class Navigation_Main:
    def __init__(self, driver):
        self.driver = driver
        self.gdpr_decline_xpath = "//div/div[2]/div/div[2]/button[2]"
        self.click_car_market_xpath = "//div[contains(text(), 'Motoryzacja')]"
        self.click_adverts_box_xpath = "//div[@class='mh85_0 mr3m_1']//a/div[1]"
        self.click_car_brands_list_xpath = "//form/div[1]/div/div/select"
        self.choose_car_from_list_xpath = "//form/div[1]/div/div/select"
        self.click_car_model_list_xpath = "//form/div[2]/div/div/select"
        self.choose_model_from_list_xpath = "//form/div[2]/div/div/select"
        self.production_date_start_xpath = "//div[3]/div/div/div/div/div[1]/div/input"
        self.production_date_end_xpath = "//div/div/div[2]/div/input"
        self.min_price_xpath = "//div[4]/div/div/div/div/div[1]/div/input"
        self.max_price_xpath = "//div[4]/div/div/div/div/div[2]/div/input"
        self.click_petrol_type_choosing_list_xpath = "//form/div[5]/div/div/select"
        self.petrol_type_xpath = "//form/div[5]/div/div/select"
        self.click_search_button_xpath = "//div/form/div[6]/div/input"
        self.choose_car_lift_version_xpath = "//div[2]/ul/li[3]/div/a"


    def decline_gdpr(self):
        self.driver.find_element(By.XPATH, self.gdpr_decline_xpath).click()

    def car_adverts_path(self):
        self.driver.find_element(By.XPATH, self.click_car_market_xpath).click()
        self.driver.find_element(By.XPATH, self.click_adverts_box_xpath).click()

    def car_brand_and_model_define(self, car_name, car_model):
        self.driver.find_element(By.XPATH, self.click_car_brands_list_xpath).click()
        self.Select(driver.find_element(By.XPATH, self.choose_car_from_list_xpath)).select_by_visible_text(car_name)
        self.driver.find_element(By.XPATH, self.click_car_model_list_xpath).click()
        self.Select(driver.find_element(By.XPATH, self.choose_model_from_list_xpath)).select_by_visible_text(car_model)

    def set_up_age(self, min_year, max_year):
        self.driver.find_element(By.XPATH, self.production_date_start_xpath).send_keys(min_year)
        self.driver.find_element(By.XPATH, self.production_date_end_xpath).send_keys(max_year)

    def set_up_price(self, min_price, max_price):
        self.driver.find_element(By.XPATH, self.min_price_xpath).send_keys(min_price)
        self.driver.find_element(By.XPATH, self.max_price_xpath).send_keys(max_price)

    def choose_petrol(self, petrol_type):
        self.driver.find_element(By.XPATH, self.click_petrol_type_choosing_list_xpath).click()
        self.Select(driver.find_element(By.XPATH, self.petrol_type_xpath)).select_by_visible_text(petrol_type)

    def perform_search(self):
        self.driver.find_element(By.XPATH, self.click_search_button_xpath).click()

    def choose_lift_version(self):
        self.driver.find_element(By.XPATH, self.choose_car_lift_version_xpath).click()
