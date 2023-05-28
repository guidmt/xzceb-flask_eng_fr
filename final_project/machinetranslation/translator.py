""" Script to convert eng to fr and vice-versa"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator=IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

language_translator.set_service_url(url)

def eng_to_fr(eng_text):
    """Function converting english to french"""
    french_text = language_translator.translate(text=eng_text,model_id='en-fr').get_result()
    french_text = french_text.get("translations")[0].get("translation")
    return french_text

def fr_to_eng(fr_text):
    """Function converting frech to english"""
    english_text = language_translator.translate(text=fr_text,model_id='fr-en').get_result()
    english_text = english_text.get("translations")[0].get("translation")
    return english_text
