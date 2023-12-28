from selenium.webdriver.common.by import By


class PageLocators:

    add_to_cart_cta = (By.CSS_SELECTOR, '.product:nth-child(1) a.button')
    cart_item = (By.CSS_SELECTOR, '.cart_item')
    coupon_code_field = (By.ID, 'coupon_code')
    coupon_code_cta = (By.NAME, 'apply_coupon')
    coupon_code_confirmation_msg = (By.CSS_SELECTOR, '.woocommerce-message')
    checkout_cta = (By.CSS_SELECTOR, '.checkout-button')
    checkout_username = (By.ID, 'billing_first_name')
    item_cart_name = (By.CSS_SELECTOR, '.product:nth-child(1) h2.woocommerce-loop-product__title')
    view_cart_cta = (By.CSS_SELECTOR, '.added_to_cart')
