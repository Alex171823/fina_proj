# What is it?

This is my final project while learning in the Hillel IT School.

## Main idea

This repository includes 2 projects: 'shop' and 'warehouse-api'. Warehouse works only as an API to shop.
Shop, by itself, sometimes updates list of books available in it and for each order sends a signal to warehouse to form a package for customers. 


## Quick Start

To get projects up and running locally on your computer:
	For each project independently, in project directory:
		1. Set up the [Python virtual environment](https://docs.python.org/3/library/venv.html#module-venv).
		2. Assuming you have Python setup, run the following commands:
		   ```
		   pip install -r requirements.txt
		   python manage.py makemigrations
		   python manage.py migrate
		   python manage.py loaddata # optional - fills database with some fixtures
		   python manage.py createsuperuser # Create a superuser (optionally) 
		   for warehouse-api 'python manage.py runserver 8080'; for shop 'python manage.py runserver 8000'
		   ```
		3. run cellery in shop directory
			```
			celery -A shop worker -l INFO -B
			```

## Main features
- Sheduled updating list of books available in shop from warehouse.
- Sending data to warehouse API as in json format.
- Session-based cart for orders with full representation of items in it and info about each.
- PostgreSQL database.
- Management commands for filling database with fake data and manual updating data from warehouse in shop project.
- DRF-based API in warehouse.
- Admin page in warehouse project.

## ATTENTION
By default all apps run in `DEBUG` mode.