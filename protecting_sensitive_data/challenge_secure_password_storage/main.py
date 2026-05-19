import hashlib

def hash_password(password):
    # 1. パスワードを UTF-8 バイト列に変換
    byte_pw = password.encode("utf-8")
    # 2. SHA-256 でハッシュ計算
    hash_object = hashlib.sha256(byte_pw)
    # 3. 16 進文字列で返却
    return hash_object.hexdigest()

# Sample calls
hashed1 = hash_password("mySecretPassword123!")
hashed2 = hash_password("another$trongP@ss")
print(hashed1)
print(hashed2)