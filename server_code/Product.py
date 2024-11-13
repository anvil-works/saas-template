import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .Users import has_subscription

# The has_subscription takes a list object and checks whether the user's subscription is valid for the decorated function
# See the Product Server Module to see it in use
def has_subscription(user, allowed_subscriptions):
  return user["subscription"] and user["subscription"] in allowed_subscriptions