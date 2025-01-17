# ci_cd_sentiments_analysis

## 📖 Overview
This project sets up an automated CI/CD pipeline to test a sentiment analysis API. The goal is to ensure the proper functioning of the API through unit and integration tests, executed via Docker containers orchestrated by Docker Compose.

## API Description
The sentiment analysis API provides the following endpoints:

  - /status: Checks the proper functioning of the API.
  - /permissions: Checks the permissions of a user (identified by a username and password).
  - /v1/sentiment: Provides sentiment analysis using an old model.
  - /v2/sentiment: Provides sentiment analysis using a new model.

---

## 🛠️ Setup

### Prerequisites
- Docker: Install Docker
- Docker Compose: Install Docker Compose

### Installation
1. **Clone the project**

git clone `https://github.com/keichk/ci_cd_sentiments_analysis.git`
cd ci_cd_sentiment_analysis

3. **Build the containers**
    ```bash
      ./setup.sh
4. **Start the containers**
    ```bash
      docker-compose up -d
5. **View the logs The results of the tests will be written to log.txt.**
   
---

## 🧪 Tests

### Authentication Test
- Endpoint: **`/permissions`**
- Test: Validates the correct user credentials (alice and bob). It should return:
    - 200 for valid credentials (alice:wonderland and bob:builder)
    - 403 for invalid credentials (alice:clementine and bob:mandarine).

### Authorization Test
- Endpoints: **`/v1/sentiment`**, **`/v2/sentiment`**
- Test: Validates user access to models based on their permissions:
    - bob has access to only the v1 model.
    - alice has access to both v1 and v2 models.
  
### Content Test
-  Endpoints: **`/v1/sentiment`**, **`/v2/sentiment`**
- Test: Analyzes two sample sentences:
    - "life is beautiful": should return a positive sentiment score.
    -  "that sucks": should return a negative sentiment score.

## 🚀 Docker Compose
The project uses Docker Compose to orchestrate the running of the API and tests in separate containers. The following services are defined:

  - API: The sentiment analysis API container (**`/fastapi`**).
  - Authentication Test: A container running tests for the **`/permissions`** endpoint.
  - Authorization Test: A container running tests for the **`/v1/sentiment`** and **`/v2/sentiment`** endpoints.
  - Content Test: A container running tests for content analysis with two sample phrases.

## 📄 Files
This project contains the following files:

 - **docker-compose.yml**: Defines the services for the API and the three test containers (authentication, authorization, content).
 - **setup.sh**: A shell script to build and start the containers.
 - **Dockerfiles**: Custom Dockerfiles for each test container.
 - **log.txt**: A file where the results of the tests are logged.

## 👨‍💻 Running Tests

1. Build and start the containers using Docker Compose
    ```bash
      ./setup.sh
      docker-compose up -d

2. Monitor the test results in log.txt.

## 🤖 Continuous Integration / Continuous Deployment
This setup can easily be integrated into a CI/CD pipeline (e.g., GitHub Actions, GitLab CI, Jenkins) to run the tests automatically before deploying the API to production.

## 📜 License
This project is licensed under the MIT License.

## 👤 Author
This project was developed by **Ben Cheick**.
