# FastAPI Products CRUD

A basic but robust RESTful API built with Python and FastAPI for managing a product inventory. This project demonstrates backend development fundamentals, including CRUD operations, dynamic filtering, and API documentation.

## Features

* **Full CRUD Operations:** Create, Read, Update, and Delete products.
* **Dynamic Filtering:** Search products by category and limit the number of results using Query Parameters.
* **In-Memory Storage:** Uses a lightweight global list to store data (perfect for local testing and demonstration).
* **Automatic Documentation:** Integrated with Swagger UI for interactive API exploration.

## Technologies Used

* **Python 3.12+**
* **FastAPI:** High-performance web framework for building APIs.
* **Uvicorn:** Lightning-fast ASGI server.
* **Git & GitHub:** Version control.

## Setup and Installation

Follow these steps to run the API on your local machine.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JhonnyelithAZ/fastapi-products-crud.git](https://github.com/JhonnyelithAZ/fastapi-products-crud.git)
   cd fastapi-products-crud
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   * On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   * On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

To start the local development server, run the following command:

```bash
python -m uvicorn main:app --reload
```

The `--reload` flag ensures that the server automatically restarts when you make code changes.

## Interactive API Documentation

Once the server is running, you can explore and test all the endpoints directly from your browser. FastAPI automatically generates this interface using Swagger UI.

1. Open your web browser.
2. Navigate to: `http://127.0.0.1:8000/docs`

From there, you can interact with the API, send GET, POST, PUT, and DELETE requests, and see the JSON responses in real-time.
