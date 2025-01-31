from ._anvil_designer import AccountManagementTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .ChangeName import ChangeName
from .ChangeEmail import ChangeEmail
from .DeleteAccountAlert import DeleteAccountAlert

class AccountManagement(AccountManagementTemplate):
  def __init__(self, **properties):
    self.user = anvil.users.get_user()
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens

  def change_name_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    new_name = alert(ChangeName(item=self.user["name"]), title="Change name", buttons=None, dismissible=True, large=True)
    if new_name:
      self.user = anvil.server.call('change_name', new_name)
      self.refresh_data_bindings()

    # TEMPLATE EXPLANATION ONLY - DELETE THIS WHEN YOU'RE READY
    Notification("Now that you've seen how the template handles editing user information, let’s explore how users can cancel a subscription. We'll do this using the Stripe Customer Portal we set up while setting up with this template. Click the Manage Subscription button, cancel your subscription and go back to this app's homepage.", title="Template Explanation", timeout=None, style="warning").show()
    Notification("The webhooks set up earlier will keep user records in this app synchronized with customer records in Stripe. For details on how this template manages cancellations and deletions, check out our full guide at https://anvil.works/learn/tutorials/using-saas-template.", title="Template Explanation", timeout=None, style="warning").show()
    Notification("To wrap up, try deleting your account. This will log you out, remove all user information from both this app and Stripe, and complete your tour of the app’s functionality.", title="Template Explanation", timeout=None, style="warning").show()

  def change_email_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    new_email = alert(ChangeEmail(item=self.user["email"]), title="Change email", buttons=None, dismissible=True, large=True)
    if new_email:
      self.user = anvil.server.call('change_email', new_email)
      self.refresh_data_bindings()

  def reset_password_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    if confirm("Resetting your password will send a reset email to your inbox and log you out. Do you want to continue?"):
      anvil.users.send_password_reset_email(self.user["email"])
      alert("A password reset email has been sent to your inbox.", title="Password reset email sent")
      anvil.users.logout()
      open_form("LoginPage")

  def delete_account_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    if alert(DeleteAccountAlert(), buttons=None, large=True):
      anvil.server.call('delete_user')
      anvil.users.logout()
      open_form('LoginPage')

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    # TEMPLATE EXPLANATION ONLY - DELETE THIS WHEN YOU'RE READY
    Notification("Welcome to your app's account management page—a solid foundation for self-service account management that you can customize for your users. Start by updating your name.", title="Template Explanation", timeout=None, style="warning").show()