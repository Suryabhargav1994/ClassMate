# Application Roommate


Architecture diagram:


![image](https://github.com/Hemasai8333/learning_proj/assets/115783953/b1379de9-2264-4dde-b84a-0fc1587a32c5)



Backend Application installation:

step1: Download the python latest version from this link https://www.python.org/downloads/

step2: Install all the pip libraries from the below list 
  1. pip install Django
  2. pip install djangorestframework
  3. pip install mysqlclient
  4. pip install django-cors-headers

step3: clone the code from this link 
    git clone --branch finalcode https://github.com/Hemasai8333/learning_proj.git

step4: download the mysql database https://dev.mysql.com/downloads/installer/

step5: open the cmd and enter the command **mysql -u root -p** after that enter the mysql password. finally create the database using the following command **create database student;**

![image](https://github.com/Hemasai8333/learning_proj/assets/115783953/c90f2d99-b1a5-4467-9ebf-c4da6288456c)

step6: In the application use the command **python manage.py migrate** this command will migrate all the tables in the database.

step7: This is the final step for the backend environment setup **python manage.py runserver 9000**

