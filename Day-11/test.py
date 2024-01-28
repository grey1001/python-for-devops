import requests 

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_details = response.json()
print(complete_details)
for title in complete_details:
    print(f"Title: {title['title']}")
    print(f"User: {title['user']['login']}")

#  

# for employee in employee_info:
#     if 'age' in employee and employee['age'] > 30:
#         print(employee)
