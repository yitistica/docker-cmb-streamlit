FROM continuumio/miniconda3
COPY . /app
WORKDIR /app/src
RUN pip3 install -r ../requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]

