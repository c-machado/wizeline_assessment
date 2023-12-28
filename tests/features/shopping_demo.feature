Feature: As a user I want to confirm the shopping workflow works as expected

    # Background:
    #     Given a user is a the homepage
    #     And a user adds a product to the cart
    #     And the user clicks to view the current cart

    # Scenario: Add coupon to the cart
    #     When the user enters a valid coupon code
    #     And the user clicks on the CTA to apply the coupon
    #     Then the system applies the coupon

    @checkout
    Scenario: Complete cart checkout
        Given a user is a the homepage
        And a user adds a product to the cart
        And the user clicks to view the current cart
        When the user clicks to complete the checkout
        And the user fills out the user <name>
    Examples:
    |name|
    |caro|
