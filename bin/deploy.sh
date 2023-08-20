cd modules

zip -r ../upload.zip .

cd ..

zip upload.zip lambda_function.py

aws --profile devenue lambda update-function-code --function-name ak-api --zip-file fileb://upload.zip