# ALX Travel App

A Django REST API application for managing travel listings, bookings, and reviews.

## Features

- **Listings Management**: Create and manage travel property listings
- **Booking System**: Handle property bookings with date ranges
- **Review System**: User reviews and ratings for properties
- **REST API**: Full API endpoints using Django REST Framework

## Models

### Listing
- UUID primary key
- Host relationship (User)
- Name, description, location
- Price per night
- Timestamps

### Booking
- UUID primary key
- Property and user relationships
- Start/end dates
- Total price calculation

### Review
- UUID primary key
- Property and user relationships
- Rating (1-5 stars)
- Comment text

## Setup

1. Install dependencies:
```bash
pip install -r requirement.txt
```

2. Run migrations:
```bash
python manage.py makemigrations listings
python manage.py migrate
```

3. Seed database:
```bash
python manage.py seed
```

## API Endpoints

The application provides REST API endpoints for listings and bookings through Django REST Framework.

## Database

Uses MySQL database with proper relationships and constraints.