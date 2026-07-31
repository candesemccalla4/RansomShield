import hashlib


def hash_file(filename):

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while data := file.read(4096):
            sha256.update(data)

    return sha256.hexdigest()



def compare_hash(old_hash,new_hash):

    if old_hash != new_hash:
        return "WARNING: File changed"

    return "File unchanged"
