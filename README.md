# FastAPI App Example

---

This is a simple example of a web application built using **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

* **Root Endpoint**: Returns a "Hello: World" message.
* **Items Endpoint**: Retrieves an item by its ID and optionally accepts a query parameter `q`.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need **Python 3.7+** installed on your system.

### Installation

1.  **Clone this repository** (or create the `app.py` file manually):

    ```bash
    git clone https://github.com/wajidkorkani/Fast-Api.git
    cd Fast-Api/Src
    ```

2.  **Create a virtual environment** (recommended for managing dependencies):

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:

    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**:

    ```bash
    pip install fastapi uvicorn
    ```

---

## Running the Application

1.  **Save the code** below into a file named `main.py` in your project directory:

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "q": q}
    ```

2.  **Run the FastAPI application** using Uvicorn from your terminal. Make sure your current directory in the terminal is the same as where `app.py` is located.

    ```bash
    uvicorn app:app --reload
    ```

    You should see output similar to this, indicating the server is running:

    ```
    INFO:     Will watch for changes in these directories: ['C:\\Users\\Zem\\Coding\\Python\\FastApi\\Fast-Api']
    INFO:     Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000) (Press CTRL+C to quit)
    INFO:     Started reloader process [XXXX] using StatReload
    ```

    The `--reload` flag automatically reloads the server when you make changes to your code, which is great for development!

---

## Usage

Once the server is running, you can access the API endpoints using your web browser or an API client (like Postman or Insomnia):

* ### **Root Endpoint**
    * **URL**: `http://127.0.0.1:8000/`
    * **Method**: `GET`
    * **Response**:
        ```json
        {"Hello":"World"}
        ```

* ### **Items Endpoint**
    * **URL**: `http://127.0.0.1:8000/items/{item_id}` (replace `{item_id}` with an integer, e.g., `5`)
    * **Method**: `GET`
    * **Example (without query parameter)**: `http://127.0.0.1:8000/items/5`
        * **Response**:
            ```json
            {"item_id":5,"q":null}
            ```
    * **Example (with query parameter)**: `http://127.0.0.1:8000/items/5?q=somequery`
        * **Response**:
            ```json
            {"item_id":5,"q":"somequery"}
            ```

---

## Stopping the Application

To stop the Uvicorn server, simply press `CTRL+C` in your terminal where the server is running.