"""Module for Morse code"""

MORSE_CODE_DICT: dict[str, str] = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ' ': '/', '\n':'\n'}
REVERSE_MORSE_CODE_DICT: dict[str, str] = {morse:char for char,morse in MORSE_CODE_DICT.items()}

def text_to_morse(input_string:str) -> str:
    """Converts a given text string to Morse code.

    :param str input_string: The input text to be converted.

    :return str: Morse code representation of the input text.
    """
    return ' '.join([MORSE_CODE_DICT.get(char.upper(), '') for char in input_string])


def morse_to_text(morse_code:str) -> str:
    """Converts Morse code to the corresponding text.

    :param str morse_code: Morse code input to be converted.

    :return str: The text representation of the Morse code.
    """
    return ''.join([REVERSE_MORSE_CODE_DICT.get(char, '') for char in morse_code.split(' ')])

def spam_cycle()->None:
    """Spam to morse and back again"""
    spam = '''
Egg and Spam
Egg, bacon, and Spam
Egg, bacon, sausage, and Spam
Spam, bacon, sausage, and Spam
Spam, egg, Spam, Spam, bacon, and Spam
Spam, Spam, Spam, egg, and Spam
Spam, sausage, Spam, Spam, Spam, bacon, Spam, tomato, and Spam
Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam, and Spam
'''
    morse_spam = text_to_morse(spam)
    text_from_morse_spam = morse_to_text(morse_spam)
    print(f"Spam Cycle: {spam}{morse_spam}{text_from_morse_spam}")

if __name__ == "__main__":spam_cycle()