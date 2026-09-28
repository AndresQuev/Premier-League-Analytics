import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------------------
# 1. Configuración de página
# -------------------------------------------------------------
st.set_page_config(
    page_title="Premier League Analytics Hub",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------
# 2. Textos Bilingües (ES / EN)
# -------------------------------------------------------------
TEXTS = {
    "ES": {
        "sidebar_ctrl": "⚙️ Control Panel",
        "sidebar_desc": "Filtros de temporada y clubes analizados.",
        "season": "Temporada",
        "all_seasons": "Todas las temporadas",
        "club": "Club",
        "all_clubs": "Todos los clubes",
        "title": "PREMIER LEAGUE ANALYTICS HUB",
        "subtitle": "Análisis avanzado de rendimiento financiero: <span style='color: #00FF85; font-weight: 600;'>Gasto en Fichajes vs. Retorno de Puntos</span> (2012–2025).",
        "kpi_spend": "Inversión Total",
        "kpi_spend_sub": "Gasto acumulado del filtro",
        "kpi_pts": "Puntos Promedio",
        "kpi_pts_sub": "Rendimiento liguero medio",
        "kpi_cost": "Costo por Punto",
        "kpi_cost_sub": "Inversión por cada punto obtenido",
        "kpi_eff": "Eficiencia Neta",
        "kpi_eff_sub": "Desempeño vs. Mercado",
        "scatter_title": "Gasto en Fichajes vs. Puntos Obtenidos",
        "scatter_x": "Inversión en Fichajes (€ Millones)",
        "scatter_y": "Puntos Obtenidos",
        "scatter_vline": "Gasto Promedio (€83.9M)",
        "scatter_hline": "Media Puntos (53.1)",
        "bar_title": "Ranking de Eficiencia Neta por Club",
        "bar_x": "Puntos por encima (+) o debajo (-) del mercado",
        "table_title": "Registro Estadístico y Financiero",
        "col_season": "Temporada",
        "col_club": "Club",
        "col_pos": "Pos.",
        "col_pts": "Pts",
        "col_pj": "PJ",
        "col_gf": "GF",
        "col_gc": "GC",
        "col_dg": "DG",
        "col_spend": "Inversión (€M)",
        "col_eff": "Eficiencia Neta"
    },
    "EN": {
        "sidebar_ctrl": "⚙️ Control Panel",
        "sidebar_desc": "Season and analyzed clubs filters.",
        "season": "Season",
        "all_seasons": "All seasons",
        "club": "Club",
        "all_clubs": "All clubs",
        "title": "PREMIER LEAGUE ANALYTICS HUB",
        "subtitle": "Advanced financial performance analysis: <span style='color: #00FF85; font-weight: 600;'>Transfer Spend vs. Points Return</span> (2012–2025).",
        "kpi_spend": "Total Investment",
        "kpi_spend_sub": "Cumulative spending for filter",
        "kpi_pts": "Average Points",
        "kpi_pts_sub": "Mean league performance",
        "kpi_cost": "Cost per Point",
        "kpi_cost_sub": "Spend per league point earned",
        "kpi_eff": "Net Efficiency",
        "kpi_eff_sub": "Performance vs. Market",
        "scatter_title": "Transfer Spend vs. Points Earned",
        "scatter_x": "Transfer Investment (€ Millions)",
        "scatter_y": "Points Earned",
        "scatter_vline": "Avg Spend (€83.9M)",
        "scatter_hline": "Avg Points (53.1)",
        "bar_title": "Net Efficiency Ranking by Club",
        "bar_x": "Points above (+) or below (-) market average",
        "table_title": "Statistical and Financial Records",
        "col_season": "Season",
        "col_club": "Club",
        "col_pos": "Pos",
        "col_pts": "Pts",
        "col_pj": "MP",
        "col_gf": "GF",
        "col_gc": "GA",
        "col_dg": "GD",
        "col_spend": "Investment (€M)",
        "col_eff": "Net Efficiency"
    }
}

# -------------------------------------------------------------
# 3. Estilos Dark Premier League
# -------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

    .stApp {
        background-color: #0F0A1A;
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stSidebar"] {
        background-color: #17102A;
        border-right: 1px solid #2B1E4A;
    }

    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    .pl-card {
        background: linear-gradient(135deg, #1E153A 0%, #16102B 100%);
        border: 1px solid #33235E;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    .pl-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: #00FF85;
    }
    .pl-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #94A3B8;
        margin-bottom: 6px;
    }
    .pl-value {
        font-size: 32px;
        font-weight: 800;
        font-family: 'Outfit', sans-serif;
        color: #FFFFFF;
        line-height: 1.1;
    }
    .pl-sub {
        font-size: 12px;
        color: #64748B;
        margin-top: 6px;
    }

    .pl-divider {
        height: 1px;
        background: linear-gradient(90deg, rgba(0,255,133,0.5) 0%, rgba(55,0,60,0.5) 100%);
        margin: 24px 0 28px 0;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 4. Datos
# -------------------------------------------------------------
@st.cache_data
def get_data():
    return pd.read_csv("powerbi_tabla_principal.csv")

df = get_data()

# -------------------------------------------------------------
# 5. Barra Lateral: Botón de Idioma y Filtros
# -------------------------------------------------------------
lang_choice = st.sidebar.radio(
    "Idioma / Language",
    options=["ES 🇪🇸", "EN 🇬🇧"],
    horizontal=True,
    label_visibility="collapsed"
)
lang = "ES" if "ES" in lang_choice else "EN"
t = TEXTS[lang]

st.sidebar.markdown(f"<h3 style='margin-top: 15px; margin-bottom: 2px; color: #00FF85 !important;'>{t['sidebar_ctrl']}</h3>", unsafe_allow_html=True)
st.sidebar.caption(t["sidebar_desc"])

temporadas = [t["all_seasons"]] + sorted(df["season_label"].unique().tolist())
filtro_temporada = st.sidebar.selectbox(t["season"], temporadas)

clubes = [t["all_clubs"]] + sorted(df["club_name"].unique().tolist())
filtro_club = st.sidebar.selectbox(t["club"], clubes)

df_view = df.copy()
if filtro_temporada != t["all_seasons"]:
    df_view = df_view[df_view["season_label"] == filtro_temporada]
if filtro_club != t["all_clubs"]:
    df_view = df_view[df_view["club_name"] == filtro_club]

# -------------------------------------------------------------
# 6. Encabezado
# -------------------------------------------------------------
st.markdown(f"<h1 style='font-size: 38px; margin-bottom: 4px;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 16px; color: #94A3B8;'>{t['subtitle']}</p>", unsafe_allow_html=True)
st.markdown("<div class='pl-divider'></div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 7. KPIs
# -------------------------------------------------------------
gasto_total = df_view["gasto_millones"].sum()
puntos_totales = df_view["puntos"].sum()
puntos_promedio = df_view["puntos"].mean()
costo_por_punto = (gasto_total / puntos_totales) if puntos_totales > 0 else 0
eficiencia_prom = df_view["residuo_eficiencia"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="pl-card">
        <div class="pl-label">{t['kpi_spend']}</div>
        <div class="pl-value">€{gasto_total:,.1f} M</div>
        <div class="pl-sub">{t['kpi_spend_sub']}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="pl-card" style="border-left-color: #37003C;">
        <div class="pl-label">{t['kpi_pts']}</div>
        <div class="pl-value">{puntos_promedio:.1f} pts</div>
        <div class="pl-sub">{t['kpi_pts_sub']}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="pl-card" style="border-left-color: #FF2882;">
        <div class="pl-label">{t['kpi_cost']}</div>
        <div class="pl-value">€{costo_por_punto:.2f} M</div>
        <div class="pl-sub">{t['kpi_cost_sub']}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    color_ret = "#00FF85" if eficiencia_prom >= 0 else "#FF2882"
    signo = "+" if eficiencia_prom > 0 else ""
    st.markdown(f"""
    <div class="pl-card" style="border-left-color: {color_ret};">
        <div class="pl-label">{t['kpi_eff']}</div>
        <div class="pl-value" style="color: {color_ret};">{signo}{eficiencia_prom:.1f} pts</div>
        <div class="pl-sub">{t['kpi_eff_sub']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 8. Gráficos Originales Intactos
# -------------------------------------------------------------
col_chart_left, col_chart_right = st.columns([1.25, 1])

with col_chart_left:
    st.markdown(f"### {t['scatter_title']}")
    
    fig_scatter = px.scatter(
        df_view,
        x="gasto_millones",
        y="puntos",
        color="club_name",
        hover_data={
            "club_name": True,
            "season_label": True,
            "posicion_final": True,
            "diferencia_goles": True,
            "gasto_millones": ":.1f",
            "puntos": True
        },
        labels={
            "gasto_millones": t["scatter_x"],
            "puntos": t["scatter_y"],
            "club_name": "Club"
        }
    )
    
    fig_scatter.add_vline(
        x=83.9, line_dash="dash", line_color="#475569", line_width=1.5,
        annotation_text=t["scatter_vline"], annotation_position="top left",
        annotation_font_color="#94A3B8", annotation_font_size=11
    )
    fig_scatter.add_hline(
        y=53.1, line_dash="dash", line_color="#475569", line_width=1.5,
        annotation_text=t["scatter_hline"], annotation_position="bottom right",
        annotation_font_color="#94A3B8", annotation_font_size=11
    )

    fig_scatter.update_layout(
        plot_bgcolor="#16102B",
        paper_bgcolor="#16102B",
        font=dict(family="Inter, sans-serif", color="#F8FAFC"),
        height=480,
        showlegend=False,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(gridcolor="#2B1E4A", zeroline=False),
        yaxis=dict(gridcolor="#2B1E4A", zeroline=False)
    )
    fig_scatter.update_traces(marker=dict(size=9, opacity=0.9, line=dict(width=1, color="#FFFFFF")))
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_chart_right:
    st.markdown(f"### {t['bar_title']}")
    
    df_rank = df_view.groupby("club_name")["residuo_eficiencia"].mean().reset_index()
    df_rank = df_rank.sort_values(by="residuo_eficiencia", ascending=True)
    
    df_rank["Color"] = df_rank["residuo_eficiencia"].apply(lambda x: "#00FF85" if x >= 0 else "#FF2882")

    fig_bar = go.Figure(go.Bar(
        x=df_rank["residuo_eficiencia"],
        y=df_rank["club_name"],
        orientation="h",
        marker=dict(color=df_rank["Color"], line=dict(width=0)),
        hovertemplate="<b>%{y}</b><br>Eficiencia neta: %{x:+.1f} pts<extra></extra>"
    ))
    
    fig_bar.update_layout(
        plot_bgcolor="#16102B",
        paper_bgcolor="#16102B",
        font=dict(family="Inter, sans-serif", color="#F8FAFC"),
        height=480,
        xaxis_title=t["bar_x"],
        yaxis_title="",
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(gridcolor="#2B1E4A", zeroline=True, zerolinecolor="#64748B")
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------------------------------------------
# 9. Tabla
# -------------------------------------------------------------
st.markdown("<div class='pl-divider'></div>", unsafe_allow_html=True)
st.markdown(f"### {t['table_title']}")

tabla_mostrar = df_view[[
    "season_label", "club_name", "posicion_final", "puntos", 
    "partidos_jugados", "goles_favor", "goles_contra", "diferencia_goles", 
    "gasto_millones", "residuo_eficiencia"
]].rename(columns={
    "season_label": t["col_season"],
    "club_name": t["col_club"],
    "posicion_final": t["col_pos"],
    "puntos": t["col_pts"],
    "partidos_jugados": t["col_pj"],
    "goles_favor": t["col_gf"],
    "goles_contra": t["col_gc"],
    "diferencia_goles": t["col_dg"],
    "gasto_millones": t["col_spend"],
    "residuo_eficiencia": t["col_eff"]
}).sort_values(by=[t["col_season"], t["col_pos"]])

st.dataframe(
    tabla_mostrar,
    use_container_width=True,
    hide_index=True
)