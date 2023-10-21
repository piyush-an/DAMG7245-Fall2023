terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.52.0"
    }
  }
}

provider "aws" {
  shared_credentials_files = ["~/.aws/credentials"]
  region                   = var.aws_region

  default_tags {
    tags = var.default_tags
  }
}

resource "aws_s3_bucket" "s3_bucket" {
  bucket        = var.s3_bucket_name
  force_destroy = false
}

resource "aws_s3_bucket_public_access_block" "s3_bucket_public" {
  bucket = aws_s3_bucket.s3_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "public_read_access" {
  bucket = aws_s3_bucket.s3_bucket.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : ["s3:GetObject"],
        "Resource" : [
          "${aws_s3_bucket.s3_bucket.arn}/*"
        ]
      }
    ]
  })
}
