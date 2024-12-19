FROM python:3.12.6
RUN apt-get update && apt-get install -y git git-lfs && git lfs install
WORKDIR /app
COPY . .
RUN git clone https://github.com/AndreyGrebenyuk-vkr/composites_app_and_research.git
RUN git lfs pull
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]