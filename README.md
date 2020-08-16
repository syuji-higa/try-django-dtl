- Tried the book: https://www.amazon.co.jp/%E9%80%9F%E7%BF%92-Django-3-%E9%80%9F%E7%BF%92%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E5%B1%B1%E7%94%B0%E7%A5%A5%E5%AF%9B-ebook/dp/B089VXJYC7

## Command

### Create
```sh
# Cerate project
$ django-admin startproject {project-name}

# Create app
$ python manage.py startapp {app-name}

# Create migration file
$ python manage.py makemigrations {app-name}

# Run migration
$ python manage.py migrate

# Collects static
$ python manage.py collectstatic
```

### Fixture
```sh
# Run fixture
$ python manage.py loaddata {app-name}

# Create fixture
$ python manage.py dumpdata --format yaml --output {name}.yaml {model}
```

### Start
```sh
# Run server
$ python manage.py runserver
```

### Django Shell
```sh
# Run shell
$ python manage.py shell
```

### Database
```sh
# Check database
$ sqlite3 db.sqlite3
```
