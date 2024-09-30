import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# This may need to be changed depending on the outcome of this discussion GitHub issue: 5467
if not anvil.designer.in_designer:
  PRODUCT_NAMES = anvil.server.call("get_product_names")
else:
  PRODUCT_NAMES = ["Personal"]