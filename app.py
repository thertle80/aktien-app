import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Mein Aktien- & Dividenden-Dashboard 📈")

st.write("---")
st.subheader("1. CSV-Datei hochladen")

# Upload-Feld für die CSV-Datei
hochgeladene_datei = st.file_uploader("Zieh deine 'Dividendenaktien 2026.csv' hier rein", type=["csv"])

if hochgeladene_datei is not None:
    # CSV einlesen
    df = pd.read_csv(hochgeladene_datei)
    
    st.write("---")
    st.subheader("2. Daten anzeigen & direkt im Browser bearbeiten")
    st.info("💡 Doppelklick in eine Zelle (z.B. Dezember), Wert ändern und ganz unten neu speichern!")
    
    # Macht die Tabelle im Browser voll editierbar wie Excel
    editierte_daten = st.data_editor(df, use_container_width=True, num_rows="dynamic")
    
    st.write("---")
    st.subheader("3. Aktualisierte Daten sichern")
    
    # Bereitet die geänderten Daten wieder als CSV vor
    csv_output = editierte_daten.to_csv(index=False).encode('utf-8')
    
    # Download-Button für die aktualisierte Datei
    st.download_button(
        label="💾 Geänderte CSV-Datei herunterladen",
        data=csv_output,
        file_name="Dividendenaktien 2026.csv",
        mime="text/csv"
    )
else:
    st.warning("Bitte lade oben deine CSV-Datei hoch, um das Dashboard zu starten.")
