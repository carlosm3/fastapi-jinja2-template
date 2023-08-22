# FastAPI with Jinja2 Starter Framework

This repository contains a starter framework for creating web applications using FastAPI and Jinja2.


## Dependencies

The following dependencies are required to run this application:

- FastAPI
- Jinja2
- uvicorn

You can install them by running:

```bash
pip install -r requirements.txt
```

## Getting Started

To run the development server, first navigate to the src directory:

```bash
cd src
```

Then run the following command:

```bash
uvicorn main:app --reload
```

This will start the server and you can access the application at http://localhost:8000.


## Project Structure

The project's directory structure is as follows:

```text
app_name/
├── main.py
├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── static/
│   │   └── css/
│   │   └── js/
│   │   └── img/
│   └── utils/
├── templates/
│   ├── index.html
│   └── layout.html
└── config/
```

The **main.py** file contains the main entry point for the application. The app directory contains the application code, which is organized into the following subdirectories:

- **routes**: Contains the FastAPI route definitions.
- **models**: Contains data models used by the application.
- **services**: Contains utility functions and application configuration.
- **utils**: Contains various utility functions used by the application.

The **templates** directory contains the Jinja2 template files used to generate HTML pages. The **config** directory contains any configuration files used by the application.


## License

This project is released under the MIT License. See the [LICENSE](https://github.com/carlosm3/fastapi-jinja2-template/blob/main/LICENSE) file for details.