import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para simular el ciclo económico basado en la teoría austriaca
def simulate_austrian_business_cycle(amplitude, frequency, phase, time):
    return amplitude * np.sin(frequency * time + phase)

# Configuración de la aplicación Streamlit
st.set_page_config(layout="wide")
st.title("Simulador del Ciclo Económico Austriaco")

# Configuración de las columnas en Streamlit
col1, col2 = st.columns([2, 1])

# Parámetros del ciclo económico
with col1:
    
    st.markdown("""
    
        *Parámetros del Ciclo Económico Austriaco*
        
        **Amplitud:** Representa las fluctuaciones máximas en el nivel económico durante el ciclo. Un valor alto indica oscilaciones más pronunciadas, mientras que un valor bajo indica oscilaciones más suaves.

        **Frecuencia:** Determina la duración promedio de una fase completa del ciclo económico. Una frecuencia alta implica fases más cortas y frecuentes, mientras que una frecuencia baja indica fases más largas y menos frecuentes.

        **Fase:** Controla el desplazamiento horizontal del ciclo económico. Modificar este valor cambia el punto de partida del ciclo económico en el tiempo.

        La teoría austriaca sostiene que los ciclos económicos son el resultado de desequilibrios en la economía causados por intervenciones externas, como políticas monetarias expansivas o inversiones mal dirigidas. Estos desequilibrios generan excesos de inversión y gastos en un primer momento, creando una expansión económica artificial. Sin embargo, esta expansión no es sostenible y eventualmente lleva a una fase de corrección y recesión, en la cual se ajustan los errores y se restablece el equilibrio económico.
    """)

# Controles deslizantes en la columna derecha
with col2:
    st.sidebar.header("Ajuste de Parámetros")
    amplitude = st.sidebar.slider("Amplitud", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    frequency = st.sidebar.slider("Frecuencia", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    phase = st.sidebar.slider("Fase", min_value=0.0, max_value=2 * np.pi, value=0.0, step=0.1)

# Generación de los datos simulados para el ciclo económico
time = np.linspace(0, 10, 500)
economic_cycle = simulate_austrian_business_cycle(amplitude, frequency, phase, time)

# Gráfico del ciclo económico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time, economic_cycle, linewidth=2, color='blue')
ax.set_xlabel("Tiempo", fontsize=12)
ax.set_ylabel("Nivel Económico", fontsize=12)
ax.set_title("Ciclo Económico Austriaco", fontsize=16)
ax.grid(True)

# Mostrar el gráfico utilizando Streamlit
st.pyplot(fig)

# Mostrar el mensaje de autoría
st.sidebar.markdown("Hecho por Moris Polanco, con ayuda de GPT-4")
