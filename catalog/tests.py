from django.test import TestCase
from django.urls import reverse
from .models import Item


class ItemTestCase(TestCase):

    def setUp(self):
        Item.objects.create(name='item1', stock=10, price=10.0)
        Item.objects.create(name='item2', stock=20, price=20.0)

    def test_item(self):

        # Test database access
        item1 = Item.objects.get(name='item1')
        item2 = Item.objects.get(name='item2')
        self.assertEqual(item1.stock, 10)
        self.assertEqual(item2.stock, 20)

        # Test uniqueness constraint
        with self.assertRaises(Exception):
            Item.objects.create(name='item1', stock=10, price=10.0)


class CatalogTestCase(TestCase):
    
    def setUp(self):
        Item.objects.create(name='item1', stock=10, price=10.0)
        Item.objects.create(name='item2', stock=20, price=20.0)

    def test_item_list_view(self):
        # Test item listing
        url = reverse('catalog:item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'item1')
        self.assertContains(response, 'item2')

    def test_item_create_view(self):
        # Test item creation
        url = reverse('catalog:item_create')
        data = {'name': 'item3', 'stock': 30, 'price': 30.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Item.objects.count(), 3)

    def test_item_edit_view(self):
        # Test item editing
        item = Item.objects.get(name='item1')
        url = reverse('catalog:edit_item', kwargs={'item_id': item.pk})
        data = {'name': 'item1', 'stock': 40, 'price': 40.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.stock, 40)

    def test_item_delete_view(self):
        # Test item deletion
        item = Item.objects.get(name='item1')
        url = reverse('catalog:delete_item', kwargs={'item_id': item.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Item.objects.count(), 1)

