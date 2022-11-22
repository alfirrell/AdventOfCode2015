import hashlib

key = "yzbqklnj"
def get_hash_value(key, n_zeros):
    done = False
    value = 0
    while not(done):
        value += 1
        str_to_hash = key + str(value)
        hash = hashlib.md5(str_to_hash.encode('utf-8')).hexdigest()
        done = hash[0:n_zeros] == '0' * n_zeros

    return value

get_hash_value(key, 5)


# Part 2
get_hash_value(key, 6)