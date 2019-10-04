from selenium import webdriver
import time

class NasiPadang(object):


    def getAllNilai(self, npmMahasiswa, password):

        self.url = 'http://siap.poltekpos.ac.id/siap/besan.depan.php'

        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

        self.driver.find_element_by_name('user_name').send_keys(npmMahasiswa)
        self.driver.find_element_by_name('user_pass').send_keys(password)
        self.driver.find_element_by_name('login').click()

        time.sleep(5)

        self.driver.find_element_by_link_text("Nilai Mahasiswa").click()
        self.driver.find_element_by_xpath("//option[@value='20182']").click()
        self.driver.find_element_by_xpath("//input[@value='Cari' and @name='Cari']").click()

        self.asd = self.driver.find_elements_by_xpath("//table[@class='box' and @align='left']/tbody/tr")
        self.daftar = []
        for i in self.asd:
            string = i.text[2:10].strip()+","+i.text[-12:-11]
            self.daftar.append(string.split(','))

        self.daftar.remove(self.daftar[1])
        self.daftar.remove(self.daftar[0])

        return self.daftar

    def getNilai(self, daftar):
        kode_matkul = ['PPI1102', 'T4I222D4', 'TI43142']

        res = [i for i in daftar if any(j in i for j in kode_matkul)]

        return res

    def getIndeks(self, result):
        getindesk = []
        for indeks in result:
            getindesk.append(indeks[1])
        return getindesk

    def cekNilai(self, nilai):
        switcher= {
            "A": "Lulus",
            "B": "Lulus",
            "C": "Lulus"
        }
        return switcher.get(nilai, "Anda tidak lulus")