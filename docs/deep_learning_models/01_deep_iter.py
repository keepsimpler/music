# %% [markdown]
# ## What is Cross Attention
'''
Suppose a $n$-dimensional query vector $q \in \mathbb{R}^n $ represent a feature vector, which is affected by / determined by / extracted from a  $(m,n)$-dimensional key vector $k$ and a $(m,n)$-dimensional value vector $v$.

First, a vector multiplication operator $(n) \times (m,n) = (m)$ to get the similarity between the query vector and $m$ key vectors.
Then a softmax operator to regularized into a categorical distribution.
After that, a vector multiplication operator $(m) \times (m,n) = (n)$ to extract information from $m$ value vectors and get the new query vector according the similarity between the old query vector and key vectors.
''' 

# %%
