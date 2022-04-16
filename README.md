# Commission Web Application

GuestReady(GR) commission rate for each city:

- LONDON: 10%
- PARIS: 12%
- PORTO: 9%

This Django application has the following features and pages:

1. Upload page where users could load the CSV from the spreadsheet and save the data into the database.
2. Report page, with:
   - all loaded reservations
   - total company commission amount. It is calculated as a sum reservation’s commission amounts.
     IE if we have Res-1 with amount 1500 and commission rate 10% And Res-2 with amount 2000 and commission rate 20%. Then total commission is 1500*0.1 + 2000*0.2 = 550
   - Show the company commission per month, based on the Reservation#checkout date IE for the passed reservations it should be:
     i. 2021-05 -> 977.1
     ii. 2021-06 -> 1684
3. City_commission page where the user can select the city name on the form and receive the GuestReady commission amount for this city.

### Requirements:

Python==3.8.1
Django==4.0.4
