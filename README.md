# React JS + Python Django + SQLite
i.e. [frontend] + [backend] + [database]

## <span style="color:yellow">About</span>

This web application is an internal business tool that can be used by business management personel to plan, build, and track their work force.

## <span style="color:yellow">Coding Process</span>

*Frontend:*<strong> ReactJS</strong>

*Backend:*<strong> Python Django</strong>

*Database:*<strong> SQLite3</strong>

## <span style="color:yellow">Install</span>

+ **Python**
+ **Visual Studio Code**
+ **sqlitestudio**
+ **postman**
+ **nodejs**

```shell
    - pip install django
    - pip install djangorestframework
    - pip install django-cors-headers
```

## Reference

[**django**](https://www.djangoproject.com/)

## <span style="color:yellow">Create Django Project</span>

```bash
django-admin startproject personalchronical
cd personalchronical
code .
```

<span style="color:yellow">Project layout</span>

![flow](./static/layout.PNG)

<hr>

## <span style="color:yellow">Let's go code maker!</span>

<span style="color:yellow">Run server</span>
```bash
python .\manage.py runserver
```

<span style="color:yellow">Create front-end app</span>

```bash
python .\manage.py startapp careerjournal
```

<span style="color:yellow">Add entries into `settings.py`</span>

```config
[
    ...

    'rest_framework',
    'corsheaders',
    'careerjournal.apps.CareerjournalConfig',
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    ...
]

```

<span style="color:yellow">Models code for `careerjournal/models.py`</span>

```python
# Create your models here.
class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    UserEmail = models.CharField(max_length=100)
    
class Employment(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    EmployeeTitle = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

```


<span style="color:yellow">Create database</span>

```bash
python .\manage.py makemigrations careerjournal
```

console output
```shell
PS D:\devel\PYTHON-DEV\personalChronical> python .\manage.py makemigrations careerjournal
Migrations for 'careerjournal':
  careerJournal\migrations\0001_initial.py
    - Create model Employment
    - Create model Users
PS D:\devel\PYTHON-DEV\personalChronical>
```


<span style="color:yellow">migrate tables</span>
```bash
python .\manage.py migrate careerjournal
```

*You can verify the existence of the database using the `sqlitestudio`*


<span style="color:yellow">Add file `careerjournal/serializers.py`</span>

```python
from rest_framework import serializers
from careerJournal.models import Users, Employment

class UsersSerializer(serializers.ModelsSerializer):
    class Meta:
        model=Users
        fields=('UserId', 'UserName', 'UserEmail')
        
class EmploymentSerializer(serializers.ModelsSerializer):
    class Meta:
        model=Employment
        fields=('EmployeeId', 'EmployeeName', 'EmployeeTitle', 'DateOfJoining', 'PhotoFileName')
```

<span style="color:red">**Note**</span> if `import rest_frame` throws error and you are using `venv`, then `Ctrl+shift+P`, enter <span style="color:green">Python:Select Interpreter</span>  Then, select the active venv name.  This would reference the correct virtual python scripts.


Next, create `serializer` in `careerJournal/views.py`  **see code**

Add `careerJournal/urls.py`
```python
from django.urls import re_path
from careerJournal import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    re_path(r'^user$', views.usersApi),
    re_path(r'^user/([0-9]+)$', views.usersApi),
    
    re_path(r'^employee$', views.employmentApi),
    re_path(r'^employee/([0-9]+)$', views.employmentApi),
    
    re_path(r'^employee/savefile', views.saveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Add routes to `careerJournal/views.py`
```python
from django.shortcuts import render
# csrf allows other domains to access our methods
from django.views.decorators.csrf import csrf_exempt
# JSONParser to parse incoming data models
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from careerJournal.models import Users, Employment
from careerJournal.serializers import UsersSerializer, EmploymentSerializer

# storage module
from django.core.files.storage import default_storage


# Create your views here.
# CRUD operations for the users table
@csrf_exempt
def usersApi(request, id=0):
    if request.method=='GET':
        users = Users.objects.all()
        user_serializer = UsersSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        users_serializer = UsersSerializer( data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(UserId=user_data['UserId'])
        users_serializer = UsersSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        user = Users.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Delete Successfully", safe=False)
        


# CRUD operations for the employment table
@csrf_exempt
def employmentApi(request, id=0):
    if request.method=='GET':
        employees = Employment.objects.all()
        employee_serializer = EmploymentSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmploymentSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee = Employment.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmploymentSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        employee = Employment.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete Successfully", safe=False)
    
    
@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
```

Insert paths into server `urls.py`
```python
from django.urls import include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('careerJournal.urls'))
]
```

<br><br>
<hr>

# <span style="color:yellow">Create the Frontend ReactJS Project</span>

Create a separate frontend ReactJS project and open it in separate VSCode.

```bash
npx create-react-app journalclient
cd journalclient
code .
```

Edit `src/App.js` and `public/index.html`

```javascript
/* src/App.js */
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App container">
      <h3 className="d-flex justify-content-center m-3">
        React JS Frontend
      </h3>  
    </div>
  );
}

export default App;
```

Insert CDN links for css/javascript from [getbootstrap.com](https://getbootstrap.com/docs/5.3/getting-started/introduction/) code into `public/index.html`
at the head tag and at bottom of body tag.

**Install React Router DOM**

```bash
npm install react-router-dom
```

Add files `src/Home.js`, `src/User.js`, and `src/Employment.js` to extend components.

```javascript
/* src/Home.js */
import React, {Component} from 'react';

export class Home extends Component {
    render() {
        return (
            <div>
                <h3>This is the Home page</h3>
            </div>
        )
    }
}
```

```javascript
/* scr/Employment.js */
import React, {Component} from 'react';

export class Employment extends Component {
    render() {
        return (
            <div>
                <h3>This is the Employment page</h3>
            </div>
        )
    }
}
```

```javascript
/* src/User.js */
import React, {Component} from 'react';

export class User extends Component {
    render() {
        return (
            <div>
                <h3>This is the User page</h3>
            </div>
        )
    }
}
```

Register extended components in `src/App.js`

```javascript
...
import {Home} from './Home';
import {User} from './User';
import {Employment} from './Employment';
/* modules needed for routing*/
import { BrowserRoute, Route, Routes, NavLink } from 'react-router-dom';
...

```

Create file `src/Variables.js` to store API endpoints.  i.e. Referencing the endpoints from the Backend server.
```javascript
export const variables = {
    API_URL:"http://127.0.0.1:8000/",
    PHOTO_URL:"http://127.0.0.1:8000/Photos/"
}
```

Very usefull [Bootstrap Icons](https://icons.getbootstrap.com/) for `edit` and `delete` to liven up the frontend.

## <span style="color:yellow">Frontend Snapshots</span>

![Home](./static/HomePage.PNG)

![Account Page](./static/AccountPage.PNG)

![EmployeeProfile Page](./static/PersonelPage.PNG)


# <span style="color:yellow">Dockerize Django</span>

**Reference** [dockerizing django app](https://blog.logrocket.com/dockerizing-django-app/)

This section provides steps to containerize the application we worked on above.

**Create file `requirements.txt`**

```bash
pip install pipreqs
pipreqs .
```

**Create file `Dockerfile`**

```Dockerfile
# base image  
FROM python:3.11.1   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver  
```

**Build this docker container**

The docker image `businesspersonelchronicler-v1.0` below can be deployed on a hosting site.

```bash
docker build . -t businesspersonelchronicler-v1.0
```

**docker compose**
```bash
version: '3'

services:

  web:
    build: .
    command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```

**Using docker-compose to build/run the backend server**

```bash
docker-compose up --build
```



<br><br>
# <span style="color:yellow">Production Deployment to NGINX server on Ubuntu</span>


In order for the software to work, there would be two separate deployments; one for the `frontend` and another for the `backend`.

## **Deploy the frontend**

Thus far, you are developing the frontend ReactJS app in Visual Studio Code.  To deploy the app, you will need to take the `build` folder and deposit it into the hosting machine.

### <span style="color:yellow">Produce the `journalclient/build`</span> 

```script
cd journalclient
npm run build
```

To deploy the frontend app on `nginx` server, all you need is the content in the `build` folder.  

<br>

### <span style="color:yellow">Deploy and Configure the NGINX Server</span>

For the purpose of least obstructive demonstration, let's use the Windows 10 Subsystem Linux instance (WSL2).

Open powershell and type `wsl --install`

Read here for additional instructions on starting a [Windows Subsystem Linux-2](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10)

Assume you have access to terminal on WSL2 Ubuntu, follow these steps:

**Install nginx**

[nginx on ubuntu](http://www.theappliedarchitect.com/deploying-react-in-production/) Step by step:
Note, the systemd might not be available on WSL2 Windows10.  Fear not, you can fall back to using system service command.  e.g. `sudo service nginx {start/stop/reload/restart}`

From the WSL2 Ubuntu terminal, upgrade, and install nginx.

```bash
sudo apt upgrade
sudo apt install net-tools
sudo apt nginx
sudo ufw app list
```

The last command should verify if nginx installed correctly.

```Output
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
```

**Enable HTTP on port 80**

```bash
sudo ufw allow 'Nginx HTTP'
sudo ufw status

sudo service nginx start
```

**Verify nginx is active and accessible to the browser**

```bash
curl http://localhost:80
```

**Mount a Windows Drive Until Logoff**

Note the letter of the windows drive (where the `journalclient/build` folder resides) that you would like to map in WSL2. Let's use letter D in this example.

On the Ubuntu terminal, create a new folder for that drive letter under /mnt if it does not already exist. (ex: `mkdir -p /mnt/d`)

Mount the drive with `sudo mount -t drvfs D: /mnt/d`

Optionally, to persist the mount point, open `/etc/fstab` and add a line such as the following:

```bash
D: /mnt/d drvfs defaults 0 0
```

Reload the fstab file with `sudo mount -a`

It is ready to transfer content in D:\...\`build` int
### <span style="color:yellow">Configure Nginx</span>

Nginx has one server block enabled by default and is configured to serve documents out of a directory at /var/www/html. While this works well for a single site, it can become difficult to manage if you are hosting multiple sites. Instead of modifying /var/www/html, we’ll create a directory structure within /var/www for the your_domain website, leaving /var/www/html in place as the default directory to be served if a client request doesn’t match any other sites.

1. Decide what you name your domain.  Let's call it `businessjournal.com`

2. Create the root web directory for your_domain as follows:

```bash
sudo mkdir -p /var/www/businessjournal.com
sudo chown -R $USER:$USER /var/www/businessjournal.com

sudo nano /etc/nginx/sites-available/businessjournal.com
```

Insert the following text:

```text
server {
        listen 5000;
        listen [::]:5000;

        root /var/www/businessjournal.com/html;
        index index.html index.htm index.nginx-debian.html;

        server_name businessjournal.com www.businessjournal.com;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

Note that the server is listening on port `5000`.  (Since port 80 is defaulted to default NGINX starting site).
* listen — Defines what port Nginx will listen on. In this case, Nginx.HTTP will listen on port 5000.

* root — Defines the document root where the files served by this website are stored.

* index — Defines in which order Nginx will prioritize index files for this website. It is a common practice to list index.html files with higher precedence than index.php files to allow for quickly setting up a maintenance landing page in PHP applications. You can adjust these settings to better suit your application needs.

* server_name — Defines which domain names and/or IP addresses this server block should respond for. Point this directive to your server’s domain name or public IP address.

* location / — The first location block includes a try_files directive, which checks for the existence of files or directories matching a URL request. If Nginx cannot find the appropriate resource, it will return a 404 error.

* location ~ \.php$ — This location block handles the actual PHP processing by pointing Nginx to the fastcgi-php.conf configuration file and the php8.1-fpm.sock file, which declares what socket is associated with php8.1-fpm.

* location ~ /\.ht — The last location block deals with .htaccess files, which Nginx does not process. By adding the deny all directive, if any .htaccess files happen to find their way into the document root, they will not be served to visitors.

<br>

3. Activate your configuration by linking to the configuration file from Nginx’s sites-enabled directory:

```bash
sudo ln -s /etc/nginx/sites-available/businessjournal.com /etc/nginx/sites-enabled/
```

4. This will tell Nginx to use the configuration next time it is reloaded. You can test your configuration for syntax errors by running the following:

```bash
sudo nginx -t
```

5. Reload nginx serive

```bash
sudo service nginx reload
```

6. Test your domain in the browser

```bash
http://localhost:5000
```

7. In case step #6 fail, you will need to set a proxy port `80:5000`

Edit file ``

```bash
server {
        listen 80;
        server_name businessjournal.com;

        location / {
                proxy_pass      http://localhost:5000;
                proxy_http_version      1.1;
                proxy_set_header        Upgrade $http_upgrade;
                proxy_set_header        Connection keep-alive;
                proxy_set_header        Host $host;
                proxy_cache_bypass      $http_upgrade;
                proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header        X-Forwarded-Proto $scheme;
        }

```

8.  Verify that you see the Home page `http://localhost:5000`

![homepage](./static/HomePage.PNG)





