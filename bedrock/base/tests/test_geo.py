from django.test import override_settings, TestCase, RequestFactory

from bedrock.base.geo import get_country_from_request


class TestGeo(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_geo_header(self):
        """Country code from request header should work"""
        req = self.factory.get('/', HTTP_CF_IPCOUNTRY='de')
        assert get_country_from_request(req) == 'DE'

    @override_settings(DEV=False)
    def test_geo_no_header(self):
        """Country code when header absent should be None"""
        req = self.factory.get('/')
        assert get_country_from_request(req) is None

    def test_geo_param(self):
        """Country code from header should be overridden by query param
           for pre-prod domains."""
        req = self.factory.get('/', data={'geo': 'fr'}, HTTP_CF_IPCOUNTRY='de')
        assert get_country_from_request(req) == 'FR'

        # should use header if at prod domain
        req = self.factory.get('/', data={'geo': 'fr'},
                               HTTP_CF_IPCOUNTRY='de',
                               HTTP_HOST='www.mozilla.org')
        assert get_country_from_request(req) == 'DE'

    @override_settings(DEV=False)
    def test_invalid_geo_param(self):
        req = self.factory.get('/', data={'geo': 'france'}, HTTP_CF_IPCOUNTRY='de')
        assert get_country_from_request(req) == 'DE'

        req = self.factory.get('/', data={'geo': ''}, HTTP_CF_IPCOUNTRY='de')
        assert get_country_from_request(req) == 'DE'

        req = self.factory.get('/', data={'geo': 'france'})
        assert get_country_from_request(req) is None
