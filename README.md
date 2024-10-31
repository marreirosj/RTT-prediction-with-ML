# RTT prediction with ML
 
## Description

Developed to predict Remaining Time to Travel (RTT) and, based on it, Estimated Time of Arrival (ETA) for ships to a maritime port, using AIS receiver data from the port (short-distance prediction).


![Pipeline] (./Extras/pipeline.png)


## Requirements
* <a href= "https://www.python.org/"> Python 3.11.1 </a>
* <a href= "https://scikit-learn.org/stable/index.html"> Scikit-learn 1.2.1 </a>
* <a href= "https://pandas.pydata.org/"> Pandas 2.2.2 </a>
* <a href= "https://numpy.org/"> Numpy 1.26.4 </a>
* <a href= "https://matplotlib.org//"> Matlotlib </a>
* <a href= "https://seaborn.pydata.org/"> Seaborn </a>
* <a href= "https://pypi.org/project/folium/"> Folium </a>
* <a href= "https://pypi.org/project/geopandas/"> Geopandas </a>
* <a href= "https://pypi.org/project/Cartopy/"> Cartopy </a>
* <a href= "https://docs.python.org/3/library/math.html"> Math </a>

## Premises
* At least one '.txt' zipped file from AIS receiver
* If the files are unzipped and in '.csv' format script 'unzip_to_csv' not needed
* Original data (used in this work) is not available due to confidentiality issues
* After loading and first cleaning, appearence should have the follpwing features:
![Pipeline] (./Extras/head1.png)

## Installation
```bash
# Download the project
wget

## Usage

*** 2 scripts:
* 'unzip_to_csv' will unzip files and put them on csv folders. Because of harware issues, this script was adapted to automatically make some changes on data, as eliminating unnecessary columns (based on literature review) or selecting ships from type 70 (container cargos). It alsio use the chunksize parameter in order to deal with the large ammount of data in each dataset.
* 'splitted_csv' to split the data into several '.csv' files, each one with one 'ShipVoyage' representing one single voyage of one specific ship (order by MMSI number)

*** '.csv' in use:
* zipped '.txt' files goes to the 'Raw_Data' folder
* unzipped '.txt' files goes to the 'Unzipped' folder
* zipped '.txt' files goes to the 'Raw_Data' folder
*** Inside 'CSV' folder: 
* data after first cleaning is compilled in '.csv' nammed 'filtered_dataset'
* data after complete cleaning is compilled in '.csv' nammed 'cleaned_dataset'
* data after splitted into 'ShipVoyage' feature is saved in 'voyages_splitted' folder
* data after voyage selection is divided between 'voyage_reached' and 'voyages_out' folders
* data from outliers is saved in 'voyage_outliers' folder
* final data after handling is saved in 'voyages_final' folder
* correlation matrix is saved

*** Inside 'Plots' folder:
* 'finished_voyages' folder contains plots of all finished voyages (reached the port)
* inside 'finished_voyages' a folder named 'eliminated' contains finished voyages that were eliminated for some reason
* 'unfinished_voyages' folder contains plots of all unfinished voyages (didn't reached the port)
* 'Outliers' contains plots of outliers voyage that were removed

*** 4 codes
* 'RTT_&_ETA_predict' contains all the loading of data, data handling, EDA and feature engineering
* 'ETA_predict_KNN' contains ML model using K-nearest neighbors algorithm
* 'ETA_predict_MLP' contains ML model using Multilayer Perceptron neural network
* 'ETA_predict_KNN' contains ML model using Random Forest Regression technique

## Credits
<p> <a href= "https://github.com/marreirosj"> João Marreiros </a> </p>

## License
GPLv3
