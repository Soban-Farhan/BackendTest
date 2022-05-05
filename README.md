## Backend Developer Test
This is really simple (not simple) REST API made for a Backend Developer Assingnment

### What to do?
Currently the project is only setup to use python virtualenv.
Please follow all the instructions carefully:

#### Setup Virtualenv method

1. Please download `Python 3.10.4` from [here](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
2. Please follow all instruction from [Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv)
3. Activate your newly create env and run the following command
```bash
pip install -r requirements.txt
```

4. Run the following command to setup the Recipe and Recipe Rating table with mockdata avaiable in db folder. 
The program will create a sqllite3 file in the same folder for database crud opertions
```bash
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
