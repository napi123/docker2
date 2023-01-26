## Instructions

- Run Docker Desktop
- Run Anaconda Powershell prompt in repository folder
- Build an image
```
docker build -t quadratic_function_app:v1.0 .
```
- Run the container
```
docker run --rm -it -p 5000:5000 quadratic_function_app:v1.0
```
--rm - cleans up the container after stopping service
-it - interactive mode
-p - maps ports

- Run application on  http://localhost:5000/a=1/b=2/c=3/xmin=-100/xmax=100/ymin=-100/ymax=100
Change the parameters passed in the URL and see how it affects the plot
- After finishing exploration you can remove the image, as the container has already been removed because of the --rm flag
```
docker image rm quadratic_function_app:v1.0
```

