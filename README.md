# Olympic-History
An analysis of the last 120 Years of the Olympics. This project will explore the most medals per country. In addition, the project dives into the mean age of Olympians from 1998-2016. The project also explores the top populated countries. Furthermore, Seaborn/Matplotlib is used to visualize this analyzation. 

## Data Sources
- https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results 
- https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset 

## Definitions
- ID - Unique number for each athlete
- Name - Athlete's name 
- Sex - M or F
- Age - Integer
- Height - In centimeters
- Team - Team name
- NOC - National Olympic Committee 3-letter country code
- Games - Year and season
- Year - Integer
- Season - Summer or Winter
- City - Host city
- Sport - Sport
- Event - Event
- Medal - Gold, Silver, Bronze, or NA
- Rank: Rank by Population
- CCA3: 3 Digit Country/Territories Code
- Country/Territories: Name of the Country/Territories
- Capital: Name of the Capital
- Continent: Name of the Continent
- 2022 Population: Population of the Country/Territories in the year 2022
- 2020 Population: Population of the Country/Territories in the year 2020
- 2015 Population: Population of the Country/Territories in the year 2015
- 2010 Population: Population of the Country/Territories in the year 2010
- 2000 Population: Population of the Country/Territories in the year 2000
- 1990 Population: Population of the Country/Territories in the year 1990
- 1980 Population: Population of the Country/Territories in the year 1980
- 1970 Population: Population of the Country/Territories in the year 1970
- Area (km²): Area size of the Country/Territories in square kilometer
- Density (per km²): Population Density per square kilometer
- Growth Rate: Population Growth Rate by Country/Territories
- World Population Percentage: The population percentage by each Country/Territories


## Requirements

- Python 3.11.1
- Jupyter
- Pandas
- Numpy
- Matplotlib
- Seaborn

## Instructions
- Python file 'clean.py' 
    - Run command 'python clean.py' in command line
- Jupyter notebook file 'analyze.ipynb' run all cells 

## Challenges (Requirements)

-	Read Two data files (CSV)
-	Cleaned data and performed a pandas merge with 2 data sets, calculated new values based on new data set
-	3 seaborn/matplotlib visualizations
-	Virtual Environment:
    - Python -m venv venv
    - cd venv
    - cd Scripts
    - . activate
-	Markdown cells in Jupyter Notebook

