from django.test import TestCase
from django.urls import reverse
from .models import Item


class ItemTestCase(TestCase):

    def setUp(self):
        """Set up initial test data for the Item model."""
        Item.objects.create(name='item1', stock=10, price=10.0)
        Item.objects.create(name='item2', stock=20, price=20.0)

    def test_item(self):
        """Test model constraints and validation."""
        
        # Test database access and object retrieval
        item1 = Item.objects.get(name='item1')
        item2 = Item.objects.get(name='item2')
        self.assertEqual(item1.stock, 10)
        self.assertEqual(item2.stock, 20)

    def test_uniqueness_constraint(self):
        """Test uniqueness constraint on item names."""
        item1 = Item.objects.get(name='item1')
        item2 = Item.objects.get(name='item2')
        
        # Test that item names are unique
        self.assertNotEqual(item1.name, item2.name)

    def test_negative_stock(self):
        """Test negative stock value."""
        item = Item.objects.get(name='item1')
        
        # Test that stock cannot be negative
        item.stock = -5
        with self.assertRaises(Exception):
            item.save()

    def test_negative_price(self):
        """Test negative price value."""
        item = Item.objects.get(name='item1')
        
        # Test that price cannot be negative
        item.price = -5.0
        with self.assertRaises(Exception):
            item.save()


class CatalogTestCase(TestCase):
    
    def setUp(self):
        """Set up initial test data for catalog views."""
        Item.objects.create(name='item1', stock=10, price=10.0)
        Item.objects.create(name='item2', stock=20, price=20.0)

    def test_item_list_view(self):
        """Test the item list view."""
        url = reverse('catalog:item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'item1')
        self.assertContains(response, 'item2')

    def test_item_create_view(self):
        """Test the item creation view."""
        url = reverse('catalog:item_create')
        data = {'name': 'item3', 'stock': 30, 'price': 30.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Item.objects.count(), 3)

    def test_item_edit_view(self):
        """Test the item edit view."""
        item = Item.objects.get(name='item1')
        url = reverse('catalog:edit_item', kwargs={'item_id': item.pk})
        data = {'name': 'item1', 'stock': 40, 'price': 40.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.stock, 40)

    def test_item_delete_view(self):
        """Test the item delete view."""
        item = Item.objects.get(name='item1')
        url = reverse('catalog:delete_item', kwargs={'item_id': item.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Item.objects.count(), 1)


class RedItemTestCase(TestCase):

    def test_item_create_with_image(self):
        # Create an item with an image
        item = Item.objects.create(
            name='item3', 
            stock=10, 
            price=10.0,
            image='item3.jpg'
        )
        self.assertEqual(item.image.url, 'item3.jpg')

    def test_item_view_with_image(self):
        # Create an item with an image
        item = Item.objects.create(
            name='item3', 
            stock=10, 
            price=10.0,
            image='item3.jpg'
        )

        # Ensure the image is displayed in the item list
        url = reverse('catalog:item_list')
        response = self.client.get(url)
        self.assertContains(response, 'item3.jpg')
