### Dockerfile书写
```shell
# 这是测试的dockerfile
FROM centos
RUN echo '这是测试的dockerfile'
```

### 构建Dockerfile
docker build [OPTIONS] PATH | URL
-t 设置文件名和tag信息  
  docker build /Users/xiami/dev/docker-demo/dockerfile-dir -t test-images:v1.0  

-f 提供文件  
docker build /Users/xiami/dev/docker-demo/dockerfile-dir/test-file -t test-images:v1.0

### Dockerfile命令
* FROM: 指定基础镜像
* RUN: 构建镜像过程需要执行的命令
* CMD: 添加启动容器时需要执行的命令,多条只有最后一条生效,可以在启动容器时被覆盖修改
* ENTRYPOINT: 同CMD,但这个一定会被执行,不会被覆盖修改
* LABEL: 为镜像添加对于的数据
* MAINTAINER: 表明镜像的作者,将被遗弃,被LABEL代替
* EXPOSE: 设置对外暴露的端口
* ENV: 设置执行命令的环境变量,并且在构建完成后,依然生效
* ARG: 设置只在构建过程中使用的环境变量,并且在构建完成后,消失
* ADD: 将本地文件或目录拷贝到镜像的文件系统中,能解压特定格式文件,能将URL作为要拷贝的文件
* COPY: 将本地文件或目录拷贝到镜像的文件系统中
* VOLUME: 添加数据卷
* USER: 执行以哪个用户的名义执行RUN,CMD和ENTRYPOINT命令
* WORKDIR: 设置工作目录

### RUN
1. RUN <command> 执行shell命令,会保留之前的环境变量
  RUN /bin/bash -c echo 'HELLO'
2. RUN ['executable', 'param1', 'param1'] exec方式执行,会终结之前的终端,不会保留之前的环境变量

### CMD,ENTRYPOINT
CMD的命令会被覆盖,ENTRYPOINT不会覆盖

### EXPOSE
可以写多个端口,还能修改协议,tcp,udp

### ADD
可以添加本地文件,tar格式可以解压成功或失败,也可以添加url

### COPY
只能拷贝文件,不能解压,但可以多做一步tar来解压
COPY sh.sh /root/dir