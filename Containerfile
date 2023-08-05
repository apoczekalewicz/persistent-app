FROM python:3.8-slim-buster
WORKDIR /
RUN pip install flask && pip install flask_restful
ADD src/  /
RUN chgrp 0 /data && chmod g+rwx /data/
EXPOSE 8080
USER 1001
CMD [ "python", "/app.py"]
