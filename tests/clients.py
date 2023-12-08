import openapi_client
from dotenv import load_dotenv

from models.base import Base
from nguylinc_python_utils.sqlalchemy import init_db

load_dotenv()
configuration = openapi_client.Configuration(
    host="http://localhost:8080",
)

api = openapi_client.ApiClient(configuration)
petApi = openapi_client.PetApi(api)

session = init_db(Base)
