# Postgres

## Client
Run `psql -U gamnes -d postgres` access the `postgres` database with `gamnes` user

### Commands

[All commands](https://www.postgresql.org/docs/current/app-psql.html)

SQL requests:

- find duplicate `SELECT pks, COUNT(*) FROM leitner_flashcard GROUP BY pks HAVING COUNT(*) > 0;`
- change password `ALTER USER user WITH PASSWORD 'newpwd';`

Other:

- `\q` close the client
- `\du` list roles/users
- `\l` list databases

## Environment variables

```sh title=".env"
PGDATABASE = "db"
PGHOST = "host"
PGUSER =  "user"
PGPASSWORD =  "pwd"
```

## Docker image

```yaml title="docker-compose.yml"
services:
    db:
        image: postgres:14
        env_file:
            - .env
        environment:
            POSTGRES_DB: ${PGDATABASE}
            POSTGRES_USER: ${PGUSER}
            POSTGRES_PASSWORD: ${PGPASSWORD}
        restart: unless-stopped
        volumes:
            - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

The image will:

- create a database and user when ran
- expose 5432 port by default
- create `/var/lib/postgresql/data` volume (so it's better to link it to existing one)
