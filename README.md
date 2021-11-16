# Lenme-Django-Task

All endpoints in api app views are based on assumption the data coming from frontend, can be easily refactored if there's a need, also refactoring models and make migrations. 

- For scheduling tasks; I am informed that its development is not required. 
- But I can provide a general overview about the process: 
  
   - First, we can use celery cron job that runs every 180 days. 
   - to hit the endpoint of complete loan to update its status with 'Complete'
   
- Or the frontend (admin app not users app) can provide a trigger (button) to hit this endpoint. 
   

- The logic of completing is make sure the status before update is 'Funded'. 
- Then make sure that the borrower paid pack by hitting the point of complete loan. 






<a href="https://lenme.com/backend-test/">  Task reference </a> 
