FROM prefecthq/prefect:2.5.0-python3.9
COPY requirements.txt .
COPY add_nexus.sh .
RUN chmod +x ./add_nexus.sh
RUN ./add_nexus.sh
RUN pip install -r requirements.txt
ADD flows /opt/prefect/flows
ADD data /opt/prefect/data