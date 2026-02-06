# -*- coding: utf-8 -*-
import sys
from datetime import datetime

import plotly.graph_objects as go
import streamlit as st

from src.paginas.venta_invisible import construir_fig_venta_invisible
from src.paginas.riesgo_operativo import construir_fig_riesgo_operativo
from src.reportes import generar_reporte_ejecutivo_pdf


def _init_report_state() -> None:
    if "pdf_reporte" not in st.session_state:
        st.session_state.pdf_reporte = None

    if "fig_ciudades" not in st.session_state:
        st.session_state.fig_ciudades = None

    if "fig_riesgo" not in st.session_state:
        st.session_state.fig_riesgo = None


def _validar_figura(fig, nombre: str) -> None:
    if fig is None:
        raise ValueError(f"La figura '{nombre}' es None")
    if not isinstance(fig, go.Figure):
        raise TypeError(
            f"La figura '{nombre}' no es un objeto Plotly Figure. "
            f"Tipo recibido: {type(fig)}"
        )


def render_report_section(df_filtrado, health_scores, metricas_calidad) -> None:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📄 Reporte Ejecutivo PDF")

    _init_report_state()

    if st.sidebar.button("🛠️ Preparar Reporte"):
        try:
            with st.spinner("🔄 Generando reporte ejecutivo..."):

                # 1. Construir figuras
                st.session_state.fig_ciudades = construir_fig_venta_invisible(df_filtrado)
                st.session_state.fig_riesgo = construir_fig_riesgo_operativo(df_filtrado)

                # 2. Validación defensiva
                _validar_figura(st.session_state.fig_ciudades, "Venta Invisible")
                _validar_figura(st.session_state.fig_riesgo, "Riesgo Operativo")

                # 3. Generación del PDF
                st.session_state.pdf_reporte = generar_reporte_ejecutivo_pdf(
                    df_filtrado=df_filtrado,
                    health_scores=health_scores,
                    metricas_calidad=metricas_calidad,
                    fig_ciudades=st.session_state.fig_ciudades,
                    fig_riesgo=st.session_state.fig_riesgo
                )

            st.sidebar.success("✅ Reporte listo para descargar")

        except Exception:
            st.sidebar.error("❌ Error al generar el reporte PDF")
            import traceback
            print(traceback.format_exc(), file=sys.stderr)

    if st.session_state.pdf_reporte is not None:
        st.sidebar.download_button(
            label="⬇️ Descargar Reporte PDF",
            data=st.session_state.pdf_reporte,
            file_name=f"Reporte_Ejecutivo_TechLogistics_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )
