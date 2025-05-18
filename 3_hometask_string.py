import re


def normalize_letter_case(initial_text: str) -> str:
    """To normalize text from letter case point of view"""
    lower_text = initial_text.lower()
    sentences = re.split(r'(?<=[.?!])\s+', lower_text)
    normalized_sentences = [s.capitalize() for s in sentences]
    return ' '.join(normalized_sentences)


def fix_iz(initial_text: str) -> str:
    """To fix iz as a mistake"""
    fixed_text = re.sub(r'\biz\b', 'is', initial_text)
    return fixed_text


def add_last_sentence(initial_text: str) -> str:
    """To create additional sentence with last words"""
    sentences = re.split(r'(?<=[.?!])\s+', initial_text)
    last_words = [s.strip().rstrip('.!?').split()[-1] for s in sentences if s.strip()]
    new_sentence = ' '.join(last_words).capitalize() + '.'
    return initial_text + new_sentence


def calculate_white_spaces(initial_text: str) -> int:
    whitespace_count = len(re.findall(r'\s', initial_text))
    return whitespace_count


if __name__ == "__main__":
    original_text = ''' tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

'''
    normalized_text = normalize_letter_case(original_text)
    print(normalized_text)
    fixed_iz_text = fix_iz(normalized_text)
    print(fixed_iz_text)
    text_with_last_sentence = add_last_sentence(fixed_iz_text)
    print(text_with_last_sentence)
    print(calculate_white_spaces(original_text))
