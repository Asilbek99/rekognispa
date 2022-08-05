# Introduction

The goal of this project is to provide web based platform for facial recognition.



### Main features

* Age and emotion prediction

* Facial features detection

* Facial behaviours

* Multiple faces recognition in a single image.

* User registration and logging

* Records ownership

# Rekognispa


## Getting Started

First clone the repository from Github and switch to the new directory:

    git clone git@github.com/HeeZJee/rekognispa.git
    cd rekognispa
    
Activate the virtualenv for your project.
    
Install project dependencies:

    pip install -r requirements.txt
    
    
Then simply apply the migrations:

    python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

### **Environment Variables required for this project**

**SECRET_KEY**=[ your django secret key ]

**S3_BUCKET_NAME**=[your aws bucket name]

**S3_BUCKET_URL**=[your aws bucket url]

**AWS_ACCESS_KEY_ID**=[your aws acess key]

**AWS_SECRET_ACCESS_KEY**=[your aws secret key]  

**AWS_DEFAULT_REGION**=[your aws default region]

**AWS_STORAGE_BUCKET_NAME**=[your aws bucket name]
