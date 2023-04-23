# Bank Recommendation API Documentation

- This API is used to get the best *7* services/products the bank can offer.
- API Input:
    - `employee_index`: "A active, B ex employed, F filial, N not employee, P passive",
    - `sex`: "V Male or H Female",
    - `new_customer_index`: "1 if the customer registered in the last 6 months. 0 if not.",
    - `first_primary`: "1 (First/Primary), 99 (Primary customer during the month but not at the end of the month)",
    - `customer_type`: "Customer type at the beginning of the month ,1 (First/Primary customer), 2 (co-owner ),P (Potential),3 (former primary), 4(former co-owner)",
    - `customer_relation_type`: "Customer relation type at the beginning of the month, A (active), I (inactive), P (former customer),R (Potential)",
    - `residence_index`: "Residence index (S (Yes) or N (No) if the residence country is the same than the bank country)",
    - `foreigner_index`: "Foreigner index (S (Yes) or N (No) if the customer`s birth country is different than the bank country)",
    - `spouse_index`: "Spouse index. 1 if the customer is spouse of an employee",
    - `deceased_index`: "Deceased index. (S (Yes) or N (No))",
    - `address_type`: "Address type. 1, primary address",
    - `activity_index`: "Activity index (1, active customer; 0, inactive customer)",
    - `segmentation`: "segmentation: 01 - VIP, 02 - Individuals 03 - college graduated",
    - `customer_country_residence`: "Customer`s Country residence",
    - `customer_channel`: "Channel used by the customer to join",
    - `age`: "Age",
    - `seniority`: "Customer seniority (in months)",
    - `rent`: "Gross income of the household"

- API Output options (Only 7 products are returned):
    - `Current Accounts`, 
    - `Derivada Account`, 
    - `Payroll Account`, 
    - `Junior Account`, 
    - `Más Particular Account`, 
    - `Particular Account`, 
    - `Particular Plus Account`, 
    - `Short-term Deposits`, 
    - `Medium-term Deposits`, 
    - `Long-term Deposits`, 
    - `e-account`,
    - `Funds`, 
    - `Mortgage`, 
    - `Pensions`, 
    - `Loans`, 
    - `Taxes`, 
    - `Credit Card`, 
    - `Securities`, 
    - `Home Account`, 
    - `Payroll`, 
    - `Pensions`, 
    - `Direct Debit`

- API URL:
    > POST: `http://127.0.0.1:5000/recommend/`

------

- 1st Example

    **Request Body**
    ```json
    {
        "employee_index":"N",
        "sex":"V",
        "new_customer_index":"1",
        "first_primary":"1",
        "customer_type":"1",
        "customer_relation_type":"I",
        "residence_index":"S",
        "foreigner_index":"N",
        "spouse_index":"S",
        "deceased_index":"N",
        "address_type":"1",
        "activity_index":"1",
        "segmentation":"02 - Individuals",
        "customer_country_residence":"BZ",
        "customer_channel":"KHP",
        "age":"25",
        "seniority":"34",
        "rent":"111404.91"
    }
    ```

    **Response Message**
    ```json
    {
        "recommendation": [
            "Current Accounts",
            "Payroll",
            "Direct Debit",
            "Pensions",
            "Payroll Account",
            "e-account",
            "Securities"
        ]
    }
    ```

------

- 2nd Example

    **Request Body**
    ```json
    {
        "employee_index":"F",
        "sex":"H",
        "new_customer_index":"0",
        "first_primary":"1",
        "customer_type":"3.0",
        "customer_relation_type":"P",
        "residence_index":"N",
        "foreigner_index":"S",
        "spouse_index":"N",
        "deceased_index":"S",
        "address_type":"1",
        "activity_index":"1",
        "segmentation":"03 - College Graduated",
        "customer_country_residence":"BZ",
        "customer_channel":"LV",
        "age":"23",
        "seniority":"34",
        "rent":"56438.19"
    }
    ```

    **Response Message**
    ```json
    {
        "recommendation": [
            "Current Accounts",
            "Direct Debit",
            "Pensions",
            "Payroll",
            "Payroll Account",
            "e-account",
            "Credit Card"
        ]
    }
    ```

------

- 3rd Example

    **Request Body**
    ```json
    {
        "employee_index":"S",
        "sex":"V",
        "new_customer_index":"1",
        "first_primary":"99",
        "customer_type":"P",
        "customer_relation_type":"R",
        "residence_index":"N",
        "foreigner_index":"N",
        "spouse_index":"N",
        "deceased_index":"N",
        "address_type":"1",
        "activity_index":"1",
        "segmentation":"01 - VIP",
        "customer_country_residence":"PR",
        "customer_channel":"KAN",
        "age":"45",
        "seniority":"34",
        "rent":"11140454.91"
    }
    ```

    **Response Message**
    ```json
   {
        "recommendation": [
            "Current Accounts",
            "Long-term Deposits",
            "Direct Debit",
            "Credit Card",
            "e-account",
            "Pensions",
            "Payroll"
        ]
    }
    ```

------

