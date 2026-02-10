import os
from openai import OpenAI
from pydantic import BaseModel
from googletrans import Translator
from googletrans import LANGUAGES

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_code(code: str):
    return code.lower() in LANGUAGES

def get_lang_code(name: str):
    name = name.lower()
    for code, lang in LANGUAGES.items():
        if lang == name:
            return code
    return None

def get_lang(value: str):
    if is_code():
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



tools = [
    {
        "type" : "function",
        "function": {
            "name" : "get_translation",
            "description" : "Gets the translation of a text from a given language to english.",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "text" : {"type" : "number"},
                    "lang_ori" : {"type" : "number"},
                },
                "required" : [ "text" , "lang_ori"],
                "additionalProperties" : False ,
            },
            "strict" : True,
        },
    }

]