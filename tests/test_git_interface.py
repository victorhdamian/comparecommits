from src.comparecommits.git_interface import get_commits
import pytest

def test_git_interface(self):
    org = "aws-ia"
    repo = "terraform-aws-eks-blueprints"
    head = "e7040b657d95be543ed9c46187126ee8afe3a927"
    base = "dbd9ca385b0f8055e9aab1a54f76e0e74159fbe4"
    assert get_commits(org, repo, base, head) == ''