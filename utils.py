
import os
import pytest

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()


# MySQL Source Connection
def get_mysql_engine():

    required_variables = [
        "MYSQL_HOST",
        "MYSQL_PORT",
        "MYSQL_DATABASE",
        "MYSQL_USERNAME",
        "MYSQL_PASSWORD"
    ]

    missing_variables = [
        variable for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing_variables:
        pytest.fail(f"Missing MySQL environment variables: {missing_variables}")

    url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("MYSQL_USERNAME"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        database=os.getenv("MYSQL_DATABASE")
    )

    return create_engine(url)


# Databricks Target Connection
def get_databricks_engine():

    required_variables = [
        "DATABRICKS_ACCESS_TOKEN",
        "DATABRICKS_SERVER_HOSTNAME",
        "DATABRICKS_HTTP_PATH"
    ]

    missing_variables = [
        variable for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing_variables:
        pytest.fail(f"Missing Databricks environment variables: {missing_variables}")

    connection_url = URL.create(
        "databricks",
        username="token",
        password=os.getenv("DATABRICKS_ACCESS_TOKEN"),
        host=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        query={
            "http_path": os.getenv("DATABRICKS_HTTP_PATH")
        }
    )

    return create_engine(connection_url)
