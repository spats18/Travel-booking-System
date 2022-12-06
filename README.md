# Travel booking System
## Objective
The objective of this Application is to computerize the process of travel booking. To book travel arrangements, each user must register with a unique user ID and password. The application is showing the hotels and car rentals that can be reserved. The application is also maintaining all the previous bookings done by the customer.
This project not only keeps the record of various customers and their bookings, packages, etc, but it reduces the extensive paperwork. It is making the system more versatile and user-friendly.
## User Manual
1. Run the program and you should be welcomed at the Homepage
2. Click ‘Sign-up’ if you do not have an account, otherwise skip to step 3.
3. Click ‘Log-in’ with your credentials.
4. After completing registration, you can book your trip by clicking ‘Book a Trip’.
5. Click submit after you are done inputting the information.
6. After entering the booking information, you can check your current bookings by clicking ‘View Current Bookings’.
7. On this page, you will be able to see the name, email address, hotel name, and amount paid for your booking(s).
8. If you would like more information on this Tourism Management application, please visit the ‘About’ page.
## ER Diagram
![] (Image/Travel%20Booking%20System%20ER.png)
### Tables
#### 1. Customer
##### Customer account details
c_id (Primary Key), c_name , c_email, c_password, c_age, c_address, c_contact

#### 2. Hotel
##### The list of all hotels available to book.
h_id (Primary Key), h_name, h_address, h_city, h_email, h_contact, h_charges_per_night, h_rating

#### 3. Car Rentals
##### The car rental available to book
cr_id (Primary Key), cr_name, cr_address, cr_city, cr_email, cr_contact, cr_charges_per_day, cr_rating

#### 4. Bookings
##### Which customer booked which hotel and car rental
b_id (Primary Key), h_id, cr_id, b_start_date, b_end_date, b_booking_date, b_amount_paid, b_tour_package

#### 5. Booked Trips
##### Trips booked by all customers
c_id (Primary Key), b_id (Primary Key)

#### 6. Tours
##### Special packages available for the customer to book
h_id (Primary Key), cr_id (Primary Key), t_days, t_nights, t_original_price, t_discount_percent, t_city, t_package_name

## Implementation:

### Back-end Development:
We used PostgreSQL as the language for data definition and data manipulation The server for our database was be hosted locally on our laptop. The ER diagram represents the relation between different entities and attributes. 

### Front-end Development:
We used HTML and Bootstrap alongside Jinja to design the application's front end. We be deployed our code locally through Visual Studio Code. 

### Connectivity between Front-end and Back-end:
We used the Flask framework to connect the dots between the database and the front-end application.


