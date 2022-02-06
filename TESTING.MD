
# Testing

## Navigation

-   Each navigation link works as intended, including the account links leading to profile, login and logout.
-   The navigation collapses to hamburger on mobile.
-   The correct cost of the shopping cart is displayed and updated.

## Homepage

### New Products

-   The "New Products" section of the homepage shows all products marked as "new" by the site's administrator. The information displayed is correct.
-   The "new" overlay is present on all new products.

## Product Listing

-   The pages listing products display the correct information, for each product and the number of products.
-   Fixed header isnt blocking anything either on mobile or desktop. 

### Search

-   The search functionality works as intended. It returns products whose name, producer and description contain the searched keyword.

### Filtering

-   Various search filters on the products page display the correct items.
-   Using the tag on a product to more of the same category works as intended.

## Product Details

-   The product pages display the correct information and image.
-   Products can successfully be added to the cart using the button.

## Shopping Cart

-   The shopping cart displays all items selected by the user.
-   Updating the quantities of products in the cart works as intended.
-   It is possible to remove an item from the cart.
-   Clicking "Proceed to Payment" leads to the checkout page.
-   If the shopping cart is empty, it is displayed as such and message that its empty is provided.

## Checkout and Payment

-   The checkout form loads appropriately.
-   The checkout form comes pre-filled if a profile has been saved with information.
-   The items in the shopping cart are correctly displayed.
-   The correct total and subtotals are displayed.
-   Customer can choose to svae his information during checkout to his profile.
-   Stripe payment works correctly, webhooks have been tested and received.
-   An unsuccessful payment returns the reason for the failure.
-   Email verification for orders sends out as intended.

## Profile

-   The profile page displays the saved profile information.
-   The form to update profile information is displayed successfully when entering your profile page.
-   The profile information updates successfully when this form is filled.
-   The correct order history is displayed successfully.
-   Clicking on the order number takes you to the receipt page to show you your receipt again.
-   Creating a user has been tested and mails are beeing sent out as intended to verify your e-mail.

## Administrative Tools

Links to adminsitrative tools in the navigation can only be seen if a user is logged in as an superuser.

### Homepage

-   Images of different sizes can be uploaded without breaking the layout of the elements of the page.

### Product Management

#### Adding a Product

-   Adding a new product works as intended.
-   All required fields must be filled to add a new product.
-   If no image is selected by the administrator, a default image is chosen.

#### Editing/Deleting a Product

-   Deleting a product from a product page works as intended.
-   Accessing a product's edit page can be done through the product's page or the management page successfully.
-   When editing a product, its information populates the fields of the form.
-   A product can be updated successfully if all required fields are filled.


## Responsiveness

This application was tested for responsiveness across a variety of devices to ensure content remained readable and editable on various screen sizes.

The navigation of the site was tested by using it and trying to break it. Bugs that were found during the process has after this been fixed and will be taken up in the Bugs found section.

These tests were performed on the following devices and browsers:

-   Chrome and Firefox on Desktop
-   Chrome Laptop
-   Chrome on Tablet
-   Chrome on Samsung S21
-   Chrome on Samsung S10+
-   Firefox on Samsung S10+

## Bugs Found

-   Toaster brought in the HTML from the page it was supposed to show. 
    
    FIXED, the problem was that a div wasent fully closed in the toast file.

-   Pictures wasent showing as intended. 

    FIXED, typo caused the code not to be able to find the proper URL to display it from.

-   Navbar wasent showing the colors of one of the dropdowns.

    FIXED, Again a div that wasent placed as intended when i wrote the code.

- Pictures wasent showing after loading the fixtures.

    FIXED, typo of the extension of the fileformat. jpg was mistaken for jpeg.

- Got error when showing prices

    FIXED, Misscalculated the DecimalField so it didnt take enough digits.

- Wasent able to checkout when using desktop

    FIXED, had forgot to put in URLs for the checkout in the view for big screens.

- Site broke when adding new models, but only on heroku.

    FIXED, forgotten to export the DB to heroku.

Other then these bugs there been some minor ones that been fixed along the way. but as far as i can see i cant find any major bugs that causes any problems for the site. 