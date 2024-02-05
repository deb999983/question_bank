### QuestionBank API
To start up the API first build the images by running the command
```
make build
```

then start up the services by running the command,
```
make up
```

The above command will start up the following services,
- **question_bank_db**
- **question_bank_api**

After the services have been started, visit http://localhost:9060/swagger/,
to try out the apis.
