# Tidy Data Project

This project applies tidy data principles to the dataset: "Mutant Moneyball" - X-Men comic card resale values across four decades (1960s–1990s) and four markets (Heritage, eBay, Wizard, and oStreet). The raw wide-format data is reshaped into a tidy long-format dataset, then explored with a pivot table and visualizations.

Tidy data rules: each variable in its own column, each observation its own row, each observational unit its own table.

---

## How to Run

- Install `Jupyter`, then load: `jupyter notebook tidydata_analysis.ipynb`

- Place mutant_moneyball.csv in the same folder (.csv file available in the TidyData-Project folder in GitHub repository), then run all cells.

---

## Libraries Included

- `matplotlib`
- `matplitlib.pyplot`
- `matplotlib.ticker`
- `pandas`
- `numpy`

---

## Dataset Overview

Source: [Mutant Moneyball on GitHub](https://github.com/EliCash82/mutantmoneyball). One row per X-Men member, columns named TotalValue{Decade}s_{Market}. Through cleaning: melted data from wide to long form, split column names into Decade and Market, cleaned "$" and "," from monetary strings, and dropped rows with no recorded sale.

---

## Visualizations

- Chart 1: Top 10 mutants by total card value (horizontal bar chart)
![viz1_value_by_decade_market (1)](https://github.com/user-attachments/assets/2514d122-8e89-4868-bf29-affaa9e4369c)

- Chart 2: Total card value by decade and market (grouped bar chart)
<img width="1321" height="681" alt="Screenshot 2026-03-20 223224" src="https://github.com/user-attachments/assets/097d7a5a-d655-4354-b153-1f890dae448c" />

---

## References

- Wickham, H. (2014). Tidy Data. https://www.jstatsoft.org/article/view/v059i10
- Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
