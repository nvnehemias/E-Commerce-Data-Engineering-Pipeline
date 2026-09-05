# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.validate_price import validate_price

def test_price_does_exists():

    validate_price_data = {
        "customer_id": 101,
        "price": 55.00,
        "email": "alice@example.com"
    }

    result = validate_price(validate_price_data,"price")

    assert result == True, f"Expected True for valid price: {result}"

def test_price_does_not_exists():

    validate_price_data = {
        "customer_id": 101,
        "price": None,
        "email": "alice@example.com"
    }

    result_2 = validate_price(validate_price_data,"price")

    assert result_2 == False, f"Expected False for non-existent price: {result_2}"

def test_price_less_than_zero():

    validate_price_data = {
        "customer_id": 101,
        "price": -20.00,
        "email": "alice@example.com"
    }

    result_3 = validate_price(validate_price_data,"price")

    assert result_3 == False, f"Expected False for invalide price: {result_3}"


def test_price_integer():

    validate_price_data = {
        "customer_id": 101,
        "price": "abc",
        "email": "alice@example.com"
    }

    result_4 = validate_price(validate_price_data,"price")

    assert result_4 == False, f"Expected False for integer price: {result_4}"