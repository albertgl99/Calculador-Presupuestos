🖩 Dynamic Budget Calculator
Una calculadora interactiva que muestra precios en tiempo real para servidores personalizados basados en variables como CPU, RAM y SSD. Incluye animaciones y la posibilidad de descargar el presupuesto en PDF.

🚀 Características
Ajustes dinámicos de configuración de servidor (CPU, RAM, SSD).
Actualización de precios en tiempo real.
Animaciones fluidas para una mejor experiencia.
Generación de presupuestos en PDF.
Backend con Django para cálculos y generación de PDFs.
🛠️ Tecnologías
Frontend: HTML, CSS, JavaScript, GSAP (animaciones).
Backend: Django, Python.
Generación de PDFs: ReportLab o WeasyPrint.
API: Para cálculos dinámicos basados en las configuraciones seleccionadas.
📦 Instalación
Clona este repositorio:
bash
Copiar código
git clone https://github.com/tuusuario/dynamic-budget-calculator.git
cd dynamic-budget-calculator
Configura un entorno virtual:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
Inicia el servidor:
bash
Copiar código
python manage.py runserver
💻 Uso
Abre el navegador en http://localhost:8000.
Ajusta las configuraciones del servidor y observa el precio en tiempo real.
Descarga el presupuesto en formato PDF.
📝 Contribuciones
¡Contribuciones son bienvenidas! Por favor, crea un pull request o abre un issue.

📄 Licencia
Este proyecto está bajo la licencia MIT.
