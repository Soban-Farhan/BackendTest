## Backend Developer Test
This is really simple (not simple) REST API made for a Backend Developer Assingnment

```
Note: Making this Repo public as it maybe useful for some to study or even reference.
```
### What to do?
Currently the project is only setup to use python virtualenv.
Please follow all the instructions carefully:


#### Setup Virtualenv method

1. Please download `Python 3.10.4` from [here](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
2. ~~Please follow all instruction from [Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)~~
3. ~~Activate your newly create env and run the following command~~

```
Note: Don't need the stuff above as I'm built different. The code utilizes all liberaries available in python v3.10.4.
```

<br/>
4. Run the following command to setup the Recipe and Recipe Rating table with mockdata avaiable in db folder. 
The program will create a sqllite3 file in the same folder for database crud opertions
```code
python db_table_creation.py
```

- These command will also work on your root environments but, I highly recommend using a virtual environment.


5. Project consists of static urls mentioned in the assignments file.

##### Recipes
| Name   | Method      | URL                    | Protected |
| ---    | ---         | ---                    | ---       |
| List   | `GET`       | `/recipes`             | ✘         |
| Create | `POST`      | `/recipes`             | ✓         |
| Get    | `GET`       | `/recipes/{id}`        | ✘         |
| Update | `PUT/PATCH` | `/recipes/{id}`        | ✓         |
| Delete | `DELETE`    | `/recipes/{id}`        | ✓         |
| Rate   | `POST`      | `/recipes/{id}/rating` | ✘         |

6. For any Protected request, please use the provided credentials as the program uses some hard coded values. For postman, enter the following values into Basic auth section.
```text
username: test
password: password
``` 

If you want to change these credetials. Go to servers folder and open default_user.py file. Find `basic_auth_token()` function end of the `servers.default_user.py` and change username and password too

7. The program should run and we should be good for grading the assignment. 

## Postman url and body examples

### LIST:
```code
URL: `http://localhost:5000/recipes`
```

### CREATE:
```code
URL: `http://localhost:5000/recipes`
Body:
{
    "name": "Crab and chickpea vindaloo",
    "pre_time": 6860,
    "difficulty": 3,
    "vegetarian": false
}
Authentication: Required
```

### GET:
```code
URL: `http://localhost:5000/recipes/{id}`
```

### UPDATE:
```code
URL: `http://localhost:5000/recipes/{id}`
Body:
{
    "name": "Crab and Mashed potatoes",
    "pre_time": 8034,
    "difficulty": 2,
    "vegetarian": false
}
Authentication: Required
```

### DELETE:
```code
URL: `http://localhost:5000/recipes/{id}`
Authentication: Required
```

### RATE:
```code
URL: `http://localhost:5000/recipes/{id}/rating`
Body:
{
    "recipe_id": 15,
    "rating": 5
}
```
