from selenium import webdriver


class Crawling():

    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")
        # self.driver = webdriver.Chrome('chromedriver', chrome_options=options)

        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox(executable_path='/home/kahee/geckodriver')

    def login_process(self):
        """
        로그인
        :return:
        """

        self.driver.get('https://library.sejong.ac.kr/identity/Login.ax?url=%2Fstudyroom%2FMain.ax')
        self.driver.implicitly_wait(30)
        self.driver.get_screenshot_as_file('naver_main_headless.png')

        self.driver.find_element_by_name('userID').send_keys('13010063')
        self.driver.find_element_by_name('password').send_keys('940131')
        self.driver.find_element_by_xpath('//a[@href="javascript:identify.goLogin();"]').click()

        # self.driver.get('http://naver.com')
        # self.driver.implicitly_wait(3)
        # self.driver.get_screenshot_as_file('naver_main_headless.png')

    def change_page(self):
        """
        로그인 된 경우 다음 페이지로 이동
        :return:
        """

        self.driver.implicitly_wait(3)
        self.driver.get("http://library.sejong.ac.kr/studyroom/Main.ax")
        self.driver.get_screenshot_as_file('test.png')


test = Crawling()
test.login_process()

