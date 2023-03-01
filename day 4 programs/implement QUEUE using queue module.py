import queue
q=queue.Queue(maxsize=3)
a=q.put(10)
q.put(20)
q.put(30)
print(a)

print(q.get())  # get() diplays which element we delete
print(q.get())
print(q.get())
