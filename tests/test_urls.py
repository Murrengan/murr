from django.urls import reverse, resolve


class TestUrls:
    """Testing urls"""
    def test_about_url(self):
        """Test root template about"""
        path = reverse('about')
        assert resolve(path).view_name == 'about'
