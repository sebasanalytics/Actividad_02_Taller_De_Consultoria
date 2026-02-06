# -*- coding: utf-8 -*-
import streamlit as st

from src.paginas.resumen_ejecutivo import mostrar_resumen_ejecutivo
from src.paginas.fuga_capital import mostrar_fuga_capital
from src.paginas.crisis_logistica import mostrar_crisis_logistica
from src.paginas.venta_invisible import mostrar_venta_invisible
from src.paginas.diagnostico_fidelidad import mostrar_diagnostico_fidelidad
from src.paginas.riesgo_operativo import mostrar_riesgo_operativo
from src.paginas.salud_dato import mostrar_salud_datos


def render_tabs(df_filtrado, health_scores, metricas_calidad) -> None:
    tabs = st.tabs([
        "📈 Resumen Ejecutivo",
        "💰 Fuga de Capital",
        "🚚 Crisis Logística",
        "👻 Venta Invisible",
        "⭐ Diagnóstico Fidelidad",
        "⚠️ Riesgo Operativo",
        "📊 Salud de los Datos"
    ])

    with tabs[0]:
        mostrar_resumen_ejecutivo(df_filtrado, health_scores, metricas_calidad)

    with tabs[1]:
        mostrar_fuga_capital(df_filtrado)

    with tabs[2]:
        mostrar_crisis_logistica(df_filtrado)

    with tabs[3]:
        mostrar_venta_invisible(df_filtrado, renderizar=True)

    with tabs[4]:
        mostrar_diagnostico_fidelidad(df_filtrado)

    with tabs[5]:
        mostrar_riesgo_operativo(df_filtrado, renderizar=True)

    with tabs[6]:
        mostrar_salud_datos(df_filtrado, metricas_calidad)
