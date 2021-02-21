def mattrans(m):
  t = []
  for i in range(len(m[0])):
    t.append([])
  for i in range(len(m[0])):
    for j in range(len(m)):
      t[i].append(m[j][i])
  return t
