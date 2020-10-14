# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:14:20 2020

@author: alejandro.gutierrez
"""
# PAGINA PRINCIPAL
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MainPage():
    def __init__(self,my_driver):
        self.driver = my_driver
        self.on_demand = (By.ID, 'ctl00_ctl00_ctl00_ctl00_cphContent_cphContent_cphContent_cphLeftColumn_rpReportsList_ctl00_rpReportsForGroup_ctl00_lnkReport')    
        self.select_vendor = 'ctl00_ctl00_ctl00_ctl00_cphContent_cphHeader_cbxImpersonateAs'
        
        
    def on_demand_click(self):
        try:
            ondemand = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(self.on_demand))
            ondemand.click()
        except TimeoutException:
            print ("Loading -on_demand_click- MAIN PAGE took too much time!")
            
        
    def select_vendor_click(self):
        try:
            select_vdr = Select(self.driver.find_element_by_id(self.select_vendor))
            select_vdr.select_by_visible_text("BROWN & HALEY, INC") #select_by_index(1)
        except TimeoutException:
            print ("Loading -select_vendor_click- BROWN & HALEY, INC of MAIN PAGE took too much time! (only for Candy)")
        
