FROM prefecthq/prefect:{{ cookiecutter.prefect_docker_image_tag }}
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD flows /opt/prefect/flows