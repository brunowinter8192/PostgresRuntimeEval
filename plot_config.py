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

# === SEABORN DEEP PALETTE ===
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

# === LIGHT VARIANTS (für Epsilon) ===
LIGHT_CYAN = "#A3D4E5"
LIGHT_OLIVE = "#E2D4A8"
LIGHT_RED = "#DB9194"
LIGHT_PURPLE = "#B3A8C9"

# === BASE-FARBEN ===
# Histogramme, Scatter, Propagation
PRIMARY_COLOR = DEEP_BLUE
SECONDARY_COLOR = DEEP_ORANGE
ACCENT_COLOR = DEEP_RED

# Depth Propagation
DEPTH_PREDICTED = DEEP_BLUE
DEPTH_ACTUAL = DEEP_ORANGE

# === METHODEN-FARBEN ===
METHOD_COLORS = {
    "Plan_Level": DEEP_GREEN,
    "Operator_Level": DEEP_GREEN,
    "Optimizer": DEEP_GRAY,
    "Hybrid_1_Approach_1": DEEP_GREEN,
    "Hybrid_1_Approach_2": DEEP_GREEN,
    "Hybrid_1_Approach_3": DEEP_GREEN,
    "Hybrid_1_Approach_4": DEEP_GREEN,
}

# === STRATEGIE-FARBEN ===
STRATEGY_COLORS = {
    "Error": DEEP_RED,
    "Frequency": DEEP_PURPLE,
    "Size": DEEP_CYAN,
    "Optimizer": DEEP_GRAY,
    "Hybrid_1": DEEP_GREEN,
}

STRATEGY_COLORS_EPSILON = {
    "Error": LIGHT_RED,
    "Frequency": LIGHT_PURPLE,
    "Size": LIGHT_CYAN,
}
