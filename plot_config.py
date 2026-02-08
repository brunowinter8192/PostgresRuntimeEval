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
LIGHT_GREEN = "#99CBA4"

# === BAR PLOT (single) ===
BAR_FIGSIZE = (16, 8)
BAR_WIDTH = 0.5
BAR_ALPHA = 0.8
BAR_EDGECOLOR = 'none'
BAR_LINEWIDTH = 0.8
BAR_LABEL_FONTSIZE = 9

# === BAR PLOT (grouped) ===
GROUPED_BAR_FIGSIZE = (16, 8)
GROUPED_BAR_WIDTH = 0.35
GROUPED_BAR_ALPHA = 0.85
GROUPED_BAR_EDGECOLOR = 'none'
GROUPED_BAR_LINEWIDTH = 0.8
GROUPED_BAR_LABEL_FONTSIZE = 7

# === SCATTER PLOT ===
SCATTER_FIGSIZE = (12, 10)
SCATTER_MARKER_SIZE = 10
SCATTER_ALPHA = 0.5

# === HISTOGRAM ===
HIST_FIGSIZE = (12, 10)
HIST_BINS = 15
HIST_ALPHA = 0.8
HIST_EDGECOLOR = 'black'

# === GRID (alle Plot-Typen) ===
GRID_AXIS = 'y'
GRID_ALPHA = 0.3
GRID_LINESTYLE = '--'

# === Y-AXIS MARGIN ===
BAR_TOP_MARGIN_CM = 1.5  # Fester physischer Abstand oben (alle Bar-Plots)

# === Y-AXIS SCALES (User-definiert pro Plot-Kontext) ===
# Scale und Step werden vom User individuell vorgegeben.
# Plan_Level_1
PLAN_LEVEL_MRE_Y_SCALE = 50       # A_01g: MRE in %
PLAN_LEVEL_MRE_Y_STEP = 10        # Ticks: 0, 10, 20, 30, 40, 50
PLAN_LEVEL_RUNTIME_Y_SCALE = 3500  # A_01h: Runtime in ms
PLAN_LEVEL_RUNTIME_Y_STEP = 500   # Ticks: 0, 500, ..., 3500
PLAN_LEVEL_COMPARE_Y_SCALE = 50   # A_01i: Vergleichs-MRE in %
PLAN_LEVEL_COMPARE_Y_STEP = 10    # Ticks: 0, 10, 20, 30, 40, 50
# Operator_Level
OPERATOR_LEVEL_MRE_Y_SCALE = 50       # A_01f: MRE in %
OPERATOR_LEVEL_MRE_Y_STEP = 10        # Ticks: 0, 10, 20, 30, 40, 50
OPERATOR_LEVEL_COMPARE_Y_SCALE = 50   # A_01h: Vergleichs-MRE in %
OPERATOR_LEVEL_COMPARE_Y_STEP = 10    # Ticks: 0, 10, 20, 30, 40, 50
# Hybrid_1
HYBRID_1_MRE_Y_SCALE = 50            # A_01a: MRE in %
HYBRID_1_MRE_Y_STEP = 10             # Ticks: 0, 10, 20, 30, 40, 50

# === CAP/OVERFLOW ===
CAP_OVERFLOW_COLOR = DEEP_RED
# Welche Overflow-Labels nach unten verschoben werden entscheidet der User dynamisch.
# Fester Abstand zwischen Legende-Unterkante und verschobenem Label:
CAP_LABEL_GAP_CM = 0.5

# === BASE-FARBEN ===
# Alle Plots die NICHT MRE-Template-Plots sind (Runtime, Histogramme, Scatter, Propagation)
PRIMARY_COLOR = DEEP_BLUE
SECONDARY_COLOR = DEEP_ORANGE
ACCENT_COLOR = DEEP_RED

# Depth Propagation
DEPTH_PREDICTED = DEEP_BLUE
DEPTH_ACTUAL = DEEP_ORANGE

# === METHODEN-FARBEN (nur MRE-Template-Plots) ===
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


# === HILFSFUNKTIONEN ===

# Festen physischen Top-Margin (BAR_TOP_MARGIN_CM) auf Y-Achse anwenden
def apply_top_margin(ax, fig, y_scale: float, y_step: float = None) -> None:
    fig.canvas.draw()
    ax_height_inches = fig.get_size_inches()[1] * ax.get_position().height
    margin_inches = BAR_TOP_MARGIN_CM / 2.54
    margin_data = y_scale * (margin_inches / (ax_height_inches - margin_inches))
    ax.set_ylim(0, y_scale + margin_data)
    if y_step:
        ax.set_yticks(range(0, int(y_scale) + 1, int(y_step)))
