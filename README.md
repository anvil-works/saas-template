# Welcome to Anvil's SaaS Template

[Anvil's SaaS (Software as a Service) template](https://anvil.works/build#clone:SUTICB6NGVZM7J5S=CB3DXR7V65FYL6UQOF2VQF5L) is a solid starting point and foundation for your subscription-based SaaS product. This template uses [Stripe's](https://stripe.com) API for subscription management, and includes simplified user permissions for you to use throughout your app. It's an ideal starting point for your project.

> [Stripe](https://stripe.com) provides tools for businesses to accept, manage, and process payments online and in person, offering features like customizable APIs, fraud prevention, subscription billing, and global currency support.

## Contents

In this guide, we’ll walk through the key components of the template, covering:

- **[Introduction](#introduction)**: Briefly learn about Anvil and the benefits of using this template.
- **[Prerequisites](#prerequisites)**: What you’ll need to get started.
- **[Template Structure](#understanding-the-templates-structure)**: A high-level overview of the app’s architecture and Stripe integration.
- **[Template Setup](#setting-up-the-template)**: Step-by-step instructions to get the template up and running with your account.
- **[Testing The App](#testing-the-app)**: Test the integration and explore the template’s functionality from a user’s perspective. 
- **[Make The app Your Own](#making-the-app-your-own)**: With the integration set up, it's time to make the app your own.

## Introduction

### Anvil

If you're new here, welcome! [Anvil](/) is a platform for building full-stack web apps with nothing but Python. No need to wrestle with JS, HTML, CSS, Python, SQL and all their frameworks – just **build it all in Python**.

You're going to need to know the basics of Anvil before using this template, so I'd recommend following our [10-minute intro tutorial](https://anvil.works/learn/tutorials/feedback-form). This should give you enough knowledge to begin using the SaaS template.

### Why use Anvil's SaaS template?

This template is a solid foundation for building your own SaaS app. It gives you:

- Full [Stripe](https://stripe.com) payment and checkout
- Subscription management synced with the app
- Account management synced with Stripe
- Easy-to-configure user permissions

Overall, it's an ideal starting point for your project.

## Prerequisites

To follow this guide you will need the following:

1. An understanding of Python
2. A [Stripe account](https://dashboard.stripe.com/login)
3. Basic knowledge of Anvil (a great place to start is with Anvil's [Feedback form tutorial](https://anvil.works/learn/tutorials/feedback-form))

## Understanding the template's structure

The template is divided into two main parts: the Stripe integration and the Anvil app. Stripe manages payments, subscriptions, and invoicing, while the Anvil app handles user authentication and permissions.

The app relies on the following Stripe features:

- [Customer Portals](https://docs.stripe.com/customer-management) - allows our customers to self-manage their payment details, invoices, and subscriptions in one place.
- [Pricing Tables](https://docs.stripe.com/payments/checkout/pricing-table) - displays our prices, configured easily from our Stripe dashboard and takes users into Stripes checkout flow.
- [APIs](https://docs.stripe.com/api) - to send data and requests to our Stripe account.
  - [Retrieve price list](https://docs.stripe.com/api/prices/list)
  - [Retrieve a customer](https://docs.stripe.com/api/customers/retrieve)
  - [Cancel a subscription](https://docs.stripe.com/api/subscriptions/cancel)
  - [Delete a customer](https://docs.stripe.com/api/customers/delete)
- [Webhooks](https://docs.stripe.com/webhooks) - to send data to our Anvil app when an event happens in Stripe.
  - `customer.subscription.updated`
  - `customer.created`

Here's an API flow to help visualise the integration:

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/api-call-diagram.png" width="700px"/>

And here's a user flow diagram to visualise the functionality available to the end user:

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/user-flow-diagram.png" width="700px"/>

---

## Setting up the template

This section will guide you through getting started with the template, understanding its features, and further developing it to suit your needs.
  
Let's get started!

### Step 1 - Cloning The Template

Start by cloning the template app with the following link:
https://anvil.works/build#clone:SUTICB6NGVZM7J5S=CB3DXR7V65FYL6UQOF2VQF5L

### Step 2 - Stripe Account Setup

Next, we'll set up our Stripe account. [Register for a Stripe account](https://dashboard.stripe.com/login) and login. Then enter your [business details](https://support.stripe.com/questions/business-information-requirements-to-use-stripe?locale=en-GB) to start capturing recurring revenue (or skip this step if you're only going to use [Stripe's test mode](https://stripe.com/docs/test-mode?locale=en-GB)). Lastly, activate Stripe's [test mode](https://stripe.com/docs/test-mode?locale=en-GB).

### Step 3 - Add The API Key

For the integration to work, we need to add your Stripe API key to the app. You can find your keys by clicking on "Developers", on the bottom left corner of the Stripe dashboard, and going to the API keys tab.

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/developers-button-stripe.png" width="400px"/>

Copy your [Stripe account's Secret key](https://stripe.com/docs/keys) and, in the SaaS template app's [App Secrets](https://anvil.works/docs/security/encrypting-secret-data), set the value of "stripe\_test\_api\_key" to your key.

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/app-secrets-location.png" width="450px"/>

### Step 4 - Creating A Pricing Table

Next, we need to create a pricing table for our customers to use. Start in the Anvil app editor, [publish this app](https://anvil.works/docs/deployment-new-ide/quickstart) and take a copy of the URL - we'll use this in later in this step.

In the Stripe dashboard, [navigate to the Products catalogue](https://dashboard.stripe.com/test/products?active=true), select the [Pricing tables tab](https://dashboard.stripe.com/test/pricing-tables), and create a [pricing table](https://stripe.com/docs/payments/checkout/pricing-table).

1. Click on the textbox under "Products" and select "Add new product". <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/add-a-product.png" width="600px"/>
4. Name your product 'Personal', give it a [price](https://stripe.com/docs/products-prices/how-products-and-prices-work#what-is-a-price) and save it by clicking 'Add product'. Then, click 'Continue' onto the next step. 
5. In the Payment settings, under "Confirmation page", select "Don't show confirmation page" and enter your **published app's URL**. <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/pricing-table.png" width="800px"/>


### Step 5 - Adding The Pricing Table To Your App

Stripe's website should take you to your [pricing table's page (if not, follow this link and select your pricing table)](https://dashboard.stripe.com/test/pricing-tables). Now, we'll embed the pricing table in our SaaS app.

1. Copy the code for the pricing table. <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/stripe-dashboard-pricing-table-code.png" width="800px"/>
2. Open the StripePricing Form in the Anvil Editor. Then [edit the custom HTML](https://anvil.works/docs/ui/components/forms#HTML-Forms-&-Custom-HTML-Forms) by clicking the three dots at the top of the designer. <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/edit-html-button.png" width="800px"/>
3. Paste the code into the StripePricing Form's custom HTML.
4. Lastly, add `anvil-name="stripe-pricing-table"` to the `stripe-pricing-table` tag. The final HTML should look like this:

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/stripe-pricing-html.png" width="800px"/>

---

### Step 6 - Setting Up The Webhooks

We need Stripe to tell us when a new customer is created and when their subscription is updated so we can update our Users table with the Stripe subscription details. We'll use [webhooks](https://www.redhat.com/en/topics/automation/what-is-a-webhook) to do this. [There is a guide to setting up webhooks in Stripe here](https://docs.stripe.com/webhooks/quickstart) but let me give you brief instructions.

#### Customer Created

1. Open the [Webhooks page](https://dashboard.stripe.com/test/webhooks) in Stripe by selecting the "Developers" link in the bottom left and navigating to the webhooks tab. <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/developers-webhook-dashboard.png" width="700px"/>
2. Click the "Create an event destination" button.
3. Set the endpoint URL to your published app's URL with "/_/api/stripe/stripe_customer_created" added to the end - i.e. "https://my-saas.anvil.app/_/api/stripe/stripe\_customer\_created". <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/endpoint-url.png" width="600px"/>
4. Then click "+ select events" and select "customer.created" under events to listen for. <img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/searching-events.png" width="600px"/>
5. From now on, this will call the `stripe_customer_created` function in your Anvil app's StripeFunctions module when a customer is created. Here's an image of the set-up webhook:</br><img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/webhook-setup.png" width="500px"/>

#### Subscription Updated

1. Add another endpoint in Stripe.
2. Set the endpoint URL to your published app's URL with "\/_/api/stripe/stripe\_subscription\_updated" added to the end i.e. "https://my-saas.anvil.app/\_/api/stripe/stripe\_subscription\_updated"
3. Then select "customer.subscription.updated" under events to listen for.
4. From now on, this will call the `stripe_subscription_updated` function in the StripeFunctions Server Module every time a customer is created.

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/finished-webhooks.png" width="600px"/>

### Step 7 - Setting Up The Customer Portal

Let's quickly set up a way for users to manage their subscription. Go to the Stripe dashboard and use the search bar at the top to find the customer portal screen.

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/customer-portal-location.png" width="800px"/>

Set up a [customer portal](https://dashboard.stripe.com/settings/billing/portal), activate the test link and copy it.

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/customer-portal-setup.png" width="800px"/>

Then open the SaaS app's AccountManagement form and point the "manage\_subscription\_link" component's URL to the copied link:

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/manage-subscription-button.png" width="800px"/>

We're going to let users manage their email address from the Account page of our app, so we'll disable the ability for users to change their email in their customer portal. The SaaS template syncs email updates with Stripe automatically. Back in the [customer portal](https://dashboard.stripe.com/settings/billing/portal) config page, uncheck the "Email address" checkbox under customer information:

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/customer-portal-email-checkbox.png" width="800px"/>

With these steps completed, your Stripe integration is ready for testing.

---

## Testing The App

The template has a number of [Notifications](https://anvil.works/docs/client/alerts-and-notifications#notifications) which will guide you through testing the app as a user. This will both test the integration we've set up and let you experience what the app is like as a user. [Run the app](https://anvil.works/docs/editor#the-anvil-editor) and follow along with the in-app instruction notifications.

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/notification-example.png" width="800px"/>

Here's a user flow diagram for you to see all the actions you can take with the template:

<img src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/user-flow-diagram.png" width="600px"/>

---

---

## Making The App Your Own

Now that your Stripe integration is set up and you've experienced the app from a user's perspective, it's time to make this app your own.

### Step 1 - Remove The Template Notifications

First, we can search (_ctrl+shift+F_) for the "# TEMPLATE EXPLANATION ONLY" comments and delete the relevant code below.

### Step 2 - Using User Permissions

For a SaaS app to earn money, you'll want to have premium features that are restricted to paid users on specific plans - this is where user permissions come in.

#### What's Included With The Template

The template comes with a bespoke function and decorator designed to simplify managing user permissions:

- `user_has_subscription`: A function that works with [`@anvil.server.callable`](https://anvil.works/docs/api/anvil.server.html#callable). It verifies whether the user's subscription is included in the list of subscriptions authorized to use the function decorated by `@anvil.server.callable`. If permission is denied, a [`PermissionDenied`](https://anvil.works/docs/api/anvil.server#PermissionDenied) exception is thrown.
- `@catch_permission_errors`: A decorator that catches any [`anvil.server.PermissionDenied`](https://anvil.works/docs/api/anvil.server#PermissionDenied) exceptions raised by the decorated client-side function. If permission is denied, it prompts the user to upgrade their subscription.

#### Using The Functions Together

You can use `@anvil.server.callable`, `user_has_subscription` and `@catch_permission_errors` together as follows:

##### 1. You restrict access to a function with `@anvil.server.callable` and `user_has_subscription`

To restrict access to a premium function to users with a valid subscription, start by decorating the premium function with `@anvil.server.callable`. You can pass `@anvil.server.callable`'s `require_user` argument `user_has_subscription`. `user_has_subscription` takes a list of allowed subscriptions and checks if the logged-in user’s subscription matches any entry in the list.

From the template, this example function is only allowed to be run by users with a "personal" subscription:

``` Python
# Here's an example of a function that would require a paid subscription
@anvil.server.callable(require_user=user_has_subscription(["personal"]))
def calculate_percentage_of(number, total_number):
    percentage = (int(number) / int(total_number)) * 100
    return percentage
```

If the user has an active subscription which is in the allowed subscriptions passed to `user_has_subscription`, the function will run. If they don’t meet the subscription requirement, a permissions error is raised and caught by `@catch_permission_errors` - let me show you how to use `@catch_permission_errors`.

##### 2. You use `@catch_permission_errors` on the client-side to prompt user
  
With the server-side function restricted, it's time to prompt users to upgrade if they try to use a premium feature without the right subscription - for this, you can use `@catch_permission_errors`. `@catch_permission_errors` will catch any `anvil.server.PermissionDenied` exceptions thrown by our server-side function and prompt users to upgrade if they don’t meet the subscription requirement.

From the example in the template:

``` Python
# Catch_permission_errors catches exceptions that are thrown by a user not being subscribed and gives them a notification to upgrade
  @catch_permission_errors
  # This function is a simple example function to show you functionality that is gated behind a paywall
  def calculate_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.number_1_textbox.text and self.number_2_textbox.text:
      
      # This makes a call to a restricted function 
      percentage = anvil.server.call('calculate_percentage_of', self.number_1_textbox.text, self.number_2_textbox.text)
    ...
```

And that's it, you can restrict any number of features this way.

### Step 3 - Take Stripe out of test mode

When you're ready to go live, switch Stripe from [test mode](https://docs.stripe.com/test-mode) to live mode.

Next, update the app's account management link (configured in [step 7](#step-7---setting-up-the-customer-portal)) to use the [customer portal's live link](https://docs.stripe.com/customer-management/activate-no-code-customer-portal#url-parameters).

Finally, replace the [API keys](#step-2---add-the-api-key) in your Anvil app with the production keys.
