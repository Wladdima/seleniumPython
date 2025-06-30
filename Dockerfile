FROM python:3.12

WORKDIR /app

COPY requirements.txt .

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "-c", "pytest --alluredir=allure-results && allure generate allure-results --clean -o allure-report", "test_cart_page.py"]