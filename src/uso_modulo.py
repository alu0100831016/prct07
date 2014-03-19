#! /usr/bin/python
import modulo
t_upla= (10, 100, 1000, 10000, 100000, 1000000)
l = [ ]
for i in range(len(t_upla)):
  a= modulo.aprxpi(t_upla[i])
  l=l+[a]
print l