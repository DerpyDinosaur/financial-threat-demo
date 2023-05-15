FROM python:3.11 AS build

WORKDIR backend
COPY database.bak ./database.json

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

########## Develop ##########

FROM build as dev
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]

########## Production ##########

FROM build as prod
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]