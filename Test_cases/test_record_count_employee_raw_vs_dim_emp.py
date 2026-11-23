
import pandas as pd
from logger import get_logger

logger = get_logger("record_count", "logs/record_count.log")


def mysql_count(mysql_engine):

    df = pd.read_sql(
        "SELECT COUNT(*) AS record_count FROM EMPLOYEE_RAW",
        mysql_engine
    )

    return int(df.at[0, "record_count"])


def databricks_count(databricks_engine):

    df = pd.read_sql(
        """
        SELECT COUNT(*) AS record_count
        FROM curated.curated_schema.DIM_EMP
        """,
        databricks_engine
    )

    return int(df.at[0, "record_count"])


def test_record_count(mysql_engine, databricks_engine):
    """Validate source and target record counts."""

    logger.info("Starting record count validation")

    source_count = mysql_count(mysql_engine)
    target_count = databricks_count(databricks_engine)

    logger.info(f"Source count: {source_count}")
    logger.info(f"Target count: {target_count}")
    
    try:
        assert source_count == target_count, (
            f"Record count mismatch: "
            f"Source={source_count}, Target={target_count}"
        )

        logger.info("Record count validation PASSED")

    except AssertionError:
        logger.error(
            f"Record count validation FAILED. "
            f"Source={source_count}, Target={target_count}"
        )
        raise