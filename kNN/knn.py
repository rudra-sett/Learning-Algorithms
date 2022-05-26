from json.tool import main
import numpy as np
from sklearn import neighbors
# takes in 2 vector-type objects (usually features in a dataset) and returns some kind of distance
def distance(v1, v2):
  sum_squared_distance = 0
  v1 = [v1]
  v2 = [v2]
  for i in range(len(v1)):
      sum_squared_distance += np.power(v1[i] - v2[i], 2)
  return np.sqrt(sum_squared_distance)

  v1 = np.array(v1)
  v2 = np.array(v2)

  dist = np.sqrt(np.add(np.square(v1),np.square(v2)))
  return dist



# the main knn loop
def knn(k, new_item, data):

  
  # distances is a dict that maps the distance to each item to the index of said item
  distances = {}
  for index,item in enumerate(data):
    dist = distance(item,new_item)
    distances[dist] = index

  # sort the dict of distances and indices, this will be the keys/distances sorted
  k_nearest_distances = sorted(distances)[:k]

  # get the indices first n neighbors
  k_nearest_neighbors = [distances[i] for i in k_nearest_distances]

  return k_nearest_neighbors


def test():

  data1 = np.random.normal(10,1,10)
  data2 = np.random.normal(20,1,10)

  data = np.concatenate((data1,data2))
  labels = np.concatenate((np.ones(10),np.zeros(10)))

  test_point = 14

  neighbors = knn(4,test_point,data)

  print(neighbors)

test()