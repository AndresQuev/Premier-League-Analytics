⚽ Premier League: Financial Efficiency & Performance Analytics (2012–2025)
An interactive, bilingual (English / Spanish) sports analytics dashboard exploring the relationship between transfer market expenditure and league points return across Premier League clubs.

🔗 Live Interactive Demo: https://premier-league-analytics-xdbfznpahjw2vahhagvavp.streamlit.app/

PROJECT OVERVIEW

Analytical Question: Does spending more money on player transfers guarantee sporting success in the Premier League?

Methodological Approach: Regression-based benchmarking to estimate expected league points given transfer investments, isolating club efficiency residuals.

Key Visualizations:

Dynamic KPI cards: Cumulative transfer investment, league points average, and financial cost per point.

Analytical Scatter Quadrant plotting transfer expenditure vs. league points alongside historical league averages.

Net sporting efficiency ranking by club (points above or below market baseline).

Interactive language toggle (English 🇬🇧 / Español 🇪🇸).

TECH STACK

Core Language: Python

Data Processing & Transformation: Pandas

Interactive Data Visualization: Plotly (Express & Graph Objects)

Web Application & Dashboarding: Streamlit

UI / Styling: Custom CSS (Premier League Dark Broadcast Theme)

Version Control & Deployment: Git, GitHub, Streamlit Community Cloud

LOCAL SETUP & INSTALLATION

Step 1: Clone the repository
git clone https://github.com/AndresQuev/Premier-League-Analytics.git
cd Premier-League-Analytics

Step 2: Install required dependencies
pip install -r requirements.txt

Step 3: Run the application
python -m streamlit run app.py

REPOSITORY STRUCTURE

app.py                      -> Main Streamlit interactive application code

powerbi_tabla_principal.csv -> Processed historical transfer & performance dataset

requirements.txt            -> Environment dependencies for execution

README.md                   -> Project documentation and overview

AUTHOR & CONTACT

Author: Andrés Quevedo

GitHub: https://github.com/AndresQuev

Project: Premier League Transfer Efficiency Analytics Hub
