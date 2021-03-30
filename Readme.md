# Creating project using gitlab api

* To create project using gitlab api first thing you need to do is sign up and get Personal Access Token via gitlab.

* now make one python file to run our python code for example main.py

* now open main.py file wich one in the repo you can see the code to create project using api 

* In that main.py we can see we are using requests library to make post call to the gitlab api 

* in the post req we can see we can pass the name of project and description of the project in json format 

* second thing we can see is to pass private token after passing private token we are done and now we can run the file and check status of our project using 
```
print(res.status_code)
```

And this is our code for post req 

```python
res = requests.post("https://gitlab.com/api/v4/projects", json={"name":"earth", "description":"3rd project via python"}, headers={'PRIVATE-TOKEN': '*********'})
```


# Deleting project using gitlab api 

* In main.py file wich is in our repo you can see code to delete the project

```
res = requests.delete("https://gitlab.com/api/v4/projects/25493054", headers={'PRIVATE-TOKEN': '************'})
```

* in above code we just have to pass project ID in url and private token to delete a particular prject 