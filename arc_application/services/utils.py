import random
import string


def random_string_generator(number_of_chars):
    """this function generates random strings

    Args:
        number_of_chars (int): number of characters in sting
    """
    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=number_of_chars))
