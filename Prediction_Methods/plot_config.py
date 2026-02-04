# Prediction_Methods/plot_config.py
# Zentrale Plot-Konfiguration für alle Analyse-Scripts

# === BASICS ===
FIGSIZE = (10, 6)
DPI = 300
TITLE_FONTSIZE = 14
LABEL_FONTSIZE = 12
TICK_FONTSIZE = 10

# === MRE BAR PLOT SETTINGS ===
MRE_Y_LIMIT = 1.0  # Y-Achse bei 100% begrenzen
MRE_ANNOTATION_OFFSET = 0.05  # Offset für Annotation über dem Bar (in Y-Einheiten)

# === MULTI-SUBPLOT SETTINGS ===
PLOTS_PER_PAGE = 4  # 2x2 Grid
SUBPLOT_ROWS = 2
SUBPLOT_COLS = 2

# === SEABORN DEEP PALETTE ===
# Kräftige, professionelle Farben
DEEP_BLUE = "#4C72B0"
DEEP_ORANGE = "#DD8452"
DEEP_GREEN = "#55A868"
DEEP_RED = "#C44E52"
DEEP_PURPLE = "#8172B3"
DEEP_BROWN = "#937860"
DEEP_PINK = "#DA8BC3"
DEEP_GRAY = "#8C8C8C"
DEEP_OLIVE = "#CCB974"
DEEP_CYAN = "#64B5CD"

# === STANDARD-FARBEN (für Nicht-MRE-Plots) ===
PRIMARY_COLOR = DEEP_BLUE
SECONDARY_COLOR = DEEP_ORANGE
ACCENT_COLOR = DEEP_RED
NEUTRAL_COLOR = DEEP_BROWN

# === MRE-METHODEN-FARBEN ===
# Kontrast-Paare: Blau+Orange, Grün+Rot, Lila+Olive
METHOD_COLORS = {
    # Baselines (Blau + Orange für Vergleiche)
    "Operator_Level": DEEP_BLUE,
    "Plan_Level_SVM": DEEP_BLUE,       # ML = Blau
    "Plan_Level_RF": DEEP_GREEN,
    "Plan_Level_XGBoost": DEEP_RED,
    "Optimizer": DEEP_ORANGE,           # Optimizer = Orange (Kontrast zu Blau)

    # Hybrid_1 Approaches (Grün, Lila, Cyan, Pink)
    "Hybrid_1_Approach_1": DEEP_GREEN,
    "Hybrid_1_Approach_2": DEEP_PURPLE,
    "Hybrid_1_Approach_3": DEEP_CYAN,
    "Hybrid_1_Approach_4": DEEP_PINK,

    # Hybrid_2 Strategies (Lila + Cyan Familie)
    "Hybrid_2_Size_Baseline": DEEP_PURPLE,
    "Hybrid_2_Size_Epsilon": DEEP_CYAN,
    "Hybrid_2_Frequency_Baseline": DEEP_GREEN,
    "Hybrid_2_Frequency_Epsilon": DEEP_PINK,
    "Hybrid_2_Error_Baseline": DEEP_BLUE,
    "Hybrid_2_Error_Epsilon": DEEP_ORANGE,

    # Online_1 Strategies (Grün, Lila, Cyan)
    "Online_1_Error": DEEP_RED,
    "Online_1_Size": DEEP_GREEN,
    "Online_1_Frequency": DEEP_PURPLE,

    # Dynamic (LOTO)
    "Dynamic_Operator": DEEP_BLUE,
    "Dynamic_Plan": DEEP_GREEN,
    "Dynamic_Hybrid_1": DEEP_PURPLE,
}
