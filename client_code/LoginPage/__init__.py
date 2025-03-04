from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Calculator import Calculator

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.login_with_form(allow_cancel=True, show_signup_option=True, allow_remembered=True)
    if user:
      open_form('Calculator')

  # TODO check if this works in init, move if it does
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if anvil.users.get_user():
      open_form('Calculator')
    # TEMPLATE EXPLANATION ONLY - DELETE THIS ELSE BRANCH WHEN YOU'RE READY
    else:
      Notification("Welcome to Anvil's SaaS template. For information on how to use this template, see our guide here: <a href='https://anvil.works/learn/tutorials/using-saas-template'>https://anvil.works/learn/tutorials/using-saas-template</a>", title="Getting Started", timeout=None, style="warning").show()
      Notification("Here's your SaaS app's login page. To start click login and then signup for an account.", title="Template Explanation", timeout=None, style="warning").show()