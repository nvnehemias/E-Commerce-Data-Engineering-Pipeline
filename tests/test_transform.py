# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.transform_order import transform_order

def test_transform_does_not_exists():

    new_columns = ["column_1","column_2"]
    new_values = ["1"]

    result = transform_order(new_columns,new_values)

    assert result == False, f"Expected False for valid price: {result}"