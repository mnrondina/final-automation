from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Config. Driver

def driver_config():
    chrome_opciones = Options()
    chrome_opciones.add_argument("--disable-dev-shm-usage")
    chrome_service = Service()
    driver = webdriver.Chrome(options=chrome_opciones, service=chrome_service)
    driver.maximize_window()
    return driver

# Inicializando el Driver

def test_login():
    driver = driver_config()

    try:
        driver.get("https://www.saucedemo.com") 
        username_input = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
        print("Login exitoso!")

        driver.find_element(By.XPATH, "//button[contains (@data-test, 'add-to-cart')]").click()
        badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        assert badge.text == "1", f"El contador del carrito debe mostrar 1, pero muestra {badge.text}"
        print("Producto añadido correctamente")

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        carrito_item = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
        print("Producto visible en el carrito")

        # Cerrar Sesión

        driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
        print("Cierre de sesión exitoso")
        print("Todas las pruebas pasaron con éxito!")
        return True
    
    except Exception as e:
        print(f"Error durante la prueba {e}")
        return False

    finally:
        print("Cerrando navegador...")
        time.sleep(3)
        driver.quit()
        
# Autoimplementación
if __name__ == "__main__":
    test_login()