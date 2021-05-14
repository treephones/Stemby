from random import randint as rand

def gen_cache_name():
    return "".join([str(rand(1,9)) for _ in range(8)])