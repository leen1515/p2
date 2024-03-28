
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def display_null_percentage(null_percentage_df):

    null_percentage_df_sorted = null_percentage_df.sort_values(by="Percentage of null values")

    num_colors = len(null_percentage_df_sorted)
    colors_list = plt.cm.viridis(np.linspace(0, 1, num_colors))
    
    plt.figure(figsize=(20, 8))
    barplot = sns.barplot(
        x="Columns",
        y="Percentage of null values",
        data=null_percentage_df_sorted,
        palette=colors_list,
    )

    plt.ylabel("Percentage of null values")
    plt.xlabel("Variables")
    plt.title("null values presence")
    plt.xticks(rotation=60, ha="right")

    for p in barplot.patches:
        barplot.annotate(
            format(
                p.get_height(), ".1f"
            ),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center", 
            xytext=(0, 10),
            textcoords="offset points",
        )

    plt.show()