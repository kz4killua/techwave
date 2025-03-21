from django.test import TestCase  # Import Django's built-in test case class
from django.urls import reverse  # Import reverse to generate URLs for views
from .models import Item  # Import the Item model to interact with the database


# Test case for the Item model
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

        # Test uniqueness constraint (same name should raise an error)
        with self.assertRaises(Exception):
            Item.objects.create(name='item1', stock=10, price=10.0)

        # Test negative stock value (should raise an error)
        with self.assertRaises(Exception):
            Item.objects.create(name='item3', stock=-10, price=10.0)

        # Test negative price value (should raise an error)
        with self.assertRaises(Exception):
            Item.objects.create(name='item3', stock=10, price=-10.0)


# Test case for catalog views
class CatalogTestCase(TestCase):
    
    def setUp(self):
        """Set up initial test data for catalog views."""
        Item.objects.create(name='item1', stock=10, price=10.0)
        Item.objects.create(name='item2', stock=20, price=20.0)

    def test_item_list_view(self):
        """Test the item list view."""
        url = reverse('catalog:item_list')  # Generate the URL for item listing
        response = self.client.get(url)  # Make a GET request
        self.assertEqual(response.status_code, 200)  # Ensure response is OK
        self.assertContains(response, 'item1')  # Check if item1 is in response
        self.assertContains(response, 'item2')  # Check if item2 is in response

    def test_item_create_view(self):
        """Test the item creation view."""
        url = reverse('catalog:item_create')  # Generate the URL for item creation
        data = {'name': 'item3', 'stock': 30, 'price': 30.0}  # Data to create a new item
        response = self.client.post(url, data)  # Send POST request
        self.assertEqual(response.status_code, 302)  # Check for redirect after creation
        self.assertEqual(Item.objects.count(), 3)  # Ensure the item count increased

    def test_item_edit_view(self):
        """Test the item edit view."""
        item = Item.objects.get(name='item1')  # Get an existing item
        url = reverse('catalog:edit_item', kwargs={'item_id': item.pk})  # Generate edit URL
        data = {'name': 'item1', 'stock': 40, 'price': 40.0}  # Updated data
        response = self.client.post(url, data)  # Send POST request to update item
        self.assertEqual(response.status_code, 302)  # Ensure redirect after edit
        item.refresh_from_db()  # Refresh item from database
        self.assertEqual(item.stock, 40)  # Verify stock was updated

    def test_item_delete_view(self):
        """Test the item delete view."""
        item = Item.objects.get(name='item1')  # Get an existing item
        url = reverse('catalog:delete_item', kwargs={'item_id': item.pk})  # Generate delete URL
        response = self.client.post(url)  # Send POST request to delete item
        self.assertEqual(response.status_code, 302)  # Ensure redirect after delete
        self.assertEqual(Item.objects.count(), 1)  # Verify item count is reduced
