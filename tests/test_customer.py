# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

# import 
from ecommerce_pipeline.validate_customer import validate_customer 

def test_customer_exists():

    validate_customer_data = {
        "customer_id": 101,
        "name": "Alice Smith",
        "email": "alice@example.com"
    }

    result = validate_customer(validate_customer_data,"customer_id")

    assert result == True, f"Expected True for valid customer: {result}"

def test_customer_missing():

    validate_customer_data = {
        "customer_id": None,
        "name": "Alice Smith",
        "email": "alice@example.com"
    }
    
    result_2 = validate_customer(validate_customer_data,"customer_id")
    
    assert result_2 == False, f"Expected False for invalid customer: {result_2}"

def test_customer_is_integer():

    validate_customer_data = {
        "customer_id": "abc",
        "name": "Alice Smith",
        "email": "alice@example.com"
    }
        
    result_3 = validate_customer(validate_customer_data,"customer_id")
        
    assert result_3 == False, f"Expected False for invalid customer: {result_3}"