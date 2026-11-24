
# Import Pandas for executing SQL queries and handling query results
import pandas as pd

# Import custom logger function for maintaining execution logs
from logger import get_logger


# Initialize logger and specify the log file location
logger = get_logger("null_check", "logs/null_check.log")


# ============================================================
# 1. EMPLOYEE_ID NULL VALIDATION
# ============================================================

# Function to check NULL values in EMPLOYEE_ID column
def null_employee_id_check(databricks_engine):

    # Execute SQL query to retrieve records where EMPLOYEE_ID is NULL
    df1 = pd.read_sql(
        """
        SELECT EMPLOYEE_ID
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EMPLOYEE_ID IS NULL
        """,
        databricks_engine
    )

    # Return the total number of NULL records
    return len(df1)


# Pytest test function to validate EMPLOYEE_ID NULL values
def test_employee_id_null_check(databricks_engine):
    """Validates NULL employee IDs in the target table."""

    # Log the start of validation
    logger.info("EMPLOYEE_ID NULL check started")

    # Call validation function and capture NULL record count
    null_id = null_employee_id_check(databricks_engine)

    try:
        # Assert that there are no NULL values in EMPLOYEE_ID
        assert null_id == 0, (
            f"Found {null_id} NULL employee IDs in target"
        )

        # Log successful validation
        logger.info("NULL check Employee_ID PASSED")

    except AssertionError:
        # Log failure details if NULL records are found
        logger.error(
            f"NULL check Employee_ID FAILED. "
            f"Target contains {null_id} NULL employee IDs"
        )

        # Re-raise the assertion error so Pytest marks the test as FAILED
        raise


# ============================================================
# 2. GENDER NULL VALIDATION
# ============================================================

# Function to check NULL values in GENDER column
def gender_null_check(databricks_engine):

        # Execute SQL query to retrieve records where GENDER is NULL
        df2 = pd.read_sql(
            """
            SELECT EMPLOYEE_ID,GENDER FROM CURATED.CURATED_SCHEMA.DIM_EMP 
            WHERE GENDER IS NULL;
            """,
            databricks_engine
    )

        # Return the total number of NULL records
        return len(df2)


# Pytest test function to validate GENDER NULL values
def test_gender_null_check(databricks_engine):
    """Validates NULL Gender in the target table."""

    # Log the start of validation
    logger.info("GENDER NULL Check started")

    # Call validation function and capture NULL record count
    null_gender = gender_null_check(databricks_engine)

    try:
        # Assert that there are no NULL values in GENDER
        assert null_gender == 0, (
            f"Found {null_gender} NULL in target"
        )

        # Log successful validation
        logger.info("NULL check GENDER PASSED")

    except AssertionError:
        # Log failure details if NULL records are found
        logger.error(
            f"NULL check GENDER FAILED. "
            f"Target contains {null_gender} NULL Gender"
        )

        # Re-raise the assertion error
        raise


# ============================================================
# 3. JOB_TITLE NULL VALIDATION
# ============================================================

# Function to check NULL values in JOB_TITLE column
def nulL_job_title_check(databricks_engine):

     # Execute SQL query to retrieve records where JOB_TITLE is NULL
     df3=pd.read_sql(
          """
        SELECT EMPLOYEE_ID, JOB_TITLE FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        WHERE  JOB_TITLE IS NULL;
        """,
        databricks_engine
     )

     # Return the total number of NULL records
     return len(df3)


# Pytest test function to validate JOB_TITLE NULL values
def test_null_job_title(databricks_engine):
     """Vaidates NULL JOB_TITLE in target"""
     
     # Log the start of validation
     logger.info("JOB_TITLE NULL Check started")

     # Call validation function and capture NULL record count
     nulL_job_title=nulL_job_title_check(databricks_engine)
     
     try:
        # Assert that there are no NULL values in JOB_TITLE
        assert nulL_job_title==0,(
               f"Found {nulL_job_title} in target"

          )

        # Log successful validation
        logger.info("Null Gender check Passed")
     
     except AssertionError:
         # Log failure details if NULL records are found
         logger.error(
             f" JOB_TTLE Null check Failed"
             f"Target has {nulL_job_title} null JOB_TITLE"
         )

         # Re-raise the assertion error
         raise
     

# ============================================================
# 4. HIRE_DATE NULL VALIDATION
# ============================================================

# Function to check NULL values in HIRE_DATE column
def null_hire_date_check(databricks_engine):

    # Execute SQL query to retrieve records where HIRE_DATE is NULL
    df4=pd.read_sql(
        """
        SELECT EMPLOYEE_ID,  HIRE_DATE FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        WHERE HIRE_DATE  IS NULL;
        """,
        databricks_engine
    )

    # Return the total number of NULL records
    return len(df4)


# Pytest test function to validate HIRE_DATE NULL values
def test_hire_date_null_check(databricks_engine):
    """Validates that there is no null values in target for HIRE_DATE"""

    # Log the start of validation
    logger.info("Null HIRE_DATE validation started")

    # Call validation function and capture NULL record count
    null_hire_date=null_hire_date_check(databricks_engine)

    try:
        # Assert that there are no NULL values in HIRE_DATE
        assert null_hire_date==0,(
            f" found {null_hire_date} in Target"
        )

        # Log successful validation
        logger.info("HIRE_DATE null check passed")

    except AssertionError:
        # Log failure details if NULL records are found
        logger.error(
            f"HIRE_DATE Null check failed"
            f"Target contains {null_hire_date} "
        )

        # Re-raise the assertion error
        raise


# ============================================================
# 5. CITY NULL VALIDATION
# ============================================================

# Function to check NULL values in CITY column
def nul_city_check(databricks_engine):

    # Execute SQL query to retrieve records where CITY is NULL
    df5=pd.read_sql(
        """
        SELECT  EMPLOYEE_ID, CITY FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        WHERE  CITY IS NULL;
        """,
        databricks_engine
    )

    # Return the total number of NULL records
    return len(df5)


# Pytest test function to validate CITY NULL values
def test_city_nul_check(databricks_engine):
    """Validates that there are no null cities are present"""

    # Log the start of validation
    logger.info("Null CITY Validation is started") 

    # Call validation function and capture NULL record count
    city_null=nul_city_check(databricks_engine) 

    try:
        # Assert that there are no NULL values in CITY
        assert city_null==0,(
            f"Target Conatins the null cities"
        )

    except AssertionError:
        # Log failure details and NULL record count
        logger.error(
            f"target conatains the null city values"
            f"target coatins total {city_null} null values in city column"
        )

        # Re-raise the assertion error
        raise


# ============================================================
# 6. COUNTRY NULL VALIDATION
# ============================================================

# Function to check NULL values in COUNTRY column
def null_country_check(databricks_engine):

    # Execute SQL query to retrieve records where COUNTRY is NULL
    df6=pd.read_sql(
        """
        SELECT  EMPLOYEE_ID, COUNTRY FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        WHERE  COUNTRY IS NULL
        """,
        databricks_engine
     )

    # Return the total number of NULL records
    return len(df6)


# Pytest test function to validate COUNTRY NULL values
def test_country_null_check(databricks_engine):
    """Validates that there are no null valyues present in country columns"""

    # Log the start of validation
    logger.info("Null city c]validation started")

    # Call validation function and capture NULL record count
    country_null=null_country_check(databricks_engine)

    try:
        # Assert that there are no NULL values in COUNTRY
        assert country_null==0,(
            f"Country null validation failed"
        )

    except AssertionError:
        # Log failure details and NULL record count
        logger.error(
            f"Country null check validation failed"
            f"Country column contains {country_null} values"
        )

        # Re-raise the assertion error
        raise


# ============================================================
# 7. ORIGINAL_SALARY NULL VALIDATION
# ============================================================

# Function to check NULL values in ORIGINAL_SALARY column
def null_salary_check(databricks_engine):

    # Execute SQL query to retrieve records where ORIGINAL_SALARY is NULL
    df7=pd.read_sql(
        """
        SELECT  EMPLOYEE_ID, ORIGINAL_SALARY
        FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        WHERE  ORIGINAL_SALARY IS NULL
        """,
        databricks_engine 

    )

    # Return the total number of NULL records
    return len(df7)


# Pytest test function to validate ORIGINAL_SALARY NULL values
def test_sal_null_check(databricks_engine):
    """Validates that there are no null values present in salary column in target"""

    # Log the start of validation
    logger.info("Salary NULL Validatin started")

    # Call validation function and capture NULL record count
    salary_null=null_salary_check(databricks_engine)

    try:
        # Assert that there are no NULL values in ORIGINAL_SALARY
        assert salary_null==0,(
            f"Salary Null Validation Failed"
        )

    except AssertionError:
        # Log failure details and NULL record count
        logger.error(
            f" Salary Null Validation failed"
            f"Target salary column conatin {salary_null} null values "
        )

        # Re-raise the assertion error
        raise


# ============================================================
# 8. EMPLOYMENT_STATUS NULL VALIDATION
# ============================================================

# Function to check NULL values in EMPLOYMENT_STATUS column
def null_employement_status_check(databricks_engine):

    # Execute SQL query to retrieve records where EMPLOYMENT_STATUS is NULL
    df8=pd.read_sql(
        """
        SELECT  EMPLOYEE_ID, EMPLOYMENT_STATUS
        FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        WHERE  EMPLOYMENT_STATUS IS NULL   
        """,
        databricks_engine
    )

    # Return the total number of NULL records
    return len(df8)


# Pytest test function to validate EMPLOYMENT_STATUS NULL values
def test_employement_status_check(databricks_engine):
    """ Validates that there are no null employement_status present in target"""

    # Log the start of validation
    logger.info("Employement null check started")

    # Call validation function and capture NULL record count
    employement_null=null_employement_status_check(databricks_engine)

    try:
        # Assert that there are no NULL values in EMPLOYMENT_STATUS
        assert employement_null==0,(
            f"Employement_status Check Failed "
        )

    except AssertionError:
        # Log failure details and NULL record count
        logger.error(
            f"Employement_status null check failed"
            f"Employement_statyus conatins {employement_null} values"
        )

        # Re-raise the assertion error
        raise
