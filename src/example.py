import bm3d
import imageio
import numpy as np
import sewar
import argparse

def bm3d_denoise(noise, clean, size):

    img_noisy = imageio.imread(noise)
    img_noisy = img_noisy[:size,:size].astype(np.float64)
    
    img_fore = imageio.imread(clean)
    raw = img_fore.astype(np.float)
    img_fore = (raw[:256,:256,0] + raw[:256,:256,0] + raw[:256,:256,0])/3


    with open('/nas/exp/bm3d_exp/result.txt', 'w') as fh:
        for tlambda in np.linspace(0.05, 2.0, num=25):
            print(tlambda)
        
            combined = img_noisy.astype(np.float) * tlambda + img_fore.astype(np.float)
            
            combined = np.clip(combined, 0, 255)
            
            img_denoised = bm3d.bm3d(combined, sigma_psd=30/255, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)
            img_denoised = np.clip(img_denoised, 0, 255)
            
            psnr = sewar.full_ref.psnr(img_fore.astype(np.uint8), img_denoised.astype(np.uint8))
            ssim = sewar.full_ref.ssim(img_fore.astype(np.uint8), img_denoised.astype(np.uint8))
            
            fh.write("{}, {}, {}\n".format(tlambda, psnr, ssim[0]))
            
            #imageio.imwrite('denoised.png', img_denoised)
            #imageio.imwrite('clean.png', clean)
            


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--noise", help="input noise")
    parser.add_argument("-c", "--clean", help="clean image")
    parser.add_argument("-s", "--size", help="image shape, default square")
    args = parser.parse_args()
    if args.noise is None or args.clean is None:
        print(parser.print_help())
        exit()

    tsize = args.size
    if tsize is None:
        tsize = 256

    #print(args.noise)
    #print(args.clean)
    #print(args.size)
    
    bm3d_denoise(args.noise, args.clean, tsize)


    # background_noise = "/home/yguan/data/SI/CUT_CH1_no_signal/test02978_x13020_y17820_w512_h512.tif"
    # foreground = "/home/yguan/data/Spatial_Envelope/spatial_envelope_256x256_static_8outdoorcategories/insidecity_hous114.jpg"
