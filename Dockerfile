FROM scrapinghub/base:12.04    
EXPOSE 5000    
WORKDIR /app    
CMD ["python2", "/app/lodgeit.wsgi"]    
ADD requirements.txt /app/requirements.txt    
RUN pip install -r /app/requirements.txt    
ADD . /app
