from ._anvil_designer import CalculatorTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..user_permissions import catch_permission_errors

class Calculator(CalculatorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  # Catch_permission_errors catches excpetions that are thrown by a user not being subscribed and gives them a notification to upgrade
  @catch_permission_errors
  # This function is a simple example function to show you functionality that is gated behind a paywall
  def calculate_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.number_1_textbox.input_text and self.number_2_textbox.input_text:
      percentage = str(anvil.server.call('calculate_percentage_of', self.number_1_textbox.input_text, self.number_2_textbox.input_text))
      self.answer_text.text = f"{self.number_1_textbox.input_text} is {percentage}% of {self.number_2_textbox.input_text}"
      self.answer_text.visible = True
      # TEMPLATE EXPLANATION ONLY - DELETE ROWS 27-28 WHEN YOU'RE READY
      Notification("Now you can use the calculator. Click the account button in the navbar to open the account settings.", title="Template Explanation", timeout=None, style="warning").show()
    else:
      Notification("Please enter two numbers.")

