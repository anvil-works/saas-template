import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil import designer

# This module is a legacy design choice pre-layouts as PRODUCT_NAMES was used all over the place. Now it's probably worth removing and calling it only once in the homepagae layout.
if anvil.designer.in_designer:
  PRODUCT_NAMES = ["Personal"]
else:
  print("elsing")
  PRODUCT_NAMES = anvil.server.call("get_product_names")