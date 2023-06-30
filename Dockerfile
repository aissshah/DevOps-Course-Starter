FROM python:3.12.0b2-buster as base

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV POETRY_HOME=/root/.local/share/pypoetry/venv/
ENV PATH="$PATH:$POETRY_HOME/bin"

WORKDIR /src
COPY poetry.lock pyproject.toml /src/

RUN poetry config virtualenvs.create false && poetry install --no-root --no-directory --no-dev

COPY . /src/

FROM base as production

ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:app"

FROM base as development

RUN poetry install
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

FROM base as test

RUN poetry install
RUN poetry run pytest