from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time
MAX_WAIT = 5


class LayoutAndStylingTest(FunctionalTest):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.broswtest_multiple_users_can_start_lists_at_different_urlser.quit()

    def test_layout_and_styling(self):
        # Edith entra na home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Ela nota que o input box está centralizado
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # Ela inicia uma nova lista e nota que o input
        # também está centralizado
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )   