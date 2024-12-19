FROM python:3.12.6
RUN apt-get update && apt-get install -y git git-lfs && git lfs install
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN git pull https://github.com/AndreyGrebenyuk-vkr/composites_app_and_research.git
EXPOSE 5000

CMD ["python", "app.py"]