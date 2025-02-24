# Appstore

## Overview
This is a Django-based Appstore service that allows users to create and sell apps. Admins can verify apps before they are available for purchase.

## Features
- User authentication (signup/login with token-based authentication)
- App creation and management
- Admin verification process
- Listing verified apps
- Purchasing apps
- API documentation using Swagger

## Setup Instructions
### Prerequisites
- Docker & Docker Compose installed

### Running the Application with Docker
1. Clone the repository:
   ```sh
   git clone git@github.com:m69fard/formaloo.git
   cd formaloo
   ```

2. Create a `.env` file for environment variables.

   ```
   SECRET_KEY=secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1
   DB_NAME=appstore
   DB_USER=user
   DB_PASSWORD=password
   DB_HOST=db
   DB_PORT=5432
   ```

3. Start the services:
   ```sh
   docker-compose up --build
   ```

4. The application will be available at `http://localhost:8000`

### Database Setup & Migrations
The database is automatically configured in Docker. However, to run migrations manually:
```sh
docker-compose exec web python manage.py migrate
```

### Creating a Superuser
To create a superuser:
```sh
docker-compose exec web python manage.py createsuperuser
```

### Test
To run tests
```sh
docker-compose exec web python manage.py test
```


## API Documentation
Swagger UI is available at:
```
http://localhost:8000/swagger/
```
Redoc documentation:
```
http://localhost:8000/redoc/
```

## Assumptions Made
- Authentication is handled via token-based authentication.
- The database used is PostgreSQL.

## Known Issues & Limitations
- The login, signup and purchase APIs are currently mock.
- No frontend UI is provided; interactions are via API.

