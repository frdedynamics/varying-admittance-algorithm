from unittest import TestCase
from .context import package_mojo


class TestMain(TestCase):
    def test_main(self):
        try:
            package_mojo.app.main()
        except ValueError as e:
            self.fail(msg=e)
