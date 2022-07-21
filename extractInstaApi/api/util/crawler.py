#! python
# encoding UTF-8
import os
import time
import traceback
import logging
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .detect_arch import detect_machine as dm


class InstaCrawler:
    """
    Instagram Crawler
    링크를 전달받으면 해당 링크에 포스팅된 이미지를 추출하는 기능으로 구성된 클래스
    """
    #path_drv = '/usr/bin/safaridriver'
    # Safari Automation으로 인스타 접근할 경우 white blank만 출력되는 모습을 보인다.
    # Chrome webdriver를 이용, Incognito mode를 사용하여 접근하도록 한다.
    # util로 m1과 intel을 구분하는 기능을 추가해야겠다.
    # 와 주석도 인공지능으로 자동으로 작성해줘? 미쳤네..
    # 더 좋은 경로 정리 코드가 있으면 좋을듯..
    def __init__(self, url):
        '''
        True: x86
        False: ETC
        '''
        if dm:
            self.path_drv = './api/util/chromedriver'
        else:
            self.path_drv = './api/util/chromedriver_m1'

        # 상속할 경우 중복을 줄이기 위한 방법
        # 단 여기서는 상속하지 않기 때문에 의미없음
        #super().__init__(url)
        self.url = url
        self.instagram_link = 'https://www.instagram.com'
        print(os.getcwd())

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers = self.headers

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        self.drv = webdriver.Chrome(executable_path=self.path_drv, options=chrome_options)
        print(f'webdriver path {self.path_drv}')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info(f'crawler init (URL: {url})')
        print(f'crawler init {url}')

    def extract_image(self):
        try:
            self.drv.get(self.url)
            time.sleep(5)
            #image_list = self.drv.find_elements(By.CLASS_NAME, 'eLAPa RzuR0')
            image_list = self.drv.find_elements(By.CLASS_NAME, '_aamh')
            print(len(image_list))

        except Exception:
            traceback.print_exception()

        finally:
            self.drv.quit()
            logging.info(f'Webdriver quit')

        return 0

    def login(self):
        try:
            self.drv.get(self.instagram_link)
            time.sleep(1)
            print(f'test {self.url}')

            user_name = self.drv.find_elements(By.NAME, 'username')
            user_name[0].send_keys('eyedi318@hanyang.ac.kr')
            pw = self.drv.find_elements(By.NAME, 'password')
            pw[0].send_keys('ideyedi318!')

            btn_login = self.drv.find_elements(By.CLASS_NAME, 'sqdOP')
            # .. css 객체가 3개가 잡히네??
            print(f'Login btn [{len(btn_login)}]: {btn_login}')
            btn_login[1].click()

            time.sleep(5)

            btn_save_info = self.drv.find_elements(By.CLASS_NAME, 'sqdOP')
            print(f'Save_info btn [{len(btn_save_info)}]: {btn_save_info}')
            btn_save_info[1].click()

            # session 유지때문에 하나의 엔드포인트에서 처리해야할까..
            self.drv.get(self.url)

            src_sets = self.drv.find_elements(By.CSS_SELECTOR, 'srcset')
            print(src_sets)
            print(src_sets[0].text)
            # Test
            time.sleep(20)

        except Exception:
            traceback.print_exc()

        finally:
            #self.drv.quit()
            print(f'Session 유지?, api 형태라.. http 연결 끊기면 연결 세션도 유지 안될꺼 같은데')

        return 0

    # Github codepliot automation
    def get_html(self):
        response = self.session.get(self.url)
        return response.text

    def get_json(self):
        response = self.session.get(self.url)
        return response.json()

    def get_text(self):
        response = self.session.get(self.url)
        return response.text

    def get_status_code(self):
        response = self.session.get(self.url)
        return response.status_code

    def get_headers(self):
        response = self.session.get(self.url)
        return response.headers

    def get_cookies(self):
        response = self.session.get(self.url)
        return response.cookies

    def get_history(self):
        response = self.session.get(self.url)
        return response.history

    def get_encoding(self):
        response = self.session.get(self.url)
        return response.encoding

    def get_content(self):
        response = self.session.get(self.url)
        return response.content

    def get_raw_headers(self):
        response = self.session.get(self.url)
        return response.raw.headers

    def get_raw_content(self):
        response = self.session.get(self.url)
        return response.raw.read()

    def get_raw_text(self):
        response = self.session.get(self.url)
        return response.raw.read().decode('utf-8')


if __name__ == '__main__':
    unittest = InstaCrawler('https://www.instagram.com')
    unittest.login()

