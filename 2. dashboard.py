import streamlit as st
import numpy as np
import plotly.graph_objects as go
from config import RIEMANN_ZEROS
from core.hamiltonian import build_hamiltonian
from core.fourier_analyzer import riemann_fourier_analysis

st.set_page_config(page_title="Riemann Lab", layout="wide")
st.title("🧪 Riemann Nuclear Resonance Laboratory")

epsilon = st.sidebar.slider("ε", 0.0, 1.0, 0.45, 0.001)
beta2 = st.sidebar.slider("β₂", 0.0, 0.6, 0.30, 0.005)
n_max = st.sidebar.selectbox("N_max", [12, 14, 16, 18], index=2)

if st.button("Запустити розрахунок"):
    with st.spinner("Обчислення..."):
        H = build_hamiltonian(n_max, epsilon, beta2)
        eigenvalues = np.sort(np.real(np.linalg.eigvalsh(H)))
        fourier = riemann_fourier_analysis(eigenvalues, RIEMANN_ZEROS, epsilon)
        
        st.success(f"Максимальна значущість: **{fourier['max_sigma']:.2f}σ**")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fourier['frequencies'], y=fourier['power'], mode='lines'))
        for p in fourier['peaks']:
            fig.add_vline(x=p['t'], line_dash="dash", line_color="red")
        st.plotly_chart(fig, use_container_width=True)
