import streamlit as st
from retangulo import Retangulo

class Retangulo_UI:
    def main():
        st.header("Calculos com Rêtangulo")
        base  = st.text_input("Base")
        altura = st.text_input("Altura")
        if st.button("calcular"):
            r = Retangulo (float(base), float(altura))
            st.write(r) 
            st.write(f"Area: { r.calcular_area()}") 
            st.write(f"diagonal: {r.calcular_diagonal()}") 
