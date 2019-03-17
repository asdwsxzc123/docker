### docker compose file 顶级配置项
* version: 指定docker Compose File版本号
* services: 定义多个服务并配置启动参数
* volumes: 声明或创建在多个服务中共同使用的数据卷对象
* networks: 定义在多个服务中共同使用的网络对象
* configs: 声明将在本服务中使用的一些配置文件
* secrets: 声明将在本服务中药使用的一些秘钥,密码文件
* x-***: 自定义配置,主要用于复用相同的配置

### docker compose搭建项目
1. 搭建一个flask的小型web项目
2. 根据项目环境,利用Dockerfile构建镜像
3. 撰写docker-compose.yaml配置文件,启动项目
<!-- docker run -p 6379:6379 --name redis -v /Users/li/docker/redis/redis.conf:/etc/redis/redis.conf -v /Users/li/docker/redis/data:/data -d redis redis-server /etc/redis/redis.conf  -->
