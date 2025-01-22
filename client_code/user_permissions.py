import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import Notification, alert
  
# A decorator function to display notifications that encourage people to upgrade
def catch_permission_errors(func):
  def wrapper(self, *args, **kargs):
    try:
      return func(self)
    except anvil.server.PermissionDenied:
      # TEMPLATE EXPLANATION ONLY - DELETE THIS NOTIFICATION WHEN YOU'RE READY
      Notification("Without a subscription, the calculator's function fails and users are shown a notification asking them to upgrade.", title="Template Explanation", timeout=None, style="warning").show()
      
      Notification("Please upgrade your subscription to use this functionality.", title="Please upgrade your subscription", timeout=None).show()
      
      # TEMPLATE EXPLANATION ONLY - DELETE THIS NOTIFICATION WHEN YOU'RE READY
      Notification("Click on the upgrade button in the top left to be taken to Stripe's pricing page for this app", title="Template Explanation", timeout=None, style="warning").show()
    except anvil.users.AuthenticationFailed:
      Notification("Please log in to use this functionality.", title="Please log in", timeout=3).show()
  wrapper.__name__ = func.__name__ # Preserve the name of the decorated function
  return wrapper
  
  