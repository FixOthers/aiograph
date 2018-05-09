import pytest

from aiograph import Telegraph, types
from aiograph.utils import exceptions


def test_prepare_content():
    telegraph = Telegraph()
    with pytest.raises(exceptions.ContentRequired):
        telegraph._prepare_content(None)
    with pytest.raises(TypeError):
        telegraph._prepare_content(42)

    content = telegraph._prepare_content('content')
    assert isinstance(content, str)

    content = telegraph._prepare_content(['content'])
    assert isinstance(content, str)


def test_token_property(telegraph: Telegraph):
    telegraph.token = 'abcdef01234567890'
    assert telegraph.token == 'abcdef01234567890'

    with pytest.raises(TypeError):
        telegraph.token = 42

    account = types.Account(short_name='test', author_name='Test',
                            access_token='abcdef01234567890')
    telegraph.token = account
    assert telegraph.token == account.access_token

    with pytest.raises(TypeError):
        account = types.Account(short_name='test', author_name='Test')
        telegraph.token = account

    del telegraph.token

    assert telegraph.token is None


def test_service(telegraph):
    assert telegraph.service == 'telegra.ph'
    assert telegraph.api_url == f"https://api.{telegraph.service}/"
    assert telegraph.service_url == f"http://{telegraph.service}"

    with pytest.raises(ValueError):
        telegraph.service = telegraph.service_url

    telegraph.service = 'example.com'

# def test_socks5_proxy(): pass
