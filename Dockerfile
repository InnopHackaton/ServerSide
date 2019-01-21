FROM ubuntu

RUN apt-get -yqq update
RUN apt-get -yqq install python3 python3-gnupg python3-crypto
RUN useradd hackathon

COPY src/ /home/hackathon
COPY configs/config.ini /home/hackathon/configs/config.ini
COPY configs/setupgpg.sh /home/hackathon/configs/setupgpg.sh
WORKDIR /home/hackathon

RUN export GNUPGHOME=/home/hackathon
RUN bash /home/hackathon/configs/setupgpg.sh
RUN gpg --export hack@hack.ru > pubkey.asc

EXPOSE 1337
EXPOSE 1338

