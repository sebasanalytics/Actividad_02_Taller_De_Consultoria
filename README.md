# 📊 Actividad_02_Taller_Consultoría
**Integrantes del equipo:** Juan Morales, Sebastian Ruiz, Daniel Pareja

---

## 📋 Descripción General

Este proyecto implementa un **EDA (Exploratory Data Analysis) interactivo** usando Streamlit y Plotly para analizar tres datasets relacionados:
- 📦 **Inventario**: Gestión de stock y productos
- ⭐ **Feedback**: Comentarios y satisfacción de clientes
- 💳 **Transacciones**: Ventas y logística

## 🗂️ Estructura del Proyecto

```
├── app.py                          # Aplicación principal Streamlit
├── data_cleaning_rules.py          # Documentación de reglas de limpieza
├── inventario.py                   # Procesamiento de inventario
├── feedback.py                     # Procesamiento de feedback
├── transacciones.py                # Procesamiento de transacciones
├── requirements.txt                # Dependencias Python
├── README.md                       # Este archivo
├── inventario_central_v2.csv       # Dataset: Inventario
├── feedback_clientes_v2.csv        # Dataset: Feedback
└── transacciones_logistica_v2.csv  # Dataset: Transacciones
```

## 🧹 Reglas de Limpieza Documentadas

El proyecto incluye documentación detallada de **todas** las transformaciones aplicadas:

### 📦 Inventario (9 reglas)
1. **Normalización de texto**: Minúsculas y eliminación de espacios
2. **Limpieza Lead_Time_Dias**: Eliminación de unidades, conversión de "inmediato" a 1, extracción de máximos en rangos
3. **Estandarización Categoria**: Mapeo de variaciones (laptops→laptop, smartphones→smartphone)
4. **Imputación Lead_Time_Dias**: Llenar nulos con mediana (5)
5. **Conversión de fecha**: Última_Revisión a datetime
6. **Detección de outliers**: Método IQR en variables numéricas
7. **Tratamiento Costo_Unitario_USD**: Reemplazo de valores extremos con mediana de smartphones
8. **Imputación Stock_Actual**: Llenar nulos con 0
9. **Conversión Stock_Actual**: Negativos a positivos

### ⭐ Feedback (6 reglas)
1. **Eliminación de duplicados**: Filas exactamente iguales
2. **Imputación Edad_Cliente**: Rango válido 18-90 años con mediana
3. **Normalización Recomienda_Marca**: Mapeo a SI/NO, llenar nulos con moda
4. **Normalización Ticket_Soporte_Abierto**: Conversión a booleano (True/False)
5. **Conversión de comentarios**: Asegurar tipo string
6. **Auditoría inicial**: Documentación de duplicados y nulos

### 💳 Transacciones (14 reglas)
1. **Conversión de Fecha_Venta**: String a datetime
2. **Normalización de texto**: Todas las columnas a minúsculas
3. **Conversión Cantidad_Vendida**: Negativos a positivos (abs)
4. **Imputación Estado_Envio (sin ticket)**: "entregado" si sin problemas de soporte
5. **Imputación Estado_Envio (con ticket)**: "devuelto" si con ticket abierto
6. **Normalización ciudades**: bog→bogotá, med→medellín
7. **Imputación Costo_Envio (físico)**: 0 para canal físico
8. **Feature Engineering - Margen**: Cálculo de márgenes absoluto y porcentual
9. **Merge con Inventario**: Traer Bodega_Origen
10. **Creación ID grupal**: bodega-ciudad para imputaciones
11. **Imputación Tiempo_Entrega_Real**: Mediana por grupo bodega-ciudad
12. **Imputación Costo_Envio**: Mediana por grupo bodega-ciudad
13. **Eliminación fila**: Remover índice 0
14. **Imputación Estado_Envio final**: Lógica basada en fechas (entregado vs en camino)

## 🚀 Cómo Ejecutar

### Instalación de dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación estará disponible en `http://localhost:8501`

## 📊 Características de la Aplicación

### 1. 📊 Exploración de Datos
- Vista previa de los primeros 5 registros
- Información general del dataset (filas, columnas, tamaño)
- Distribución de tipos de datos
- Visualización interactiva de valores nulos
- Análisis de variables numéricas (histogramas, box plots, estadísticas)
- Análisis de variables categóricas (top 15 categorías)

### 2. 🧹 Reglas de Limpieza
- Documentación interactiva de todas las transformaciones
- Código ejecutado para cada regla
- Variables afectadas
- Impacto de cada operación
- Búsqueda por dataset

### 3. 📈 Análisis Específico
- **Transacciones**: Series temporal de ventas, análisis por canal y estado
- **Inventario**: Distribución de categorías, bodegas, análisis de stock
- **Feedback**: Distribución de edades, recomendaciones, tickets de soporte

## 📁 Módulos Principales

### `app.py`
Aplicación Streamlit con tres vistas:
- Panel de exploración de datos
- Documentación de reglas de limpieza
- Análisis específico por dataset
- Funciones modulares para cada análisis

### `data_cleaning_rules.py`
Documentación estructurada de todas las reglas de limpieza en formato diccionario, facilitando su visualización en el dashboard.

### `inventario.py`
Funciones de procesamiento:
- `iqr_outliers()`: Detección de outliers método IQR
- `select_max_lead_time()`: Extracción de máximos de rangos
- `procesar_inventario()`: Pipeline completo de limpieza

### `feedback.py`
Función de procesamiento:
- `clean_feedback_dataset()`: Pipeline completo con normalización y imputación

### `transacciones.py`
Función de procesamiento:
- `procesar_transacciones()`: Pipeline con 14 pasos de transformación y enriquecimiento

## 💡 Decisiones de Diseño

### Arquitectura Modular
- Cada dataset tiene su propio módulo de procesamiento
- Funciones reutilizables para análisis específicos
- Documentación centralizada en `data_cleaning_rules.py`

### Imputación Estratégica
- **Inventario**: Mediana global para Lead_Time, mediana por categoría para costos
- **Feedback**: Mediana para edad, moda para variables binarias
- **Transacciones**: Mediana grupal (bodega-ciudad) para tiempos y costos

### Feature Engineering
- Creación de márgenes en transacciones
- Identificador grupal para imputaciones contextualizadas
- Cálculo de fechas de entrega esperadas

## 📊 Visualizaciones Interactivas

Todas las gráficas utilizan **Plotly** para:
- Zoom y paneo
- Hover con información detallada
- Descarga de imágenes
- Interactividad completa

Tipos de gráficas:
- **Histogramas**: Distribuciones con media/mediana
- **Box plots**: Detección de outliers
- **Barras**: Conteos y agregaciones
- **Líneas**: Series temporales
- **Donas**: Proporciones

## 📝 Notas Importantes

- Todos los comentarios describen **exactamente qué hace cada línea** de código
- Sin código omitido (`...existing code...`)
- Documentación de formato de datos esperado para cada operación
- Impactos claramente descritos para cada transformación

## 🔧 Mantenimiento

Para agregar nuevas reglas de limpieza:
1. Implementar en el módulo correspondiente
2. Documentar en `data_cleaning_rules.py`
3. Actualizar este README
4. Probar visualización en Streamlit