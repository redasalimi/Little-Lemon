from django.test import TestCase
from Restaurant.models import MenuItem
# Create your tests here.


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemStr = item.get_item()
        self.assertEqual(itemStr, "IceCream : 80")