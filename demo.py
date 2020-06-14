import qr_generator
import sys

if __name__ == '__main__':
    if(len(sys.argv)) < 2:
        print("Insufficient parameters.")
    elif((len(sys.argv))==2):
        qr_generator.gen_qr(sys.argv[1])
    elif((len(sys.argv))==3):
        qr_generator.gen_qr(sys.argv[1],sys.argv[2])
    elif((len(sys.argv))==4):
        qr_generator.gen_qr(sys.argv[1], sys.argv[2], sys.argv[3])
