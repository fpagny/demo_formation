# encoding: UTF-8
from behave import *
from src.allocation import allocate_cost
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True

class Actionwords:
    def __init__(self):
        self.budget = None
        self.hospitalList = None
        self.allocations = None

    def a_total_budget_of_p1(self, p1):
        self.budget = int(p1)

    def an_hospital_list(self):
        self.hospitalList = {'hospital1': 300, 
			     'hospital2': 500,
			     'hospital3': 800}

    def the_cost_allocation_matrix_is_generated(self):
        self.allocations = allocate_cost(self.budget, self.hospitalList)

    def the_output_is_equal_to_the_total_budget(self):
        total = 0
        for hospitalBudget in self.allocations:
            total += hospitalBudget
        assert total == self.budget
        #assert total == (self.budget + 1)

    def all_allocations_must_be_superior_to_p1(self, p1):
        minBudget = int(p1)
        assert all([a >= minBudget for a in self.allocations]) is True

    def a_launched_browser_on_main_atih_page(self):
        self.driver = webdriver.Firefox(options=options)

    def a_p1_and_a_p2(self, p1, p2):
        self.firstName = p1
        self.lastName = p2

    def the_main_page_is_visited_and_searched_for_user_identity(self):
        self.driver.get("https://www.atih.sante.fr/")
        time.sleep(1)
        elem = self.driver.find_element_by_id('edit-terms')
        elem.send_keys(self.firstName + ' ' + self.lastName)
        elem.send_keys(Keys.ENTER)

    def the_searched_text_appears_in_results_header(self):
        block = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.text-title-flat")))
        texts = block.find_elements_by_css_selector("strong")
        text = texts[1].get_attribute("innerHTML")
        assert text == (self.firstName + ' ' + self.lastName)
