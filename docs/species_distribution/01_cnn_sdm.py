# %% [markdown]

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
