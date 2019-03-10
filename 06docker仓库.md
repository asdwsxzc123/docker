### 搭建不带认证的
流程:  
1. docker pull registry
2. docker run -dti --restart always // 是否一起启动
                  --name my-registry // 仓库名称
                  -p 8000:5000 // 端口映射8000到5000
                  -v /Users/xiami/dev/docker-demo/registry:/var/lib/registry  // 挂载数据集
                  registry // 镜像名称
注意:  
    registry内部对外开放端口是5000,默认镜像存放于容器内的/var/lib/regsitry目录下,如果容器被删除则存放于容器中的镜像也会丢失   
    本地利用`curl 127.0.0.1:8000/v2/_catalog` 查看本地仓库

### 上传镜像
1. 利用docker tag重命名需要上传的镜像  
    docker tag IMAGE 服务器ip:端口/IMAGE_NAME
2. 利用docker push 上传刚才重命名的镜像  
    docker push 服务器ip:端口/centos  

docker tag centos 127.0.0.1:8000/centos  
docker push 127.0.0.1:8000/centos  

注意:  
  必须重命名为服务器ip:端口/IMAGE_NAME  
  如果push出现https的错误需要往配置文件/etc/docker/daemon.json添加 
  `"insecure-registries: ["服务器ip:端口"]"`  
  然后重启docker

### 下载镜像
docker pull 127.0.0.1:8000/centos   

### 搭建带认证的仓库
1. 删除先前创建的无认证的仓库容器  
    docker rm -f my-registry
2. 创建存储认证用户名和密码的文件  
    mkdir /Users/xiami/dev/docker-demo/my-registry/auth -p  
3. 创建密码验证文件,注意将USERNAME,PASSWORD提换成设置的用户名和密码  
    docker run --entrypoint htpasswd registry -Bbn root root > /Users/xiami/dev/docker-demo/my-registry/auth/htpasswd
4. 重启仓库镜像  
```docker
  docker run -d -p 8000:5000 --restart=always --name docker-registry
              -v /Users/xiami/dev/docker-demo/registry:/var/lib/registry
              -v /Users/xiami/dev/docker-demo/my-registry/auth:/auth
              -e 'REGISTRY_AUTH=htpasswd"
              -e 'REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm'
              -e 'REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd"
              registry
```

### 下载带认证的仓库
1. docker login -u username -p password 127.0.0.1:8000   
2. docker pull / push
3. docker logout 127.0.0.1:8000