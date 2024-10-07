from ._anvil_designer import AccountPageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..AccountSettingsLayout.AccountPanel import AccountPanel

class AccountPage(AccountPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def settings_button_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.raise_event("x-close-alert")
    alert(AccountPanel(), title=anvil.users.get_user()["email"], dismissible=True, buttons=None, large=True)

  def logout_button_click(self, **event_args):
    """This method is called when the component is clicked."""
    anvil.users.logout()
    open_form('LoginPage')
    self.raise_event("x-close-alert")

  # TEMPLATE EXPLANATION ONLY - DELETE ROWS 29-32 WHEN YOU'RE READY
  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    Notification("The AccountPage is a simple beginning to self-serve account management and a good foundation for you to build on for your users.\n\nClick the Settings button next.", title="Template Explanation", timeout=None, style="warning").show()
