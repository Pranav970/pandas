# Reproducible Example
import pandas as pd

pd.crosstab(
    index=["index1","index2"],
    columns=  ["one", "one"],
    values=[12,10],
    normalize=1,
    margins=True,
    dropna=True,
    aggfunc='skew'
)
