




from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.wd.implicitly_wait(5)

    def add_one_digit(self, number):
        wd = self.wd
        path = "//ul[@class='digits']//li[.='{}']".format(number.digit)
        wd.find_element_by_xpath(path).click()

    def display_text(self):
        wd = self.wd
        text = wd.find_element_by_css_selector("div.display").text
        return text

    def open_home_page(self):
        wd = self.wd
        wd.get("http://qa-test.klika-tech.com/")

    def destroy(self):
        self.wd.quit()