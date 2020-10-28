import bm3d
import imageio


fn = "/home/yguan/data/SI/CUT_CH1_signal/test01566_x15650_y21060_w512_h512.tif"
img_noisy = imageio.imread(fn)


img_denoised = bm3d.bm3d(img_noisy, sigma_psd=30/255, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)

imageio.imwrite('denoised.png', img_denoised)

