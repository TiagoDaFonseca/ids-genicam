FROM python:3.6.9

RUN apt-get update
RUN apt-get install -y libqt5core5a libqt5gui5 libqt5widgets5 libqt5quick5 
RUN apt-get install -y qml-module-qtquick-window2 qml-module-qtquick2
RUN apt-get install -y qtbase5-dev qtdeclarative5-dev qml-module-qtquick-controls 
RUN apt-get install -y qml-module-qtquick-dialogs qml-module-qt-labs-settings qml-module-qt-labs-folderlistmodel
RUN apt-get install -y qml-module-qtquick-layouts libusb-1.0-0
RUN mkdir -p etc/udev/rules.d

WORKDIR /usr/src/app

COPY ./ids/* ./
RUN dpkg -i ./ids-peak-linux-x86-1.1.8.0-64.deb

COPY ./script/* ./script/ 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /usr/src/app/script
CMD [ "python", "./camera.py" ]
