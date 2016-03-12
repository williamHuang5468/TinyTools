import re

def cutSentence(whole_sentence):
    setences = divide(whole_sentence)
    for setence in setences:
        print (setence + "\r\n\r\n")

def divide(string):
    """
    >>> divide("This is a apple. Hello.")
    ['This is a apple.', 'Hello.']
    """
    setences = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", string)
    return setences

