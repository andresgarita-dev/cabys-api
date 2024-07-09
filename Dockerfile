FROM python:3.11-alpine
LABEL maintainer=info@andresgarita.com
RUN addgroup -S user && adduser -SD -h /home/user -G user user
RUN apk update
RUN apk add tzdata && cp /usr/share/zoneinfo/America/Costa_Rica /etc/localtime \
    && echo "America/Costa_Rica" > /etc/timezone
WORKDIR /home/user
COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps gcc libc-dev g++ libffi-dev libxml2-dev curl gnupg\
    && apk add --no-cache unixodbc unixodbc-dev libstdc++ \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps
COPY . .
RUN chown -R user:user /home/user && chmod +x /home/user/entrypoint.sh
USER user