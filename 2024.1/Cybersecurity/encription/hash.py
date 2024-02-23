import hashlib

def calc_hash(text):
    hash_md5 = hashlib.md5()
    hash_md5.update(text.encode())

    hash_sha256 = hashlib.sha256()
    hash_sha256.update(text.encode())

    hash_sha512 = hashlib.sha512()
    hash_sha512.update(text.encode())

    return hash_md5.hexdigest(), hash_sha256.hexdigest(), hash_sha512.hexdigest()

text = 'Testing hello world'
hash_md5, hash_sha256, hash_sha512 = calc_hash(text)

print(hash_md5)
print(hash_sha256)
print(hash_sha512)