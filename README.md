# TaxiCo - Taxi Booking System

A Django-based taxi booking platform that allows users to book rides, track available taxis, and manage bookings with an intuitive web interface.

## 🚖 Features

- **User Authentication**: Registration and login system for passengers
- **Taxi Booking**: Book rides with pickup and dropoff locations
- **Real-time Taxi Tracking**: Find the closest available taxi using GPS coordinates
- **Booking Management**: View, update, and cancel existing bookings
- **Driver Management**: Register drivers and manage taxi fleet
- **Responsive Design**: Mobile-friendly interface with Bootstrap styling

## 🛠️ Technology Stack

- **Backend**: Django 4.1.7
- **Database**: SQLite3 (default)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Additional Libraries**: 
  - phonenumbers (phone number validation)
  - Google Maps API integration

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for version control)

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TaxiCo_Remastered3.git
   cd TaxiCo_Remastered3
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your Google Maps API key:
     ```
     GOOGLE_MAPS_API_KEY=your_api_key_here
     ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
TaxiCo_Remastered3/
├── TAXICO/                 # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── authentication/        # User authentication app
│   ├── models.py          # User, Booking, Taxi models
│   ├── views.py           # Authentication views
│   ├── urls.py            # Authentication URLs
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, images
├── base/                  # Core application logic
│   ├── models.py          # Additional models
│   ├── views.py           # Main application views
│   ├── urls.py            # Base app URLs
│   └── templates/         # Base templates
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── db.sqlite3            # SQLite database
```

## 🗄️ Database Models

### Booking Model
- User association
- Pickup and dropoff locations
- Taxi assignment
- Booking status and timestamps
- Passenger count

### Taxi Model
- Driver information
- License plate
- GPS coordinates (latitude, longitude)
- Availability status

### User Registration Model
- Extended user profile
- Contact information
- Address and job preferences

## 🎯 Usage

### For Passengers:
1. **Register/Login**: Create an account or log in
2. **Book a Ride**: Enter pickup and destination locations
3. **Track Taxi**: View the closest available taxi on the map
4. **Manage Bookings**: View, update, or cancel your bookings

### For Administrators:
1. **Access Admin Panel**: Visit `/admin` with superuser credentials
2. **Manage Taxis**: Add/remove taxis and drivers
3. **Monitor Bookings**: Track all booking activities
4. **User Management**: Manage user accounts and permissions

## 🔧 Configuration

### Google Maps Integration
To enable map functionality:
1. Get a Google Maps API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the following APIs:
   - Maps JavaScript API
   - Geocoding API
   - Places API
3. Add the API key to your environment variables

### Database Configuration
The project uses SQLite by default. To use PostgreSQL or MySQL:
1. Install the appropriate database adapter
2. Update `DATABASES` in `settings.py`
3. Run migrations with the new database

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Phone number validation may need regional adjustments
- Map loading requires active internet connection
- Some styling inconsistencies on older browsers

## 🔮 Future Enhancements

- [ ] Real-time GPS tracking for active rides
- [ ] Payment integration (Stripe, PayPal)
- [ ] SMS notifications for booking updates
- [ ] Driver mobile app
- [ ] Ride history and ratings system
- [ ] Multi-language support

## 📞 Support

If you encounter any issues or have questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation in the `docs/` folder (if available)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap for responsive design components
- Google Maps API for location services
- All contributors who helped improve this project

---

**Note**: This is a development version. Please ensure proper security measures before deploying to production.
