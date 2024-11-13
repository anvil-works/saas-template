import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .Users import has_subscription

# Here's an example of a function that would require a paid subsciption
@anvil.server.callable(require_user=has_subscription(anvil.users.get_user(), ["personal"]))
def calculate_percentage_of(number, total_number):
    percentage = (int(number) / int(total_number)) * 100
    return percentage