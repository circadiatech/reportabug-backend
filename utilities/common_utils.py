import uuid
import hashlib
import traceback


def get_true_random_string(length=16):
    """
    Used cryptographically safe UUID4 to generate a random string, then shortens it length to the required lenght after
    generating a hash of it.
    length (int): An integer to specify the required length of the returned random string.
    # TODO: Shortening the length can lead to unsafe random strings. Models should support an api key of at least 32
    # TODO: Bytes which is considered secure according to python community discussions.
    """
    true_random_string = ""
    try:
        random_string = str(uuid.uuid4())
        print(f"[DEBUG]: Generated true random string is {random_string}")
        true_random_string = hashlib.sha256(random_string.encode('utf-8')).hexdigest()
        print(f"[DEBUG]: Generated SHA256 hash of the string is {true_random_string}")
    except Exception:
        print("[ERROR]: Unable to generate random string.", traceback.format_exc())

    # Length validation checks and corrections
    if length < 1 or length > 64:
        length = 64

    return true_random_string[:length]


"""
Custom Unit Tests
"""
if __name__ == '__main__':
    # This test is for normal usage.
    random_string = get_true_random_string(16)
    print(f"[DEBUG]: Random String Value: {random_string}")
    assert len(random_string) == 16

    # This test is for edge case usage.
    random_string = get_true_random_string(0)
    print(f"[DEBUG]: Random String Value: {random_string}")
    assert len(random_string) == 64

    # This test is for edge case usage.
    random_string = get_true_random_string(100)
    print(f"[DEBUG]: Random String Value: {random_string}")
    assert len(random_string) == 64