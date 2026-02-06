# -*- coding: utf-8 -*-
from datetime import datetime
import streamlit as st


def render_header(df_filtrado, health_scores) -> None:
    st.title("📊 TechLogistics S.A.S")
    st.markdown("### Sistema de Soporte a Decisiones (DSS) – Auditoría de Consultoría")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Transacciones Analizadas", f"{len(df_filtrado):,}")
    with col_b:
        st.metric("Columnas del Modelo", f"{df_filtrado.shape[1]:,}")
    with col_c:
        fecha_act = datetime.now().strftime("%d/%m/%Y %H:%M")
        st.metric("Última Actualización", fecha_act)

    with st.expander("🧭 Flujo de datos y limpieza aplicada", expanded=False):
        st.markdown(
            """
            **Pipeline del DSS**
            1. **Carga de datasets fuente** (Inventario, Feedback, Transacciones)
            2. **Limpieza específica por módulo** (normalización, imputación, outliers)
            3. **Consolidación** en el dataset maestro
            4. **Análisis de negocio** (márgenes, riesgo, fidelidad)
            """
        )

        st.markdown("**Salud del dato por módulo**")
        hs_tabla = [
            {"Módulo": k, "Antes": v.get("Antes", 0), "Después": v.get("Despues", 0)}
            for k, v in health_scores.items()
        ]
        st.dataframe(
            hs_tabla,
            use_container_width=True
        )
