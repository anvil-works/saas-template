# SaaS with Stripe and Anvil

Anvil's SaaS (Software as a Service) template is a solid starting point and foundation for your subscription-based SaaS product. This template uses Stripe's API for subscription management, and simplifies user permissions with out-of-the-box Python decorators. It's an ideal starting point for your project.

## Contents

In this guide, we’ll walk through the key components of the template, covering:

- **Introduction**: Briefly learn about Anvil, SaaS apps, and the benefits of using this template.
- **Prerequisites**: What you’ll need to get started.
- **Template Structure**: A high-level overview of the app’s architecture and Stripe integration.
- **Template Setup**: Step-by-step instructions to get the template up and running with your account.
- **Testing The App**: Test the integration and explore the template’s functionality from a user’s perspective.
- **Make The app Your Own**:
- **Extending the Template**: Tips and guidance for building on and customizing the template further.

## Introduction

### Anvil

If you're new here, welcome! [Anvil](/) is a platform for building full-stack web apps with nothing but Python. No need to wrestle with JS, HTML, CSS, Python, SQL and all their frameworks – just **build it all in Python**.

You're going to need to know the basics of Anvil before using this template, so I'd recommend following our 10-minute intro tutorial. This should give you enough knowledge to begin using the SaaS template.

### SaaS Apps

SaaS (Software as a Service) apps are 

### Why use this template?

This template is a solid foundation for building your own SaaS app. This template gives you:

- Full Stripe payment and checkout
- Subscription management synced with the app
- Account management synced with Stripe
- Easy-to-configure user permissions

![The User Flow Diagram For The Template"](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/user-flow-diagram.png)

Overall, it's an ideal starting point for your project.

## Prerequisites

To follow this guide you will need the following:

1. An understanding of Python
2. A [Stripe account](https://dashboard.stripe.com/login)
3. Basic knowledge of Anvil (a great place to start is with Anvil's [Feedback form tutorial](https://anvil.works/learn/tutorials/feedback-form))

## Understanding the template's structure

The template is divided into two main parts: the Stripe integration and the Anvil app. Stripe manages payments, subscriptions, and invoicing, while the Anvil app handles user authentication and permissions.

The app relies on the following Stripe features:

- [Customer Portals](https://docs.stripe.com/customer-management)
- [Pricing Tables](https://docs.stripe.com/payments/checkout/pricing-table)
- [APIs](https://docs.stripe.com/api)
  - [Retrieve price list](https://docs.stripe.com/api/prices/list)
  - [Retrieve a product](https://docs.stripe.com/api/products/retrieve)
  - [Retrieve a customer](https://docs.stripe.com/api/customers/retrieve)
  - [Cancel a subscription](https://docs.stripe.com/api/subscriptions/cancel)
  - [Delete a customer](https://docs.stripe.com/api/customers/delete)
- [Webhook](https://docs.stripe.com/webhooks) for the following events:
  - `customer.subscription.updated`
  - `customer.created`

Here's an API flow to help visualise the integration:

![API Flow Diagram](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/api-call-diagram.png)

---

## Setting up the template

This section will guide you through getting started with the template, understanding its features, and further developing it to suit your needs.
  
Let's get started!

---

### Step 1 - Stripe Account Setup

We'll start by setting up our Stripe account. [Register for a Stripe account](https://dashboard.stripe.com/login) and login. Then enter your [business details](https://support.stripe.com/questions/business-information-requirements-to-use-stripe?locale=en-GB) to start capturing recurring revenue (or skip this step if you're only going to use [Stripe's test mode](https://stripe.com/docs/test-mode?locale=en-GB)). Lastly, activate Stripe's [test mode](https://stripe.com/docs/test-mode?locale=en-GB).

---

### Step 2 - Add The API Key

For the integration to work, we need to add your Stripe API key to the app. Copy your [Stripe account's Secret key](https://stripe.com/docs/keys) and, in this app's [App Secrets](https://anvil.works/docs/security/encrypting-secret-data), set the value of "stripe\_test\_api\_key" to your key.

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/app-secrets-location.png)

---

### Step 3 - Creating A Pricing Table

Next, we need to create a pricing table for a customers to use. Start in the Anvil app editor, [publish this app](https://anvil.works/docs/deployment-new-ide/quickstart) and take a copy of the URL - we'll use this in later in this step.

In the Stripe dashboard, [navigate to the Products catalogue](https://dashboard.stripe.com/test/products?active=true), select the [Pricing tables tab](https://dashboard.stripe.com/test/pricing-tables), and create a [pricing table](https://stripe.com/docs/payments/checkout/pricing-table).

1. Create a [product](https://stripe.com/docs/products-prices/how-products-and-prices-work#what-is-a-product) called "Personal"
2. Add one [price](https://stripe.com/docs/products-prices/how-products-and-prices-work#what-is-a-price) to the Personal product
3. In the payment settings for each product you will find a "Confirmation page" section. In that section select "Don't show confirmation page" and enter the URL of this app that we copied in step 5.

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/pricing-table.png)

---

### Step 4 - Adding The Pricing Table To Your App

Stripe's website should take you to your [pricing table's page (if not, follow this link and select your pricing table)](https://dashboard.stripe.com/test/pricing-tables). We need to add the details of this to our SaaS app.

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/stripe-dashboard-pricing-table-code.png)

1. Copy the code for the pricing table.
2. Open the StripePricing form in the Anvil editor and [edit the custom HTML](https://anvil.works/docs/ui/components/forms#HTML-Forms-&-Custom-HTML-Forms)
3. And paste the code it into the StripePricing form's custom HTML.
4. Lastly, add `anvil-name="stripe-pricing-table"` to the stripe-pricing-table tag. The final HTML should look like this:

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/stripe-pricing-html.png)

---

### Step 5 - Setting Up The Webhooks

We need Stripe to tell us when a new customer is created and when their subscription is updated, so we can update our Users table with the Stripe subscription details. We'll use webhooks to do this. [There is a guide to setting up webhooks in Stripe here](https://stripe.com/docs/development/dashboard/register-webhook?locale=en-GB#add-a-webhook-endpoint) but let me give you brief instructions.

#### Customer Created

1. Open the [Webhooks page](https://dashboard.stripe.com/test/webhooks) in Stripe and click the "+ Add endpoint" button.
2. Set the endpoint URL to your published app's URL with "/\_/api/stripe/stripe\_customer\_created" on the end - i.e. "https://my-saas.anvil.app/\_/api/stripe/stripe\_customer\_created". ![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/endpoint-url.png)
3. Then click "+ select events" and select "customer.created" under events to listen for. ![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/searching-events.png)
4. From now on, this will call the \`stripe\_customer\_created\` function in your Anvil app's StripeFunctions module when a customer is created. ![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/webhook-setup.png)

#### Subscription Updated

1. Add another endpoint in Stripe.
2. Set the endpoint URL to your published app's URL with "/\_/api/stripe/stripe\_subscription\_updated" on the end i.e. "https://my-saas.anvil.app/\_/api/stripe/stripe\_subscription\_updated"
3. Then select "customer.subscription.updated" under events to listen for.
4. From now on, this will call the \`stripe\_subscription\_updated\` function in the StripeFunctions module every time a customer is created.

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/finished-webhooks.png)

---

### Step 6 - Setting Up The Customer Portal

Let's quickly set up a way for users to cancel their subscription. Go the Stripe dashboard and set up a [customer portal](https://dashboard.stripe.com/settings/billing/portal).

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/customer-portal-location.png)

Activate the test link and copy it. Then open the SaaS app's AccountManagement form and point the "manage\_subscription\_link" component's URL to the copied link

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/manage-subscription-button.png)

### Step 7 - Swapping The Startup Form

Lastly, in the Anvil editor, switch the [startup form](https://anvil.works/docs/client/components/forms#the-startup-form-or-module) from "APP_README" to "LoginPage".

With these steps completed, your Stripe integration is ready for testing.

---

## Testing The App

The template has a number of [Notifications](https://anvil.works/docs/client/alerts-and-notifications#notifications) which will guide you through testing the app as a user. This will both test the integration we've set up and let you experience what the app is like as a user. [Run the app](https://anvil.works/docs/editor#the-anvil-editor) and follow along with the in-app instruction notifications.

![](https://anvil-website-static.s3.eu-west-2.amazonaws.com/templates/saas-template/notification-example.png)

---

## Making The app Your Own

Now that your Stripe integration is set up and you've experienced the app from a user's perspective, it's time to make this app your own.

Let's start by removing all of the in-app instruction notifications:

1. Search (_ctrl+shift+F_) for "# TEMPLATE EXPLANATION ONLY" comments and delete all the lines mentioned in the comment
2. Take Stripe out of test mode and update API keys
3. Begin creating your own functionality and authenticating user permissions with `@anvil.server.callable(require_user=has_subscription)`
