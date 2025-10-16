# 🍔 food_api

API REST para la gestión de un restaurante, creada con **Django + Django REST Framework (DRF)**.  
Permite administrar **Platos** y **Pedidos** mediante endpoints, sin usar Django Admin.

---

## ⚙️ Requisitos
- Python 3.10+
- virtualenv

---

## 🚀 Instalación y ejecución
```bash
# 1️⃣ Crear y activar entorno virtual
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux / Mac
source venv/bin/activate

# 2️⃣ Instalar dependencias
pip install django djangorestframework django-filter

# 3️⃣ Aplicar migraciones
python manage.py migrate

# 4️⃣ Ejecutar servidor
python manage.py runserver
📚 Endpoints principales
🍽️ Platos
Método	Endpoint	Descripción
GET	/api/platos/	Listar todos los platos (con búsqueda y ordenamiento)
POST	/api/platos/	Crear un nuevo plato
GET	/api/platos/{id}/	Ver detalles de un plato
PUT/PATCH	/api/platos/{id}/	Actualizar plato
DELETE	/api/platos/{id}/	Eliminar plato

🧾 Pedidos
Método	Endpoint	Descripción
GET	/api/pedidos/	Listar todos los pedidos
POST	/api/pedidos/	Crear pedido ({"platos": [1,2]})
GET	/api/pedidos/{id}/	Ver detalle del pedido (muestra platos anidados)
PUT/PATCH	/api/pedidos/{id}/	Actualizar pedido (estado o platos)
DELETE	/api/pedidos/{id}/	Eliminar pedido
