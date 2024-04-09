
data = [[1, 6, 'Yes'],
        [4, 5, 'No'],
        [6, 4, 'No'],
        [2, 6, 'Yes'],
        [8, 4, 'Yes'],
        [2, 5, 'Yes'],
        [3, 1, 'No']]

a = 4
b = 7
# euclidean distance
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


k = 1
nearest_neighbors = []
for point in data:
    dist = euclidean_distance([a, b], point[:2])
    nearest_neighbors.append((dist, point))

nearest_neighbors.sort(key=lambda x: x[0])
#distances
print("Distances are: ",nearest_neighbors)


votes = {}
for neighbor in nearest_neighbors[:k]:
    cls = neighbor[1][2]
    votes[cls] = votes.get(cls, 0) + 1

predicted_val = max(votes, key=votes.get)

print("The predicted Output for k=1 ({}, {}) is: {}".format(a, b, predicted_val))



k = 3
nearest_neighbors = []
for point in data:
    dist = euclidean_distance([a, b], point[:2])
    nearest_neighbors.append((dist, point))

nearest_neighbors.sort(key=lambda x: x[0])
# for i in len(nearest_neighbors):
#     print("value :",nearest_neighbors[0])
votes = {}
for neighbor in nearest_neighbors[:k]:
    cls = neighbor[1][2]
    votes[cls] = votes.get(cls, 0) + 1

predicted_val = max(votes, key=votes.get)

print("The predicted Output for for k= 3({}, {}) is: {}".format(a, b, predicted_val))




k = 5
nearest_neighbors = []
for point in data:
    dist = euclidean_distance([a, b], point[:2])
    nearest_neighbors.append((dist, point))

nearest_neighbors.sort(key=lambda x: x[0])
# for i in len(nearest_neighbors):
#     print("value :",nearest_neighbors[0])

votes = {}
for neighbor in nearest_neighbors[:k]:
    cls = neighbor[1][2]
    votes[cls] = votes.get(cls, 0) + 1

predicted_val = max(votes, key=votes.get)

print("The predicted Output for  k=5({}, {}) is: {}".format(a, b, predicted_val))