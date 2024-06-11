# %% [markdown]
## Introduction
#  -------------------------------------

# Species Distribution Models (SDMs) are ecological tools used to predict the probability of species occurrence based on specific environmental conditions. These models analyze geographic and environmental data of where species have been found to predict the potential distribution range of species. SDMs are very popular in quantitative ecology and constitute the most widely used modeling framework for projecting potential future range shifts of species in global change impact assessments.

# The inputs for SDMs typically include geo-referenced biodiversity observation data (e.g., individual locations, presence of species, species counts, species richness; the response or dependent variable) and geographic layers of environmental information (e.g., climate, land cover, soil attributes; the predictor or independent variables). Such information is now widely available in digital formats. For example, online repositories provide data on species distributions (e.g., GBIF and OBIS), individual animal locations (e.g., Movebank), climate data (e.g., WorldClim and CHELSA), as well as land cover and other remote sensing products (e.g., Copernicus).

# The goal of SDMs is relate biodiversity observations at specific sites to the prevailing environmental conditions at those sites, which can be achieved using various statistical and machine learning algorithms. Once the biodiversity-environment relationship is estimated, predictions can be made in space and time by projecting the model onto available environmental layers

# *References*:
> https://damariszurell.github.io/SDM-Intro/

# %%

import pandas as pd
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# %%
# 假设你已经有了一个包含物种出现数据的地理空间数据集
# 这个数据集至少包含两列：物种是否存在（1表示存在，0表示不存在）和地理坐标

# 加载数据集
# data = gpd.read_file('path_to_your_species_data.shp')

# 为了示例，我们创建一个假的数据集
# 假设我们有两个环境变量：温度和降水，以及物种出现的数据
data = pd.DataFrame({
    'species_presence': [1, 0, 1, 0, 1],  # 物种出现（1）或不存在（0）
    'temperature': [22, 15, 30, 18, 25],  # 温度
    'precipitation': [1200, 800, 1500, 900, 1300]  # 降水量
})

# %%
from shapely import Point
# 将数据转换为GeoDataFrame，这里我们使用假的坐标
data['geometry'] = pd.Series([
    Point(-97.73, 30.27),
    Point(-97.74, 30.29),
    Point(-97.72, 30.28),
    Point(-97.75, 30.26),
    Point(-97.76, 30.30),
], index=data.index)

# %%
gdf = gpd.GeoDataFrame(data, geometry='geometry')

# %%
