from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.utils import parse_price, parse_discount, clean_text, safe_find_element_text
import yaml

# Carregar configuração
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

def scrape_steamdb_sales():
    driver = webdriver.Chrome()
    driver.get(config['steamdb_url'])

    # Espera até que os dados estejam carregados
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'app')))
    
    games = []
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.app')
    for row in rows:
        try:
            # Nome
            name = clean_text(safe_find_element_text(row, By.CSS_SELECTOR, 'a.b', default="N/A"))

            # Preço
            discount_price = 0.0
            price_elements = row.find_elements(By.CSS_SELECTOR, 'td.dt-type-numeric')
            for element in price_elements:
                data_sort = element.get_attribute("data-sort")
                text = element.text.strip()

                # Ignorar elementos com data-sort="100"
                if data_sort == "100":
                    continue
                if (
                    data_sort and 
                    data_sort.isdigit() and 
                    len(data_sort) in [3, 4, 5] and "R$" in text
                ):
                    try:
                        discount_price = float(data_sort) / 100.0
                        break 
                    except ValueError:
                        pass

            # Porcentagem desconto
            discount_percent_elements = row.find_elements(By.CSS_SELECTOR, 'td.dt-type-numeric')
            discount_percent = "0%"
            for element in discount_percent_elements:
                discount_text = element.text.strip()

                if discount_text and "%" in discount_text:
                    discount_percent = discount_text
                    break

            discount_percent = parse_discount(discount_percent)

            # Avaliações
            reviews = "Sem Avaliação"
            for element in price_elements:
                data_sort = element.get_attribute("data-sort")
                if data_sort and "." in data_sort and data_sort.replace(".", "").isdigit():  # Identifica avaliações pelo padrão decimal
                    reviews = f"{float(data_sort)}%"  # Converte para porcentagem
                    break

            # print(f"Texto do Preço Capturado: {discount_price}")  # Depuração
            # print(f"Texto da Avaliação Capturada: {reviews}")  # Depuração
            # print(f"Texto do Nome Capturado: {name}")  # Depuração
            # print(f"Texto do Desconto Capturado: {discount_percent}")  # Depuração

            games.append({
                'Nome': name,
                'Preco_Com_Desconto': discount_price,
                'Percentual_De_Desconto': discount_percent,
                'Avaliacao': reviews
            })
        except Exception as e:
            print(f"Erro ao processar linha: {e}")
    driver.quit()
    return games
