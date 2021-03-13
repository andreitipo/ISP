FROM python:3.8

ENV TARGETPATH=/home/kelevra/Documents/Test/ISP/Lab1/app/

RUN mkdir -p "${TARGETPATH}"

WORKDIR "${TARGETPATH}"

COPY fib.py "${TARGETPATH}"

CMD ["python3","fib.py"]

