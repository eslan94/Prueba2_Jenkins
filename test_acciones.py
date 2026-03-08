import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestPrueba2:

    def setup_method(self):
        servicio = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=servicio)
        self.driver.maximize_window()
        self.driver.get("https://webdriveruniversity.com/Actions/index.html")

   

    def realizar_arrastrar_y_soltar(self, id_origen, id_destino):
        origen = self.driver.find_element(By.ID, id_origen)
        destino = self.driver.find_element(By.ID, id_destino)
        acciones = ActionChains(self.driver)
        acciones.drag_and_drop(origen, destino).perform()

    def test_interacciones_avanzadas_mouse(self):
        acciones = ActionChains(self.driver)

        # 1. Arrastrar y Soltar
        self.realizar_arrastrar_y_soltar("draggable", "droppable")
        
        texto_destino = self.driver.find_element(By.ID, "droppable").text
        assert "Dropped!" in texto_destino

        # 2. Doble Click
        zona_doble_click = self.driver.find_element(By.ID, "double-click")
        acciones.double_click(zona_doble_click).perform()
        assert "double" in zona_doble_click.get_attribute("class")

        # 3. Click y Mantener
        caja_click = self.driver.find_element(By.ID, "click-box")
        acciones.click_and_hold(caja_click).perform()
        assert "Well done" in caja_click.text
        
        print("\n✅ Todas las acciones de la Prueba 2 fueron validadas exitosamente.")