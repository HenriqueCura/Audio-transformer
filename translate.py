from deep_translator import GoogleTranslator
from langdetect import detect


def get_lang_text(text: str)->str: 
    return detect(text)


def get_translation(text: str,lang_ori: str):
    translated = GoogleTranslator(source=lang_ori, target='en').translate(text)
    #translated = translator.translate(text, src=lang_ori, dest="en").text
    return translated

def main(text: str):
    lang: str = get_lang_text(text)
    if lang != 'en':
        return get_translation(text,lang)
    return text

