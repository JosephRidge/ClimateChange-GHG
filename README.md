# ClimateChange-GHG
Climate change is one of the most pressing issues facing our planet today. It is caused by the release of greenhouse gases into the atmosphere, which trap heat and cause the planet to warm. 
This warming is having a number of devastating effects on the environment, including rising sea levels, more extreme weather events, and the loss of biodiversity.

> # How to Contribute/ Getting Started
    - Navigate to your local machine
    - Create a folder under Documents
    - Call it DataScience 
    - Right Click on it and click "open with termninal" or "open with cmd"
    - it will launch a terminal window with the folder as the path
    - run a ```git clone https://github.com/JosephRidge/ClimateChange-GHG.git``` 
    - It should clone the whole repository to your local machine 
    - Launch VSCode or whatever editor your are using 
    - check for the current version control branch you are on and swicth to develop
    - Remember do not work on the main branch (this is very important)
    - Next Create a branch and name it using this approach: feature-{nameOfWhatYouAreBuilding} eg if you are working on data visualization you will name your branch as **feature-data-visualization**
    - Build your module or write your code and push to your current branch that should be named as previous step
    - Create a pull request to merge to develop
    - One of the team member will review and merge to develop
    - I will merge to main



## Methodology ( [CRISP-DM](https://www.sv-europe.com/crisp-dm-methodology/) )
> ###  Data Collection (CRISP-DM: Business Understanding):
Utilize the provided sources to gather relevant data on greenhouse gas emissions, sea level rise, and forest coverage. Understand the business objectives and requirements related to climate change analysis and identify the data sources necessary to address these objectives.
Data Preprocessing (CRISP-DM: Data Understanding & Data Preparation):

> ###  Clean and prepare the collected data
Addressing missing values, outliers, and inconsistencies. This step ensures the data's quality before analysis. Understand the structure and quality of the data through exploration and prepare it for further analysis.
Exploratory Data Analysis (EDA) (CRISP-DM: Data Understanding):

> ###  Conduct EDA
To understand data distributions, identify patterns, and explore relationships between variables. Visualization techniques can aid in gaining insights from the data. Explore the data to understand its characteristics and relationships between variables, which will inform subsequent analyses.
Predictive Modeling (CRISP-DM: Modeling):

> ###  Develop machine learning models
To predict future trends or outcomes based on historical data. For example, you can use regression models to predict future greenhouse gas emissions or sea level rise. Build predictive models using appropriate algorithms and techniques to forecast climate change indicators based on historical data patterns.
Statistical Analysis (CRISP-DM: Evaluation):

> ###  Apply statistical methods to identify significant relationships and trends in the data. 
This can involve correlation analysis, hypothesis testing, and regression analysis to understand the impact of different factors on climate change indicators. Evaluate the performance of predictive models and assess the significance of relationships between variables using statistical techniques.
Recommendation Generation (CRISP-DM: Deployment):

> ###  Generate recommendations for addressing climate change.
 These recommendations can be tailored to various stakeholders, such as policymakers, businesses, and individuals, emphasizing actions to reduce greenhouse gas emissions, mitigate sea level rise impacts, and preserve forest ecosystems. Deploy the findings and recommendations to stakeholders for informed decision-making and action.

# Data Sources

## 1.GHG Emisssons
-[National contributions to climate change due to historical emissions of carbon dioxide, methane and nitrous oxide](https://zenodo.org/records/7636699#.ZFCy4exBweZ)

Jones et al. – National contributions to climate change
National contributions to climate change due to historical emissions of carbon dioxide, methane and nitrous oxide.
This dataset describes the global warming response to national emissions CO₂, CH₄ and N₂O from fossil and land use sources during 1851-2021.
National CO₂ emissions data are collated from the Global Carbon Project (Andrew and Peters, 2022; Friedlingstein et al., 2022).
National CH₄ and N₂O emissions data are collated from PRIMAP-hist (HISTTP) (Gütschow et al., 2022).

A time series of cumulative CO₂-equivalent emissions is constructed for each country, gas, and emissions source (fossil or land use). Emissions of CH₄ and N₂O emissions are related to cumulative CO₂-equivalent emissions using the Global Warming Potential (GWP*) approach, with best-estimates of the coefficients taken from the IPCC AR6 (Forster et al., 2021).

Warming in response to cumulative CO₂-equivalent emissions is estimated using the transient climate response to cumulative carbon emissions (TCRE) approach, with best-estimate value of TCRE taken from the IPCC AR6 (Forster et al., 2021, Canadell et al., 2021). 'Warming' is specifically the change in global mean surface temperature (GMST).

The data files provide emissions, cumulative emissions and the GMST response by country, gas (CO₂, CH₄, N₂O or 3-GHG total) and source (fossil emissions, land use emissions or the total).

>        Jones, Matthew W., Peters, Glen P., Gasser, Thomas, Andrew, Robbie M., Schwingshackl, Clemens, Gütschow, Johannes, Houghton, Richard A., Friedlingstein, Pierre, Pongratz, Julia, & Le Quéré, Corinne. (2023). National contributions to climate change due to historical emissions of carbon dioxide, methane and nitrous oxide [Data set]. In Scientific Data (2023.1). Zenodo.

## Forest Cover 
[globalforestwatch](https://www.globalforestwatch.org/dashboards/country/KEN/?map=eyJjYW5Cb3VuZCI6dHJ1ZX0%3D)


## Sea Level Data
[Kenya Marine and Fisheries Research Institute](https://www.kmfri.go.ke/index.php?id=10)

### Extra Sources 
- [Targeting GHG Emissiona](https://www.epa.gov/ghgemissions/global-greenhouse-gas-emissions-data)
- [Sea Level Rise](https://www.climate.gov/news-features/understanding-climate/climate-change-global-sea-level)
- [Forest Coverage](https://www.researchgate.net/figure/Forest-coverage-of-land-area-Data-source-World-Bank-55_fig3_329132267)


# Thanks, be awesome, be kindl!