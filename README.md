# disaster-relief-emergency-resource-management-system
A FastAPI-based Disaster Relief &amp; Emergency Resource Management System with JWT Authentication, Role-Based Authorization, Relief Camp Management, Victim Registration, Resource Distribution, Volunteer Management, Reports, Search, Pagination, SQLAlchemy ORM, Swagger Documentation, and Docker support.
# Disaster Relief & Emergency Resource Management System

## Features

- JWT Authentication
- Role-Based Authorization
- Relief Camp Management
- Victim Registration
- Resource Distribution
- Volunteer Management
- Reports
- Search
- Pagination
- SQLAlchemy ORM
- Docker Support

## Installation


pip install -r requirements.txt


Run


uvicorn main:app --reload


Swagger


http://127.0.0.1:8000/docs


## Roles

- Admin
- Relief Coordinator
- Volunteer

## Business Rules

- Camp capacity cannot be exceeded
- Camp availability updates automatically
- Resources require quantity greater than zero
- Volunteer can be assigned to only one active camp
- Email must be unique
