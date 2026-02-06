# 📊 Actividad_02_Taller_Consultoría
**Integrantes del equipo:** Juan Morales, Sebastian Ruiz, Daniel Pareja

---

## 📋 Contexto y propósito

Este proyecto desarrolla un **Dashboard de Soporte a Decisiones (DSS)** para la empresa ficticia **TechLogistics S.A.S**. Su objetivo es **integrar, limpiar y analizar** tres fuentes de datos operativos y de negocio para identificar riesgos, pérdidas y oportunidades de mejora.

Datasets analizados:
- 📦 **Inventario**: disponibilidad, lead time, costos y rotación.
- ⭐ **Feedback**: satisfacción del cliente, NPS, tickets de soporte.
- 💳 **Transacciones**: ventas, logística, rentabilidad y desempeño operativo.

El resultado es un **EDA interactivo** construido en **Streamlit + Plotly**, con métricas ejecutivas, visualizaciones y reportes para toma de decisiones.

---

## 🧭 Flujo de datos y limpieza

1. **Carga de datasets fuente**
2. **Limpieza y estandarización por módulo**
3. **Consolidación en un dataset maestro (DSS)**
4. **Cálculos analíticos y métricas de negocio**
5. **Visualización y storytelling ejecutivo**

Cada módulo reporta **métricas de salud del dato** antes y después de la limpieza para evidenciar el impacto.

---

## 🧹 Reglas de limpieza por módulo

### 📦 Inventario (9 reglas)
1. Normalización de texto: minúsculas y eliminación de espacios
2. Limpieza de Lead_Time_Dias: eliminar unidades, convertir “inmediato” a 1, extraer máximos en rangos
3. Estandarización de categoría: laptops → laptop, smartphones → smartphone
4. Imputación Lead_Time_Dias con mediana
5. Conversión de fecha Última_Revisión
6. Detección de outliers con IQR
7. Tratamiento de costos atípicos (mediana)
8. Imputación de Stock_Actual con 0
9. Stock_Actual negativos → positivos

### ⭐ Feedback (6 reglas)
1. Eliminación de duplicados exactos
2. Imputación de Edad_Cliente (rango válido 18–90)
3. Normalización de Recomienda_Marca (SI/NO)
4. Normalización de Ticket_Soporte_Abierto (boolean)
5. Conversión de comentarios a string
6. Auditoría inicial de nulos y duplicados

### 💳 Transacciones (14 reglas)
1. Conversión de Fecha_Venta a datetime
2. Normalización de texto en columnas
3. Cantidad_Vendida: negativos → positivos
4. Estado_Envio sin ticket → “entregado”
5. Estado_Envio con ticket → “devuelto”
6. Normalización de ciudades (BOG → Bogotá, MED → Medellín)
7. Costo_Envio en canal físico → 0
8. Feature engineering: margen absoluto y porcentual
9. Merge con Inventario para Bodega_Origen
10. ID grupal bodega–ciudad para imputaciones
11. Imputación Tiempo_Entrega_Real con mediana grupal
12. Imputación Costo_Envio con mediana grupal
13. Eliminación de fila índice 0
14. Imputación Estado_Envio final por lógica de fechas

---

## 🧩 Estructura del proyecto

```
├── app.py                          # Aplicación principal Streamlit
├── requirements.txt                # Dependencias
├── README.md                       # Este documento
├── data/
│   ├── inventario_central_v2.csv
│   ├── feedback_clientes_v2.csv
│   └── transacciones_logistica_v2.csv
├── docs/
│   ├── Decision_Etica_Imputacion.md
│   └── Explicacion_Health_Score.md
├── reports/
└── src/
	├── data_loader.py              # Orquestación de carga + consolidación
	├── inventario.py               # Limpieza y métricas de inventario
	├── feedback.py                 # Limpieza y métricas de feedback
	├── transacciones.py            # Limpieza y métricas de transacciones
	├── reportes.py                 # Generación de reportes PDF
	└── paginas/                    # Pestañas del dashboard
		├── resumen_ejecutivo.py
		├── fuga_capital.py
		├── crisis_logistica.py
		├── venta_invisible.py
		├── diagnostico_fidelidad.py
		├── riesgo_operativo.py
		└── salud_dato.py
```

---

## 📊 Dashboard y storytelling

El tablero está organizado por módulos y escenarios de negocio:

1. **Resumen Ejecutivo**: KPIs clave y salud del dato
2. **Fuga de Capital**: impacto por márgenes negativos
3. **Crisis Logística**: tiempos de entrega, correlación NPS
4. **Venta Invisible**: ingresos sin inventario y riesgo operativo
5. **Diagnóstico de Fidelidad**: paradoja entre stock alto y NPS bajo
6. **Riesgo Operativo**: bodegas “a ciegas” y tickets de soporte
7. **Salud del Dato**: auditoría de calidad por módulo

Las visualizaciones siguen buenas prácticas:
- Escalas consistentes y paletas perceptuales
- Comparaciones claras para variables numéricas
- Segmentación para variables categóricas
- Contexto ejecutivo en cada pestaña

---

## 🚀 Ejecución

Instalación de dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:
```bash
streamlit run app.py
```

La app estará disponible en http://localhost:8501

---

## ✅ Decisiones de diseño

- **Arquitectura modular** por dataset
- **Imputación estratégica** contextualizada
- **Feature engineering** para rentabilidad, riesgos y métricas operativas
- **Auditoría de calidad** con indicadores antes/después

---

## 🔧 Mantenimiento

Para agregar nuevas reglas de limpieza:
1. Implementar en el módulo correspondiente
2. Documentar en la sección de reglas y/o docs
3. Actualizar README
4. Probar visualización en Streamlit