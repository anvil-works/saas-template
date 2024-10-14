from ._anvil_designer import ChangeNameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ChangeName(ChangeNameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def save_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('change_name', self.name_text_box.input_text)
    # TEMPLATE EXPLANATION ONLY - DELETE ROWS 20-21 WHEN YOU'RE READY
    Notification("This calls the change_name function in the Users server module.", title="Template Explanation", timeout=None, style="warning").show()
    self.raise_event("x-close-alert", value=self.name_text_box.input_text)

