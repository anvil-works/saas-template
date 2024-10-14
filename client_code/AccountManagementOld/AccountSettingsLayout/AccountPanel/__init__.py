from ._anvil_designer import AccountPanelTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AccountPanel(AccountPanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def reset_password_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.send_password_reset_email(self.user["email"])
    alert("A password reset email has been sent to your inbox.", title="Password reset email sent")
