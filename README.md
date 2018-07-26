## Pizza Ordering Simple Services Example
###### An example Django REST framework project for test pizza ordering services API endpoints with no UI 


### Services Scenarios
* create an order with API.
* Get an order with API.
* Update an order with API.
* Delete an order with API.
* Get all orders list for a customer.
* Get all orders list.

### API Endpoints
* **/orders/** (order create and list endpoint)
* **/orders/{customer_id}/** (order list for a customer endpoint)
* **/order/{order_id}** (order retrieve, update and destroy endpoint)

### Install
* pip install -r requirements.txt

### General Usage Notes
1. Check the connection with PostgreSQL **./pizza_app/sitting.py**
2. Run **python manage.py makemigrations**
3. Run **python manage.py migrate**
4. Create **superuser** and add/delete/update orders using your admin account
5. Run **python manage.py test order** for testing the database models and endpoint functions
6. Run **python manage.py runserver** to run the project on the localhost **http://127.0.0.1:8000**

##### version 1.0 26.07.2018
