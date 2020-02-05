sudo yum upgrade -y
easy_install-3.6 pip
pip install --upgrade pip
pip install boto3 --user
pip install nose --user
pip install tornado --user
pip install boto3 awscli moto botocore
pip install botocore==1.14.8
pip install boto3==1.9.201

pip install bs4
pip install soupsieve
hdfs dfs -mkdir images
hdfs dfs -get s3://scrapproject/code_scrap.py
hdfs dfs -get s3://scrapproject/image_scrap.py
hdfs dfs -get s3://scrapproject/rds_incremental.py

wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.45.tar.gz
tar -xvzf mysql-connector-java-5.1.45.tar.gz
sudo cp mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar /usr/lib/spark/jars/

python code_scrap.py
spark-submit rds_incremental.py
spark-submit image_scrap.py
