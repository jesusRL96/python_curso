# means cluster is an unsupervised algorithm
# it defines cluster by its own
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

digits = load_digits()
data = scale(digits.data)

# 10 clusters because there are 10 different numbers
model = KMeans(n_clusters=10, init='random', n_init=10)
model.fit(data)

# model.predict([]) it should predict which number is, using an image, we can't test it now