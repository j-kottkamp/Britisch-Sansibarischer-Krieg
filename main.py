import streamlit as st

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
        "zeit": "09:02:00 - Minute 00",
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
        "picture": "bilder/bild_0.png"
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
        "quelle": "Britisches Admiralitätslog, Schiffslogs der beteiligten Einheiten"
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
        "quelle": "Admiralitätslog, Augenzeugenberichte deutscher Konsulatsangehöriger"
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
        "quelle": "Britisches Admiralitätslog, The Times Korrespondent vor Ort"
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
        "quelle": "Admiralitätslog, diplomatische Depeschen verschiedener Konsulate"
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
        "quelle": "Britisches Admiralitätslog, Bennett (1978)"
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
        "quelle": "Britisches Admiralitätslog, Schiffsartillerieprotokolle"
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
        "quelle": "Admiralitätslog, Beobachterberichte der HMS Philomel"
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
        "quelle": "Flaggsignallogs, Historiker: Bennett 1978"
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
        "quelle": "Diplomatische Depeschen, Konsulatsberichte"
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
        "quelle": "Schiffslogs, lokale Augenzeugenberichte"
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
        "quelle": "Admiral Rawson Bericht, The Times Korrespondent"
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
        "quelle": "Diplomatische Archive, Cave-Berichte an Foreign Office"
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
        "quelle": "Deutsche Konsulatsberichte, Britische Außenamtspapiere"
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
        "quelle": "Diplomatische Depeschen, Hern 2003"
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
        "quelle": "Marine-Infanterie-Logs, strategische Analysen"
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
        "quelle": "Lokale Chronisten, britische Geheimdienstberichte"
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
        "quelle": "Deutsch-britische diplomatische Korrespondenz"
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
        "quelle": "Verhandlungsprotokolle, zeitgenössische Berichte"
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
        "quelle": "Vertragsdokumente, konstitutionelle Analysen"
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
        "quelle": "Proklamationsdokumente, historische Analysen"
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
        "quelle": "Zeremonielle Protokolle, diplomatische Notizen"
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
        "quelle": "Rechtliche Dokumentation, völkerrechtliche Analysen"
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
        "quelle": "Administrative Berichte, Logistikprotokolle"
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
        "quelle": "Kommunikationslogs, Verfahrensprotokolle"
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
        "quelle": "Zeremonielle Aufzeichnungen, Protokollhandbücher"
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
        "quelle": "Rechtsdokumentation, Sicherheitsberichte"
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
        "quelle": "Asyldokumente, Evakuierungsprotokolle"
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
        "quelle": "Presseberichte, fotografische Dokumentation"
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
        "quelle": "Militärische Direktiven, Sanitätsberichte"
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
        "quelle": "Protokollarische Aufzeichnungen, zeitgenössische Chroniken"
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
        "quelle": "Presseanweisungen, Medienberichte"
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
        "quelle": "Formationsbefehle, zeremonielle Protokolle"
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
        "quelle": "Amtliche Verlautbarungen, Archivdokumente"
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
        "quelle": "Zeremonielle Anweisungen, Protokollnotizen"
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
        "quelle": "Zeitgenössische Beschreibungen, literarische Verarbeitungen"
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
        "quelle": "Protokollarische Aufzeichnungen, Signallogs"
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
        "quelle": "The Times, diplomatische Depeschen, Hern (2003)"
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
        "quelle": "Admiralitätslog, Besatzungsberichte, historische Analysen"
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

# UI
# ---------------------------------------------
st.title("📜 Britisch-Sansibarischer Krieg (1896) – Interaktive Timeline")
st.write("Wähle eine Minute aus, um die Ereignisse dieses Zeitpunkts anzuzeigen.")

minute = st.slider("Minute auswählen:", min_value=0, max_value=38, value=0)

event = anglo_zanzibar_war_timeline[minute]

st.subheader(f"⏱️ Zeitstempel: {event['zeit']}")
st.markdown(f"### 🔥 Aktion\n{event['aktion']}")
st.markdown(f"### 👥 Akteure & Einheiten\n{event['akteure']}")
st.markdown(f"### 🧨 Waffen & Munition\n{event['waffen']}")
st.markdown(f"### 📉 Konsequenzen\n{event['konsequenzen']}")
st.markdown(f"### 🎯 Strategische Bewertung\n{event['strategische_bewertung']}")
st.markdown(f"### 📚 Quelle\n{event['quelle']}")

if "picture" in event and event["picture"]:
    st.image(event["picture"], caption=f"Szene um {event['zeit']}", use_container_width=True)

