nouran@nouran-Swift-SF315-41:~/Downloads/3/Virtualization II/Project/worker_container$ ll
total 16
drwxrwxr-x 2 nouran nouran 4096 Jan 31 17:37 ./
drwxrwxr-x 4 nouran nouran 4096 Jan 31 17:00 ../
-rw-rw-r-- 1 nouran nouran  113 Jan 31 17:32 Dockerfile
-rw-rw-r-- 1 nouran nouran 2390 Jan 31 16:59 project.py
nouran@nouran-Swift-SF315-41:~/Downloads/3/Virtualization II/Project/worker_container$ docker build -t project/1.0 .
Sending build context to Docker daemon   5.12kB
Step 1/5 : FROM python:latest
 ---> 4b9378be0bb9
Step 2/5 : RUN pip3 install numpy
 ---> Using cache
 ---> b25d666b3858
Step 3/5 : WORKDIR /run
 ---> Using cache
 ---> 844a8306e85f
Step 4/5 : COPY project.py .
 ---> Using cache
 ---> 6b640de1be7e
Step 5/5 : ENTRYPOINT ["python3", "project.py"]
 ---> Using cache
 ---> dd0d690aec7d
Successfully built dd0d690aec7d
Successfully tagged project/1.0:latest
nouran@nouran-Swift-SF315-41:~/Downloads/3/Virtualization II/Project/worker_container$ docker run -v "$(pwd)":/run project/1.0 .
/run/project.py:34: RuntimeWarning: invalid value encountered in true_divide
  delta = (y6 - y5)/y6
nouran@nouran-Swift-SF315-41:~/Downloads/3/Virtualization II/Project/worker_container$ ll
total 2324
drwxrwxr-x 2 nouran nouran    4096 Jan 31 17:37 ./
drwxrwxr-x 4 nouran nouran    4096 Jan 31 17:00 ../
-rw-rw-r-- 1 nouran nouran     113 Jan 31 17:32 Dockerfile
-rw-r--r-- 1 root   root    122625 Jan 31 17:37 h.txt
-rw-rw-r-- 1 nouran nouran    2390 Jan 31 16:59 project.py
-rw-r--r-- 1 root   root   2236949 Jan 31 17:37 y.txt
nouran@nouran-Swift-SF315-41:~/Downloads/3/Virtualization II/Project/worker_container$ 

