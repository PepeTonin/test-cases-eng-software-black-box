from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("https://practice.sdetunicorns.com/")
        self.assert_title("Practice E-Commerce Site – SDET Unicorns")
        self.assert_element(".custom-logo-link")
