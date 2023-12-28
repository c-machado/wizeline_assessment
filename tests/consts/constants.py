from dataclasses import dataclass


@dataclass
class Constants:
    BASE_URL = 'https://demos.bellatrix.solutions/'
    # BASE_URL = 'https://blog.google/'
    CART_URL = 'cart'
    COUPON_CODE = 'happybirthday'
    COUPON_MSG = 'Coupon code applied successfully.'
    PRODUCT_NAME = "Falcon 9"
    SEARCH_URL = 'search/?query='
    PROD_URL = 'blog.google'
    CHROME_PROFILE = '/Users/cmachado/Documents/chrome_huge_inc'
    CHROME_WINDOWS_SIZE = {
        'mobile': 'window-size=414,1000',
        'tablet': 'window-size=600,800',
        'desktop': 'window-size=1920,1080',
    }
    MOBILE_PLATFORMS = ['ANDROID', 'IOS']
    UA_BROWSERS = ['edge', 'ie', 'firefox', 'safari', 'ios', 'android']
    USER_AGENTS = {
        'android': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/100.0.4896.58 Mobile Safari/537.36',
        'ios': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
        ' Version/15.3 Mobile/15E148 Safari/604.1',
        'edge': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/100.0.4896.60 Safari/537.36 Edg/99.0.1150.36',
        'firefox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'safari': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) '
        'Version/15.3 Safari/605.1.15',
    }
