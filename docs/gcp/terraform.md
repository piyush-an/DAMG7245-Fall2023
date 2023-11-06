---
tags:
  - GCP
  - Compute Engine
  - Terraform
# hide:
#   - navigation
#   - toc

---


# Provisioning a Compute Engine on Google Cloud Platform (GCP) using Terraform
## Introduction

Welcome to the comprehensive guide for setting up infrastructure on Google Cloud Platform (GCP) and establishing a connection to Visual Studio Code (VS Code)  using Terraform. 

## Prerequisite

1. Install Terraform

    Install Terraform on your local machine. You can download the appropriate Terraform package for your operating system from the [official Terraform website](https://developer.hashicorp.com/terraform/downloads) and follow the installation instructions for your platform.
    Ensure that Terraform is added to your system's PATH to enable running Terraform commands from the terminal or command prompt.

    To verify the installation, open a terminal or command prompt and type 
    ```terraform
    terraform -v
    ``` 
    This command should display the installed Terraform version.

2. Create Service Account

    1. Access your GCP Console using your credentials.
    2. Navigate to the **IAM & Admin** section in the GCP Console.
    3. Select **Service Accounts** and click on **Create Service Account**
    4. Fill in the necessary details for the service account, such as name and description.
    5. Assign the role **`Compute Admin`** to the service account. This role grants the necessary permissions to manage Compute Engine resources.
    6. After creating the service account, generate and download the key for this service account as a JSON file.
    7. This key file contains the authentication credentials required by Terraform to manage resources on GCP.
    8. Save Key Contents to tfkey.json:
    9. Once the JSON key file is downloaded, open the file and copy its contents.
    10. Create a file named `tfkey.json` in the directory where you'll be working with your Terraform code.
    11. Paste the contents of the downloaded JSON key into the `tfkey.json` file.
    ???+ warning
        Ensure the key file (`tfkey.json`) remains secure and isn't shared publicly, as it contains sensitive authentication information allowing access to your GCP resources.

3. SSH Key Generation

    1. Use the following command to generate an SSH key pair:
        ```bash
        ssh-keygen -t rsa -f ce -C ubuntu -b 2048
        ```
        - `-t rsa`: Specifies the type of key to create (RSA).
        - `-f ce`: Sets the file name of the generated key to 'ce' (You can change 'ce' to a name of your choice).
        - `-C ubuntu`: Provides a comment, typically the username or a descriptive tag.
        - `-b 2048`: Specifies the number of bits in the key (2048-bit key in this case).
    2. Upon execution, you might be prompted to enter a passphrase to secure your private key. Press Enter for an empty passphrase if you prefer not to use one.
    3. The command will generate two files: `ce` (private key) and `ce.pub` (public key) in your current directory.
    4. The corresponding public key (`ce.pub`) can be shared with your Compute Engine instance or other services for authentication.
    ???+ warning
        Ensure the private key (`ce`) remains secure and isn't shared publicly. This private key will be used to authenticate SSH connections to your Compute Engine instance.

## Tutorials

1. Update the .tfvars (Terraform variables) file.
    ```terraform title="terraform.tfvars"
    project_id = "emerald-road-403117"
    region = "us-east1"
    zone = "us-east1-b"
    name = "class-demo-redis"
    ssh_key_filename = "ce-tf"
    machine_type = "e2-standard-4"
    storage = 100
    ```
    1. **`project_id`:** Replace the value with your specific GCP Project ID.
    2. **`region`:** Set the desired region for deploying resources in GCP.
    3. **`zone`:** Choose the appropriate zone within the specified region.
    4. **`name`:** Define a unique name for the Compute Engine instance or resource.
    5. **`ssh_key_filename`:** Enter the name of the SSH key file generated previously.
    6. **`machine_type`:** Select the desired machine type for the Compute Engine instance.
    7. **`storage`:** Specify the amount of storage required for the instance (in GB).

2. Update the main.tf file to open the firewall ports

    ```terraform title="main.tf"
    allow {
        protocol = "tcp"
        ports    = ["80", "8080", "50001", "50002", "50003", "50004"] # TODO: Change ports as required
    }
    ```

3. Initialize the Terraform Configuration

    Execute the following command in your terminal or command prompt to initialize your Terraform configuration:

    ```bash
    terraform init
    ```
    This command initializes the working directory and prepares the configuration, ensuring all necessary plugins and modules are downloaded.

4. Generate and Review an Execution Plan:

    To view the changes Terraform will apply before actually deploying the infrastructure, use the following command:

    ```bash
    terraform plan
    ```
    This command generates an execution plan by examining the current state of your infrastructure and comparing it to the desired state defined in your configuration files (*.tf). Review the proposed changes in the plan output.

    Sample output:
    ```bash
    Plan: 3 to add, 0 to change, 0 to destroy.

    Changes to Outputs:
    + ExternalIP = (known after apply)
    ```

5. Apply Changes to Deploy Infrastructure
    Execute the following command to apply the changes defined in your Terraform configuration and deploy the infrastructure:

    ```bash
    terraform apply
    ```
    The apply command implements the changes defined in your configuration files, creating or modifying the infrastructure according to the execution plan. It prompts for confirmation before making any changes.

    Sample output:
    ```bash
    Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

    Outputs:
    ExternalIP = "34.139.43.201"
    ```

6. SSH Connection using the Generated Key
    Use the following command in your terminal to connect to your Compute Engine instance via SSH:

    ```bash
    ssh -i ce ubuntu@34.139.43.201
    ```
    1. `-i ce`: Specifies the identity file (private key) for authentication. Replace ce with the actual name of your SSH private key file.
    2. `ubuntu@34.139.43.201`: Replace this with the actual username and IP address (or hostname) of your Compute Engine instance.


7. Deploying Services and Docker Containers to Compute Engine

    To run your application services on your Compute Engine instance, follow these steps:

    1. Clone Repository and Prepare Environment
    2. Build Docker Image
    3. Run Docker Compose

    This will facilitate running your application services within containers on the remote server.

8. Destroy Resources 

    ???+ warning
        Proceed once you no longer require the resources

    If you intend to remove all resources defined in your configuration, you can execute the following command:

    ```bash
    terraform destroy
    ```
    The destroy command removes all resources defined in your Terraform configuration. It is irreversible and should be used judiciously, as it will delete the provisioned infrastructure.
    Sample output:
    ```bash
    Destroy complete! Resources: 3 destroyed.
    ```

Continued exploration and further customization of the deployed resources can enhance and optimize the infrastructure, catering to specific project requirements and evolving needs.

Happy provisioning and managing your infrastructure on GCP with Terraform!