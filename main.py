import requests



#-------------------to create a project in  gilab api-----------

res = requests.post("https://gitlab.com/api/v4/projects", json={"name":"earth", "description":"3rd project via python"}, headers={'PRIVATE-TOKEN': '************'})
print(res.text)




#---------------to delete a existing project ---------------------------

res = requests.delete("https://gitlab.com/api/v4/projects/25493054", headers={'PRIVATE-TOKEN': '************'})

print(res.status_code)


