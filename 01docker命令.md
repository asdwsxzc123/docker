docker search images 查询远端仓库镜像
docker pull images 拉取远端镜像
docker run images 运行镜像
docker kill images 关闭镜像进程
docker rmi -f images 删除镜像
docker save images > images.tar 镜像打包
docker load -i images.tar 镜像解压
docker tag images:tag1 images:tag2 镜像tag重命名,只是增加了引用
docker inspect images 查看镜像详情
    -f go的format语法
    docker image inspect centos | grep Created
    docker image inspect -f "{{json .Id}}" centos 
docker history [options] images 历史分层信息
    -h --human 将创建时间,大小进行优化打印(默认true)
    -q --quiet 只打印镜像id
        --no-trunc 不缩略显示
docker ps -a 查看所有容器状态
    