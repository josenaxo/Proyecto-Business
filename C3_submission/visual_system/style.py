"""Shared visual rules of the project (C3). Every final chart imports this file.

Rules (see also README, section "Visual system"):
  colour : blue = logistic regression model | grey = reference rule, neutral context, share ramps | amber = highlight only
  cues   : the reference rule is hatched; every value is printed; shapes mark feature type (circle numeric, diamond category)
  text   : title = finding (bold 14), subtitle = population + period + unit (9.5 grey), source line (8.5 grey, bottom-left)
  scales : scores 0-1 from zero (never truncated); shares 0-100% with the same scale in every panel; ratios on a log scale centred on 1
"""
import textwrap
import matplotlib.pyplot as plt

C_MODEL = "#1F5FA8"   # logistic regression (our model)
C_REF = "#8C8C8C"     # reference rule / neutral context
C_ALERT = "#D9822B"   # highlight only: differences, errors, dominant factor
C_INK = "#222222"
C_GRID = "#DDDDDD"
HATCH_REF = "///"
CONTEXT = ("Test set, 1,192 people (204 persistent), decision date 1 Sep 2025, "
           "predicting Sep 2025 - Aug 2026")


def apply():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": C_INK,
        "axes.labelcolor": C_INK, "text.color": C_INK, "xtick.color": C_INK,
        "ytick.color": C_INK, "axes.spines.top": False, "axes.spines.right": False,
        "figure.dpi": 130,
    })


def heading(fig, title, subtitle, width_title=70, width_sub=105, top=0.97):
    """Figure-level title (the finding) + subtitle (population, period, unit). Returns y where the plot may start."""
    t = textwrap.fill(title, width_title)
    sub = textwrap.fill(subtitle, width_sub)
    nt, ns = t.count(chr(10)) + 1, sub.count(chr(10)) + 1
    fig.text(0.01, top, t, fontsize=14, fontweight="bold", ha="left", va="top")
    fig.text(0.01, top - 0.055 * nt, sub, fontsize=9.5, color="#555555", ha="left", va="top")
    return top - 0.055 * nt - 0.04 * ns


def source(fig, text="Source: Group 01, C2 classification notebook (test set)."):
    fig.text(0.01, 0.005, text, fontsize=8.5, color="#555555", ha="left", va="bottom")
