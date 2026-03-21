# TidyData-Project

This project applies tidy data principles to the dataset: "Mutant Moneyball" — X-Men comic card resale values across four decades (1960s–1990s) and four markets (Heritage, eBay, Wizard, and oStreet). The raw wide-format data is reshaped into a tidy long-format dataset, then explored with a pivot table and visualizations.

Tidy data rules: each variable in its own column, each observation its own row, each observational unit its own table.

## How to Run

by installing jupyter then load:
jupyter notebok tidydata_analysis.ipynb

Place mutant_moneyball.csv in the same folder (.csv file available in the TidyData-Project folder in GitHub repository), then run all cells.

## Dataset Overview

Source: [Mutant Moneyball on GitHub](https://github.com/EliCash82/mutantmoneyball). One row per X-Men member, columns named TotalValue{Decade}s_{Market}. Through cleaning: melted data from wide to long form, split column names into Decade and Market, cleaned "$" and "," from monetary strings, dropped rows with no recorded sale.

## Visualizations

- Chart 1: Top 10 mutants by total card value (horizontal bar chart)
![Total X-Men Card Value by Decade and Market](viz1_value_by_decade_market(1).png)
- Chart 2: Total card value by decade and market (grouped bar chart)
![Top 10 X-Men by Total Card Value](viz2_top10_mutants(1).png)

## References

Wickham, H. (2014). Tidy Data. https://www.jstatsoft.org/article/view/v059i10
Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf








# TidyData-Project

Applies tidy data principles to the *Mutant Moneyball* dataset — X-Men comic card resale values across four decades (1960s–1990s) and four markets (Heritage, eBay, Wizard, oStreet). The raw wide-format data is reshaped into a tidy long-format dataset, then explored with pivot tables and visualizations.

**Tidy data rules (Wickham, 2014):** each variable in its own column, each observation its own row, each observational unit its own table.

---

## How to Run

```bash
pip install pandas matplotlib numpy jupyter
jupyter notebook tidy_data_notebook.ipynb
```

Place `mutant_moneyball.csv` in the same folder, then run all cells (`Kernel > Restart & Run All`).

---

## Dataset

Source: [Mutant Moneyball on GitHub](https://github.com/EliCash82/mutantmoneyball). One row per X-Men member, columns named `TotalValue{Decade}s_{Market}`. Pre-processing: melted wide→long, split column names into `Decade` and `Market`, cleaned `$`/`,` from monetary strings, dropped rows with no recorded sale.

---

## Visualizations

**Total card value by decade and market:**

![Total X-Men Card Value by Decade and Market](viz1_value_by_decade_market(1).png)

**Top 10 mutants by total card value:**

![Top 10 X-Men by Total Card Value](viz2_top10_mutants(1).png)

---

## References

- Wickham, H. (2014). *Tidy Data*. https://www.jstatsoft.org/article/view/v059i10
- Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
