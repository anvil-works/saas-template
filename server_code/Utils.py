import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .Subscriptions import has_subscription

# Here's an example of a function that would require a paid subsciption
@anvil.server.callable(require_user=has_subscription(["personal", "pro"]))
def calculate_percentage_of(number, total_number):
    percentage = (number / total_number) * 100
    return percentage