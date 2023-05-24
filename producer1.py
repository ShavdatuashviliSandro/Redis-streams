import redis

r = redis.Redis()
r.flushdb()

key = 'numbers'

n = 1

while True:
    data = {'n': n}
    msg_id = r.xadd(key, data)

    print(f'Length:', r.xlen(key))
    print(f'Memory Usage: ', r.memory_usage(key))
    print(f'Produced the number {n} as message id {msg_id.decode("utf-8")}')
    print('-------------------------------------------------')

    n += 1