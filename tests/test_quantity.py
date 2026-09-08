# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.validate_quantity import validate_quantity

def test_quantity_zero():

    validate_quantity_data = {
            "customer_id": 101,
            "quantity": 0,
            "email": "alice@example.com"
        }
    
    result = validate_quantity(validate_quantity_data,"quantity")

    assert result == False, f"Expected False for valid price: {result}"

def test_quantity_negative():

    validate_quantity_data = {
            "customer_id": 101,
            "quantity": -10,
            "email": "alice@example.com"
        }
    
    result_2 = validate_quantity(validate_quantity_data,"quantity")

    assert result_2 == False, f"Expected False for valid price: {result_2}"