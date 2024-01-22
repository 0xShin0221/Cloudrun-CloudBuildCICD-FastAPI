cloudrun-repo-create:
	@echo Creating Cloud Run Repository...
	gcloud artifacts repositories create $(REPOSITORY) --location $(REGION) --repository-format "docker"

cloudrun-deploy: 
	@echo Deploying to Cloud Run...
	gcloud run deploy $(REPOSITORY) --image gcr.io/$(GOOGLE_CLOUD_PROJECT)/$(REPOSITORY) --platform managed --region $(REGION)
