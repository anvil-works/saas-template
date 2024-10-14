from ._anvil_designer import AccountSettingsLayoutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AccountSettingsLayout(AccountSettingsLayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  
  def account_tab_button_click(self, **event_args):
      """This method is called when the component is clicked."""
      alert(AccountPanel(), title=anvil.users.get_user()["email"], dismissible=True, buttons=None, large=True)

  def subscription_tab_button_click(self, **event_args):
    """This method is called when the component is clicked."""
    alert(SubscriptionPanel())
