# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:14:46 2020

@author: alejandro.gutierrez
"""

# PAGINA INICIO

class InitialPage():
    def __init__(self,my_driver):
        self.driver = my_driver
        self.button = '//*[@id="content"]/div/div/div[2]/form/p[4]/input'
        self.loginn_1 ='UserName'
        self.pswd = 'Password'
        
    def login(self,email,psd):
        self.driver.find_element_by_id(self.loginn_1).send_keys(email)
        self.driver.find_element_by_id(self.pswd).send_keys(psd)
        self.driver.find_element_by_xpath(self.button).click()

