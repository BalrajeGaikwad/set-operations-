s={12,3,432,22,43,65,665}
t={'A',"b",'c'}

u=set()

s.add("hello")
s.update(t)
u=s.copy()

print(u)
print(s)

s.remove(432)

s.remove(12)

print(s)