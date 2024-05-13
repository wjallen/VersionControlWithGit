FROM python:3.9

RUN pip install pytest

WORKDIR /code
COPY pi.py test_pi.py ./

RUN chmod +x pi.py
ENV PATH="/code:$PATH"

CMD ["python3", pi.py", "-h"]
