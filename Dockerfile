FROM public.ecr.aws/lambda/python:3.10

# Install requirements
COPY requirements.txt  .

# Install and set as trusted hosts
RUN  pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to the handler function (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]