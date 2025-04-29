FROM python.3.13


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /shop_apii


COPY reguirements.txt /shop_apii/reguirements.txt

RUN pip install -r /shop_apii/reguirements.txt

COPY . .