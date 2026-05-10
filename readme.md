# SauceDemo Automation Project 🧪

Este proyecto consiste en un script de **QA Automation** utilizando **Python** y **Selenium WebDriver**. Realiza una prueba de flujo completo (End-to-End) sobre la web de prácticas [SauceDemo](https://www.saucedemo.com/).

## 📋 Funcionalidades del Test

El script automatiza el siguiente flujo:
1.  **Login**: Ingreso con credenciales de usuario estándar.
2.  **Validación**: Verificación de ingreso exitoso al inventario.
3.  **Carrito**: Selección de un producto y verificación de que el contador del carrito aumente a "1".
4.  **Navegación**: Entrada a la sección del carrito para confirmar la visibilidad del producto.
5.  **Logout**: Cierre de sesión seguro desde el menú lateral.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Framework de Automatización:** Selenium WebDriver
*   **Patrón de Esperas:** WebDriverWait (Explicit Waits) para robustez.
*   **Driver:** ChromeDriver (gestionado a través de Service).
