FROM python:3.7

WORKDIR /app
ADD . /app
EXPOSE 5000

#RUN apt-get update -y && \
#    apt-get install -y python3-pip

#RUN pip3 install pip --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python3", "./server.py"]
