# Pipeline README

This repository contains a CI/CD pipeline for deploying an application to a Kubernetes cluster. The pipeline is defined in the `pipeline.yml` file.

## Pipeline Overview

The pipeline consists of the following stages:

1. **Build**: This stage builds the application and pushes the Docker image to the container registry.

2. **Deploy**: This stage deploys the application to the Kubernetes cluster. It includes two deployment scenarios:

   - **Regular Deployment**: If the pipeline is triggered by a branch other than a pull request, the application is deployed to the main environment.
   
   - **Pull Request Deployment**: If the pipeline is triggered by a pull request, a separate namespace is created for the pull request changes, and the application is deployed to that namespace for review and testing.

## Pipeline Configuration

Before running the pipeline, make sure to replace the following placeholders in the `pipeline.yml` file:

1. `{{ branch }}`: Replace this placeholder with the desired branch name that will trigger the pipeline.

2. `{{ containerRegistryConnection.Id }}`: Replace this placeholder with the ID of the container registry service connection established during pipeline creation.

3. `{{#toAlphaNumericString imageRepository 50}}{{/toAlphaNumericString}}`: Replace this placeholder with a unique alphanumeric string representing your image repository. You can modify the `toAlphaNumericString` function implementation in `functions/alphanumeric.py` to customize the string conversion. The second argument, `50`, specifies the maximum length of the converted string.

4. `{{ containerRegistryConnection.Authorization.Parameters.loginServer }}`: Replace this placeholder with the login server URL of your container registry connection.

5. `{{#toAlphaNumericString containerRegistryConnection.Name 50}}{{/toAlphaNumericString}}{{#shortGuid}}{{/shortGuid}}-auth`: Replace this placeholder with an alphanumeric string generated based on the `containerRegistryConnection.Name` and a short GUID followed by `-auth`. You can modify the `toAlphaNumericString` function implementation in `functions/alphanumeric.py` to customize the string conversion.

6. `$(Build.BuildId)`: Replace this placeholder with the appropriate build ID or version tag for your Docker image.

7. `ubuntu-latest`: If necessary, replace this placeholder with the desired agent VM image name for the pipeline.

8. `{{#if reviewApp}}` and `{{/if}}`: These placeholders define a conditional block that depends on the presence of the `reviewApp` variable. The content within these placeholders will be included only if the `reviewApp` variable is present. Modify the content within this block based on your specific requirements.

9. `'review-app-$(System.PullRequest.PullRequestId)'`: Replace this placeholder with the desired name for the new namespace being created to deploy the pull request changes. The placeholder includes the `System.PullRequest.PullRequestId` value, which represents the ID of the pull request.

10. `{{ k8sResource.EnvironmentReference.Name }}.{{ k8sResource.Name }}`: Replace this placeholder with the appropriate values for the environment reference name and the Kubernetes resource name for the deployment environment.

11. `{{ servicePort }}`: Replace this placeholder with the desired port number for the Kubernetes service.

Make sure to review and customize the deployment YAML files in the `manifests` directory (`deployment.yml` and `service.yml`) to match your application's configuration.

## Usage

To use the pipeline, follow these steps:

1. Replace the placeholders mentioned above in the `pipeline.yml` file.

2. Commit and push the changes to your repository.

3. The pipeline will be triggered automatically based on the configured branch or pull request events.

4. Monitor the pipeline execution and review the deployment status.

For more information on how to work with the pipeline and deploy your application to Kubernetes, refer to the [official documentation](https://docs.example.com/pipeline).
## Pipeline Configuration

The pipeline configuration file (`pipeline.yml`) includes various placeholders that need to be replaced with actual values before executing the pipeline. Let's go through each placeholder and understand how it gets replaced during pipeline execution:

- `{{ branch }}`: This placeholder represents the branch that triggers the pipeline. During execution, this placeholder will be replaced with the actual branch name that triggers the pipeline.

- `{{ containerRegistryConnection.Id }}`: This placeholder is associated with the container registry service connection. It will be replaced with the actual ID of the container registry service connection established during pipeline creation.

- `{{#toAlphaNumericString imageRepository 50}}{{/toAlphaNumericString}}`: This placeholder is a function call to `toAlphaNumericString`, which converts the `imageRepository` value to an alphanumeric string. It takes the `imageRepository` value and a maximum length of 50 characters as arguments. During execution, this function call will be replaced with the actual alphanumeric string derived from the `imageRepository` value.

- `{{ containerRegistryConnection.Authorization.Parameters.loginServer }}`: This placeholder represents the login server URL of the container registry connection. It will be replaced with the actual login server URL associated with the container registry connection.

- `{{#toAlphaNumericString containerRegistryConnection.Name 50}}{{/toAlphaNumericString}}{{#shortGuid}}{{/shortGuid}}-auth`: This placeholder combines the `containerRegistryConnection.Name` value, a function call to generate an alphanumeric string, and a short GUID followed by `-auth`. During execution, this placeholder will be replaced with the concatenated alphanumeric string, short GUID, and `-auth`.

- `$(Build.BuildId)`: This placeholder refers to the unique ID of the current build. It is a predefined variable that will be replaced with the actual build ID during execution.

- `ubuntu-latest`: This placeholder represents the agent VM image name. It can be replaced with the desired VM image name, but it does not require substitution during pipeline execution as it is a static value.

- `{{#if reviewApp}}`, `{{/if}}`: These placeholders define a conditional block based on the presence of the `reviewApp` variable. The content within these placeholders will be included only if the `reviewApp` variable is present. During execution, the conditional block will be evaluated, and if the `reviewApp` variable is set, the content within the block will be included in the pipeline.

- `'review-app-$(System.PullRequest.PullRequestId)'`: This placeholder defines the name of the new namespace being created to deploy the PR changes. It includes the `System.PullRequest.PullRequestId` value, which represents the ID of the pull request. During execution, this placeholder will be replaced with the actual value of the pull request ID.

## Getting Started

To use this pipeline configuration, follow these steps:

1. Replace the placeholders mentioned above in the `pipeline.yml` file with the appropriate values specific to your environment and requirements.

2. Commit and push the modified `pipeline.yml` file to your repository.

3. Set up the necessary service connections and configure any additional settings as per your pipeline requirements.

4. Trigger the pipeline by pushing changes to the configured branch or through any other defined triggering mechanism.

5. Monitor the pipeline execution and review the build and deployment logs for any issues or errors.

The `{{#toAlphaNumericString ...}}{{/toAlphaNumericString}}` syntax in the pipeline YAML file represents a function call to `toAlphaNumericString`. The `#` symbol denotes the start of the function call, and the `/` symbol denotes the end of the function call.

Within this function call, you can pass arguments that will be processed by the `toAlphaNumericString` function. For example, in the provided content:

```yaml
imageRepository: '{{#toAlphaNumericString imageRepository 50}}{{/toAlphaNumericString}}'
```

The `imageRepository` value is passed as an argument to the `toAlphaNumericString` function, along with a maximum length of 50 characters. The `toAlphaNumericString` function implementation (defined separately in the `functions/alphanumeric.py` file) will process the provided value and return an alphanumeric string.

So, the `{{#toAlphaNumericString ...}}{{/toAlphaNumericString}}` syntax is used to indicate a function call and pass arguments within the YAML file.
