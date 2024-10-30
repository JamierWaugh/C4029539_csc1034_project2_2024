Booking Management Project
===
Overview
---
I am to create a booking management service using OOP, this will act similar to MongoDB.

My system should contain the following functionality:
*A full list of all bookings and their details should be retrieved from the application.
Booking details include room (string), start (datetime), hours (int), title (string), and contact (string)
*Add, edit, and delete bookings.
All bookings are daily and are only available on any day from Monday to Friday, between 09:00 and 18:00.
*Ensure that the system is unable to double book a room.
You should be able to search the application for bookings by (completely matching) room or start. This should return a list of all matches and their details.
*A way for the user to identify all bookings that occur in a given room and between a given range of dates. This should return a list of all matches and their details.
*Allow a user to identify all available rooms for a specific start time and hours. This should return a list of available rooms.
*Store data in a file for subsequent re-use i.e., load/save data to/from csv file.