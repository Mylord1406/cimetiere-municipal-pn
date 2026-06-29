FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    proj-bin \
    postgresql-client \
    libcairo2-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Trouver et lier GDAL au bon endroit
RUN ln -s $(find /usr -name "libgdal.so*" | head -1) /usr/lib/libgdal.so || true

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

COPY requirements_linux.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements_linux.txt

COPY . .

RUN python manage.py collectstatic --noinput --settings=config.settings.production || true

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --settings=config.settings.production && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]