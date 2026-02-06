# -*- coding: utf-8 -*-
from datetime import datetime
import streamlit as st

from src.filtros import crear_sidebar_filtros


@st.cache_data(show_spinner=False)
def _convertir_df_a_csv(df):
    return df.to_csv(index=False).encode("utf-8-sig")


def render_sidebar_filters(df_dss):
    return crear_sidebar_filtros(df_dss)


def render_sidebar_export(df_filtrado) -> None:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📥 Exportar Datos Consolidados")

    csv_master = _convertir_df_a_csv(df_filtrado)

    st.sidebar.download_button(
        label="💾 Descargar Tabla Maestra (CSV)",
        data=csv_master,
        file_name=f"techlogistics_consolidado_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
