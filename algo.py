def lv(a,b):
	a_len = len(a)
	b_len = len(b)
	a = '#' + a
	b = '#' + b
	m = [[0 for x in range(a_len)] for y in range(b_len)] 

	for i in range(0,a_len):
		m[i][0] = i

	for j in range(0,b_len):
		m[0][j] = j

	for i in range(1,a_len):
		for j in range(1, b_len):
			if a[i] == b[j]:
				m[i][j] = m[i-1][j-1]
			else:
				m[i][j] = min(m[i-1][j]+1, m[i][j-1]+1, m[i-1][j-1]+1)

	# print(m)
	return m[a_len - 1][b_len - 1]


a = 'if not s: return len(t)'
b = 'if not t: return len(s)'

a = a.replace(' ',"")
b = b.replace(' ',"")

lv_dist = lv(a,b)
similarity = 1 - (lv_dist/max(len(a),len(b)))

print(similarity*100)