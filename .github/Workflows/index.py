# name: Python program
 
# on:
#   workflow_dispatch
 
# jobs:
#   Runs_the_Python_Program:
#     # runs-on: self-hosted
#     runs-on: ubuntu-latest
#     steps:
#       - name: checkout content
#         uses: actions/checkout@v2
 
#       - name: setup python
#         uses: actions/setup-python@v2
#         with:
#           python-version: '3.11'
#       - name: run python program
#         run: python index.py
 
# #   Example_environment_variables:
# #     needs: Runs_the_Python_Program
# #     runs-on: ubuntu-latest
# #     if: ${{always()}}
# #     env: 
# #       First_name: "Divpreet"
# #     steps:
# #       - name: Accessing the environment variable
# #         run: echo ${{env.First_name}}
 
# #   secret_example:
# #     needs: Example_environment_variables
# #     runs-on: ubuntu-latest
# #     steps:
# #       - name: checkout code
# #         uses: actions/checkout@v2
 
# #       - name: Use a secret variable
# #         env: 
# #           SECRET_TOKEN: ${{secrets.MY_SECRET_NAME}}
# #         run: |
# #             echo "The secret token is $SECRET_TOKEN"