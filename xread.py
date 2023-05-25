import redis

r = redis.Redis()

key = 'numbers'

last_id = '0-1'
n_sum = 0

streamsDict = {}

while True:
    streamsDict[key] = last_id
    msgs = r.xread(streamsDict, count=1)

    print(msgs)
    break
    if not msgs:
        break

for msg in msgs[0][1]:
    last_id = msg[0]
    n_sum += int(msg[1][b'n'])

print('sum', n_sum)
