# IBM Data Science Professional Certificate

Practical notebooks, datasets, code, and reports developed through the **IBM Data Science Professional Certificate** on Coursera. This repository focuses on applying an end-to-end data science workflow, from data acquisition to predictive modeling and communication of results.

## Featured Project: SpaceX Falcon 9 Landing Prediction

**Objective:** Analyze historical SpaceX launch data and predict whether the Falcon 9 first stage will land successfully. The project combines data collection, exploratory analysis, interactive visualization, and supervised machine learning.

## Project Workflow

| Stage | Methods and tools | Deliverable |
| --- | --- | --- |
| Data collection | SpaceX API, Python requests, web scraping | Source notebooks and collected datasets |
| Data preparation | Pandas, missing-value handling, feature preparation | Cleaned datasets |
| Exploratory analysis | SQL, Pandas, Matplotlib, Seaborn | Queries, tables, and visualizations |
| Geospatial analysis | Folium | Interactive launch-site maps |
| Interactive analytics | Plotly Dash | Dashboard with launch-site and payload filters |
| Predictive analysis | Scikit-learn, cross-validation, GridSearchCV | Evaluated classification models |
| Reporting | Technical slides and supporting results | Final PDF presentation |

### Predictive Models

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)

Models are compared using test-set accuracy and confusion matrices. Hyperparameters are selected through cross-validation with `GridSearchCV`.

## Repository Structure

The initial Capstone layout is shown below. Additional labs and final deliverables will be added as they are prepared.

```text
elvenj-ibm-data-science-professional-certificate/
├── README.md
├── LICENSE
├── .gitignore
└── applied-data-science-capstone/
    ├── notebooks/
    │   ├── README.md
    │   └── jupyter-labs-spacex-data-collection-api.ipynb
    └── data/
        └── dataset_part_1.csv
```

Upcoming materials include the web-scraping and data-wrangling labs, SQL and visualization notebooks, Folium maps, a Plotly Dash application, classification results, and the final presentation.

## Technologies

**Python · Jupyter · Pandas · NumPy · SQL · Matplotlib · Seaborn · Folium · Plotly Dash · Scikit-learn · Git**

## Getting Started

```bash
git clone https://github.com/elvenj/elvenj-ibm-data-science-professional-certificate.git
cd elvenj-ibm-data-science-professional-certificate
jupyter notebook
```

Open the notebooks under `applied-data-science-capstone/notebooks/`. Dependencies and data paths may vary across IBM labs; follow each notebook's setup instructions.

## Data Provenance and Reproducibility

The project uses historical SpaceX launch data and educational resources provided or referenced in the IBM Capstone labs. External API availability may change; saved datasets do not, by themselves, establish that a live API request succeeded. Methods and execution results should be interpreted from the corresponding notebooks.

## Project Status

**In progress.** The repository is being organized incrementally. Final metrics, visualizations, and conclusions will be published after the relevant notebook outputs are verified.

## Acknowledgments

[IBM Data Science Professional Certificate — Coursera](https://www.coursera.org/professional-certificates/ibm-data-science)

## License

Original code and documentation are covered by the repository's [MIT License](LICENSE), where applicable. IBM course materials, external datasets, and third-party content retain their respective licenses and attribution requirements.
