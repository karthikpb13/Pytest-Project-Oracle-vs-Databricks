import pandas as pd
from logger import get_logger

logger = get_logger("duplicate_check", "logs/duplicate_check.log")

def duplicate_check(databricks_engine):

    df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, COUNT(*) AS duplicate_count
        FROM curated.curated_schema.dim_emp
        GROUP BY EMPLOYEE_ID
        HAVING COUNT(*) > 1
        """,
        databricks_engine
    )

    return df["duplicate_count"].sum()

def test_duplicate_check(databricks_engine):
    """ Validates the duplicates in target"""

    logger.info("Duplicate Check Started")

    duplicate_count = duplicate_check(databricks_engine)
    
    try:
        assert duplicate_count == 0, (
        f"Found {duplicate_count} duplicate employee records"
        )

        logger.info("Duplicate check PASSED")

    except AssertionError:
        logger.error("duplicate check failed"
                 f"Target contains total {duplicate_count} duplicate values"
                )
        raise