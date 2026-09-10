# importing libraries 
import sys 
from pathlib import Path

# Adding proejct root to obtain correct path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))

from ecommerce_pipeline.convert_order import convert_order

