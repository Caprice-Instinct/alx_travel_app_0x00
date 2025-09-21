from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **options):
        # Create a sample host user if it doesn't exist
        host_user, created = User.objects.get_or_create(
            username='host1',
            defaults={
                'email': 'host1@example.com',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        
        # Sample listings data
        sample_listings = [
            {
                'name': 'Cozy Beach House',
                'description': 'A beautiful beach house with ocean views',
                'location': 'Miami, FL',
                'pricepernight': Decimal('150.00')
            },
            {
                'name': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin in the mountains',
                'location': 'Aspen, CO',
                'pricepernight': Decimal('200.00')
            },
            {
                'name': 'City Center Apartment',
                'description': 'Modern apartment in downtown',
                'location': 'New York, NY',
                'pricepernight': Decimal('300.00')
            },
            {
                'name': 'Lakeside Villa',
                'description': 'Luxury villa by the lake',
                'location': 'Lake Tahoe, CA',
                'pricepernight': Decimal('400.00')
            },
            {
                'name': 'Desert Oasis',
                'description': 'Unique desert experience',
                'location': 'Phoenix, AZ',
                'pricepernight': Decimal('180.00')
            }
        ]

        # Create listings
        for listing_data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                name=listing_data['name'],
                defaults={
                    'host_id': host_user,
                    'description': listing_data['description'],
                    'location': listing_data['location'],
                    'pricepernight': listing_data['pricepernight']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created listing: {listing.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Listing already exists: {listing.name}')
                )

        self.stdout.write(
            self.style.SUCCESS('Database seeding completed!')
        )