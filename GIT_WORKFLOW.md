# Git Workflow for the Churn Prediction MLOps Project

## 1. Aim
To manage project source code, configuration files, documentation, and workflow definitions using Git and GitHub.

## 2. Repository
The project repository is hosted on GitHub:

`https://github.com/Deepu1006-bot/churn-prediction`

The primary branch is `main`.

## 3. Check Repository Status
Run the following command from the project root:

`git status`

This command displays modified, staged, and untracked files.

## 4. Stage Changes
To stage all intended project changes:

`git add .`

Before committing, review the staged files:

`git status`

Do not commit virtual environments, passwords, access tokens, or unnecessary large generated files.

## 5. Commit Changes
Create a descriptive commit:

`git commit -m "Complete MLOps pipeline and CI documentation"`

## 6. Push Changes
Push the commit to GitHub:

`git push origin main`

If Git reports a conflict or authentication error, resolve that issue before retrying.

## 7. GitHub Actions
The project contains two workflow files:

- `.github/workflows/lab8_ci.yml`
- `.github/workflows/lab9_failure_tests.yml`

Check the repository's Actions tab to inspect execution status and downloadable artifacts.

## 8. Conclusion
Git and GitHub provide version control and collaboration, while GitHub Actions supports automated pipeline execution and testing.
