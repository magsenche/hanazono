# Hanazono

![logo](./docs/assets/logo.png)

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)

Hanazono is a versatile tool designed to help you build a website for your personal notes while enhancing your learning through a spaced-repetition based daily quiz system using Leitner boxes.

It leverages [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) for writing notes, making it easy to create and manage your content.

You can check my hanazono [azure](https://hanazono.azurewebsites.net/) or [render](https://hanazono.onrender.com) (may be slow due to free hosting). Log in is required to have access to the Daily Quiz.

1. write your notes as markdown `.md` file
2. define flashcards as a [question admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/?h=admon#+type:question)
   ```
   ??? question "<question>"
       <answer>
   ```
   or
   ```
   ???+ question "<question>"
       <answer>
   ```

## Environment variable
```ini
# Server port
SERVER_PORT = 8001

# Database creation (see [postgress](https://hub.docker.com/_/postgres))
POSTGRES_DB = "postgres"
POSTGRES_USER =  "user"
POSTGRES_PASSWORD =  "pwd"

# Database connection
POSTGRES_HOST = "db" # set it to "db" when using docker-compose (postgres service name)
POSTGRES_PORT = 5432

# Django admin
DJANGO_SUPERUSER_USERNAME=${POSTGRES_USER}
DJANGO_SUPERUSER_PASSWORD=${POSTGRES_PASSWORD}
DJANGO_SUPERUSER_EMAIL="user@mail.com"

# Django settings
DJANGO_SETTINGS_MODULE="hanazono_conf.production"
SECRET_KEY = "y0urv3rys3cr3tk3y"
ALLOWED_HOSTS = "localhost"
STANDALONE = false

# Redis connection
REDIS_PORT = 6379
REDIS_HOST = "redis"
```

## Launch your Hanazono
There are several ways to get your own Hanazono instance up and running. Choose the method that best suits your needs and technical expertise.

### Docker
#### Docker Compose (recommended)
This is the easiest and most recommended approach if you're comfortable with Docker. It offers a streamlined setup with minimal configuration.

1. setup your environment variables (automatic if you use pdm)
2. write and put your notes as markdown files in the `docs` folder
3. start django server and postgres database services `docker-compose up`:
   - creates a postgres database
   - extracts flashcards from your notes
   - creates django admin user
   - builds the site and run the django server on http://localhost:{SERVER_PORT}

As `docs` folder is mounted in the server container: updates are directly available from the site. You just need to click on "Update site" from the admin panel.

#### Standalone (for Free Hosting)
Useful if you can't use docker-compose for instance free host provider such as [render](https://render.com/) or azure.

Here, Hanazono operates within a single container and uses a local SQLite3 database instead of an external one.

1. make sur to set:
   - `DJANGO_SETTINGS_MODULE="hanazono_conf.production"`
   - `STANDALONE=true` to use a sqlite3 database
2. use `Dockerfile.standalone` to build the image `docker build -f Dockerfile.standalone -t hanazono-server:latest .`
3. push your image and upload it on your host
4. run the server `docker run --env-file .env -p 8000:8000 hanazono-server:latest`

### PDM (recommended for development)

1. set `DJANGO_SETTINGS_MODULE="hanazono_conf.settings"` if in dev mode & make sure to have you database up and running
2. install dependencies `pdm install`
3. put environment variables in an `.env` file
4. start the postgres database
5. initialize the server `pdm run init` (extracts flashcards and build the static files in `site/`)
6. run the django server `pdm run manage runserver`

### Without PDM
Follow the same steps as above but without using PDM commands (refer to `pyproject.toml`). Make sure to editably install the project.

## AI Assistant
To use the ai assistant package to help you generate notes or flashcards, change `pdm install --without aiassistant` into `pdm install` to install the [aisan](https://github.com/magsenche/aiasan) package. See [example](https://github.com/magsenche/hanazono/blob/main/examples/aiassistant.py)

## TODO
### Features
- [x] make a Notes django model
- [x] provide tools to analyze flashcards/notes
- [ ] use ai assistant from the website directly

### Test
- [x] re-write tests

### Documentation
- [x] install without PDM
- [ ] start PostgreSQL database instructions
- [x] add typing everywhere
- [ ] ~~add docstring (may not be necessary if typing & good naming)~~
- [ ] add showcase video

### Distribution & Deployment
- [x] use a production server
- [x] correctly package the project
- [ ] use a multi-stage build to install `aiasan` and only copy necessary files to lighten the image
- [x] deploy without docker-compose
- [x] optional dependencies for ai assistant
- [ ] export & import database automatically on new deployement