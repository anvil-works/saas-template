import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from datetime import datetime

# The has_subscription takes a list object and checks whether the user's subscription is valid for the decorated function
# See Utils to see it in use
def has_subscription(subscription):
  return lambda user: user["subscription"] in subscription
  