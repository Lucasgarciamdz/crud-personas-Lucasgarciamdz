FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/crud-personas-Lucasgarciamdz.git
WORKDIR /crud-personas-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]