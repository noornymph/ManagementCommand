# ManagementCommand
A Django Management Command that inserts Dummy Users in the Database. It will also store 100 PST date times in a separate table. There will be a scheduled Cron Job, that will run after every 5 minutes and update 10 date times in UTC. Once all 100 date times are in UTC, the cron job will start converting date time objects in PST. 
