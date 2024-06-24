monthly = [2200, 2350, 2600, 2130, 2190]
print(f"Feb spent more than Jan by {monthly[1] - monthly[0]}")
print(f"Total expense of Q1: {sum(monthly[:3])}")
print(f"Spent 2000 in months {[monthly.index(x) for x in monthly if x==2000]}")
#The listcomp above is for fun
# (2000 in monthly) is sufficient
monthly[3] -= 200
print(f"New April amount: {monthly[3]}")

heros=['spider man','thor','hulk','iron man','captain america']
print(f"\n\nLength of list: {len(heros)}")
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(heros.index("hulk") + 1, "black panther")
print(heros)
heros[1:3] = ["doctor strange"]
print(heros)
heros.sort()
print(heros)

maxnum = int(input('Input a max number '))
print(list(range(1,maxnum+1)))