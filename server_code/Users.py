import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .StripeFunctions import delete_stripe_customer


@anvil.server.callable(require_user=True)
def change_name(name):
  user = anvil.users.get_user()
  user["name"] = name

@anvil.server.callable(require_user=True)
def change_email(email):
  user = anvil.users.get_user()
  user["email"] = email

@anvil.server.callable(require_user=True)
def delete_user():
  user = anvil.users.get_user()
  if user["stripe_id"]:
    delete_stripe_customer(user["stripe_id"])
  user.delete()

