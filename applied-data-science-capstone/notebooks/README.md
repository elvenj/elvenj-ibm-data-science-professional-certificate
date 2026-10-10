# SpaceX Falcon 9 capstone notebooks

## Purpose

Explore historical launches and evaluate whether launch attributes help predict Falcon 9 first-stage landing outcomes. These notebooks support the IBM Applied Data Science Capstone, whose final presentation received **15/15 (100%)**.

## Workflow

The laboratory sequence covers data collection, preparation, SQL and visual exploration, interactive mapping and classification. Prepared IBM CSV files provide the analytical inputs when a saved collection exercise cannot complete.

## Notebook index

| Stage | Notebook | Main task |
| --- | --- | --- |
| API collection | [SpaceX API](jupyter-labs-spacex-data-collection-api.ipynb) | Normalize launch JSON and retrieve metadata. |
| Web scraping | [Wikipedia tables](jupyter-labs-webscraping.ipynb) | Extract launch records from HTML tables. |
| Wrangling | [Data preparation](labs-jupyter-spacex-Data%20wrangling.ipynb) | Inspect missing values and define landing-outcome labels. |
| Visual EDA | [EDA and visualization](edadataviz.ipynb) | Compare launch sites, payloads, orbits and annual success rates. |
| SQL EDA | [SQLite analysis](jupyter-labs-eda-sql-coursera_sqllite.ipynb) | Query customers, payloads, boosters, dates and outcomes. |
| Geospatial analysis | [Folium map](lab_jupyter_launch_site_location.ipynb) | Locate launch sites and explore proximity and outcomes. |
| Classification | [Machine learning prediction](SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb) | Tune Logistic Regression, SVM, Decision Tree and KNN. |

The original IBM filenames and saved outputs are preserved. The interactive dashboard is a separate [Python application](../dashboard/spacex-dash-app.py).

## Inputs

| Input | Use |
| --- | --- |
| [dataset_part_1.csv](../data/dataset_part_1.csv) | Prepared launch attributes. |
| [dataset_part_2.csv](../data/dataset_part_2.csv) | 90 labeled launches for EDA and classification. |
| [dataset_part_3.csv](../data/dataset_part_3.csv) | 80 encoded predictors for the 90 launches. |
| [spacex_launch_dash.csv](../data/spacex_launch_dash.csv) | 56 launches for dashboard comparisons. |
| [spacex_web_scraped.csv](../data/spacex_web_scraped.csv) | Saved scraping export, with no data rows. |

The SQL notebook uses the IBM 101-record launch dataset. Maps in the presentation use the IBM 56-record geospatial dataset. Source links and cohort definitions appear in the report.

## Execution notes

- **API:** The saved notebook contains live-metadata endpoint errors. The prepared 90-record CSV supports the subsequent analyses.
- **Scraping:** An extraction error interrupts the saved run. Its empty CSV is excluded from reported results.
- **Folium:** Original task cells remain unfinished and map outputs are not saved in the notebook. The presentation maps were reproduced separately from the course geospatial dataset.
- **Modeling:** The saved workflow fits preprocessing before splitting the data. Cross-validation with preprocessing inside a pipeline and a chronological test are recommended for further evaluation.

The assignment grade describes the final presentation assessment. These notes describe the saved notebook executions and the limits of reproducing them.

## Deliverables

- [Final presentation, PDF](../presentation/Data_Science_Capstone_Project_Report.pdf)
- [Editable PowerPoint](../presentation/Data_Science_Capstone_Project_Report.pptx)
- [Grading feedback, 100%](../presentation/1791646837589_Data_Science_Capstone_Project_Report_feedback.pdf)
- [Coursera completion certificate, PDF](../../certificates/IBM_Data_Science_Professional_Certificate_A0RHXCNNKOOF.pdf)
- [Verify the Coursera certificate](https://www.coursera.org/verify/professional-cert/A0RHXCNNKOOF)
- [IBM Data Science Professional Certificate (V3), Credly badge](https://www.credly.com/badges/199c233f-e1c2-4b45-a649-5ebaaf39ff46/public_url)

[Back to the repository overview](../../README.md)
