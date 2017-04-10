from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ansicolor.ansicolor import red

class RDSParser:

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1280, 1024)
        self.driver.get('http://www.rcs-rds.ro/acoperire-servicii')
        self.incarcare_elemente()
        self.aflam_judete()
        self.selectam_meniu_cu_meniu()
        self.bye_bye()


    def incarcare_elemente(self):
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, 'judet')))
        except TimeoutException, e:
            print e

    def aflam_judete(self):
        meniu_judete = self.driver.find_element_by_id('judet')
        lista_judete = meniu_judete.find_elements_by_tag_name('option')
        self.lista_listelor_de_judete = []
        for element in lista_judete:
            if element.get_attribute('value') == '#':
                pass
            else:
                #print element.get_attribute('value')
                self.lista_listelor_de_judete.append(element.get_attribute('value'))
        print len(self.lista_listelor_de_judete)

    def selectam_meniu_cu_meniu(self):
        select_judet = Select(self.driver.find_element_by_id('judet'))
        meniu_localitati = self.driver.find_element_by_id('localitate')
        for element in self.lista_listelor_de_judete:
            select_judet.select_by_value(element)
            #self.driver.save_screenshot('judete/%s.png' % element)
            lista_localitati = meniu_localitati.find_elements_by_tag_name('option')
            for element_i in lista_localitati:
                print str(element_i.get_attribute('value')).encode('utf-8')
                try:
                    print str(element.get_attribute('value')).encode('utf-8')
                except AttributeError, e:
                    print e

    def bye_bye(self):
        self.driver.save_screenshot('rds_rcs.png')
        self.driver.quit()

if __name__ == '__main__':
    a = RDSParser()
