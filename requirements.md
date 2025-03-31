pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
pip install Pillow

### REST APIs

###### ACCOUNT LOGIN/REGISTER

http://127.0.0.1:8000/account/register/
http://127.0.0.1:8000/account/login/

### MOVIES

###### GET MOVIE LIST

http://127.0.0.1:8000/movies/list/

###### MOVIE POST - ONLY ADMIN - CREATE MOVIE LIST

http://127.0.0.1:8000/movies/list/create

###### GET/PUT/DELETE - ONLY ADMIN

http://127.0.0.1:8000/movies/2/

#### WATCHLIST MOVIE CRUD

##### GET - LIST THE WATCHLIST MOVIES FOR PARTICULAR USER ONLY

http://127.0.0.1:8000/account/movie/watchlist/

###### POST - ONLY EXISTING MOVIES ID

http://127.0.0.1:8000/account/movie/watchlist/add/1/
{
"movie": 1
}

###### DELETE - REMOVE MOVIE FROM WATCHLIST

http://127.0.0.1:8000/account/movie/watchlist/remove/1/
