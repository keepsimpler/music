# %% [markdown]
## AI and SDM
### Introduce Species Distribution Model
#  -------------------------------------
'''
物种分布模型（Species Distribution Models，简称SDMs）是一种用于预测物种在特定环境条件下出现概率的生态学工具。这些模型通过分析物种出现地点的地理和环境数据，来预测物种的潜在分布范围。
物种分布模型在定量生态学中非常流行，并且是全球变化影响评估中用于预测物种潜在范围变化的最广泛使用的建模框架。

物种分布模型的输入通常包括地理参考的生物多样性观测数据（例如个体位置、物种存在、物种计数、物种丰富度；响应或因变量）和环境信息的地理图层（例如气候、土地覆盖、土壤属性；预测或自变量）。这些信息现在广泛以数字化格式提供。例如，在线存储库提供有关物种分布的数据（例如GBIF和OBIS）、有关单个动物位置的数据（例如Movebank）、有关气候的数据（例如WorldClim和CHELSA）以及土地覆盖和其他遥感产品的数据（例如Copernicus）。

物种分布模型的目的是将特定地点的生物多样性观测与这些地点的特定环境条件联系起来，可以使用不同的统计和机器学习算法来实现这一点。一旦估计了生物多样性-环境关系，我们可以通过将模型投影到可用的环境图层上，在空间和时间上进行预测。
'''
'''
Species Distribution Models (SDMs) are ecological tools used to predict the probability of species occurrence based on specific environmental conditions. These models analyze geographic and environmental data of where species have been found to predict the potential distribution range of species.
SDMs are very popular in quantitative ecology and constitute the most widely used modeling framework for projecting potential future range shifts of species in global change impact assessments.

The inputs for SDMs typically include georeferenced biodiversity observation data 

'''

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

# 将数据转换为GeoDataFrame，这里我们使用假的坐标
data['geometry'] = pd.Series([
    {'type': 'Point', 'coordinates': (-97.73, 30.27)},
    {'type': 'Point', 'coordinates': (-97.74, 30.29)},
    {'type': 'Point', 'coordinates': (-97.72, 30.28)},
    {'type': 'Point', 'coordinates': (-97.75, 30.26)},
    {'type': 'Point', 'coordinates': (-97.76, 30.30)}
], index=data.index)

# %%
gdf = gpd.GeoDataFrame(data, geometry='geometry')
# %%
import pandas as pd
# %%
df = pd.read_csv(
    'data/species_distribution/cnn_sdm/full_dataset.csv',
    header='infer',
    sep=';',
    low_memory=False,
    )
# %%
from pprint import pprint
pprint(df.columns)
# %%
ids = df['id'].to_numpy()
labels = df['Label'].to_numpy()
positions = df[['Latitude', 'Longitude']].to_numpy()
# %%
ids.shape, labels.shape, positions.shape
# %%
from sklearn.model_selection import train_test_split
# %%
test_size = 0.1
val_size = 0.1
train_labels, test_labels, train_positions, test_positions, train_ids, test_ids = train_test_split(
    labels, positions, ids, test_size=test_size,
)
train_labels, val_labels, train_positions, val_positions, train_ids, val_ids = train_test_split(
    train_labels, train_positions, train_ids, test_size=val_size,
)
# %%
print(train_ids.shape, train_labels.shape, train_positions.shape)
print(test_ids.shape, test_labels.shape, test_positions.shape)
print(val_ids.shape, val_labels.shape, val_positions.shape)
# %%
from sunyata.cnn_sdm.raster import PatchExtractor
# %%
extractor = PatchExtractor("data/species_distribution/cnn_sdm/rasters_GLC19/")
extractor.add_all()
# %%
lat, lng = 43.6, 3.8
patch = extractor[(lat, lng)]

# %%
from sunyata.cnn_sdm.dataset import EnvironmentalDataset
# %%
train_dataset = EnvironmentalDataset(
    train_labels,
    train_positions,
    train_ids,
    patch_extractor=extractor,
)
# %%
torch_tensor, label = train_dataset[0]
# %%
torch_tensor.shape, label.shape
# %%
