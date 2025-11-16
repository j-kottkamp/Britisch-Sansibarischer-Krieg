import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Britisch-Sansibarischer Krieg – Timeline", layout="wide")

anglo_zanzibar_war_timeline = {
    "metadata": {
        "konflikt": "Britisch-Sansibar-Krieg",
        "datum": "27. August 1896",
        "dauer_minuten": 38,
        "beginn_ortzeit": "09:02",
        "ende_ortzeit": "09:40",
        "befehlshaber_britisch": "Konteradmiral Harry Rawson",
        "befehlshaber_sansibar": "Khalid bin Barghash",
        "quellen_schwerpunkte": ["Admiralitätslogs", "Diplomatische Depeschen", "Presseberichte", "Sekundärliteratur"]
    },
    
    0: {
        "zeit": "00:00 - 09:02 Uhr",
        "aktion": """Das britische Ostasiengeschwader eröffnet um 09:02 Uhr präzise das Feuer auf den Sultanspalast. 
        Dieser Zeitpunkt markiert das Ende des Ultimatums und den Beginn der kürzesten militärischen Auseinandersetzung 
        der modernen Geschichte. Die ersten Salven zielen systematisch auf die strukturellen Hauptpfeiler des Palastes.""",
        "akteure": """HMS St. George (Flaggschiff), HMS Philomel, HMS Racoon, HMS Thrush, HMS Sparrow - 
        Sansibar: Palastgarde (ca. 2.800 Mann), HHS Glasgow (Kanonenboot), Küstenbatterien""",
        "waffen": """6,3-Zoll-Geschütze der St. George, 4,7-Zoll-Geschütze der kleineren Kreuzer - 
        Die Briten nutzen ihre überlegene Reichweite und Feuerkraft für ein konzentriertes Zerstörungsfeuer""",
        "konsequenzen": """Die ersten Treffer verwandeln den hölzernen Palastkomplex in ein Inferno. 
        Die sansibarischen Verteidiger sind von der Präzision und Intensität des Feuers völlig überrascht. 
        Erste schwere Verluste unter der Palastgarde.""",
        "strategische_bewertung": """Die Briten demonstrieren imperialistische Entschlossenheit - 
        Rawson führt einen chirurgischen Schlag zur sofortigen Demoralisierung des Gegners""",
        "quelle": "Britisches Admiralitätslog, Rawson-Bericht an Admiralität",
        "picture": "bilder/Bild_0.png"
    },
    
    1: {
        "zeit": "00:01",
        "aktion": """Fortgesetztes koordiniertes Bombardement. Die Schiffe feuern in rhythmischen Salven, 
        wobei jedes Geschütz spezifische Sektoren des Palastkomplexes bearbeitet. 
        Die Disziplin der Royal Navy ermöglicht ein systematisches Abtragen der Verteidigungsstrukturen.""",
        "akteure": "Wie zuvor, erste Auflösungserscheinungen in den sansibarischen Reihen",
        "waffen": "Koordinierte Salvenfeuer mit unterschiedlichen Kalibern für maximale Zerstörungswirkung",
        "konsequenzen": """Dachkonstruktionen stürzen ein, schwere Brände breiten sich aus. 
        Die moralische Wirkung auf die sansibarischen Verteidiger ist verheerend.""",
        "strategische_bewertung": """Britische Doktrin der überwältigenden Feuerüberlegenheit wird perfekt umgesetzt - 
        Ziel ist die sofortige Kampfunfähigkeit des Gegners""",
        "quelle": "Britisches Admiralitätslog, Schiffslogs der beteiligten Einheiten",
        "picture": "bilder/Bild_1.png"
    },
    
    2: {
        "zeit": "00:02",
        "aktion": """Die HHS Glasgow, das einzige seegehende Kriegsschiff Sansibars, eröffnet das Feuer auf die HMS St. George. 
        Dieser Akt der Verzweiflung unterstreicht die taktische Hilflosigkeit der Sansibarischen Streitkräfte. 
        Das Feuer der Glasgow ist unpräzise und ballistisch unterlegen.""",
        "akteure": "HHS Glasgow unter Lieutenant Lloyd Mathews (loyal zu Khalid) vs. gesamtes britisches Geschwader",
        "waffen": "9-Pfünder-Vorderlader der Glasgow gegen moderne Hinterlader der Royal Navy",
        "konsequenzen": "Keine Treffer auf britischen Schiffen - technologische und ausbildungsmäßige Überlegenheit der Briten wird deutlich",
        "strategische_bewertung": """Symbolischer Akt des Widerstands ohne reale militärische Bedeutung - 
        demonstriert das Machtgefälle zwischen imperialer Marine und lokalen Streitkräften""",
        "quelle": "Admiralitätslog, Augenzeugenberichte deutscher Konsulatsangehöriger",
        "picture": "bilder/Bild_2.png"
    },
    
    3: {
        "zeit": "00:03",
        "aktion": """Britische Schiffe konzentrieren Teile ihrer Feuerkraft auf die HHS Glasgow. 
        Die Überlegenheit der britischen Artillerie wird innerhalb von Sekunden evident. 
        Gleichzeitig wird das Palastbombardement unvermindert fortgesetzt.""",
        "akteure": "HMS St. George und HMS Thrush als Hauptangreifer der Glasgow",
        "waffen": "Präzises Direktfeuer mittlerer Kaliber auf kurze Distanz",
        "konsequenzen": """Die Glasgow erhält multiple Treffer an der Wasserlinie und beginnt sofort zu sinken. 
        Besatzung kann sich teilweise retten - erstes nennenswertes sansibarisches Materialverlust""",
        "strategische_bewertung": """Systematische Eliminierung jeglicher gegnerischen Marinepräsenz - 
        typisches Vorgehen imperialer Mächte zur Sicherung der Seeherrschaft""",
        "quelle": "Britisches Admiralitätslog",
        "picture": "bilder/Bild_3.png"
    },
    
    4: {
        "zeit": "00:04",
        "aktion": """Das Gefecht erreicht seinen Höhepunkt. Der Palast steht in Flammen, die Glasgow sinkt, 
        die Landbatterien werden systematisch ausgeschaltet. Die Briten zeigen bemerkenswerte Feuerdisziplin 
        und koordinieren ihre Angriffe perfekt.""",
        "akteure": "Komplettes britisches Geschwader im koordinierten Einsatz",
        "waffen": "Vollständiges Waffenarsenal der Royal Navy im Einsatz",
        "konsequenzen": """Zusammenbruch der organisierten sansibarischen Verteidigung. 
        Verluste unter Zivilisten beginnen signifikant zu werden durch Streuwirkungen""",
        "strategische_bewertung": """Klassischer Fall von 'Shock and Awe' vor der Begriffsprägung - 
        überwältigende Gewaltanwendung zur schnellen Konfliktbeendigung""",
        "quelle": "Admiralitätslog",
        "picture": "bilder/Bild_4.png"
    },
    
    5: {
        "zeit": "00:05",
        "aktion": """Der Sultanspalast ist nun vollständig eingeschlossen von Flammen. 
        Die HHS Glasgow ist gesunken oder am unmittelbaren Sinken. 
        Die britischen Schiffe wechseln zu gezieltem Einzelfeuer auf verbliebene Widerstandsnester.""",
        "akteure": "Britische Schiffe im Abnutzungsmodus, sansibarische Streitkräfte in Auflösung",
        "waffen": "Gezieltes Einzelfeuer statt Salven",
        "konsequenzen": """Physische und moralische Zerstörung der sansibarischen Kampfkraft. 
        Desertionen und Fluchtbewegungen werden massenhaft""",
        "strategische_bewertung": """Übergang von der Zerstörungs- zur Kontrollphase - 
        Briten etablieren faktische Seeherrschaft vor Sansibar""",
        "quelle": "Britisches Admiralitätslog, Bennett (1978)",
        "picture": "bilder/Bild_5.png"
    },
# Minute 6 - Übergang zur Zielauswahl
    6: {
        "zeit": "00:06",
        "aktion": """Das britische Geschwader wechselt von flächendeckendem Bombardement zu präziser Zielauswahl. 
        Die Hauptstrukturen des Palastes sind bereits zerstört, nun konzentrieren sich die Geschütze auf verbliebene 
        Widerstandsnester und mögliche Aufenthaltsorte von Khalids Führungsstab. Die Feuerrate nimmt bewusst ab.""",
        "akteure": "HMS Thrush und HMS Sparrow als primäre Zielerfasser, HMS St. George koordiniert",
        "waffen": "Präzisionsfeuer mit 4,7-Zoll-Geschützen, vereinzelt Maschinengewehrfeuer zur Zielmarkierung",
        "konsequenzen": "Gezielte Eliminierung letzter organisierter Verteidigungspunkte - moralischer Zusammenbruch der Palastgarde",
        "strategische_bewertung": """Übergang von der Zerstörungs- zur Kontrollphase - 
        Briten demonstrieren Fähigkeit zu chirurgischen Schlägen nach initialem Schock""",
        "quelle": "Britisches Admiralitätslog, Schiffsartillerieprotokolle",
        "picture": "bilder/Bild_6.png"
    },

    # Minute 7-9 - Konsolidierungsphase
    7: {
        "zeit": "00:07",
        "aktion": """Das Artilleriefeuer reduziert sich auf vereinzelte Schüsse. Rauchschwaden behindern die Sicht, 
        was gezieltes Feuer erschwert. Britische Beobachter kartieren die Zerstörungen und melden Rückzugsbewegungen 
        der sansibarischen Truppen. Erste Anzeichen von Flucht in die deutsche Botschaft werden registriert.""",
        "akteure": "Britische Artilleriebeobachter, sansibarische Überlebende in Auflösung",
        "waffen": "Einzelfeuer nur bei bestätigten Zielen - ökonomischer Munitionseinsatz",
        "konsequenzen": "Brandausbreitung auf angrenzende Stadtviertel - beginnende humanitäre Krise",
        "strategische_bewertung": """Demonstration von Kontrolle durch dosierte Gewaltanwendung - 
        typisch für imperialistische Interventionen zur Aufrechterhaltung des Drucks""",
        "quelle": "Admiralitätslog, Beobachterberichte der HMS Philomel",
        "picture": "bilder/Bild_7.png"
    },

    8: {
        "zeit": "00:08", 
        "aktion": """Letzte koordinierte Schüsse auf intakte Gebäudeteile. Die Briten testen die Reaktion der Verteidiger 
        und stellen fest, dass organisieter Widerstand kollabiert ist. Signalflaggen werden zwischen den Schiffen ausgetauscht 
        zur Koordination der nächsten Phase.""",
        "akteure": "Britische Flottillenkommunikation, versprengte sansibarische Einheiten",
        "waffen": "Symbolische letzte Salven zur psychologischen Wirkung",
        "konsequenzen": "Endgültiger Zusammenbruch der Kommandostrukturen auf sansibarischer Seite",
        "strategische_bewertung": """Psychologische Kriegführung durch demonstrative Feuerpausen 
        gefolgt von punktuellen Schlägen - bricht verbliebenen Widerstandswillen""",
        "quelle": "Flaggsignallogs, Historiker: Bennett 1978",
        "picture": "bilder/Bild_8.png"
    },

    9: {
        "zeit": "00:09",
        "aktion": """Feuerpause tritt ein. Die Briten nutzen die Rauchlücken zur Schadensbewertung. 
        Erste Meldungen über Khalids Flucht zum deutschen Konsulat erreichen die Schiffe. 
        Die Royal Navy bereitet Landungstruppen vor, hält sie aber zurück.""",
        "akteure": "Britische Aufklärung, deutsche Konsulatsangehörige, fliehender Sultan",
        "waffen": "Beobachtungsgeräte - keine Schussabgabe",
        "konsequenzen": "De-facto-Ende der Kampfhandlungen - Beginn des diplomatischen Nachspiels",
        "strategische_bewertung": """Perfekte Timing - militärische Aktion endet genau mit Erreichen der politischen Ziele - 
        Meisterstück imperialer Krisenbewältigung""",
        "quelle": "Diplomatische Depeschen, Konsulatsberichte",
        "picture": "bilder/Bild_9.png"
    },

    # Minuten 10-20 - Diplomatische Initialphase
    10: {
        "zeit": "00:10",
        "aktion": """Komplette Feuerpause. Dichter Rauch hüllt den zerstörten Palast ein. 
        Britische Schiffe manövrieren in bessere Beobachtungspositionen. 
        Erste informelle Kontakte zwischen britischen Offizieren und sansibarischen Vermittlern.""",
        "akteure": "Junior-Offiziere beider Seiten, Stadtbevölkerung in Panik",
        "waffen": "Keine - Fokus auf Kommunikation und Beobachtung",
        "konsequenzen": "Überlebende sammeln sich - chaotische Szenen in der Innenstadt",
        "strategische_bewertung": """Übergang von militärischer zu politischer Dominanz - 
        Briten nutzen die Atempause zur Positionsverbesserung""",
        "quelle": "Schiffslogs, lokale Augenzeugenberichte",
        "picture": "bilder/Bild_10.png"
    },

    11: {
        "zeit": "00:11",
        "aktion": """Rauch beginnt sich zu lichten, Ausmaß der Zerstörung wird sichtbar. 
        Britische Kommandostruktur evaluiert die Situation - keine Landung befohlen. 
        Erste Hilfsmaßnahmen für Verwundete werden von Stadtbewohnern organisiert.""",
        "akteure": "Britische Kommandoebene, sansibarische Zivilbevölkerung",
        "waffen": "Keine Kampfhandlungen",
        "konsequenzen": "Langsame Realisierung der vollständigen Niederlage auf sansibarischer Seite",
        "strategische_bewertung": """Demonstration von Sieger-Großmut durch Verzicht auf sofortige Besetzung - 
        klassisches Mittel zur Erleichterung der politischen Unterwerfung""",
        "quelle": "Admiral Rawson Bericht",
        "picture": "bilder/Bild_11.png"
    },

    12: {
        "zeit": "00:12",
        "aktion": """Formelle Kontaktaufnahme zwischen britischem Konsul Basil Cave und deutschen Vermittlern. 
        Die Briten insistieren auf sofortiger bedingungsloser Kapitulation. 
        Verwirrung über Khalids Verbleib - verschiedene Gerüchte kursieren.""",
        "akteure": "Konsul Basil Cave, deutsche Diplomaten, sansibarische Würdenträger",
        "waffen": "Diplomatischer Druck als primäres Mittel",
        "konsequenzen": "Beginn institutioneller Übergabeverhandlungen",
        "strategische_bewertung": """Schnelle Nutzung des militärischen Erfolgs für politische Forderungen - 
        typische Koordination zwischen militärischer und diplomatischer Macht im Empire""",
        "quelle": "Diplomatische Archive, Cave-Berichte an Foreign Office",
        "picture": "bilder/Bild_12.png"
    },

    13: {
        "zeit": "00:13",
        "aktion": """Deutsche Vermittler überbringen erste Kapitulationsbedingungen. 
        Britische Schiffe bleiben in Kampfbereitschaft, aber mit reduzierter Besatzung an Geschützen. 
        Medizinische Versorgung für sansibarische Verwundete wird diskutiert.""",
        "akteure": "Deutsches Konsulat als neutrale Instanz, britische Kommandostruktur",
        "waffen": "Drohpotential der Artillerie als Verhandlungshebel",
        "konsequenzen": "Erste institutionalisierte Kommunikationskanäle etabliert",
        "strategische_bewertung": """Geschickte Nutzung deutscher Vermittlung zur Wahrung des Gesichts - 
        ermöglicht sansibarischer Seite würdevollere Kapitulation""",
        "quelle": "Deutsche Konsulatsberichte, Britische Außenamtspapiere",
        "picture": "bilder/Bild_13.png"
    },

    14: {
        "zeit": "00:14", 
        "aktion": """Khalids Flucht zum deutschen Konsulat wird bestätigt. 
        Britische Forderungen präzisieren sich: Installation von Hamud bin Muhammed als neuem Sultan. 
        Diskussion über Behandlung der fliehenden Palastwache.""",
        "akteure": "Khalid bin Barghash, deutsche Schutzmacht, britische politische Führung",
        "waffen": "Politische und diplomatische Instrumente dominieren",
        "konsequenzen": "Legitimität von Khalids Herrschaft endgültig gebrochen",
        "strategische_bewertung": """Wichtiger psychologischer Moment - Flucht des Sultans zerstört 
        letzte Hoffnungen auf Wiederbelebung des Widerstands""",
        "quelle": "Admiral Rawson Bericht",
        "picture": "bilder/Bild_14.png"
    },

    15: {
        "zeit": "00:15",
        "aktion": """Britische Forderungen werden sansibarischen Vertretern formell übergeben. 
        Frist für formelle Kapitulation wird gesetzt. Royal Marines werden in Landungsboote verladen, 
        aber nicht abgesetzt - demonstrative Vorbereitung.""",
        "akteure": "Royal Marines in Bereitschaft, sansibarische Verhandlungsdelegation",
        "waffen": "Demonstration amphibischer Fähigkeiten als Druckmittel",
        "konsequenzen": "Steigender Druck auf sansibarische Seite zur schnellen Entscheidung",
        "strategische_bewertung": """Geschicktes Pokerspiel - Androhung weiterer Gewalt 
        bei gleichzeitiger Verhandlungsbereitschaft""",
        "quelle": "Admiral Rawson Bericht, Marine-Infanterie-Logs",
        "picture": "bilder/Bild_15.png"
    },

    16: {
        "zeit": "00:16",
        "aktion": """Sansibarische Delegation kehrt mit britischen Forderungen zurück. 
        Interner Machtkampf unter den verbliebenen Würdenträgern - keine einheitliche Position. 
        Britische Schiffe patrouillieren demonstrativ vor der Küste.""",
        "akteure": "Sansibarischer Adel, traditionelle Autoritäten, britische Seestreitkräfte",
        "waffen": "Mobilisierte Schiffsartillerie als ständige Präsenz",
        "konsequenzen": "Politisches Vakuum auf sansibarischer Seite",
        "strategische_bewertung": """Ausnutzung innerer Zerstrittenheit des Gegners - 
        klassisches Divide-et-impera in Echtzeit""",
        "quelle": "Lokale Chronisten, britische Geheimdienstberichte",
        "picture": "bilder/Bild_16.png"
    },

    17: {
        "zeit": "00:17",
        "aktion": """Deutsche Vermittler erhöhen Druck auf sansibarische Seite zur Annahme der Bedingungen. 
        Hinweis auf begrenzte deutsche Schutzzusagen nur für Khalid persönlich. 
        Britische Frist läuft weiter.""",
        "akteure": "Deutsche Diplomatie, sansibarische Entscheidungsträger",
        "waffen": "Diplomatischer und politischer Druck",
        "konsequenzen": "Isolation der hardliner unter den sansibarischen Würdenträgern",
        "strategische_bewertung": """Effektive Koordination zwischen britischer und deutscher Diplomatie - 
        zeigt europäische Solidarität in imperialen Grundsatzfragen""",
        "quelle": "Deutsch-britische diplomatische Korrespondenz",
        "picture": "bilder/Bild_17.png"
    },

    18: {
        "zeit": "00:18",
        "aktion": """Erste sansibarische Signale zur Kapitulationsbereitschaft. 
        Diskussion über konkrete Modalitäten: Übergabe von Waffen, Behandlung der Besiegten, 
        Sicherheitsgarantien für die Bevölkerung.""",
        "akteure": "Sansibarische Unterhändler, britische Verhandlungsführer",
        "waffen": "Verhandlungsgeschick als primäres Werkzeug",
        "konsequenzen": "Durchbruch in den Kapitulationsverhandlungen",
        "strategische_bewertung": """Beginnender Erfolg der kombinierten Militär-Diplomatie-Strategie - 
        sansibarische Seite erkennt Ausweglosigkeit der Situation""",
        "quelle": "Verhandlungsprotokolle, zeitgenössische Berichte",
        "picture": "bilder/Bild_18.png"
    },

    19: {
        "zeit": "00:19",
        "aktion": """Details der Thronbesteigung von Hamud bin Muhammed werden ausgehandelt. 
        Britische Garantien für traditionelle Institutionen gegen politische Unterwerfung. 
        Formulierungen der Kapitulationsurkunde werden diskutiert.""",
        "akteure": "Juristische Berater beider Seiten, traditionelle sansibarische Autoritäten",
        "waffen": "Vertragstexte und protokollarische Formeln",
        "konsequenzen": "Institutionelle Kontinuität unter britischer Oberhoheit wird sichergestellt",
        "strategische_bewertung": """Wichtiger Balanceakt - Erhaltung scheinbarer Souveränität 
        bei faktischer Implementierung britischer Kontrolle""",
        "quelle": "Vertragsdokumente, konstitutionelle Analysen",
        "picture": "bilder/Bild_19.png"
    },

    20: {
        "zeit": "00:20",
        "aktion": """Kapitulationsurkunde nimmt konkrete Form an. Hamud bin Muhammed wird offiziell 
        als neuer Sultan proklamiert. Britische Anerkennung wird zugesichert gegen politische Zugeständnisse.""",
        "akteure": "Hamud bin Muhammed, britische politische Repräsentanten",
        "waffen": "Rechtliche und protokollarische Instrumente",
        "konsequenzen": "Politische Transition formal eingeleitet",
        "strategische_bewertung": """Reibungsloser Übergang der Herrschaft - entspricht britischer 
        Präferenz für indirekte Herrschaft durch kooperative lokale Herrscher""",
        "quelle": "Proklamationsdokumente, historische Analysen",
        "picture": "bilder/Bild_20.png"
    },

    # Minuten 21-30 - Finale Verhandlungsphase
    21: {
        "zeit": "00:21",
        "aktion": """Finale Beratungen über Kapitulationsbedingungen. Deutsche Vermittler garantieren 
        sicheres Geleit für Khalid ins Exil. Britische Marine bereitet Ehrenformation für neuen Sultan vor.""",
        "akteure": "Alle beteiligten diplomatischen Parteien",
        "waffen": "Protokollarische und zeremonielle Vorbereitungen",
        "konsequenzen": "Reibungsloser Herrscherwechsel institutionell abgesichert",
        "strategische_bewertung": """Demonstration imperialer Stärke durch Großzügigkeit gegenüber 
        Besiegten - stabilisiert zukünftige Herrschaftsverhältnisse""",
        "quelle": "Zeremonielle Protokolle, diplomatische Notizen",
        "picture": "bilder/Bild_21.png"
    },

    22: {
        "zeit": "00:22", 
        "aktion": """Kapitulationsdokument wird von sansibarischer Seite geprüft. 
        Letzte Widerstände einiger traditionalistischer Würdenträger werden überwunden. 
        Britische Schiffe signalisieren Bereitschaft zur formellen Beendigung der Feindseligkeiten.""",
        "akteure": "Sansibarische Rechtsgelehrte, britische juristische Berater",
        "waffen": "Vertragsrecht und internationale Abkommen",
        "konsequenzen": "Juristische Legitimierung des Machtwechsels",
        "strategische_bewertung": """Wichtiger Präzedenzfall für 'regime change' durch imperialen Druck - 
        Kombination aus militärischer Macht und legalistischer Begründung""",
        "quelle": "Rechtliche Dokumentation, völkerrechtliche Analysen",
        "picture": "bilder/Bild_22.png"
    },

    23: {
        "zeit": "00:23",
        "aktion": """Deutsche Seite bestätigt Khalids Asyl und bereitet dessen Transfer vor. 
        Britische Marine verringert Kampfbereitschaft stufenweise. 
        Erste Planungen für Wiederaufbau und Entschärfung werden initiiert.""",
        "akteure": "Deutsche Schutztruppe, britische Pioniereinheiten",
        "waffen": "Logistische und administrative Vorbereitungen",
        "konsequenzen": "Rückkehr zur Normalität wird eingeleitet",
        "strategische_bewertung": """Schneller Übergang von Krieg zu Friedenssicherung - 
        zeugt von professioneller Planung und Erfahrung in kolonialen Operationen""",
        "quelle": "Administrative Berichte, Logistikprotokolle",
        "picture": "bilder/Bild_23.png"
    },

    24: {
        "zeit": "00:24",
        "aktion": """Formelle Annahme der Kapitulationsbedingungen durch sansibarische Delegation. 
        Nur noch technische Details müssen geklärt werden. 
        Britische Signalflaggen zeigen 'Erwartung' gegenüber Landeinheiten.""",
        "akteure": "Technische Unterhändler, Kommunikationspersonal",
        "waffen": "Signalflaggen und Kommunikationstechnik",
        "konsequenzen": "Unmittelbar bevorstehende formelle Beendigung des Konflikts",
        "strategische_bewertung": """Perfekte Synchronisation militärischer und diplomatischer 
        Zeitabläufe - professionelle Krisenbewältigung""",
        "quelle": "Kommunikationslogs, Verfahrensprotokolle",
        "picture": "bilder/Bild_24.png"
    },

    25: {
        "zeit": "00:25",
        "aktion": """Vorbereitung der Zeremonie zur Amtseinführung des neuen Sultans. 
        Britische Musikkorps werden in Position gebracht. 
        Letzte Koordination mit deutschen Beobachtern über Khalids Abtransport.""",
        "akteure": "Zeremonielle Einheiten, protokollarische Experten",
        "waffen": "Symbolische und repräsentative Handlungen",
        "konsequenzen": "Rasche Normalisierung der politischen Verhältnisse",
        "strategische_bewertung": """Geschickte Nutzung symbolischer Politik zur Konsolidierung 
        militärischer Erfolge - typisch für britische Imperialpraxis""",
        "quelle": "Zeremonielle Aufzeichnungen, Protokollhandbücher",
        "picture": "bilder/Bild_25.png"
    },

    26: {
        "zeit": "00:26",
        "aktion": """Finale redaktionelle Änderungen am Kapitulationsdokument. 
        Datum und Uhrzeit der Unterzeichnung werden festgelegt. 
        Sicherheitsvorkehrungen für die Zeremonie werden koordiniert.""",
        "akteure": "Juristische Redakteure, Sicherheitskräfte",
        "waffen": "Rechtstexte und Sicherheitsprotokolle",
        "konsequenzen": "Formelle Beendigung des Konflikts steht unmittelbar bevor",
        "strategische_bewertung": """Sorgfältige rechtliche Absicherung des erzwungenen 
        Herrscherwechsels - vermeidet spätere Anfechtungen""",
        "quelle": "Rechtsdokumentation, Sicherheitsberichte",
        "picture": "bilder/Bild_26.png"
    },

    27: {
        "zeit": "00:27",
        "aktion": """Khalid wird offiziell deutschen Schutz überstellt. 
        Britische Seite bestätigt Verzicht auf Strafverfolgung gegen ihn. 
        Evakuierungsroute zum Hafen wird festgelegt.""",
        "akteure": "Khalid bin Barghash, deutsche Schutztruppe, britische Grenzkontrolleure",
        "waffen": "Diplomatische Immunitäten und Schutzvereinbarungen",
        "konsequenzen": "Sicherer Abgang des gestürzten Herrschers",
        "strategische_bewertung": """Politischer Kompromiss ermöglicht sauberen Schnitt - 
        Vermeidung von Märtyrertum des gestürzten Sultans""",
        "quelle": "Asyldokumente, Evakuierungsprotokolle",
        "picture": "bilder/Bild_27.png"
    },

    28: {
        "zeit": "00:28",
        "aktion": """Vorbereitung der weißen Flagge über den Palastruinen. 
        Obwohl der Palast zerstört ist, wird protokollarisch korrekte Kapitulationssymbolik durchgeführt. 
        Britische Fotografen dokumentieren den historischen Moment.""",
        "akteure": "Protokollarische Experten, Pressevertreter",
        "waffen": "Symbolische Flaggen und zeremonielle Handlungen",
        "konsequenzen": "Visuelle Dokumentation der britischen Sieges für die Weltpresse",
        "strategische_bewertung": """Bewusste Inszenierung für internationale Öffentlichkeit - 
        Demonstration britischer Entschlossenheit und Großzügigkeit""",
        "quelle": "Presseberichte, fotografische Dokumentation",
        "picture": "bilder/Bild_28.png"
    },

    29: {
        "zeit": "00:29",
        "aktion": """Letzte Instruktionen an alle beteiligten Einheiten über Verhalten nach Kapitulation. 
        Britische Marineinfanterie erhält Regeln für Interaktion mit lokaler Bevölkerung. 
        Medizinische Hilfe für Verwundete wird koordiniert.""",
        "akteure": "Militärische Führung, medizinisches Personal, zivile Hilfskräfte",
        "waffen": "Dienstvorschriften und Einsatzregeln",
        "konsequenzen": "Geordneter Übergang zur Besatzungsverwaltung",
        "strategische_bewertung": """Professionelle Nachkriegsplanung - vermeidet unnötige 
        Reibereien und stabilisiert Besatzungsregime""",
        "quelle": "Militärische Direktiven, Sanitätsberichte",
        "picture": "bilder/Bild_29.png"
    },

    30: {
        "zeit": "00:30",
        "aktion": """Alle Vorbereitungen für die formelle Kapitulation sind abgeschlossen. 
        Die weiße Flagge ist einsatzbereit, die Dokumente liegen zur Unterzeichnung bereit. 
        Nur noch der formale Akt der Hisung steht aus.""",
        "akteure": "Finale protokollarische Teams beider Seiten",
        "waffen": "Zeremonielle Utensilien und Dokumente",
        "konsequenzen": "Unmittelbar bevorstehende Beendigung des Krieges",
        "strategische_bewertung": """Perfekte choreographierte Übergabe - entspricht 
        britischer Vorliebe für geordnete und rechtmäßig erscheinende Machtwechsel""",
        "quelle": "Protokollarische Aufzeichnungen, zeitgenössische Chroniken",
        "picture": "bilder/Bild_30.png"
    },

    # Minuten 31-36 - Finale Vorbereitungen
    31: {
        "zeit": "00:31",
        "aktion": """Letzte Kommunikation zwischen Schiffen und Land über genauen Zeitpunkt der Flaggenhisung. 
        Deutsche Beobachter bestätigen Bereitschaft zur Übernahme Khalids. 
        Britische Pressekorrespondenten erhalten Zugang für Berichterstattung.""",
        "akteure": "Internationale Presse, diplomatische Beobachter, Kommunikationspersonal",
        "waffen": "Medienarbeit und öffentliche Darstellung",
        "konsequenzen": "Globale mediale Verbreitung des Ereignisses vorbereitet",
        "strategische_bewertung": """Moderne Medienstrategie - Sicherstellung positiver 
        Darstellung britischen Vorgehens in Weltöffentlichkeit""",
        "quelle": "Presseanweisungen, Medienberichte",
        "picture": "bilder/Bild_31.png"
    },

    32: {
        "zeit": "00:32",
        "aktion": """Countdown zur formellen Kapitulation beginnt. 
        Alle britischen Schiffe in Paradeformation. 
        Letzte Bestätigung, dass keine feindlichen Aktivitäten mehr stattfinden.""",
        "akteure": "Flottenkommando, Formationseinheiten",
        "waffen": "Protokollarische Schiffsformationen",
        "konsequenzen": "Militärisch zeremonieller Abschluss des Konflikts",
        "strategische_bewertung": """Demonstration vollständiger Kontrolle durch 
        präzise choreographierte Marineformationen""",
        "quelle": "Formationsbefehle, zeremonielle Protokolle",
        "picture": "bilder/Bild_32.png"
    },

    33: {
        "zeit": "00:33",
        "aktion": """Finale Bestätigung der Kapitulationsbereitschaft von sansibarischer Seite. 
        Keine verbliebenen Widerstände oder Bedingungen. 
        Britische Seite bereitet offizielle Verlautbarung vor.""",
        "akteure": "Politische Führung beider Seiten, Pressesprecher",
        "waffen": "Offizielle Kommuniques und Verlautbarungen",
        "konsequenzen": "Historische Dokumentation des Kriegsendes",
        "strategische_bewertung": """Sorgfältige Dokumentation für Geschichtsschreibung und 
        rechtliche Absicherung des Vorgehens""",
        "quelle": "Amtliche Verlautbarungen, Archivdokumente",
        "picture": "bilder/Bild_33.png"
    },

    34: {
        "zeit": "00:34", 
        "aktion": """Weiße Flagge wird physisch in Position gebracht. 
        Britische Marine bereitet Salutschüsse für neuen Sultan vor. 
        Deutsche Seite bestätigt Bereitschaft zur Exilierung Khalids.""",
        "akteure": "Flaggenpersonal, Artillerie für Ehrensalute, Exil-Koordinatoren",
        "waffen": "Zeremonielle Artillerie und Protokollflaggen",
        "konsequenzen": "Unmittelbar bevorstehende Beendigung aller Feindseligkeiten",
        "strategische_bewertung": """Perfekte Abstimmung zwischen politischen, militärischen 
        und zeremoniellen Aspekten der Konfliktbeendigung""",
        "quelle": "Zeremonielle Anweisungen, Protokollnotizen",
        "picture": "bilder/Bild_34.png"
    },

    35: {
        "zeit": "00:35",
        "aktion": """Letzte Minute vor formeller Kapitulation. 
        Absolute Stille auf dem Schlachtfeld. 
        Nur vereinzeltes Knistern der Brände und leise Kommandos sind hörbar.""",
        "akteure": "Alle Beteiligten in erwartungsvoller Stille",
        "waffen": "Keine - symbolischer Moment des Übergangs",
        "konsequenzen": "Atmosphärischer Übergang von Krieg zu Frieden",
        "strategische_bewertung": """Psychologisch wichtiger Moment der Stille - 
        markiert bewusst den Epochenwechsel in Sansibars Geschichte""",
        "quelle": "Zeitgenössische Beschreibungen, literarische Verarbeitungen",
        "picture": "bilder/Bild_35.png"
    },

    36: {
        "zeit": "00:36",
        "aktion": """Vorbereitung der tatsächlichen Flaggenhisung. 
        Letzte protokollarische Checks. 
        Britische Kommandeure warten auf das vereinbarte Signal.""",
        "akteure": "Protokollarisches Führungspersonal, Signalgeber",
        "waffen": "Protokollarische Signalinstrumente",
        "konsequenzen": "Unmittelbar bevorstehende formelle Beendigung",
        "strategische_bewertung": """Maximale symbolische Aufladung des finalen Aktes - 
        bewusste Inszenierung historischer Bedeutung""",
        "quelle": "Protokollarische Aufzeichnungen, Signallogs",
        "picture": "bilder/Bild_36.png"
    },

    37: {
        "zeit": "00:37",
        "aktion": """Formelle Kapitulation Sansibars. Eine weiße Flagge wird gehisst, obwohl der Palast praktisch nicht mehr existiert. 
        Khalid bin Barghash flieht zur deutschen Botschaft und bittet um politisches Asyl. 
        Die Briten akzeptieren die Kapitulation und bereiten die Installation eines neuen Sultans vor.""",
        "akteure": "Sansibarische Delegation, deutscher Konsul, britische Diplomatie",
        "waffen": "Keine - symbolische Handlungen dominieren",
        "konsequenzen": "Offizielles Ende der Kampfhandlungen - Beginn britischer Besatzungsverwaltung",
        "strategische_bewertung": """Perfekte Umsetzung britischer Imperialstrategie - 
        schneller militärischer Sieg gefolgt von sofortiger politischer Konsolidierung""",
        "quelle": "The Times, diplomatische Depeschen, Hern (2003)",
        "picture": "bilder/Bild_37.png"
    },

    38: {
        "zeit": "00:38 - 09:40 Uhr",
        "aktion": """Waffenstillstand tritt in Kraft. Der kürzeste Krieg der Geschichte ist beendet. 
        Britische Marineinfanterie geht an Land zur Sicherung kritischer Punkte. 
        Die politische und militärische Kontrolle über Sansibar liegt vollständig bei Großbritannien.""",
        "akteure": "Royal Marines, britische Verwaltung, sansibarische Zivilbevölkerung",
        "waffen": "Keine - Besatzungsphase beginnt",
        "konsequenzen": "Endgültige britische Hegemonie über Sansibar - Khalid im Exil",
        "strategische_bewertung": """Abschluss einer textbookmäßigen imperialen Intervention - 
        Demonstration von Machtprojektion und politischer Entschlossenheit des British Empire""",
        "quelle": "Admiralitätslog, Besatzungsberichte, historische Analysen",
        "picture": "bilder/Bild_38.png"
    }}

# Analyse- und Kontextmodul
anglo_zanzibar_war_timeline["strategische_analyse"] = {
    "britische_strategie": {
        "ziel": "Schnelle Wiedereinsetzung pro-britischer Herrschaft in Sansibar",
        "methode": "Überwältigende maritime Übermacht kombiniert mit politischem Druck",
        "erfolgsfaktoren": ["Technologische Überlegenheit", "Disziplinierte Exekution", "Diplomatische Vorbereitung"]
    },
    "sansibarische_situation": {
        "schwächen": ["Veraltete Bewaffnung", "Unzureichende Ausbildung", "Fehlende internationale Unterstützung"],
        "fehleinschaetzungen": ["Überschätzung eigener Möglichkeiten", "Unterschätzung britischer Entschlossenheit"]
    },
    "internationale_dimension": {
        "deutsche_rolle": "Begrenzte Vermittlung, primär observation",
        "weltweite_wirkung": "Demonstration britischer imperialer Entschlossenheit"
    }
}

preface = {
0: """Gegen Ende des 19. Jahrhunderts befand sich die Insel Sansibar in einer Phase politischer Unsicherheit und 
kolonialer Abhängigkeit. 

Seit Mitte des Jahrhunderts hatte Großbritannien seinen Einfluss auf Sansibar 
stetig ausgeweitet, sowohl durch Handelsverträge als auch durch diplomatische und militärische Präsenz. 

Ein zentraler Beweggrund dafür war die Kontrolle über die ostafrikanische Küste und die Eindämmung des Sklavenhandels, 
der für Sansibar über Jahrzehnte ein wirtschaftlicher Kernbereich gewesen war.""",
        
1: """Nach dem Tod des regierenden Sultans Sayyid Khalifa bin Said am 25. August 1896 entstand sofort ein Machtvakuum. 

Nach geltenden Absprachen zwischen Großbritannien und Sansibar durfte kein neuer Sultan ohne Zustimmung der Briten den Thron 
besteigen. 

Dennoch setzte sich Sayyid Khalid bin Barghash, ein Neffe des Verstorbenen, noch am selben Tag eigenmächtig im Palast 
fest, ohne britische Genehmigung. 

Großbritannien bevorzugte hingegen Sayyid Hamud bin Mohammed, der als britenfreundlich galt und 
bereit war, Reformen zu akzeptieren. 

Khalids Handeln wurde deshalb in London nicht als legitime Thronfolge, sondern als Putsch aufgefasst.""",
        
2: """Bereits vor der Krise lagen mehrere Schiffe der Royal Navy im Hafen von Sansibar, um britische Interessen zu schützen. 
Zu den wichtigsten gehörten:
- HMS St George – Flaggschiff des Konteradmirals Harry Rawson
- HMS Philomel
- HMS Racoon
- HMS Thrush
- HMS Sparrow

Diese Schiffe bildeten die Kernflotte, die später das Feuer eröffnen sollte. Zusätzlich stand die britische Marineinfanterie an Land bereit,
um im Notfall den Palast einzunehmen oder Regierungsgebäude zu sichern.""",
    
3: """Sayyid Khalid reagierte auf die britischen Warnungen nicht mit Rückzug, sondern mit Aufrüstung. Er ließ sich im Sultanspalast verschanzen, 
besetzte Regierungsgebäude und brachte mehrere Geschütze in Stellung, darunter ältere Kanonen, einige Maxim-Maschinengewehre und rund 2.800 Kämpferaus seiner Gefolgschaft.

Obwohl seine Streitkräfte zahlenmäßig beeindruckend wirkten, waren sie schlecht ausgebildet, schlecht koordiniert und technologisch weit unterlegen. 
Khalid setzte jedoch darauf, dass die Briten nicht riskieren würden, offen Krieg gegen Sansibar zu führen.""", 
    
4: """Am 26. August stellten die Briten ein Ultimatum:
Khalid sollte den Palast räumen und seine Truppen entwaffnen – andernfalls würden militärische Maßnahmen folgen.

Khalid ignorierte diese Forderung und antwortete, dass er sich “nicht einschüchtern lasse”. Damit war der Weg in den Konflikt vorgezeichnet.

Das britische Ultimatum lief am 27. August 1896 um 09:00 Uhr ab.
Nur wenige Minuten später, exakt um 09:02 Uhr, eröffnete die Royal Navy das Feuer auf den Sultanspalast.

Damit begann der Britisch-Sansibarische Krieg, der als kürzester Krieg der Weltgeschichte in die Historie einging."""
}

preface_images = [
    "bilder/preface_0.png",
    "bilder/preface_1.png",
    "bilder/preface_2.png",
    "bilder/preface_3.png",
    "bilder/preface_4.png"
]

quellen = [
    {"name": "Life of Admiral Sir Harry Rawson", "link": "https://archive.org/details/lifeofadmiralsir00raws/page/100/mode/2up"},
    {"name": "The National Archives - ADM 53 (Royal Navy: Ships' log books)", "link": "https://discovery.nationalarchives.gov.uk/details/r/C1762"},
    {"name": "Archive.org - Zanzibar in Contemporary Times (Lyne, 1905)", "link": "https://archive.org/details/zanzibarinconte02lynegoog"},
    {"name": "Robert Frew Antiquariat - HMS St. George Augenzeugenberichte", "link": "https://www.robertfrew.com/stock-detail.php?id=55487"},
    {"name": "Naval-History.net - HMS St. George Service history", "link": "https://www.naval-history.net/OWShips-WW1-05-HMS_St_George.htm"},
    {"name": "The Times Archive", "link": "https://www.thetimes.com/tto/archive/find/british+zanzibar+war"},
    {"name": "NZ History - HMS Philomel", "link": "https://nzhistory.govt.nz/war/hms-philomel"},
    {"name": "Wikipedia - Anglo-Zanzibar War", "link": "https://en.wikipedia.org/wiki/Anglo-Zanzibar_War"},
    {"name": "Wikipedia - Pictures of Anglo-Zanzibar War", "link": "https://en.wikipedia.org/wiki/Anglo-Zanzibar_War"},
]


# UI
# ---------------------------------------------


# Custom CSS with modern styling
st.markdown("""
<style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .event-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 2px;
        margin: 15px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .event-content {
        background: #1f2029;
        border-radius: 10px;
        padding: 20px;
        position: relative;
    }
    
    .section {
        margin: 20px 0;
        padding: 15px;
        border-left: 4px solid #667eea;
        background: ##1f2029;
        border-radius: 8px 8px 8px 8px;
        transition: all 0.3s ease;
    }
    
    .section:hover,
    .source-link:hover {
        background: #1f2029;
        transform: translateX(5px);
    }
    
    .icon-header {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        color: #2c3e50;
    }
    
    .icon-header i {
        margin-right: 10px;
        font-size: 1.2em;
        color: #667eea;
    }
    
    .timestamp {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 20px;
        font-weight: 800;
        box-shadow: 0 2px 10px rgba(255,107,107,0.3);
    }
    
    .content-text {
        color: #FAFAFA;
        line-height: 1.6;
        margin-left: 28px;
    }
    
    .image-container {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    
    .sources {
        padding: 12px;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        transition: all 0.8s ease;
    }
    
    .source-title {
        font-weight: 700;
        color: #fff;
        margin-bottom: 10px;
        font-size: 1.1rem;
    }

    .source-container {
        margin-top: 20px;
        padding: 15px;
        background: #1f2029;
        border-radius: 10px;
    }

    .source-link {
        display: block;
        padding: 10px;
        border-left: 4px solid #2196f3;
        margin-bottom: 10px;
        border-radius: 6px;
        background: #262833;
        color: #e8e8e8 !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .source-link:hover {
        background: #30323f;
        transform: translateX(5px);
    }

</style>
""", unsafe_allow_html=True)

def create_event_section(icon, title, content, color="#667eea"):
    """Create a styled section with icon and content"""
    if content and content.strip():
        st.markdown(f"""
        <div class="section">
            <div class="icon-header">
                <i class="{icon}"></i>
                <h4 style="margin:0; color: {color}; font-weight:600;">{title}</h4>
            </div>
            <div class="content-text">{content.replace(chr(10), '<br>')}</div>
        </div>
        """, unsafe_allow_html=True)

def display_event(event, header2):
    """Display event information in a formatted card"""
        
    with header2:
        # Timestamp with dynamic styling
        st.markdown(f"""
        <div class="timestamp">
            <i class="fas fa-clock"></i> {event['zeit']}
        </div>
        """, unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Action section
        create_event_section("fas fa-fire", "Aktion", event['aktion'], "#e74c3c")
        
        # Actors section
        create_event_section("fas fa-users", "Akteure & Einheiten", event['akteure'], "#2ecc71")
        
        # Weapons section
        create_event_section("fas fa-gun", "Waffen & Munition", event['waffen'], "#e67e22")
    
    with col2:
        # Consequences section
        create_event_section("fas fa-chart-line", "Konsequenzen", event['konsequenzen'], "#9b59b6")
        
        # Strategic assessment section
        create_event_section("fas fa-bullseye", "Strategische Bewertung", event['strategische_bewertung'], "#3498db")
    
    # Source section (full width)
    if event['quelle'] and event['quelle'].strip():
        st.markdown(f"""
        <div class="sources">
            <div class="icon-header">
                <i class="fas fa-book"></i>
                <h4 style="margin:0; color: #2196f3; font-weight:600;">Quelle</h4>
            </div>
            <div class="content-text">{event['quelle']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    image, source = st.columns(2)
    
    with image:
        # Image with enhanced styling
        if "picture" in event and event["picture"]:
            print(event["picture"])
            #try:
            st.html('<div class="image-container">')
            print("inside markdown")
            st.image(event["picture"], 
                    caption=f"📸 Szene um {event['zeit']}", 
                    width='content')
            print("after image")
            st.html('<div>')
                
            #except Exception as e:
            #    st.error(f"Fehler beim Laden des Bildes: {e}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with source:
        st.markdown("<div class='source-title'>Quellen & Nachweise (Teilweise Analyse durch NotebookLM)</div>", unsafe_allow_html=True)

        for q in quellen:
            st.markdown(
                f"<a class='source-link' href='{q['link']}' target='_blank'>"
                f"<i class='fa-solid fa-up-right-from-square'></i> {q['name']}"
                "</a>",
                unsafe_allow_html=True
            )



    

if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False
    
if not st.session_state.button_pressed:
    title  = st.title("📜 Britisch-Sansibarischer Krieg (1896) – Preface")
    
    if "preface_index" not in st.session_state:
        st.session_state.preface_index = 0

    col1, col2 = st.columns(2)
    
    with col1:
        st.image(preface_images[st.session_state.preface_index], use_container_width=True)
        
    with col2:
        st.markdown(preface[st.session_state.preface_index])
        
        if st.button("Weiter →"):
            print(st.session_state.preface_index)
            st.session_state.preface_index += 1
        if st.session_state.preface_index == len(preface):
            st.session_state.button_pressed = True
            
        
    
    
        
        
else:
    title = st.title("📜 Britisch-Sansibarischer Krieg (1896) – Interaktive Timeline")
    header1, header2 = st.columns(2)
    with header1:
        st.write("Wähle eine Minute aus, um die Ereignisse dieses Zeitpunkts anzuzeigen.")
    
    
    minute = st.slider("Minute auswählen:", min_value=0, max_value=38, value=0)

    event = anglo_zanzibar_war_timeline[minute]

    display_event(event, header2)

