import requests
from assertpy.assertpy import assert_that

from tests.consts.api_const import BASE_URI


def test_get_tag_android_articles():
    # We use requests.get() with url to make a get request
    response = requests.get(BASE_URI)
    # response from requests has many useful properties

    # pretty_print(response.json())
    # we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.status_code).is_equal_to(200)
    # We can get python dict as response by using .json() method
    result = response.json()
    print('len response', len(result['results']))
    # get the tag associated to each article / does not work
    android_articles = [result['results'] for article in result]
    print('android articles', android_articles)
    # assert_that(android_articles).contains('category')
    for article in result['results']:
        print('article', article)
        print('article', article['tag'])
        assert_that(article['category']).contains('article')
