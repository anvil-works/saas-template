import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil import designer

if anvil.designer.in_designer:
  PRODUCT_NAMES = ["Personal"]
else:
  PRODUCT_NAMES = anvil.server.call("get_product_names")