import pandas as pd 
from logger import get_logger

logger = get_logger("data_quality","logs/data_quality.log")


##Validate no nulls present EXPERIENCE_YEARS in target dim_emp

def data_quality_experience_year_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, EXPERIENCE_YEARS FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EXPERIENCE_YEARS IS NULL
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_qaulity_experrience_check(databricks_engine):
    """Validates that there is no data qulity issues between EXPERIENCE_YEARS in target"""

    logger.info("EXPERIENCE YEARS Data quality check started ")

    exp_yrs_chk=data_quality_experience_year_check(databricks_engine)

    try:
        assert exp_yrs_chk==0,(
            "EXPERIENCE_YEAR data quality check Failed"
        )
    except AssertionError:
        logger.error(
            "EXPERIENCE_YEARS Data quality check got failed"
            f"EXPERIENCE_YEARS has total {exp_yrs_chk} as null "
        )
        raise


### Validate no nulls present INCREMENT_PERCENTAGE in target dim_emp

def data_quality_increment_percentage_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, INCREMENT_PERCENTAGE FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE INCREMENT_PERCENTAGE IS NULL
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_increment_percentage_check(databricks_engine):
    """Validates that there is no Data quality issues in INCREMENT_PERCENTAGE"""

    logger.info("INCREMENT_PERCENTAGE data quality Validation started")

    increment_perecentage_count=data_quality_increment_percentage_check(databricks_engine)

    try:
        assert increment_perecentage_count==0,(
            "INCREMENT_PERCENTAGE Dta quality check Failed"
        )
    except AssertionError:
        logger.error(
            "INCREMENT_PERCENTAGE Data quality Validation Failed"
            f"INCREMENT_PERCENTAGE in target contains total {increment_perecentage_count} with data qulity issues"
        )
        raise


## Validate no leading or trailing spaces present in EMPLOYEE_NAME in target dim_emp

def data_quality_employement_name_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, EMPLOYEE_NAME FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EMPLOYEE_NAME <> TRIM(EMPLOYEE_NAME);
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_employement_name_check(databricks_engine):
    """Validates that there is no data quality issiues in target EMPLOYEE_NAME column"""

    logger.info("EMPLOYEE_NAME Data quality validation started")

    employee_name_vali_check_count=data_quality_employement_name_check(databricks_engine)

    try:
        assert employee_name_vali_check_count==0,(
            "EMPLLOYEE_NAME Data quality check failed"
        )
    except AssertionError:
        logger.error(
            "EMPLOYEE_NAME DATA Quality validation failed"
            f"EMPLOYEE_NAME in target contains total {employee_name_vali_check_count} records with data quality issues"
        )
        raise

#### Validate no leading or trailing spaces present in GENDER in target dim_emp

def data_quality_gender_validation(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, GENDER FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE GENDER <> TRIM(GENDER)
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_gender_validation(databricks_engine):
    """Validates the data quakity issues in target GENDER column"""

    logger.info("GENDER data quality Validation started")

    gender_dq_check_cnt=data_quality_gender_validation(databricks_engine)

    try:
        assert gender_dq_check_cnt==0,(
            "GENDER data quality validation failed"
        )
    except AssertionError:
        logger.error(
            "GENDER Data quality validation failed"
            f"GENDER Column conatins total{gender_dq_check_cnt} records with data quality issues "
        )
        raise


### Validate no leading or trailing spaces present in DEPARTMENT in target dim_emp

def data_quality_department_vlidation(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, DEPARTMENT FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE DEPARTMENT <> TRIM(DEPARTMENT)
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_department_vlidation(databricks_engine):
    """Validate the data quality issues in DEPARTMENT Column in target"""

    logger.info("DEPARTMENT Data quality validation started")

    dept_data_qaulity_val_chk_cnt=data_quality_department_vlidation(databricks_engine)

    try:
        assert dept_data_qaulity_val_chk_cnt==0,(
            "Department Data Quality Validatio  failed"
        )
    except AssertionError:
        logger.error(
            "DEPARTMENT data quality Validation failed"
            f"department column has total {dept_data_qaulity_val_chk_cnt} records with data quality issues"
        )
        raise

### Validate no leading or trailing spaces present in CITY in target dim_emp

def data_quality_city_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, CITY FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE CITY <> TRIM(CITY)
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_city_check(databricks_engine):
    """Validates the data qulaity for the city column in target"""

    logger.info("Data quality check started for the CITY Column")

    city_dq_vali_chk_cnt=data_quality_city_check(databricks_engine)

    try :
        assert city_dq_vali_chk_cnt==0,(
            "Data Quality Validation failed for CITY column"
        )
    except AssertionError:
        logger.error(
            "Data quality validation failed for the CITY column "
            f"CITY column contains total {city_dq_vali_chk_cnt} records with data quality issues"
        )
        raise

### Validate no leading or trailing spaces present in COUNTRY in target dim_emp

def data_quality_country_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, COUNTRY FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE COUNTRY <> TRIM(COUNTRY)
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_country_check(databricks_engine):
    """ Validates the data quality for the COUNTRY column"""

    logger.info("Data quality validation for the COUNTRY column started")

    data_quality_country_cnt=data_quality_country_check(databricks_engine)

    try:
        assert data_quality_country_cnt ==0,(
            "Data Quality Validation for the country column failed"
        )
    except AssertionError:
        logger.error(
            "Data Quality Validation for the COUNTRY column failed"
            f"COUNTRY Column contains total {data_quality_country_cnt} records with data quality issues"
        )
        raise 

### Validate no double spaces present between first name and last name in EMPLOYEE_NAME in target dim_emp

def data_quality_employee_name_sapece_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, EMPLOYEE_NAME FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EMPLOYEE_NAME LIKE '%  %'
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_employee_name_sapece_check(databricks_engine):
    """Validates the data quality for the EMPLOYEE_NAME_SPACE"""

    logger.info("Data Quality Validation check started for the EMPLOYEE_NAME Space")

    emp_name_scpace_cnt_chk=data_quality_employee_name_sapece_check(databricks_engine)

    try:
        assert emp_name_scpace_cnt_chk==0,(
            "EMPLOYEE_NAME space validation failed for the spaces"
        )
    except AssertionError:
        logger.error(
            "EMPLOYEE_NAME space validation failed for the spaces"
            f"EMPLOYEE_NAME Contains total {emp_name_scpace_cnt_chk} records with the data quality issues"
        )
        raise

### Validate no blank values present in EMPLOYEE_NAME in target dim_emp

def data_qaulity_emp_name_blk_spc_check(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, EMPLOYEE_NAME FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE TRIM(EMPLOYEE_NAME) = ''
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_qaulity_emp_name_blk_spc_check(databricks_engine):
    """Validates that the no space issues in EMNPLOYEE_NAME"""

    logger.info("Data Quality Validation started for the EMPLOYEE_NAME with the spaces")

    emp_name_sapce_chk_cnt=data_qaulity_emp_name_blk_spc_check(databricks_engine)

    try:
        assert emp_name_sapce_chk_cnt==0,(
            "Data quality chack failed fro the EMPLOYEE_NAMEit contains the spaces"
        )
    except AssertionError:
        logger.error("Data quality failed for the EMPLOYEE_NAME eith spaces")
        raise


### Validate no blank values present in DEPARTMENT in target dim_emp

def data_qaulity_dept_blk_valu_check(databricks_engine):
    target_df=pd.read_sql(
        """
        
        SELECT EMPLOYEE_ID, DEPARTMENT FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE TRIM(DEPARTMENT) = ''
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_qaulity_dept_blk_valu_check(databricks_engine):
    """Validates that there is no blank value present oin DEPARTMENT Column"""

    logger.info("Data quality Validation started for the DEPRTMENT column for the blank space")

    dept_blk_cnt_chk=data_qaulity_dept_blk_valu_check(databricks_engine)

    try:
        assert dept_blk_cnt_chk==0,(
            "Data quality check for the DEPARTMENT for blank space failed"
        )
    except AssertionError:
        logger.error("Data Quality validation for the department with blank space failed")
        raise


### Validate no blank values present in JOB_TITLE in target dim_emp

def data_quality_job_title_blk_chk(databricks_engine):
    target_df=pd.read_sql(
        """
        SELECT EMPLOYEE_ID, JOB_TITLE FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE TRIM(JOB_TITLE) = '';        
        """,
        databricks_engine
    )

    return len(target_df)

def test_data_quality_job_title_blk_chk(databricks_engine):
    logger.error("Data quality check started for the JOB_TITLE with blank ")

    job_title_check_cnt=data_quality_job_title_blk_chk(databricks_engine)

    try:
        assert job_title_check_cnt==0(
            "Data Quality check for the JOB_TITLE with blank got failed"
        )
    except AssertionError:
        (
            "Data Quality check for the JOB_TITLE with blank got failed"
        )
        raise

def data_quality_city_blk_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, CITY
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE TRIM(CITY) = '';
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_city_blk_chk(databricks_engine):
    logger.info("Data quality check started for CITY with blank")

    city_check_cnt = data_quality_city_blk_chk(databricks_engine)

    assert city_check_cnt == 0, (
        "Data Quality check for CITY with blank got failed"
    )

def data_quality_country_blk_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, COUNTRY
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE TRIM(COUNTRY) = '';
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_country_blk_chk(databricks_engine):
    logger.info("Data quality check started for COUNTRY with blank")

    country_check_cnt = data_quality_country_blk_chk(databricks_engine)

    assert country_check_cnt == 0, (
        "Data Quality check for COUNTRY with blank got failed"
    )

def data_quality_primary_contact_blk_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, PRIMARY_CONTACT
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE TRIM(PRIMARY_CONTACT) = '';
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_primary_contact_blk_chk(databricks_engine):
    logger.info("Data quality check started for PRIMARY_CONTACT with blank")

    primary_contact_check_cnt = data_quality_primary_contact_blk_chk(
        databricks_engine
    )

    assert primary_contact_check_cnt == 0, (
        "Data Quality check for PRIMARY_CONTACT with blank got failed"
    )

def data_quality_gender_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, GENDER
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE GENDER IS NOT NULL
          AND GENDER NOT IN ('MALE', 'Female');
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_gender_chk(databricks_engine):
    logger.info("Data quality check started for GENDER values")

    gender_check_cnt = data_quality_gender_chk(databricks_engine)

    assert gender_check_cnt == 0, (
        "Data Quality check for GENDER failed: "
        "Invalid gender values found"
    )

def data_quality_employment_status_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, EMPLOYMENT_STATUS
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EMPLOYMENT_STATUS NOT IN ('Active', 'Inactive');
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_employment_status_chk(databricks_engine):
    logger.info("Data quality check started for EMPLOYMENT_STATUS")

    employment_status_check_cnt = data_quality_employment_status_chk(
        databricks_engine
    )

    assert employment_status_check_cnt == 0, (
        "Data Quality check for EMPLOYMENT_STATUS failed: "
        "Inconsistent spellings or case variants found"
    )

def data_quality_hire_date_format_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, HIRE_DATE
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE HIRE_DATE IS NOT NULL
          AND HIRE_DATE NOT RLIKE '^[0-3][0-9]-[01][0-9]-[0-9]{4}$';
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_hire_date_format_chk(databricks_engine):
    logger.info("Data quality check started for HIRE_DATE format")

    hire_date_format_cnt = data_quality_hire_date_format_chk(
        databricks_engine
    )

    assert hire_date_format_cnt == 0, (
        "Data Quality check failed: HIRE_DATE is not in DD-MM-YYYY format"
    )

def data_quality_hire_date_valid_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, HIRE_DATE
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE HIRE_DATE IS NOT NULL
          AND TRY_TO_DATE(HIRE_DATE, 'dd-MM-yyyy') IS NULL;
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_hire_date_valid_chk(databricks_engine):
    logger.info("Data quality check started for HIRE_DATE calendar validity")

    hire_date_valid_cnt = data_quality_hire_date_valid_chk(
        databricks_engine
    )

    assert hire_date_valid_cnt == 0, (
        "Data Quality check failed: Invalid calendar dates found in HIRE_DATE"
    )

def data_quality_primary_contact_format_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, PRIMARY_CONTACT
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE PRIMARY_CONTACT IS NOT NULL
          AND NOT PRIMARY_CONTACT RLIKE r'^\\+?[0-9 -]{7,15}$'
          AND NOT PRIMARY_CONTACT RLIKE r'^[^@ ]+@[^@ ]+\\.[^@ ]+$';
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_primary_contact_format_chk(databricks_engine):
    logger.info("Data quality check started for PRIMARY_CONTACT format")

    primary_contact_format_cnt = data_quality_primary_contact_format_chk(
        databricks_engine
    )

    assert primary_contact_format_cnt == 0, (
        "Data Quality check failed: Invalid phone number or email found "
        "in PRIMARY_CONTACT"
    )

def data_quality_employee_name_digit_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, EMPLOYEE_NAME
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EMPLOYEE_NAME RLIKE '[0-9]';
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_employee_name_digit_chk(databricks_engine):
    logger.info("Data quality check started for EMPLOYEE_NAME digits")

    employee_name_digit_cnt = data_quality_employee_name_digit_chk(
        databricks_engine
    )

    assert employee_name_digit_cnt == 0, (
        "Data Quality check failed: Digits found in EMPLOYEE_NAME"
    )

def data_quality_manager_id_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT E.EMPLOYEE_ID, E.MANAGER_ID
        FROM CURATED.CURATED_SCHEMA.DIM_EMP E
        LEFT JOIN CURATED.CURATED_SCHEMA.DIM_EMP M
            ON E.MANAGER_ID = M.EMPLOYEE_ID
        WHERE E.MANAGER_ID IS NOT NULL
          AND M.EMPLOYEE_ID IS NULL;
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_manager_id_chk(databricks_engine):
    logger.info("Data quality check started for MANAGER_ID")

    manager_id_check_cnt = data_quality_manager_id_chk(databricks_engine)

    assert manager_id_check_cnt == 0, (
        "Data Quality check failed: MANAGER_ID does not exist "
        "as EMPLOYEE_ID in DIM_EMP"
    )


def data_quality_self_manager_chk(databricks_engine):
    target_df = pd.read_sql(
        """
        SELECT EMPLOYEE_ID, MANAGER_ID
        FROM CURATED.CURATED_SCHEMA.DIM_EMP
        WHERE EMPLOYEE_ID = MANAGER_ID;
        """,
        databricks_engine
    )

    return len(target_df)


def test_data_quality_self_manager_chk(databricks_engine):
    logger.info("Data quality check started for self-manager validation")

    self_manager_check_cnt = data_quality_self_manager_chk(
        databricks_engine
    )

    assert self_manager_check_cnt == 0, (
        "Data Quality check failed: Employee is assigned as their own manager"
    )