# ManagementCommand
A Django Management Command that inserts Dummy Users in the Database. It will also store 100 PST date times in a separate table. There will be a scheduled Cron Job, that will run after every 5 minutes and update 10 date times in UTC. Once all 100 date times are in UTC, the cron job will start converting date time objects in PST. 

# TimeStamps Table

<img width="1440" alt="Screenshot 2024-07-30 at 1 49 12 PM" src="https://github.com/user-attachments/assets/678c0a36-b606-49b0-9c3f-903c50a59cf6">

# Dummy User Table

<img width="1440" alt="Screenshot 2024-07-30 at 2 00 53 PM" src="https://github.com/user-attachments/assets/81421628-de67-478e-b2e7-397dc497e1e5">
