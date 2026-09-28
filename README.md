# ⚽ Premier League: Financial Efficiency & Performance Analytics (2012–2025)

An interactive, bilingual (English/Spanish) sports analytics dashboard exploring the relationship between transfer market spending and league points return across Premier League clubs.

🔗 **Live Interactive Demo:** [Launch Dashboard](https://premier-league-analytics-xdbfznpahjw2vahhagvavp.streamlit.app/)

---

## 📌 Project Overview

- **Analytical Question:** Does spending more money on player transfers guarantee sporting success in the Premier League?
- **Methodology:** Regression-based benchmarking to estimate expected league points given transfer investments, isolating club efficiency residuals.

### Key Features

- **Dynamic KPI Cards:** Cumulative spend, points average, and financial cost per point.
- **Interactive Quadrants:** Transfer spending vs. league points alongside historical benchmarks.
- **Efficiency Ranking:** Club ranking by net points above or below market expectations.
- **Bilingual Toggle:** Seamless real-time switch between English 🇬🇧 and Spanish 🇪🇸.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas |
| Visualizations | Plotly (Express & Graph Objects) |
| Web Framework | Streamlit |
| Styling & UI | Custom CSS (Premier League Dark Broadcast Theme) |
| Deployment | GitHub & Streamlit Community Cloud |

---

## 💻 Local Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/AndresQuev/Premier-League-Analytics.git
cd Premier-League-Analytics
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
python -m streamlit run app.py
```

---

## 📁 Repository Structure

```text
├── app.py                         # Main Streamlit application
├── powerbi_tabla_principal.csv    # Processed historical dataset
├── requirements.txt               # Python package dependencies
└── README.md                      # Project documentation
```

---

## 👤 Author & Contact

- **Author:** Andrés Quevedo
- **GitHub:** [@AndresQuev](https://github.com/AndresQuev)
