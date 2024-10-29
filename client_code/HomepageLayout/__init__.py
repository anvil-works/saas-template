from ._anvil_designer import HomepageLayoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

from ..StripePricing import StripePricing

from ..Stripe import PRODUCT_NAMES

class HomepageLayout(HomepageLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.check_upgrade_button()

    # TEMPLATE EXPLANATION ONLY - DELETE ROWS 22-23 WHEN YOU'RE READY
    self.TEMPLATE_EXPLANATION()

  def check_upgrade_button(self):
    self.user = anvil.users.get_user()
    if self.user:
      if self.user["subscription"] == "Free" or not self.user["subscription"]:
        self.upgrade_button.visible = True
      else:
        self.upgrade_button.visible = False
    else:
      self.upgrade_button.visible = False

 # TEMPLATE EXPLANATION ONLY - DELETE THIS WHEN YOU'RE READY    
  def TEMPLATE_EXPLANATION(self):
    if not anvil.designer.in_designer:
      if anvil.users.get_user() and anvil.users.get_user()["subscription"] in PRODUCT_NAMES and not anvil.users.get_user()["cancel_subscription_at_period_end"]:
        Notification("With your subscription set up, you can now use the calculator. Check the Users module in the template's server modules and the client code user_permissions module to see how the user permissions work.", title="Template Explanation", timeout=None, style="warning").show()
      elif anvil.users.get_user() and anvil.users.get_user()["cancel_subscription_at_period_end"]:
        Notification("You've cancelled your subscription and, once it expires, your user records subscription status will be updated.", title="Template Explanation", timeout=None, style="warning").show()
        Notification("That's the tour of the app template complete. Now it's time for you to begin adding your own Stripe account details and finding out how to make the app your own.", title="Template Explanation", timeout=None, style="warning").show()
        # Notification("That's the tour of the app template complete. Now it's time for you to begin adding your own Stripe account details and finding out how to make the app your own.", title="Template Explanation", timeout=None, style="warning").show()
      else:
        Notification("This is your SaaS product's main page. For this template, we've created a very simple calculator that requires a subscription to use. Try using the calculator.", title="Template Explanation", timeout=None, style="warning").show()

  def logout_navigation_link_click(self, **event_args):
    """This method is called when the component is clicked"""
    anvil.users.logout()

  def stripe_pricing_link_click(self, **event_args):
    """This method is called when the component is clicked"""
    alert(StripePricing(), large=True)
    self.check_upgrade_button()

