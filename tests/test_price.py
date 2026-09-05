# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.validate_price import validate_price

def test_price_exists():

    validate_price_data = {
        "customer_id": 101,
        "price": None,
        "email": "alice@example.com"
    }

    result = validate_price(validate_price_data,"price")

    assert result == False, f"Expected False for invalid price: {result}"