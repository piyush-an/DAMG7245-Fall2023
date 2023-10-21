variable "aws_region" {
  description = "AWS region to create resources"
  type        = string
  default     = "us-east-1"
}

variable "default_tags" {
  type = object({ Course = string, Term = string, Assignment = string })
  default = {
    Course     = "damg7245"
    Term       = "fall2023"
    Assignment = "labs-demo-gx"
  }
}

variable "s3_bucket_name" {
  description = "AWS S3 bucket name, Note: Bucket names can consist only of lowercase letters, numbers, dots (.), and hyphens (-)."
  type        = string
  default     = "gx-nyc-trip-lab-demo"
}
