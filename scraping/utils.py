from selenium.common.exceptions import NoSuchElementException
import re

def parse_price(price_text):
    
    clean_text = re.sub(r'[^\d,]', '', price_text)  # Remove tudo exceto dígitos e vírgulas
    clean_text = clean_text.replace(',', '.')  # Substitui vírgula por ponto (padrão de decimal)
    try:
        return float(clean_text)
    except ValueError:
        return 0.0  # Retorna 0.0 se a conversão falhar

def parse_discount(discount_str):
    try:
        return int(discount_str.replace("%", "").replace("-", "").strip())
    except ValueError:
        return 0  # Valor padrão para erros de conversão

def clean_text(text):
    return text.strip()

def safe_find_element_text(element, by, selector, default=""):
    try:
        return element.find_element(by, selector).text
    except NoSuchElementException:
        return default
