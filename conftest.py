
import pytest

from utils import get_mysql_engine, get_databricks_engine


@pytest.fixture(scope="session")
def mysql_engine():

    engine = get_mysql_engine()

    yield engine

    engine.dispose()


@pytest.fixture(scope="session")
def databricks_engine():

    engine = get_databricks_engine()

    yield engine

    engine.dispose()
