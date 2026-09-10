# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.convert_order import convert_order

def test_conver_order_output():

    dataset = [
        {
            "order_id": 1001,
            "customer_id": 501,
            "product": "Running Shoes",
            "price": "89.99",
            "quantity": "2"
        },
        {
            "order_id": 1004,
            "customer_id": 504,
            "product": "T-Shirt",
            "price": "-20.00",
            "quantity": "1"
        }
    ]
    final_list, final_report = convert_order(dataset)

    assert final_report["total_orders"] == 2
    assert final_report["successful_orders"] == 1
    assert final_report["missing_customers"] == 0
    assert final_report["invalid_price"] == 1
    assert final_report["invalid_quantity"] == 0
    assert final_report["duplicate_orders"] == 0
    print(final_list)
    assert final_list == [{
                "order_id": 1001,
                "customer_id": 501,
                "product": "Running Shoes",
                "price": 89.99,
                "quantity": 2,
                "order_total": (89.99*2)
            }]
