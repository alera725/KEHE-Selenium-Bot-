# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:15:30 2020

@author: alejandro.gutierrez
"""

# PAGINA EXPORTACION
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ExportPage():
    def __init__(self,my_driver):
        self.driver = my_driver
        self.dates_filter_button = (By.ID, 'datesTab')#'datesTab'
        self.first_date_filter = 'currentStartDate'
        self.end_date_filter = 'currentEndDate'
        self.run_report_button = (By.ID, 'runTab')#'runTab'
        self.export_button = (By.ID, 'reportExport')
        self.data_only_button = (By.XPATH, '//*[@id="exporttypeset"]/label[2]/span/span')
        self.export_button_2 = (By.XPATH, '//*[@id="btnExportToCSV_CD"]/span')
        
    def set_dates(self):
        try:
            dates_set = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.dates_filter_button)) 
            dates_set.click()
            select_first = Select(self.driver.find_element_by_id(self.first_date_filter))
            select_first.select_by_index(1)
            select_end = Select(self.driver.find_element_by_id(self.end_date_filter))
            select_end.select_by_index(1) 
        except TimeoutException:
            print ("Loading -set_dates- took too much time!")

    def run_report(self):
        try:
            r_r_button =  WebDriverWait(self.driver,25).until(EC.element_to_be_clickable(self.run_report_button)) 
            r_r_button.click()
        except TimeoutException:
            print ("Loading -run_report- took too much time!")

    def export(self):
        try:
            exp = WebDriverWait(self.driver,200).until(EC.element_to_be_clickable(self.export_button)) 
            exp.click()
        except TimeoutException:
            print ("Loading -export- took too much time!")
            
    def set_export_data(self):
        try:
             dobutton = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.data_only_button)) 
             dobutton.click()
        except TimeoutException:
            print ("Loading -set_export_data- took too much time!")
            
    def export_final(self):
        try:
            eb2 = WebDriverWait(self.driver,100).until(EC.element_to_be_clickable(self.export_button_2)) 
            eb2.click()
        except TimeoutException:
            print ("Loading -export_final- took too much time!")




        
        
        
        
        
        
        
