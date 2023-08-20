-   pip

```
pip freeze > requirements.txt
```

-   upload

```
zip -r upload.zip *

aws --profile {p} lambda update-function-code --function-name {f} --zip-file fileb://upload.zip
```
