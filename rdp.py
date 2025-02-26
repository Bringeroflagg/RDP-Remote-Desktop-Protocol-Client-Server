#!/usr/bin/env python3

import select
import socket
import sys
import queue
import time
import re

# 1 = ip addr, 2 = port number, 3 = read_file, 4 = write_file
server_address = (sys.argv[1],int(sys.argv[2]))
# create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setblocking(0)
server.bind(server_address)
server.listen(5)

words_tuple = ("Send", "Receive", "SYN", "Sequence",
               "ACK", "Acknowledgment", "Window", "Length",
               "FIN")


def main():

    # create multi-thread here one for client other for server, or client goes to server and
    # it runs forever in the while loop
    read_file = sys.argv[3]
    write_file = sys.argv[4]
    client(read_file)


# DATE: EVENT; COMMAND; Sequence|Acknowledgment: Value; Length|Window: Value
def server(write_file):
    # append data received from client
    recv_data = []
    SEQ = 0
    ACK = 1
    Length = 0
    Window = 0

    '''
    forever sender{
        on application write
        packetize into packets
        
        # for packet in packets (maximize window size)
            send per receiver's window
            setup timer if not running
            update send_next
        

        on receiving ACK
        cancle time if convered
        setup timer if still unacked packets
        resend the oldest if enough dupacks
        send more if allowed by window

        on sender timeout
        resend the oldest packet
        setup timer properly
        if msg = prevMSg:
            resend prevMsg.encode()
    }
    '''
    while True:
        print(5)

    # send to method to write and save file
    write_to_file(recv_data)


def client(read_file):
    # have a queue if seq # is out of sorts, and wait for reply
    Seq = 0
    Ack = 1
    Length = 0
    Window = 0

    # receives file contents in a list, tokenized by a newline
    file_list = return_file(read_file)

    '''
        forever receiver{
            on receiving DAT
            below acked?
                drop
            beyond acked + window?
                send RST and exit
            out of order?
                buffer or drop
            in order?
                buffer and update ackno
            enough in-order data?
                write to file
            update window size
            send ACK
            if FIN:
                send contents to write to file and then send ack and fin to close connection
            if start_time - time > .100ms:
                resend packet
        
        }

        '''

    while True:

        print(5)
    # final message sent is, write_to_file name?


def return_file(r_file):
    try:
        fptr = open(r_file,"r")
        fptr_list = fptr.read().splitlines()
        fptr.close()
    except FileNotFoundError:
        print("Include valid file name, cannot open: %s" % cur_file)
        sys.exit(1)
    return fptr_list


# contents will be the things to write to file
def write_to_file(write_file, contents):
    main_file = open(write_file, 'a')
    for line in contents:
        main_file.write(line)
    main_file.close()


# used by both sender and receiver
def current_time():
    time_obj = time.localtime()
    time_now = time.strftime("%a %b %d %H:%M:%S PDT %Y:", time_obj)
    # to print Wed Sep 15 21:44:35 PDT 2021:
    return time_now


if __name__ == "__main__":
    main()