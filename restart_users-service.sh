docker stop users-service
docker rm users-service
docker run -d -p 5001:5000 --name users-service -e APP_SETTINGS=project.config.DevelopmentConfig flaskmicroservicesusers_users-service
