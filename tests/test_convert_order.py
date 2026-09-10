# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.convert_order import convert_order

def test_convert_order_output():

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
    
    assert final_list == [{
                "order_id": 1001,
                "customer_id": 501,
                "product": "Running Shoes",
                "price": 89.99,
                "quantity": 2,
                "order_total": (89.99*2)
            }]

def missing_customers():

    dataset = [
            {
                "order_id": 1001,
                "product": "Running Shoes",
                "price": "89.99",
                "quantity": "2"
            }
        ]

    final_list_2, final_report_2 = convert_order(dataset)

    for i in range(len(dataset)):
    
        assert final_report_2["total_orders"] == 1
        assert final_report_2["successful_orders"] == 0
        assert final_report_2["missing_customers"] == 1
        assert final_report_2["invalid_price"] == 0
        assert final_report_2["invalid_quantity"] == 0
        assert final_report_2["duplicate_orders"] == 0

    assert final_list_2 == []

def invalid_quantity_check():

    dataset_3 = [
            {
                "order_id": 1001,
                "customer_id": 501,
                "product": "Running Shoes",
                "price": "89.99",
                "quantity": "0"
            },
            {
                "order_id": 1001,
                "customer_id": 501,
                "product": "Running Shoes",
                "price": "89.99",
                "quantity": "1"
            }
        ]

    final_list_3, final_report_3 = convert_order(dataset_3)

    assert final_report_3["total_orders"] == 2
    assert final_report_3["successful_orders"] == 1
    assert final_report_3["missing_customers"] == 0
    assert final_report_3["invalid_price"] == 0
    assert final_report_3["invalid_quantity"] == 1
    assert final_report_3["duplicate_orders"] == 0

    assert final_list_3 == [
        {
            "order_id": 1001,
            "customer_id": 501,
            "product": "Running Shoes",
            "price": 89.99,
            "quantity": 1,
            "order_total": 89.99
        }
    ]