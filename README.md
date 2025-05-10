# reverse-proxy
- 성능
- 부하분산(LB)
- 가상호스트 및 라우팅

## python server
```bash
$ python -m http.server --directory pyweb1 8001
$ python -m http.server --directory pyweb2 8002
$ python -m http.server 8003 --directory blog 
```
## nginx
- https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview
```bash
# install
$ sudo apt install nginx

$ sudo service nginx restart
$ sudo service nginx stop 
$ sudo service nginx start
$ sudo service nginx status #-> worker 16ea
$ sudo nginx -t # syntax check
```

## nGrinder
- http://localhost:8080 (admin/admin)
```bash
$ pwd
~/app
$ tree -L 2
.
├── ngrinder-agent
│   ├── lib
│   ├── run_agent.sh
│   ├── run_agent_bg.sh
│   ├── run_agent_internal.sh
│   └── stop_agent.sh
└── ngrinder-controller
    └── ngrinder-controller-3.5.9-p1.war

# controller
$ java -jar ngrinder-controller-3.5.9-p1.war

# agent
$ run_agent.sh
```

## Scale out

``` bash
$ sudo docker compose stats
$ sudo docker compose up -d --scale web1=24
$ sudo docker compose restart lb
```
- 스케일 아웃 후 lb 도커 밖에서 재시작 방법(죽었다가 다시 살아남 에러 발생)
- 현재 상황에서는 CPU 1% 도달시 MTT 늘어짐 lb 는 5% 도달 시 스케일 아웃하더라도 늘어짐
- CPU net I/O 를 다 잘 고려해서 판단 해야함
```
$ sudo docker exec -it reverse-proxy-lb-1 bash
$ nginx -s reload
``` 
- 스케일 아웃 후 lb 도커 안에서 재시작 방법 (에러 없이 분산적용) 

```
services:
  web1:
    image: httpd:latest
    volumes:
      - ./pyweb1:/usr/local/apache2/htdocs
    deploy:
      resources:
        limits:
          cpus: "0.01" 
          memory: "40M"
    expose:
      - "80"
    environment:
      - VIRTUAL_HOST=localhost
      - VIRTUAL_PORT=80
  
  nginx-proxy:
    image: nginxproxy/nginx-proxy # https://github.com/nginx-proxy/nginx-proxy
    ports:
      - "9889:80"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro
    depends_on:
      - web1
```
- auto scaling

## Fastapi
- https://fastapi.tiangolo.com/ko/
```
$ source .venv/bin/activate
$ fastapi deb main.py
```
## PDM create requriment.txt
 
```
$ pdm export -o requirements.txt --without-hashes
```
## Docker build & run
```
$ sudo docker build -t myapi1 -f docker/fastapi/Dockerfile .
```
- 생성
```
$ sudo docker run -d --name my-api-1 -p 8949:80 myapi1
```
- run 
## ref
- https://fastapi.tiangolo.com/ko/
- http://jasonwilder.com/blog/2014/03/25/automated-nginx-reverse-proxy-for-docker/
- https://hub.docker.com/r/nginxproxy/nginx-proxy

## Deploy Blog to AWS
``` bash
$ cd ~/keys
$ ssh -i "<mykey.pem>" <서버이름>@<퍼블릭 IPv4 DNS>

$ mkdir code
$ cd code
$ git clone https://github.com/Jacob-53 (https clone)
$ cd <REPO FOLDER>
$ sudo cp -rf blog /var/www

$ cd /etc/nginx/sites-enabled
$ sudo vi blog(any name)
    ``` bash
    server {
        listen 80;
        listen [::]:80;

        server_name aws.jacob53.shop;

        root /var/www/blog;
        index index.html;

        location / {
                try_files $uri $uri/ =404;
        }
    }
    ```
$ sudo nginx -t
$ sudo systemctl restart nginx
만약 AWS 퍼블릭 IPv4 DNS 로 접속 원한다면 
$ sudo vi /etc/nginx/nginx.conf
$ server_names_hash_bucket_size 128; 수정
만약 수정 하였다면
$ sudo nginx -t
$ sudo systemctl restart nginx
접속테스트 

```
