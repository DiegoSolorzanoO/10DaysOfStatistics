from sklearn import linear_model

m, n = list(map(int, input().split(' ')))

feature_sets = []
for _ in range(n):
    set = list(map(float, input().split(' '))) 
    feature_sets.append(set)

feature_sets_totals = []
for set in feature_sets:
    feature_sets_totals.append(set.pop())

len_q_feature_sets = int(input())

q_feature_sets = []

for _ in range(len_q_feature_sets):
    set = list(map(float, input().split(' '))) 
    q_feature_sets.append(set)

lm = linear_model.LinearRegression()
lm.fit(feature_sets, feature_sets_totals)
a = lm.intercept_
bs = lm.coef_

for i in range(len_q_feature_sets):
    Y = a
    for j in range(m):
        Y += q_feature_sets[i][j] * bs[j] 
    print(round(Y, 2))
