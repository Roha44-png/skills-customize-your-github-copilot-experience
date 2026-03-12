# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API using FastAPI by creating endpoints, validating request data, and returning clear JSON responses.

## Skills Practiced

- Designing REST API endpoints
- Handling HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Validating request data with Pydantic models
- Returning consistent status codes and JSON responses

## Files Included

- `README.md` - Assignment instructions
- `starter-code.py` - Starter FastAPI application

## 📝 Tasks

### 🛠️ Task 1: Create Core API Endpoints

#### Description
Set up a FastAPI app for a simple "books" API. Add routes to list books, fetch one book by ID, and create a new book.

#### Requirements
Completed work should:

- Create a FastAPI app instance.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by ID.
- Implement `POST /books` to add a new book.
- Return JSON responses for each endpoint.

#### Example

- `GET /books` returns a JSON list of books.
- `GET /books/2` returns one book object when found.
- `POST /books` with `{ "title": "Dune", "author": "Frank Herbert" }` adds a new book.

### 🛠️ Task 2: Add Validation and Error Handling

#### Description
Improve the API by validating request bodies and handling common errors so users receive helpful feedback.

#### Requirements
Completed work should:

- Use a Pydantic model to validate incoming book data.
- Return `404` when a requested book ID does not exist.
- Return a clear error message when validation fails.
- Keep response formats consistent across endpoints.

#### Example

- Invalid `POST /books` payload (missing `title`) should return a validation error.
- `GET /books/999` should return `404` with a message like `"Book not found"`.

## Submission Checklist

- All tasks are completed.
- API starts successfully with Uvicorn.
- Endpoints return correct status codes and JSON.
- File names and structure are unchanged unless requested.
