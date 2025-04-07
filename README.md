# Django Tutorial Chai Aur Django series
### Topics covered
 - create Project by
 ```django-admin startproject my_project```

 - server run by
  ```py manage.py runserver {port_no}```
 
 - Djagno server run this way:
    ! [alt text](./server.png)
    <!-- <img src=server.png/> -->
 - create templates for rendering a html file will be inside templates folder
    - first add templates to the settings directory like this:
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    ```
    - Here inside 'DIRS' add templates

- To load static css with html file add ```{% load static %}``` above html boilerpalte
- link css like this ```<link rel="stylesheet" href={% static "style.css" %}>```
- to link static folder like html add this to the settings.py
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```
