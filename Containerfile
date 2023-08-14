FROM python:3.8-slim-buster
WORKDIR /
RUN pip install flask && pip install flask_restful
ADD src/  /
RUN chgrp -R 0 /data && chmod -R g+rwX /data
EXPOSE 8080
USER 1001
CMD [ "python", "/app.py"]
