0:  def nums():
1:      i = 5
2:      m = 4
3:      if i < m:
4:          i = m + 5
5:      else:
6:          m = i - 1
7:      c = i + m
8:      for j in range(c):
9:          i += m
10:         m = c * i
11:     if i < m:
12:         m = i + m
13:     count = i + (m / c)
14:     if count < c:
15:         a = i + count
16:     else:
17:         m = m + count
18:     c = i + m
19:     while c > count:
20:         count = count + (m - i)/10
21:         c += (i + m) / 20
22:     if count > c:
23:         count = c
24:     return count
