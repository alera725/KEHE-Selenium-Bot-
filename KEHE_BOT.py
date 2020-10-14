# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:34:14 2020

@author: alejandro.gutierrez
"""

#Importar paqueterias
import os
import shutil

#Set directory
os.chdir('C:\\Users\\PATH WHEN YOU HAVE THE FILES .PY') 

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import time 
import datetime
from KEHE_PAGINA_INICIO import InitialPage
from KEHE_PAGINA_PRINCIPAL import MainPage
from KEHE_PAGINA_PROCESO import ProcessPage
from KEHE_PAGINA_EXPORTACION import ExportPage
import pandas as pd

class DownloadSVData(unittest.TestCase):
    
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : 'C:\\Users\\SET UP PATH FOR DOWNLOADS'} 
        chrome_options.add_experimental_option('prefs', prefs)
        #chrome_options.add_argument('--headless')
        chromedriver_path = 'C:\\Users\\SET UP PATH WHERE IS chromedriver'
        url = 'https://idsrv.kroger.m6demandview.com/account/mk6signin' #GENERAL URL FOR ALL THE REPORTS
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
        self.driver.get(url)
        self.WebDriverWait = WebDriverWait
        self.PageInitial = InitialPage(self.driver)
        self.PageMain = MainPage(self.driver)
        self.PageProcess = ProcessPage(self.driver)
        self.PageExport = ExportPage(self.driver)
        self.dir_download = 'C:\\Users\\SET UP PATH FOR DOWNLOADS AGAIN'

    #@unittest.skip('Not need now')
    def test_rana_Kroger(self):
        # Obtener la descargas antes de los test
        before = os.listdir(self.dir_download) 
         
        email = 'XXXX@gmail.com' 
        pswd = 'XXXX'  
        self.PageInitial.login(email,pswd)
        self.PageMain.on_demand_click()
        self.PageProcess.saved_reports_Rana()
        self.PageProcess.saved_reports_2()
        self.PageExport.set_dates()
        self.PageExport.run_report()
        self.PageExport.export()
        self.PageExport.set_export_data()
        self.PageExport.export_final()
        time.sleep(5)
        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue

        
        # !!! IMPORTANTE !!! Aqui Checar el ultimo archivo cargado de ese retailer y vemos los renglones que tiene damos un rango de +- 100 o 50 ROWS 
        # THIS PART CAN BE DELETED IF WE DONT NEED TO COMPARE VS PREVIOUS DOWNLOADED FILE 
        previous_file_path = 'C:\\Users\\SET UP PATH WHERE ARE ALL THE FILES DOWNLOADED FOR RANA'
        previous_file = max([previous_file_path + "\\" + f for f in os.listdir(previous_file_path)],key=os.path.getctime) # Ultimo archivo cargado en la ruta del retailer 
        previous_file_n = pd.read_csv(previous_file, skiprows=14)
        n_rows_prev = len(previous_file_n.index) # Count rows 
        
        
        #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
        Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
        Initial_path = self.dir_download 
        filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
        
        current_file = pd.read_csv(filename, skiprows=14) #DROP ROWS THAT AREN'T PART OF THE DATA
        n_rows_current = len(current_file.index) #Count rows 
        
        #Aqui despues se hace si el nuevo archivo pasa el limite se guarda con otro nombre advirtiendo que puede tener error el archivo 
        #Sino se guarda el archivo con el proceso normal
        limite = n_rows_prev/3
        
        if(n_rows_current>n_rows_prev+limite or n_rows_current<n_rows_prev-limite):              
            new_name = 'ERROR PLEASE CHECK IF THIS FILE IS OK RANA Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        else:
            new_name = 'RANA Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        
        #MOVER EL ARCHIVO A LA UBICACION DESEADA
        new_download = 'C:\\Users\\SET UP PATH WHERE THE FILE DOWNLOADED ARE SAVED'
        shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
       
        #ESTO NO SE BORRARA
        #Listo
        print("RANA is READY!!") 
        time.sleep(3)
        
        
    #@unittest.skip('Not need now')
    def test_chelsea_Kroger(self):
        # Obtener la descargas antes de los test
        before = os.listdir(self.dir_download) 
                        
        email = 'XXXX@gmail.com'  
        pswd = 'XXXX'  
        self.PageInitial.login(email,pswd)
        self.PageMain.on_demand_click()
        self.PageProcess.saved_reports_Chelsea()
        self.PageProcess.saved_reports_2()
        self.PageExport.set_dates()
        self.PageExport.run_report()
        self.PageExport.export()
        self.PageExport.set_export_data()
        self.PageExport.export_final()
        time.sleep(5)
        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
            
        # !!! IMPORTANTE !!! Aqui Checar el ultimo archivo cargado de ese retailer y vemos los renglones que tiene damos un rango de +- 100 o 50 FALTAAAAAA RUTA DEL RETAILER EN EL QUE ESTAMOS Y REVISAR ULTIMO ARCHIVO Y CONTAR LOS ROWS
        previous_file_path = 'C:\\Users\\SET UP PATH WHERE ARE ALL THE FILES DOWNLOADED FOR CHELSEA'
        previous_file = max([previous_file_path + "\\" + f for f in os.listdir(previous_file_path)],key=os.path.getctime) #Ultimo archivo cargado en la ruta del retailer 
        previous_file_n = pd.read_csv(previous_file, skiprows=19)
        n_rows_prev = len(previous_file_n.index) #Count rows         
        
        #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
        Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
        Initial_path = self.dir_download 
        filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime) #Te da todo el path
        
        current_file = pd.read_csv(filename, skiprows=19)
        n_rows_current = len(current_file.index) #Count rows 
        
        #Aqui despues se hace si el nuevo archivo pasa el limite se guarda con otro nombre advirtiendo que puede tener error el archivo 
        #Sino se guarda el archivo todo normal
        limite = n_rows_prev/3
        
        if(n_rows_current > n_rows_prev + limite or n_rows_current < n_rows_prev - limite):              
            new_name = 'ERROR PLEASE CHECK IF THIS FILE IS OK CHELSEA Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        else:
            new_name = 'CHELSEA Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        
        #MOVER EL ARCHIVO A LA UBICACION DESEADA
        new_download = 'C:\\Users\\SET UP PATH WHERE THE FILE DOWNLOADED ARE SAVED'
        shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)   
        
        print("CHELSEA is READY!!") 
        time.sleep(3)

    #@unittest.skip('Not need now')   
    def test_kind_Kroger(self):
        # Obtener la descargas antes de los test
        before = os.listdir(self.dir_download) 
                 
        email = 'XXXX@gmail.com'  
        pswd = 'XXXX'  
        self.PageInitial.login(email,pswd)
        self.PageMain.on_demand_click()
        self.PageProcess.saved_reports_Kind()
        self.PageProcess.saved_reports_2()
        self.PageExport.set_dates()
        self.PageExport.run_report()
        self.PageExport.export()
        self.PageExport.set_export_data()
        self.PageExport.export_final()
        time.sleep(5)
        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
            
        # !!! IMPORTANTE !!! Aqui Checar el ultimo archivo cargado de ese retailer y vemos los renglones que tiene damos un rango de +- 100 o 50 FALTAAAAAA RUTA DEL RETAILER EN EL QUE ESTAMOS Y REVISAR ULTIMO ARCHIVO Y CONTAR LOS ROWS
        previous_file_path = 'C:\\Users\\SET UP PATH WHERE ARE ALL THE FILES DOWNLOADED FOR KIND'
        previous_file = max([previous_file_path + "\\" + f for f in os.listdir(previous_file_path)],key=os.path.getctime) #Ultimo archivo cargado en la ruta del retailer 
        previous_file_n = pd.read_csv(previous_file, skiprows=26)
        n_rows_prev = len(previous_file_n.index) #Count rows         
        
        #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
        Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
        Initial_path = self.dir_download 
        filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
        
        current_file = pd.read_csv(filename, skiprows=26)
        n_rows_current = len(current_file.index) #Count rows 
        
        #Aqui despues se hace si el nuevo archivo pasa el limite se guarda con otro nombre advirtiendo que puede tener error el archivo 
        #Sino se guarda el archivo todo normal
        limite = n_rows_prev/3
        
        if(n_rows_current>n_rows_prev+limite or n_rows_current<n_rows_prev-limite):              
            new_name = 'ERROR PLEASE CHECK IF THIS FILE IS OK KIND Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        else:
            new_name = 'KIND Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        
        #MOVER EL ARCHIVO A LA UBICACION DESEADA
        new_download = 'C:\\Users\\SET UP PATH WHERE THE FILE DOWNLOADED ARE SAVED'
        shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)     
        
        print("KIND is READY!!") 
        time.sleep(3)

        
    #@unittest.skip('Not need now')   
    def test_candy_Kroger(self):
        # Obtener la descargas antes de los test
        before = os.listdir(self.dir_download) 
                 
        email = 'XXXX@carlin-group.com'  
        pswd = 'XXXX'  
        self.PageInitial.login(email,pswd)
        self.PageMain.select_vendor_click()
        self.PageMain.on_demand_click()
        self.PageProcess.saved_reports_Candy()
        self.PageProcess.saved_reports_2()
        self.PageExport.set_dates()
        self.PageExport.run_report()
        self.PageExport.export()
        self.PageExport.set_export_data()
        self.PageExport.export_final()
        time.sleep(5)
        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
            
        # !!! IMPORTANTE !!! Aqui Checar el ultimo archivo cargado de ese retailer y vemos los renglones que tiene damos un rango de +- 100 o 50 FALTAAAAAA RUTA DEL RETAILER EN EL QUE ESTAMOS Y REVISAR ULTIMO ARCHIVO Y CONTAR LOS ROWS
        previous_file_path = 'C:\\Users\\SET UP PATH WHERE ARE ALL THE FILES DOWNLOADED FOR CANDY'
        previous_file = max([previous_file_path + "\\" + f for f in os.listdir(previous_file_path)],key=os.path.getctime) #Ultimo archivo cargado en la ruta del retailer 
        previous_file_n = pd.read_csv(previous_file, skiprows=17)
        n_rows_prev = len(previous_file_n.index) #Count rows         
        
        #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
        Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
        Initial_path = self.dir_download 
        filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
        
        current_file = pd.read_csv(filename, skiprows=17)
        n_rows_current = len(current_file.index) #Count rows 
        
        #Aqui despues se hace si el nuevo archivo pasa el limite se guarda con otro nombre advirtiendo que puede tener error el archivo 
        #Sino se guarda el archivo todo normal
        limite = n_rows_prev/3
        
        if(n_rows_current>n_rows_prev+limite or n_rows_current<n_rows_prev-limite):              
            new_name = 'ERROR PLEASE CHECK IF THIS FILE IS OK CANDY Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        else:
            new_name = 'CANDY Kroger ' + str(Current_Date) + '.csv'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        
        #MOVER EL ARCHIVO A LA UBICACION DESEADA
        new_download = 'C:\\Users\\SET UP PATH WHERE THE FILE DOWNLOADED ARE SAVED'
        shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)  
        
        print("CANDY is READY!!") 
        time.sleep(3)

        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()
       
    
    