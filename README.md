# session-tracker

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Tracks session information. Check out the project's [documentation](https://github.com/rolagzza/session-tracker).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

To use the session-tracker access the following link in your web browser:

[http://localhost:8000/track/login/](http://localhost:8000/track/login/)