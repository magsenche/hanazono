# Hanazono

![logo](./docs/assets/logo.png)

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)

Hanazono is a versatile tool designed to help you build a website for your personal notes while enhancing your learning through a spaced-repetition based daily quiz system using Leitner boxes.

It leverages [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) for writing notes, making it easy to create and manage your content.

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

## Launch your Hanazono
### Environment variable

```ini
POSTGRES_DB = "postgres"
POSTGRES_USER =  "user"
POSTGRES_PASSWORD =  "pwd"

DJANGO_SUPERUSER_USERNAME=${POSTGRES_USER}
DJANGO_SUPERUSER_PASSWORD=${POSTGRES_PASSWORD}
DJANGO_SUPERUSER_EMAIL=""

POSTGRES_HOST="db"
POSTGRES_PORT=5432
SERVER_PORT=8001
```

- database creation: `POSTGRES_DB`,`POSTGRES_USER`,`POSTGRES_PASSWORD` (see [postgress](https://hub.docker.com/_/postgres))
- database-server connection: `POSTGRES_HOST`(should be set to `db` when using docker),`POSTGRES_PORT`.
- django admin: `DJANGO_SUPERUSER_USERNAME`,`DJANGO_SUPERUSER_PASSWORD`,`DJANGO_SUPERUSER_EMAIL`
- server: `SERVER_PORT`


### Docker
1. setup your environment variables (automatic if you use pdm)
2. write and put your notes as markdown files in the `docs` folder
3. start django server and postgres database services `docker-compose up`:
   - creates a postgres database
   - extracts flashcards from your notes
   - creates django admin user
   - builds the site and run the django server on http://localhost:{SERVER_PORT}

As `docs` folder is mounted in the server container: updates are directly available from the site. You just need to click on "Update site" from the admin panel.

### PDM
1. install dependencies `pdm install`
2. put environment variables in an `.env` file
3. start the postgres database
4. initialize the server `pdm run init` (extracts flashcards and build the static files in `site/`)
5. run the django server `pdm run manage runserver`

### Without PDM
Follow the same steps as above but without using PDM commands (refer to `pyproject.toml`). Make sure to editably install the project.


## TODO
### Features
- [ ] make a Notes django model
- [ ] provide tools to analyze flashcards/notes

### Test
- [x] re-write tests

### Documentation
- [ ] install without PDM
- [ ] start PostgreSQL database instructions

### Distribution & Deployment
- [ ] use a production server
- [x] correctly package the project