from equação import Equacao
import streamlit as st
import pandas as pd
import numpy as np

class EquacaoUI:
    def main():
        #título
        st.header("equação do II Grau : Y = Ax² + Bx + C")

        #entradas
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        x = st.text_input("Valor de X para calcular Y:")
        
        #botão
        if st.button("calcular"):
            r = Equacao(float(a), float(b), float(c))
            delta = r.delta()
            x_1 = float(x)
            st.write("Resultado da equação com valor de X :", f"{ r.Y(x_1)}")
            st.write("Delta: ", delta)
            st.write("X1: ", r.X1(delta))
            st.write("X2: ", r.X2(delta))





