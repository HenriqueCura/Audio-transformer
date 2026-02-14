from googletrans import Translator
from googletrans import LANGUAGES
from langdetect import detect


def get_lang_text(text: str)->str: 
    return detect(text)

def is_code(code: str):
    return code.lower() in LANGUAGES

def get_lang_code(name: str):
    name = name.lower()
    for code, lang in LANGUAGES.items():
        if lang == name:
            return code
    return None

def get_lang(value: str):
    if is_code(value):
        return value
    else: 
        v = get_lang_code(value)
        if not v:
            return False
        else:
            return v


def get_translation(text: str,lang_ori: str):
    translator = Translator()
    lang_ori = get_lang(lang_ori)
    if lang_ori == False:
        raise Exception("Lingua não existente! Deve ser inserida uma lingua do estilo 'en' ou 'pt'.")
    translated = translator.translate(text, src=lang_ori, dest="en").text
    return translated

def main(text: str):
    lang: str = get_lang_text(text)
    if lang != 'en':
        return get_translation(text,lang)
    return text

