import math

def ItemSimilarity(train):
	# calculate co-rated users between Items 
	C = dict()
	N = dict()
	for u, items in train.items():
		for i in items:
			N[i] += 1
			for j in items:
				if i == j:
					continue
				C[i][j] += 1

	#calculate final similarity matrix W
	W = dict()
	for i, related_items in C.items():
		for j, cij in related_items.items():
			W[i][j] = cij / math.sqrt(N[i] * N[j])

	return W

def Recommendation(train, user_id, W, K):
	rank = dict()
	ru = train[user_id]
	for i, pi in ru.items():
		for j, wj in sorted(W[i].items(), key=lambda item: item[1], reverse=True)[0:K]:
			if j in ru:
				continue
			rank[j] += pi * wj
	return rank


def main():
	train = {}
	train['u1'] = {'a':1, 'b':2, 'c':3}
	train['u2'] = {'b':1, 'c':1, 'e':3}
	train['u3'] = {'c':1, 'd':1}
	train['u4'] = {'b':1, 'c':1, 'd':3}
	train['u5'] = {'a':1, 'd':3}

	W = ItemSimilarity(train)
	print W

if __name__ == '__main__':
	main()