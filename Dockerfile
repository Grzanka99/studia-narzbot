FROM python:3

RUN apt-get update && apt-get -y install nodejs npm && npm i -g nodemon

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# DEV
CMD nodemon -x "python run.py" -e "py"

# DEPLOY
# CMD ["python", "run.py"]