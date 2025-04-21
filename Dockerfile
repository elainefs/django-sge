FROM python:3.11-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
