![DEVWEAR Logo](./media/Devwear%20Readme%20Logo.PNG)

# DEVWEAR - Portfolio Project 5
Welcome To DevWear,
The Apparel Store for Developers!

## Responsive Layout
![Responsive Layout](media/Responsive2.PNG)

The layout is responsive and has been tested with various screen sizes. This screenshot was taken with the ui.dev/amiresponsive website.


[Link to live Website:](https://devwear-0c4ac54770df.herokuapp.com)

## Link to Repository
[Link to Repository:](https://github.com/BrendanCooney/devwear)

When designing this site, I wanted to keep the design simple. Due to time constraints I kept much of the CSS used in our walktough project. I do like the design and it is simple and clean. The goal of the site was to show that it can be quite simple to design and generate apparel products for Ecommerce


Build and SetupTechnologies:
This Ecommerce Project uses:
 HTML,
 CSS'
 Javascript' 
 Django,
 DJ Databases, 
 Psychopg Libraries,
 Postgres,
 Stripe Payments, 

## Business Model
The DevWear Business model is a Business to Consumer (B to C) business model. The business sells apparel and accesories to software developers. 

Currently the site is an exmple of the possible live site. Please do not make any purchases as you will not get a product yet. 
Please only use the testing cards on the [Stripe Website](https://stripe.com/docs/testing).

## Ecommerce Business Model & Marketing Strategy
This site sells goods to individual customers, and therefore follows a Business to Customer model. It is a simple B2C strategy, as it focuses on individual transactions, and doesn't need anything such as monthly/annual subscriptions.

The Target market for the business is web developers. 

Social media will be used to build a community of users around the business, and boost site visitor numbers, especially when using larger platforms such a Facebook.

A newsletter list will be used by the business to send regular messages to site users. For example, what items are on special offer, new items in stock, updates to business hours, notifications of events, and much more!

Facebook Ads will be used to grow the list. This will be done by sending potential customers to the Landing Page Sign up form through a link. 

Below are some images of the Market Research done for the project:
![Market Research](media/Market%20Research1.PNG)
![Market Research](media/Market%20Research2.PNG)


## Product Design
All products were designed by myself with Canva and Printful. Most of the designs have been created in black and white. All designs have only two colours keeping them simple and getting the message accross clearly. 

Each image was created as below and then imported into printful to create mockups.

![Will Code Design](<media/will code design.png>)

The Mockups were then converted into T-Shirt images for the store.

![will code mockup](media/Will_Code_Blk.jpg)

## Typography 

The Lato font family was used when creating and working on this project. I used Lato on Canva to produce the logo for the brand which matches the Lato Logo font used in the header of the site for the logo.

## Agile Development Process:

GitHub Projects
GitHub Projects served as the Agile tool for the Devwear project. Github used correctly  with the right tags and project creation/issue assignments can work nicely for project management. 

Below you can see the clearly planned out user stories and completed stories on the KANBAN Board. 
![Agile Planning](<media/Agile planning.PNG>)
![User Story List](<media/User Story List.PNG>)
![User Stories Complete](<media/User Stories Complete.PNG>)
Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

## User Stories
I used Excel to create a user story template and continued to create all user stories in Github projects.
![Alt text](<media/User Story Example.PNG>)

### User Story List

USER STORY: <Navigate the Store Menu>#1
As a site visitor I can Navigate the Store Menu so that **See the Products and buy a product **

USER STORY: <Navigate the Store Products>#2
As a **Site Visitor ** I can Navigate the Products so that **See the Prices **

USER STORY: <Navigate the Categories>#3
As a Site Visitor I can Navigate the Product Categories so that **See the Categories **

USER STORY: <Easily view the total of my purchases >#4
As a Site User/shopper I can **Easily view the total of my purchases ** so that Avoid spending too much


USER STORY: <Easily register for an account >#5
As a Site user/Shopper I can **Easily register for an account ** so that **I have a personal account and view my profile **

![Sign Up](media/sign_up.PNG)

USER STORY: <Easily Log in or Log out >#6
As a Site user/Shopper I can **Easily Log in or Log out ** so that Access my personal information
![Login Page](<media/Login Page.PNG>)

USER STORY: <Easily recover my password incase I forget it >#7
As a Site user/Shopper I can Easily recover my password in case I forget it ** so that ** I can recover access to my account
![Password Reset](<media/password reset.PNG>)

USER STORY: <Receive an email after registering >#8
As a Site user/Shopper I can **Receive an email after registering ** so that **Verify that my account registration was successful **
![email registration](<media/Email Registration.PNG>)

USER STORY: <Have a personalised user profile >#9
As a Site user/Shopper I can **Have a personalised user profile ** so that **View my personal order history **

USER STORY: <Sort the list of available products>#10
As a Shopper I can Sort the list of available products so that ** I can easily identify the best priced and categorically sorted products**

USER STORY: <Sort a specific category of a product>#11
As a Shopper I can Sort a specific category of a product so that I can find the best-priced product in a category or sort products in a category

USER STORY: <Sort multiple categories simultaneously>#12
As a Shopper I can Sort multiple categories simultaneously so that Find the best priced product across categories

USER STORY: <Search for a product by name or description>#13
As a Shopper I can Search for a product by name or description so that I can find a specific product I'd like to purchase


devwear #14
USER STORY: <Easily see what Ive serached for and the number of results>#14
As a Shopper I can Easily see what I've serached for and the number of results so that I can quickly decide whether the product I want is available

USER STORY: <Easily select the size and quantity of a product>#15
As a Shopper I can Easily select the size and quantity of a product so that Ensure I don’t accidentally select the wrong product quantity or size


USER STORY: <View Items in my bag to be purchased>#16
As a Shopper I can View Items in my bag to be purchased so that Identify the total cost of my purchase before checkout


USER STORY: <Adjsut the quantity of a product when purchasing it>#17
As a Shopper I can Adjsut the quantity of a product when purchasing it so that Easily make changes to my purchase before checkout

USER STORY: <Easily enter my payment information>#18
As a Shopper I can Easily enter my payment information so that I can checkout quickly with no hassles

USER STORY: <Feel my personal and payment information is safe and secure>#19
As a Shopper I can capability so that ** I can onfidently provide the needed information to make a purchase **


## Search Engine Optimization (SEO) & Social Media Marketing

The Seo is foucussed on people that like apparel and that are developers. The appropriate key words have been added to the Meta Section of base.html 

* Short-tail(head terms) keywors have been used
* Long-tail keywords have also been used.

### Sitemap 
[XML Sitemaps](https://www.xml-sitemaps.com/) was used to create the sitemap.xml file. 

### Robots

There is a robots.txt file present in the project. 

``User-agent: *
Disallow: /accounts/
Disallow: /profiles/
Disallow: /bag/
Sitemap: https://devwear-0c4ac54770df.herokuapp.com/sitemap.xml
``



## Social Media Marketing 

With Social Media making it fairly quick to get a decent media presence and exposure to the market a Facebook page is a great place to star. This is a live Facebook site and can be accessed here:

[Devwear Apparel Ltd](https://www.facebook.com/profile.php?id=61553925042570)

Below are some screenshots of the Facebook Page:
![DevwearFB1](<media/Devwear FB1.PNG>)
![DevwearFB2](<media/Devwear FB2.PNG>)

## Newsletter Marketing:
I have used the subscribe button at the bottom of the base.html file as advised in the course work this subscribes the user to a mailchimp database. This is temporary and will be upgraded at a later stage. 
![Email Subscribe](media/email_subscribe.PNG)


## Data Model
The below graphic provides an idea of the data model. The Model has been updated to include a Blog which active. The Coupon model is a work in progress and will be worked on after assessment. I have included this in Bugs and Wishlist. 

![Data Model](<media/Models.png>)

## Bugs Fixes and Project Continuation Wishlist
At the time of resubmission realise that I would like to document testing further. I have created a Blog Model and Implemented it.
I also started a Coupon Model but was not able to complete it due to time constraints. I would like to take this section live after the assessment is complete. I would also like to take the ecommerce section live and convert the stripe keys to live keys and begin actively promoting the business.

I have attempted to take learnings from outside the course and have been advised to use a book called Django By Example which I will use to further develop this site or redevelop it from the beginning useing the course material and the book. 

