# Entity Mapping System (Django REST Framework)

## Overview

The **Entity Mapping System** is a modular Django REST Framework backend designed to manage master entities and their relationships.

The system supports management of:

* Vendors
* Products
* Courses
* Certifications

and their mappings:

* Vendor → Product
* Product → Course
* Course → Certification

All APIs are implemented using **APIView only**, without using ViewSets, GenericAPIView, mixins, or routers.

API documentation is provided using **drf-yasg (Swagger & ReDoc)**.

---

# Tech Stack

* Python
* Django
* Django REST Framework
* drf-yasg (Swagger documentation)

---

# Project Architecture

```
entity_mapping_system/
│
├── common/
│   └── models.py
│
├── vendor/
├── product/
├── course/
├── certification/
│
├── vendor_product_mapping/
├── product_course_mapping/
├── course_certification_mapping/
│
├── entity_mapping_system/
│   └── settings.py
│
└── manage.py
```

Each module is implemented as a separate Django app to maintain modularity.

---

# Features

* Modular Django app architecture
* CRUD APIs for all master entities
* CRUD APIs for mapping entities
* Validation rules implemented using serializers
* Soft delete using `is_active`
* Query parameter filtering
* Swagger documentation
* ReDoc documentation

---

# Master Entities

The system manages the following entities:

* Vendor
* Product
* Course
* Certification

Each entity includes fields:

* id
* name
* code (unique)
* description
* is_active
* created_at
* updated_at

---

# Mapping Entities

The system supports three mapping relationships:

| Mapping                    | Description            |
| -------------------------- | ---------------------- |
| VendorProductMapping       | Vendor → Product       |
| ProductCourseMapping       | Product → Course       |
| CourseCertificationMapping | Course → Certification |

Each mapping contains:

* parent foreign key
* child foreign key
* primary_mapping
* is_active
* created_at
* updated_at

---

# Validation Rules

The system enforces the following validations:

* Required field validation
* Unique `code` for master entities
* Prevent duplicate mappings
* Valid foreign key relationships
* Only **one primary mapping per parent**

Example validations:

* Same vendor-product pair cannot be inserted twice
* Same product-course pair cannot be inserted twice
* Same course-certification pair cannot be inserted twice
* Only one primary mapping allowed per parent entity

---

# API Endpoints

## Vendor APIs

```
GET    /api/vendors/
POST   /api/vendors/
GET    /api/vendors/{id}/
PUT    /api/vendors/{id}/
PATCH  /api/vendors/{id}/
DELETE /api/vendors/{id}/
```

## Product APIs

```
GET    /api/products/
POST   /api/products/
GET    /api/products/{id}/
PUT    /api/products/{id}/
PATCH  /api/products/{id}/
DELETE /api/products/{id}/
```

## Course APIs

```
GET    /api/courses/
POST   /api/courses/
GET    /api/courses/{id}/
PUT    /api/courses/{id}/
PATCH  /api/courses/{id}/
DELETE /api/courses/{id}/
```

## Certification APIs

```
GET    /api/certifications/
POST   /api/certifications/
GET    /api/certifications/{id}/
PUT    /api/certifications/{id}/
PATCH  /api/certifications/{id}/
DELETE /api/certifications/{id}/
```

---

# Mapping APIs

## Vendor Product Mapping

```
GET    /api/vendor-product-mappings/
POST   /api/vendor-product-mappings/
GET    /api/vendor-product-mappings/{id}/
PUT    /api/vendor-product-mappings/{id}/
PATCH  /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/
```

## Product Course Mapping

```
GET    /api/product-course-mappings/
POST   /api/product-course-mappings/
GET    /api/product-course-mappings/{id}/
PUT    /api/product-course-mappings/{id}/
PATCH  /api/product-course-mappings/{id}/
DELETE /api/product-course-mappings/{id}/
```

## Course Certification Mapping

```
GET    /api/course-certification-mappings/
POST   /api/course-certification-mappings/
GET    /api/course-certification-mappings/{id}/
PUT    /api/course-certification-mappings/{id}/
PATCH  /api/course-certification-mappings/{id}/
DELETE /api/course-certification-mappings/{id}/
```

---

# Query Parameter Filtering

Some APIs support filtering using query parameters.

Examples:

```
/api/vendor-product-mappings/?vendor_id=1
/api/product-course-mappings/?product_id=2
/api/course-certification-mappings/?course_id=3
```

---

# API Documentation

Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

ReDoc documentation:

```
http://127.0.0.1:8000/redoc/
```

---

# Setup Instructions

## 1. Clone Repository

```
git clone <repository-url>
cd entity_mapping_system
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Run Server

```
python manage.py runserver
```

---

# Access URLs

| Service | URL                            |
| ------- | ------------------------------ |
| Admin   | http://127.0.0.1:8000/admin/   |
| Swagger | http://127.0.0.1:8000/swagger/ |
| ReDoc   | http://127.0.0.1:8000/redoc/   |

---
