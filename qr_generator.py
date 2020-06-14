import qrcode
import sys,time
#--------------------------------------------------------------------
# gen_qr() generates qr code image and saves it as a .png file
# Parameters:
# data (Mandatory)        : The text to be converted to QR Code
# img_path (Optional)     : The path to save the QR Code png file
# img_filename (Optional) : The prefix for the png file
#--------------------------------------------------------------------
def gen_qr(data,img_path='.',img_filename='qr_code'):
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(img_path+'/'+img_filename+'_'+str(time.time())+'.png')
    
if __name__ == '__main__':
    input_text = str(sys.argv[1])
    gen_qr(input_text)