from google.cloud import bigquery
from config.bigquery_config import get_bigquery_credentials, get_bigquery_config

def upload_to_bigquery(df):
    project_id, dataset_id, table_id = get_bigquery_config()
    credentials = get_bigquery_credentials()

    client = bigquery.Client(project=project_id, credentials=credentials)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job = client.load_table_from_dataframe(df, table_ref)
    job.result()

    print(f"Dados carregados com sucesso em {table_ref}")
