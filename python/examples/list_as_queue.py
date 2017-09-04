from collections import deque

queue = deque(["Eric", "John", "Michael"])
print queue

queue.append("Terry")           # Terry arrives
print queue

queue.append("Graham")          # Graham arrives
print queue

print "popleft: ",queue.popleft()                 # The first to arrive now leaves

print "popleft: ",queue.popleft()                 # The second to arrive now leaves

print queue                           # Remaining queue in order of arrival

print "popright: ",queue.pop()                 # The second to arrive now leaves

print queue                           # Remaining queue in order of arrival
