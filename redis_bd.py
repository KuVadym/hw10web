import redis

client = redis.StrictRedis(host="localhost", port=6379, password=None)

def cache_catcher(func):
    cache = []
    max_size = 5
    def wrapper(*args):
        if args in cache:
            cache.remove(args)
            cache.insert(0, args)
            print (f"Cache: {client.get(str(args))}")
            return client.get(str(args))
        else:
            cache.insert(0, args)
        if len(cache) > max_size:
            client.delete(str(cache.pop()))
        value = func(*args)
        client.set(str(args), value)
        print(value)
        return value

    return wrapper


@cache_catcher
def main_func(*args):
    return args[0]

#main_func("Kuzyk")
#main_func("Vadym")
#main_func("Artem")
#main_func("Kuzyk")
#main_func("Oleh")
#main_func("Vovk")
#main_func("Oleh")