## This code will check the kafka broker details in zookeeper metadata and send email alert on the status of broker availability

To Run the code :

    * Check the usability of the code but running it as : python3.8 check_kafka_broker.py
    * To run the code below is an example:

            python3.8 check_kafka_broker.py --total_broker 1 --zk_host_name localhost --env DEV

NOTE :

    * This script assumes tha you kafka is installed at / in the zookeeper which is the default. So you broker ids will be available in the zookeeper under /brokers/ids.
    * This code is based on python3.8
    * To send email using gmail smtp , you have to enable IMAP and Less secure app access in your gmail settings. Check in google how to do this.
    * Comment out the else section of the code if you want to be alerted only when any broker is missing.
            