import streamlit as st

st.set_page_config(page_title="Resume with Vanta", layout="wide")

# Inject Vanta.js DOTS background
st.markdown("""
<div id="vanta-bg"></div>

<style>
    #vanta-bg {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: -1;
    }
    .stApp {
        background: transparent !important;
    }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta/dist/vanta.dots.min.js"></script>
<script>
    VANTA.DOTS({
      el: "#vanta-bg",
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      scale: 1.00,
      scaleMobile: 1.00,
      color: 0x2c3e50,
      color2: 0x1abc9c,
      backgroundColor: 0xf5f5f5,
      size: 3.00,
      spacing: 40.00
    })
</script>
""", unsafe_allow_html=True)

# Example content on top of Vanta
st.title("John Doe")
st.subheader("Senior Data Scientist")
st.write("📍 San Francisco, CA")
