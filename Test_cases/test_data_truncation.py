import pandas as pd
from logger import get_logger

logger = get_logger("data_truncation", "logs/data_truncation.log")


## Employee_id Data Truncation validation 

def employee_id_data_truncation(mysql_engine, databricks_engine):

    source_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID
        FROM employee_db.EMPLOYEE_RAW
        """,
        mysql_engine
    )

    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        """,
        databricks_engine
    )

    missing_records = source_df[
        ~source_df["EMPLOYEE_ID"].isin(target_df["EMPLOYEE_ID"])
    ]

    return len(missing_records)


def test_employee_id_data_truncation(mysql_engine, databricks_engine):

    logger.info("Employee ID data truncation check started")

    missing_count = employee_id_data_truncation(
        mysql_engine, databricks_engine
    )

    try:
        assert missing_count == 0, (
            f"Found {missing_count} employee IDs missing in target"
        )

        logger.info("Employee ID data truncation check PASSED")

    except AssertionError:
        logger.error(
            f"Employee ID data truncation check FAILED. "
            f"Missing employee IDs: {missing_count}"
        )
        raise


## Gender data trucation 

def gender_data_truncation_validation(mysql_engine,databricks_engine):
    source_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, GENDER FROM employee_db.EMPLOYEE_RAW
        """,
        mysql_engine
    )

    target_df=pd.read_sql(
        """ 
        SELECT EMPLOYEE_ID,GENDER FROM CURATED.CURATED_SCHEMA.DIM_EMP
        """,
        databricks_engine   
    )

    missing_records = source_df[
            ~source_df[["EMPLOYEE_ID","GENDER"]].isin(target_df[["EMPLOYEE_ID","GENDER"]])
        ]

    return len(missing_records)


#### Gender Data Truncation Validation 
def test_gender_data_truncation_check(mysql_engine,databricks_engine):
    """This funcation validates the data truncation between Source Gender and Target Gender column """

    logger.info("Gender Data Truncation Validation Starts")

    missing_count=gender_data_truncation_validation(mysql_engine,databricks_engine)

    try:
        assert missing_count==0,(
            "Gender Data Truncation Validation Failed"
        )
    except AssertionError:
        logger.error(
            f" Gender Data Truncation validation got failed"
            f"Gender data truncatio  filed for {missing_count} records"        
        )


    ### Department data truncation validation 

def deprtment_data_truncation(mysql_engine,databricks_engine):
        source_df=pd.read_sql(
            """
            SELECT EMPLOYEE_ID, DEPARTMENT FROM employee_db.EMPLOYEE_RAW
            """,
            mysql_engine
        )

        target_df=pd.read_sql(
            """
            SELECT EMPLOYEE_ID, DEPARTMENT FROM CURATED.CURATED_SCHEMA.DIM_EMP 
            """,
            databricks_engine
        )

        missing_records=source_df[
        ~source_df[["EMPLOYEE_ID","DEPARTMENT"]].isin(target_df[["EMPLOYEE_ID","DEPARTMENT"]])]

        return len(missing_records)

def test_department_data_truncation(mysql_engine,databricks_engine):
    """Validates the data truncation between source and target department data"""

    logger.info("Department data truncation validation started")

    missing_count=deprtment_data_truncation(mysql_engine,databricks_engine)

    try :
        assert missing_count==0,(
            "Department data truncation vcalidation Failed"
        )
    except AssertionError:
        logger.error(
            "Department Data truncation validation failed"
            f"Department Data truncation failed for {missing_count} records"
        )


### Data Truncation validatio  for JOB_TITLE

def job_title_truncation_validation(mysql_engine,databricks_engine):
    source_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, JOB_TITLE FROM employee_db.EMPLOYEE_RAW
        """,
        mysql_engine   
    )

    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, JOB_TITLE FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        """,
        databricks_engine    
    )

    missing_records=source_df[
        ~source_df[["EMPLOYEE_ID","JOB_TITLE"]].isin(target_df[["EMPLOYEE_ID","JOB_TITLE"]])
    ]

    return len(missing_records)

def test_job_title_data_truncation_validation(mysql_engine,databricks_engine):
    """Validates the data truncation validation between source and target for JOB_TITLE"""

    logger.info("Data Truncation Validation for JOB_TITLE started")

    missing_count=job_title_truncation_validation(mysql_engine,databricks_engine)

    try:
        assert missing_count==0,(
            "JOB_TITLE data truncation validation Failed"
        )
    except AssertionError:
        logger.error(
            "Data Truncation Validation for JOB_TITLE failed"
            f"JOB_TITLE Data truncation validation failed for {missing_count} records"
        )


### Data Truncation validation between source salary and target salary 

def salary_data_truncation_validation(mysql_engine,databricks_engine):
    source_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID,SALARY  FROM EMPLOYEE_DB.EMPLOYEE_RAW
        
        """,
        mysql_engine   
    )

    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, ORIGINAL_SALARY  FROM CURATED.CURATED_SCHEMA.DIM_EMP
        """,
        databricks_engine   
    )

    missing_records=source_df[
            ~source_df[["EMPLOYEE_ID","SALARY"]].isin(target_df[["EMPLOYEE_ID","ORIGINAL_SALARY"]])
        ]

    return len(missing_records)

def test_sal_data_truncation(mysql_engine,databricks_engine):
    """Validates the Salary Data truncation between source and target"""

    logger.info("Salary Data Trucation Started")

    missing_count=salary_data_truncation_validation(mysql_engine,databricks_engine)

    try:
        assert missing_count==0,(
            "Salary Data Truncatio validation Failed"
        )

    except AssertionError:
        logger.error(
            f"Salary Data truncation Failed"
            f"Salary Data Truncation Failed for {missing_count} records"
        )

def mobile_data_truncation_validation(mysql_engine,databricks_engine):
    source_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, COALESCE(MOBILE_NUMBER,EMAIL) AS PRIMARY_CONTACT FROM EMPLOYEE_DB.EMPLOYEE_RAW;
        """,
        mysql_engine
    )

    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, PRIMARY_CONTACT
        FROM CURATED.curated_schema.dim_emp;
        """,
        databricks_engine
    )

    missing_records=source_df[
        ~source_df[["EMPLOYEE_ID","PRIMARY_CONTACT"]].isin(target_df[["EMPLOYEE_ID","PRIMARY_CONTACT"]])
    ]

    return len(missing_records)

def test_mobile_number_data_truncation(mysql_engine,databricks_engine):
    """Va;idates the data trunatin between source and target Mobile_number"""

    logger.info("Mobiule number Validation Started")

    missing_count=mobile_data_truncation_validation(mysql_engine,databricks_engine)

    try:
        assert missing_count==0,(
            "Mobile Number Validation Failed"
        )

    except AssertionError:
        logger.error(
            "Mobile Number Validation Failed"
            f"Mobile Numner Validation Failed for total {missing_count} Records"
        )

### City Data Truncation Validation 

def city_data_truncation_Validation(mysql_engine,databricks_engine):
    source_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID,CITY FROM EMPLOYEE_DB.EMPLOYEE_RAW
        """,
        mysql_engine
    )

    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, CITY FROM CURATED.CURATED_SCHEMA.DIM_EMP
        """,
        databricks_engine
    )

    missing_records=source_df[
        ~source_df[["EMPLOYEE_ID","CITY"]].isin(target_df[["EMPLOYEE_ID","CITY"]])
    ]

    return len(missing_records)

def test_city_data_truncation(mysql_engine,databricks_engine):
    """Validates the data truncation between source city and target ciity"""

    logger.info("City Data trunation Validation started")

    missing_count=city_data_truncation_Validation(mysql_engine,databricks_engine)

    try:
        assert missing_count==0,(
            "City Data truncation validation failed"
        )
    except AssertionError:
        logger.error(
            "City Data Truncation failed"
            f"City data truncatij failed for {missing_count} records"
        )

def country_data_truncation(mysql_engine,databricks_engine):
    source_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, COUNTRY FROM EMPLOYEE_DB.EMPLOYEE_RAW
        """,
        mysql_engine
    )

    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, COUNTRY FROM CURATED.CURATED_SCHEMA.DIM_EMP 
        """,
        databricks_engine
    )

    missing_records=source_df[
        ~source_df[["EMPLOYEE_ID","COUNTRY"]].isin(target_df[["EMPLOYEE_ID","COUNTRY"]])
    ]

    return len(missing_records)

def test_country_data_truncation(mysql_engine,databricks_engine):
    """Validates the data truncation validation"""

    logger.info("Country Data Validation Started")

    missing_count=country_data_truncation(mysql_engine,databricks_engine)

    try:
        assert missing_count==0,(
            "City Data Truncation Validation"
        )
    except AssertionError:
        logger.error(
            "City Data Truncation Validation Failed"
            f"City Data truncation Validation Failed for {missing_count} "
        )