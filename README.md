# Django_Hospital_Management

## Project Description

Django_Hospital_Management is a web-based hospital management system built with Django.  
It provides basic functionality including booking appointments, showing hospital departments, and adding doctors.  
The project uses Django’s default admin panel for backend management.  
**Note:** The CSS styling is not fully completed, but core features are functional.  
There are two main Django apps: `Hospital_Management` and `Home`.

Author: **Don Soby**

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Don-Soby-2007/Django_Hospital_Management.git
   ```

2. **Navigate to the Root Project Directory**
   ```bash
   cd Django_Hospital_Management
   ```

3. **Create and Activate a Virtual Environment (from the root folder)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` does not exist, you can manually install the dependencies:
   ```bash
   pip install django crispy-forms crispy-bootstrap5
   ```

5. **Navigate to the Hospital_Management Folder**
   ```bash
   cd Hospital_Management
   ```

## Usage

1. Ensure you are in the `Hospital_Management` directory (where `manage.py` is located):
   ```bash
   pwd  # Should end with /Django_Hospital_Management/Hospital_Management
   ```

2. Run the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

4. To manage hospital data, log in to the Django admin panel at `http://127.0.0.1:8000/admin/`.

## Dependencies

- Django
- crispy-forms
- crispy-bootstrap5

You can install all dependencies using pip (see above).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For significant changes, please open an issue first to discuss what you would like to change.

---

Feel free to update this README with more specific information as your project evolves.
