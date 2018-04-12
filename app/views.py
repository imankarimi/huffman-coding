from collections import defaultdict
from app.providers.HuffmanCoding import HuffmanCoding


def coding():
    freq = {'A': 15, 'B': 8, 'C': 6, 'D': 6, 'E': 5}
    huff = HuffmanCoding.encode(freq)
    result = {'freq': freq, 'huff': huff, 'message': freq, 'active': 0}
    return result


def message_coding():
    message = "Hi there"
    freq = defaultdict(int)
    for symbol in message:
        freq[symbol] += 1

    huff = HuffmanCoding.encode(freq)
    result = {'freq': freq, 'huff': huff, 'message': message, 'active': 1}
    return result
