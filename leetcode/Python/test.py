# def closestLocations(totalCrates, allLocations, truckCapacity):
#     # WRITE YOUR CODE HERE
#     ans = []
#     dist = list(map(lambda x: x[0]**2 + x[1]**2, allLocations))
#     d = zip(allLocations, dist)
#     d1 = sorted(d, key=lambda key: key[1])
#     for ele in d1:
#         ans.append(ele[0])
#     return ans[:truckCapacity]

# a = 3
# b = [[1,2], [3,4], [1,-1]]
# c = 2
# print closestLocations(a, b, c)
import operator

def retrieveMostFrequentlyUsedKeywords(literatureText, wordsToExclude):
	d = dict()
	ans = []
	text = literatureText.split()
	for word in text:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	keys = d.keys()
	values = d.values()
	val = list(set(text) - set(wordsToExclude))
	d1  = {key:d[key] for key in val}
	print d1
	d1 = sorted(d1.iteritems(), key=lambda x: x[1], reverse=True)
	print d1
	n = len(d); c = 1
	for i in range(1, n):
		if d1[i][1] == d1[i-1][1]:
			c += 1
		else:
			break
	for ele in d1[:c]:
		if ele[0] not in wordsToExclude:
			ans.append(ele[0])
	return d1[:c], c, d, ans, val

literatureText = "jack and jill went to the market to buy bread and cheese cheese is jack favorite food"
wordsToExclude = ["and", "he", "the", "to", "is"]

str1= "rose is a flower rose is pond a flower rose flower in garden garden garden pond pond rose is a rose is a rose is a rose is a"
w = ["rose", "is", "a"]


ans,a, d, f, v = retrieveMostFrequentlyUsedKeywords(str1, w)
print ans
print v
print a
d1 = sorted(d.iteritems(), key=lambda (k, v):(v, k), reverse=True)
print d
print f