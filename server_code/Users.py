import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .StripeFunctions import delete_stripe_customer

# @anvil.server.callable's require_user argument takes either a Boolean value. If the Boolean is True, the user has permission to run the decorated function.
# We can pass require_user a function which evaluates to True or False but we cannot pass any arguments to that function
# To get around this, we can pass require_user a higher order function - user_has_subscription - which returns an evaluated function verify_subscription
# user_has_subscription can accept arguments, use them in verify_subscription and return the evaluated verify_subscription function
# so, if we call @anvil.server.callable(require_user=user_has_subscription(["pro"])), the decorator calls user_has_subscription which returns an evaluated function object that require_user can use
# verify_subscription receives the currently logged-in user object from @anvil.server.callable automatically
# See the Product Server Module to see it in use
def user_has_subscription(allowed_subscriptions):
    def verify_subscription(user):
        # Return true if user has subscription in allowed subscriptions
        return user["subscription"] and user["subscription"] in allowed_subscriptions
    return verify_subscription

@anvil.server.callable(require_user=True)
def change_name(name):
  user = anvil.users.get_user()
  user["name"] = name
  return user

@anvil.server.callable(require_user=True)
def change_email(email):
  user = anvil.users.get_user()
  user["email"] = email
  return user

@anvil.server.callable(require_user=True)
def delete_user():
  user = anvil.users.get_user()
  if user["stripe_id"]:
    delete_stripe_customer(user["stripe_id"])
  user.delete()
  

