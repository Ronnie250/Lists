marks=[87, 66, 94, 79, 83]
print(marks)
marks.append(85)
print(marks)
marks.append(38)
print(marks)
marks.append(25)
print(marks)
marks.pop(4)
print(marks)
top=[]
average=[]
low=[]
for m in marks:
    if m>80:
        top.append(m)
    elif m>60:
        average.append(m)
    else:
        low.append(m)
top.sort()
average.sort()
low.sort()
top.reverse()
average.reverse()
low.reverse()
print(top)
print(average)
print(low)