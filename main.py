import streamlit as st

st.set_page_config(page_title="Britisch-Sansibarischer Krieg – Timeline", layout="wide")

# ---------------------------------------------
# Datensatz: Timeline als Dictionary
# ---------------------------------------------
timeline = {
    0: {
        "zeit": "09:02 – Minute 00",
        "aktion": "Die britischen Schiffe eröffnen das Feuer auf den Sultanspalast.",
        "akteure": "Britisches Ostasiengeschwader, HMS St. George, HMS Philomel, HMS Racoon, HMS Thrush, HMS Sparrow; Sansibar: Khalid bin Barghash, Palastgarde, HHS Glasgow.",
        "waffen": "6,3-Zoll- und 4,7-Zoll-Geschütze der Royal Navy.",
        "konsequenzen": "Schwere Treffer und erste Verluste im Palastbereich.",
        "quelle": "Britisches Admiralitätslog"
    },
    1: {
        "zeit": "00:01",
        "aktion": "Fortgesetztes Bombardement des Palastkomplexes.",
        "akteure": "Wie zuvor.",
        "waffen": "Koordiniertes Feuer aller Marinegeschütze.",
        "konsequenzen": "Massive strukturelle Schäden; Teile des Palastes stürzen ein.",
        "quelle": "Britisches Admiralitätslog"
    },
    2: {
        "zeit": "00:02",
        "aktion": "Die HHS Glasgow eröffnet das Feuer auf die HMS St. George – ohne Wirkung.",
        "akteure": "HHS Glasgow, britische Schiffe.",
        "waffen": "9-Pfünder-Geschütz der Glasgow.",
        "konsequenzen": "Keine britischen Verluste.",
        "quelle": "Admiralitätslog, Historiker Hern (2003)"
    },
    3: {
        "zeit": "00:03",
        "aktion": "Teile des britischen Feuers richten sich nun gegen die Glasgow.",
        "akteure": "HMS St. George, HMS Thrush, HHS Glasgow.",
        "waffen": "Mittlere Marinegeschütze.",
        "konsequenzen": "Die Glasgow wird schwer getroffen und beginnt zu sinken.",
        "quelle": "Britisches Admiralitätslog"
    },
    4: {
        "zeit": "00:04",
        "aktion": "Intensives Bombardement auf Palast und Glasgow.",
        "akteure": "Britische Schiffe, sansibarische Landbatterien.",
        "waffen": "Koordinierte Salven der Royal Navy.",
        "konsequenzen": "Landgeschütze ausgeschaltet; Palastdach in Flammen.",
        "quelle": "Admiralitätslog, The Times"
    },
    5: {
        "zeit": "00:05",
        "aktion": "Palast brennt vollständig. Glasgow sinkt.",
        "akteure": "Wie zuvor.",
        "waffen": "Fortgesetzter Beschuss.",
        "konsequenzen": "Zerstörung der sansibarischen Militärstrukturen; hohe Verluste.",
        "quelle": "Admiralitätslog, Bennett (1978)"
    },
    6: {
        "zeit": "00:06",
        "aktion": "Gezieltes Feuer auf letzte Widerstandsnester.",
        "akteure": "Britische Schiffe.",
        "waffen": "Einzelfeuer.",
        "konsequenzen": "Widerstand bricht endgültig zusammen.",
        "quelle": "Britisches Admiralitätslog"
    },
    7: {
        "zeit": "00:07",
        "aktion": "Bombardement lässt stark nach.",
        "akteure": "Britische Schiffe.",
        "waffen": "Vereinzeltes Feuer.",
        "konsequenzen": "Rauch behindert Sicht.",
        "quelle": "Britisches Admiralitätslog"
    },
    8: {
        "zeit": "00:08",
        "aktion": "Briten warten auf Kapitulationszeichen.",
        "akteure": "Britische Schiffe.",
        "waffen": "Keine.",
        "konsequenzen": "De-facto Ende der Kampfhandlungen.",
        "quelle": "Britisches Admiralitätslog"
    },
    9: {
        "zeit": "00:09",
        "aktion": "Keine britische Feuertätigkeit mehr.",
        "akteure": "Britisches Kommando.",
        "waffen": "Keine.",
        "konsequenzen": "Die Zerstörung ist vollständig.",
        "quelle": "Britisches Admiralitätslog"
    }
}

# Ereignisse 10–37 ohne Aktion
for minute in range(10, 37):
    timeline[minute] = {
        "zeit": f"00:{minute:02d}",
        "aktion": "Keine signifikante Aktion aufgezeichnet.",
        "akteure": "-",
        "waffen": "-",
        "konsequenzen": "-",
        "quelle": "Logbücher/keine Detailaufzeichnungen"
    }

timeline[37] = {
    "zeit": "00:37",
    "aktion": "Sansibar sendet Kapitulationssignal; weiße Flagge.",
    "akteure": "Sansibarische Vermittler, britischer Konsul.",
    "waffen": "Keine.",
    "konsequenzen": "Formelles Ende der Kampfhandlungen.",
    "quelle": "The Times, Hern (2003)"
}

timeline[38] = {
    "zeit": "00:38 – 09:40",
    "aktion": "Offizieller Waffenstillstand. Ende des Krieges.",
    "akteure": "Alle Parteien.",
    "waffen": "Keine.",
    "konsequenzen": "Der Krieg ist beendet.",
    "quelle": "Admiralitätslog, diplomatische Depeschen"
}

# ---------------------------------------------
# UI
# ---------------------------------------------
st.title("📜 Britisch-Sansibarischer Krieg (1896) – Interaktive Timeline")
st.write("Wähle eine Minute aus, um die Ereignisse dieses Zeitpunkts anzuzeigen.")

minute = st.slider("Minute auswählen:", min_value=0, max_value=38, value=0)

event = timeline[minute]

st.subheader(f"⏱️ Zeitstempel: {event['zeit']}")
st.markdown(f"### 🔥 Aktion\n{event['aktion']}")
st.markdown(f"### 👥 Akteure & Einheiten\n{event['akteure']}")
st.markdown(f"### 🧨 Waffen & Munition\n{event['waffen']}")
st.markdown(f"### 📉 Konsequenzen\n{event['konsequenzen']}")
st.markdown(f"### 📚 Quelle\n{event['quelle']}")

# Zusatz: Karte/Schema als ASCII
st.markdown("---")
st.markdown("### 📍 Schematische Lageübersicht (ASCII)")
st.code(
"""
Nordwesten (offene See)
------------------------
[HMS Racoon]   [HMS Glasgow]
       |              |
       |              |
       |              |
       +--------------+------> Südosten (Küste)
                             [Sultanspalast]
                             [Hafen/Altstadt]
""",
    language="text"
)
