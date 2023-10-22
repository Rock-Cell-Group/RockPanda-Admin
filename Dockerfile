# Use an official Python runtime as a parent image
FROM python:3.8-slim

WORKDIR /RockPanda-Admin

COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
# Run app.py when the container launches
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
CMD python app.py

# docker build -t rockpandaadmin .
# docker run -d -p 5000:5000 -v ${PWD}:/rockpandaadmin --name rockpandaadmin rockpandaadmin





