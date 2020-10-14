# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:15:23 2020

@author: alejandro.gutierrez
"""

#PAGINA PROCESO
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class ProcessPage():
    def __init__(self,my_driver):
        self.driver = my_driver
        self.saved_reports = (By.XPATH,'//*[@id="accordionPersonalSavedReportAnchor"]')
        self.reported_saved_rana = (By.XPATH, '//*[@id="106819"]/span/a')  #RANA 
        self.reported_saved_chelsea = (By.XPATH,'//*[@id="102249"]/span/a') #CHELSEA
        self.reported_saved_kind = (By.XPATH,'//*[@id="102250"]/span/a') #KIND
        self.reported_saved_candy = (By.XPATH,'//*[@id="85363"]/span/a') #CANDY
        self.load_button = (By.XPATH,'//*[@id="accordionPersonalSavedReportScollDown"]/div/div/div/button[1]')
        

    def saved_reports_Rana(self):
        try:
            sreports = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.saved_reports))
            sreports.click()
            rsaved =  WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.reported_saved_rana))
            rsaved.click()
        except TimeoutException:
            print ("Loading -saved_reports_Rana- took too much time!")

    def saved_reports_Chelsea(self):
        try:
            sreports = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.saved_reports))
            sreports.click()
            rsaved =  WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.reported_saved_chelsea))
            rsaved.click()
        except TimeoutException:
            print ("Loading -saved_reports_Chelsea- took too much time!")
            
    def saved_reports_Kind(self):
        try:
            sreports = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.saved_reports))
            sreports.click()
            rsaved =  WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.reported_saved_kind))
            rsaved.click()
        except TimeoutException:
            print ("Loading -saved_reports_Kind- took too much time!")
            
    def saved_reports_Candy(self):
        try:
            sreports = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.saved_reports))
            sreports.click()
            rsaved =  WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.reported_saved_candy))
            rsaved.click()
        except TimeoutException:
            print ("Loading -saved_reports_Candy- took too much time!")

    def saved_reports_2(self):
        try:
            lbutton = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.load_button))
            lbutton.click()
        except TimeoutException:
            print ("Loading -saved_reports_2- took too much time!")
        
        
        
        
        
        
        
