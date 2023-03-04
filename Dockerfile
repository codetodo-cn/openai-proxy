FROM liyaodev/base-cpu-u18-py3.8:v1.0.0
LABEL maintainer=liyaodev

RUN rm -rf /usr/local/bin/python && ln -s /usr/local/bin/python3.8 /usr/local/bin/python
RUN rm -rf /usr/local/bin/pip && ln -s /usr/local/bin/pip3 /usr/local/bin/pip

WORKDIR /www/server

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r ./requirements.txt \
    -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

ENV PYTHONUNBUFFERED 1

###### 启动处理 ##########
ENTRYPOINT ["python", "/www/server/proxy.py"]
