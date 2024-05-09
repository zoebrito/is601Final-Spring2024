# User Management System

## Introduction
Welcome to the User Management System, a powerful and scalable solution built using the FastAPI web framework. This document provides a comprehensive overview of the system's architecture, key features, and implementation details.

## Architecture
The User Management System follows a modular and layered architecture to ensure separation of concerns and promote maintainability and scalability. The core components include:
- FastAPI Application
- Database Layer
- Alembic
- Service Layer
- API Layer
- Authentication and Authorization
- Email Service

## Best Practices and Standards
The project adheres to industry best practices and coding standards to ensure code quality, clarity, and maintainability. Key practices include:
- PEP 8
- Type Hints
- Dependency Injection
- Asynchronous Programming
- Error Handling and Logging
- Testing with Pytest
- Containerization with Docker

## Key Features
### User Management
- User registration and login functionality
- User roles and permissions
- User account management (BREAD operations)
- Email verification for registered user accounts
- Automatic assignment of admin role to the first user

### API Design and Documentation
- RESTful API endpoints for user management
- Swagger/OpenAPI documentation
- Secure authentication and authorization using OAuth2

### Database Integration
- Integration with PostgreSQL database using SQLAlchemy ORM
- Efficient and scalable database design
- Asynchronous database operations

### Email Notifications
- Email templates for user verification and notifications
- Integration with Mailtrap for email testing

### Testing and Quality Assurance
- Comprehensive test suite for unit and integration testing
- Continuous Integration and Continuous Deployment (CI/CD) pipeline with GitHub Actions

### Deployment and Containerization
- Dockerization of the application
- Docker Compose for managing multi-container setup
- GitHub Actions workflow for automated testing and deployment

### Administrator User Creation
- Automatic assignment of administrator role to the first user

### CORS Support
- Basic CORS support

## User Retention Analytics (Feature Addition)
### Description
Implement user retention analytics to track and analyze user engagement and retention within the application.

### User Story
As an administrator, I want to gain insights into user retention and conversion rates from anonymous to authenticated users.

### Minimum Viable Feature
- Monitor the conversion rate of anonymous users becoming authenticated users.
- Analyze user login activity to identify users who haven't logged in for 24 hours, 48 hours, 1 week, or 1 year.

## Project Setup and Commands:

1. Fork this repository to your own account.

2. Clone the project repository to your local machine.

3. Create a local .env file with your [MailTrap](https://mailtrap.io/) SMTP settings. Mailtrap allows you to view emails when you test the site manually. When running pytest, the system uses a Mock to simulate sending emails but doesn't actually send them.

4. Alembic and Pytest:
  - When you run Pytest, it deletes the user table but doesn't remove the Alembic table. This can cause Alembic to get out of sync.
  - To resolve this, drop the Alembic table and run the migration (`docker compose exec fastapi alembic upgrade head`) when you want to manually test the site through `http://localhost/docs`.
  - If you change the database schema, delete the Alembic migration, the Alembic table, and the users table. Then, regenerate the migration using the command: `docker compose exec fastapi alembic revision --autogenerate -m 'initial migration'`.

5. Run the project:
  - `docker compose up --build`
  - Set up PGAdmin at `localhost:5050` (see docker compose for login details)
  - View logs for the app: `docker compose logs fastapi -f`
  - Run tests: `docker compose exec fastapi pytest`

## Closed Issues
- QA Issues: [Link to Closed QA Issues](https://github.com/zoebrito/is601Final-Spring2024/issues?q=is%3Aissue+is%3Aclosed)
- New Tests: [Link to New Tests](https://github.com/zoebrito/is601Final-Spring2024/pull/19)
- Feature Development: [Link to Conversion Rate Feature](https://github.com/zoebrito/is601Final-Spring2024/pull/16) and [Link to Login Activity Feature](https://github.com/zoebrito/is601Final-Spring2024/pull/17)

## Deployment to DockerHub
Successful deployment of the User Management System to DockerHub.

- Docker Repository: [Link to Docker Repository](https://hub.docker.com/r/zbrito/is601final-spring2024)
