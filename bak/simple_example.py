from figure_separator.figure_separator import FigureSeparator
fig_separator=FigureSeparator("./data/figure-separation-model-submitted-544.pb")
sub_figures=fig_separator.extract("./imgs/PMC4076561-Figure5-1.png")
print(sub_figures)

fig_separator = FigureSeparator("./data/figure-separation-model-submitted-544.pb")
print(fig_separator.extract("./imgs/PMC4076561-Figure5-1.png"))