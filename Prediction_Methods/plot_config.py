# Prediction_Methods/plot_config.py
# Zentrale Plot-Konfiguration für alle Analyse-Scripts

# === BASICS ===
FIGSIZE = (10, 6)
DPI = 300
TITLE_FONTSIZE = 14
LABEL_FONTSIZE = 12
TICK_FONTSIZE = 10

# === MRE BAR PLOT SETTINGS ===
MRE_Y_LIMIT = 1.0
MRE_ANNOTATION_OFFSET = 0.05

# === MULTI-SUBPLOT SETTINGS ===
PLOTS_PER_PAGE = 4
SUBPLOT_ROWS = 2
SUBPLOT_COLS = 2

# === TAB20 PALETTE ===
TAB20_BLUE = "#1f77b4"
TAB20_BLUE_LIGHT = "#aec7e8"
TAB20_ORANGE = "#ff7f0e"
TAB20_ORANGE_LIGHT = "#ffbb78"
TAB20_GREEN = "#2ca02c"
TAB20_GREEN_LIGHT = "#98df8a"
TAB20_RED = "#d62728"
TAB20_RED_LIGHT = "#ff9896"
TAB20_PURPLE = "#9467bd"
TAB20_PURPLE_LIGHT = "#c5b0d5"
TAB20_BROWN = "#8c564b"
TAB20_BROWN_LIGHT = "#c49c94"
TAB20_PINK = "#e377c2"
TAB20_PINK_LIGHT = "#f7b6d2"
TAB20_GRAY = "#7f7f7f"
TAB20_GRAY_LIGHT = "#c7c7c7"
TAB20_OLIVE = "#bcbd22"
TAB20_OLIVE_LIGHT = "#dbdb8d"
TAB20_CYAN = "#17becf"
TAB20_CYAN_LIGHT = "#9edae5"

# === TAB20B PALETTE (für Hybrid_2 Strategien) ===
TAB20B_BLUE = "#393b79"
TAB20B_BLUE_LIGHT = "#6b6ecf"
TAB20B_OLIVE = "#637939"
TAB20B_OLIVE_LIGHT = "#b5cf6b"
TAB20B_RED = "#843c39"
TAB20B_RED_LIGHT = "#d6616b"

# === BASE-FARBEN ===
# Allgemeine Plots (Histogramme, Scatter, Runtime-Bars)
PRIMARY_COLOR = TAB20_BLUE
SECONDARY_COLOR = TAB20_ORANGE
ACCENT_COLOR = TAB20_RED
NEUTRAL_COLOR = TAB20_GRAY

# Depth Propagation
DEPTH_PREDICTED = TAB20_BLUE
DEPTH_ACTUAL = TAB20_ORANGE

# === METHODEN-FARBEN ===
METHOD_COLORS = {
    "Plan_Level": TAB20_GREEN,
    "Plan_Level_SVM": TAB20_GREEN,
    "Optimizer": TAB20_GRAY,
    "Operator_Level": TAB20_PURPLE,
    "Operator_Level_Optimizer": TAB20_BROWN,
    "Hybrid_1_Approach_1": TAB20_RED,
    "Hybrid_1_Approach_2": TAB20_PINK,
    "Hybrid_1_Approach_3": TAB20_CYAN,
}

# === STRATEGIE-FARBEN (Hybrid_2) ===
STRATEGY_COLORS = {
    "Size": TAB20B_BLUE,
    "Size_Epsilon": TAB20B_BLUE_LIGHT,
    "Frequency": TAB20B_OLIVE,
    "Frequency_Epsilon": TAB20B_OLIVE_LIGHT,
    "Error": TAB20B_RED,
    "Error_Epsilon": TAB20B_RED_LIGHT,
    "Optimizer": TAB20_BROWN,
}
