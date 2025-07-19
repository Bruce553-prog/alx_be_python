task=input("Enter your task? ")
priority=input("what is the priority do you always give this task?(high,medium,low)  ")
time_bound=input("Is the task time bound (yes/no) ")
match priority:
    case "high":
        if time_bound=="yes":
              print(f"Reminder: {task} is a high priory task that requires immediate attention today!")
        elif time_bound=="low":
              print(f"Reminder: {task} is high priority task atleast create time for it")
        else:
              print("i am sorry, the time bound is either yes or no")
    
    case "medium":
          if time_bound=="yes":
              print(f"Reminder: '{task}' is not high priory task concider completing it after the priority is done!")
          elif time_bound=="low":
              print(f"Reminder: '{task}' is not high  priority task but work on it as soon as possible ")
          else:
              print("i am sorry, the time bound is either yes or no")
    
    case "low":
          if time_bound=="yes":
              print(f"Reminder: '{task}' is a low priority task concider completing it")
          elif time_bound=="low":
              print(f"Reminder: '{task}' is a low priority but task atleast create time for it")
          else:
              print("i am sorry, the time bound is either yes or no")
           
        
    

        


